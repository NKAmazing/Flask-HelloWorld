# Description: This is the main application file for the Flask application.

# Python imports
import os
import sys
from dotenv import load_dotenv

# Flask imports
from flask import Flask
from flask import jsonify

# OpenTelemetry imports
from opentelemetry import trace
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from azure.monitor.opentelemetry.exporter import AzureMonitorTraceExporter

# Logging imports
import logging
from azure.monitor.opentelemetry.exporter import AzureMonitorLogExporter
from opentelemetry.sdk._logs.export import BatchLogRecordProcessor
from opentelemetry._logs import (
    get_logger_provider,
    set_logger_provider,
)
from opentelemetry.sdk._logs import (
    LoggerProvider,
    LoggingHandler,
)

# Initialize Flask
app = Flask(__name__)

# Load environment variables
load_dotenv()

CONNECTION_STRING = os.environ.get('CONNECTION_STRING')
OTEL_SERVICE_NAME = os.environ.get('OTEL_SERVICE_NAME')
OTEL_TRACES_SAMPLER_ARG = os.environ.get('OTEL_TRACES_SAMPLER_ARG')

# Load configuration of OpenTelemetry
tracer_provider = TracerProvider(
    resource=Resource.create({SERVICE_NAME: OTEL_SERVICE_NAME})
)

trace.set_tracer_provider(tracer_provider)

# Configure logging
logger_provider = LoggerProvider()
set_logger_provider(logger_provider)
exporter = AzureMonitorLogExporter(
    connection_string=CONNECTION_STRING
)
logger_provider.add_log_record_processor(BatchLogRecordProcessor(exporter))

# Attach LoggingHandler to namespaced logger
handler = LoggingHandler()
logger = logging.getLogger(__name__)
logger.addHandler(handler)
logger.setLevel(logging.NOTSET)

logger.warning("Hello, World!")

# Manually flush Telemetry records
logger_provider.force_flush()

# Enable tracing for Flask library
FlaskInstrumentor().instrument_app(app)

# Enable tracing for requests library
RequestsInstrumentor().instrument()

trace_exporter = AzureMonitorTraceExporter(
    connection_string=CONNECTION_STRING
)
trace.get_tracer_provider().add_span_processor(
    BatchSpanProcessor(trace_exporter)
)

# The following code will generate two pieces of exception telemetry that are identical in nature
try:
    val = 1 / 0
    print(val)
except ZeroDivisionError:
    logger.exception("Error: Division by zero")

try:
    val = 1 / 0
    print(val)
except ZeroDivisionError:
    logger.error("Error: Division by zero", stack_info=True, exc_info=True)

# Import the application views
@app.route('/')
def index():
    return jsonify({'message': 'Hello, World!'})

if __name__ == "__main__":
    '''
    Start the Flask application.
    '''
    app.run(debug=True, port=5000, host='0.0.0.0')
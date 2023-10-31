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

# # Configure logging
# logging.basicConfig(level=logging.DEBUG)
# app_logger = logging.getLogger(__name__)

# # Log the values of environment variables
# app_logger.debug(f"APPLICATIONINSIGHTS_CONNECTION_STRING: {CONNECTION_STRING}")
# app_logger.debug(f"OTEL_SERVICE_NAME: {OTEL_SERVICE_NAME}")

# Configure logging
logger_provider = LoggerProvider()
set_logger_provider(logger_provider)

exporter = AzureMonitorLogExporter(
    connection_string=os.environ["APPLICATIONINSIGHTS_CONNECTION_STRING"]
)

logger_provider.add_log_record_processor(BatchLogRecordProcessor(exporter))

# Attach LoggingHandler to root logger
handler = LoggingHandler()
logging.getLogger().addHandler(handler)
logging.getLogger().setLevel(logging.NOTSET)

logger = logging.getLogger(__name__)

logger.warning("Hello World!")

# Telemetry records are flushed automatically upon application exit
# If you would like to flush records manually yourself, you can call force_flush()
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

# Import the application views
@app.route('/')
def index():
    return jsonify({'message': 'Hello, World!'})

if __name__ == "__main__":
    '''
    Start the Flask application.
    '''
    app.run(debug=True, port=5000, host='0.0.0.0')
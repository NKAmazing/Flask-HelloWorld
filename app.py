import os
import sys
import logging

from flask import Flask
from dotenv import load_dotenv

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from config import Config

from opentelemetry import trace
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

from azure.monitor.opentelemetry.exporter import AzureMonitorTraceExporter


# Initialize Flask
app = Flask(__name__)

load_dotenv()

print("Connection String: " + os.getenv("CONNECTION_STRING"))
print("Service Name: " + os.getenv("OTEL_SERVICE_NAME"))
print("Sampler Arg: " + os.getenv("OTEL_TRACES_SAMPLER_ARG"))

# Load configuration
app.config.from_object(Config)



# Set global TracerProvider before instrumenting
trace.set_tracer_provider(
    TracerProvider(
        resource=Resource.create({SERVICE_NAME: Config.OTEL_SERVICE_NAME})
    )
)

# Configure logging
logging.basicConfig(level=logging.DEBUG)
app_logger = logging.getLogger(__name__)

# Log the values of environment variables
app_logger.debug(f"APPLICATIONINSIGHTS_CONNECTION_STRING: {Config.CONNECTION_STRING}")
app_logger.debug(f"OTEL_SERVICE_NAME: {Config.OTEL_SERVICE_NAME}")
app_logger.debug(f"OTEL_TRACES_SAMPLER_ARG: {Config.OTEL_TRACES_SAMPLER_ARG}")

# Enable tracing for Flask library
FlaskInstrumentor().instrument_app(app)

# Enable tracing for requests library
RequestsInstrumentor().instrument()

trace_exporter = AzureMonitorTraceExporter(
    connection_string=Config.CONNECTION_STRING
)
trace.get_tracer_provider().add_span_processor(
    BatchSpanProcessor(trace_exporter)
)

# Import here to avoid circular imports
from routes import *  # noqa isort:skip

if __name__ == "__main__":
    # Run the application
    app.run(debug=True, port=5000, host='0.0.0.0')
import os
from dotenv import load_dotenv


class Config(object):
    '''
    Class to set environment variables
    '''
    
    load_dotenv()

    CONNECTION_STRING = os.environ.get('CONNECTION_STRING')
    OTEL_SERVICE_NAME = os.environ.get('OTEL_SERVICE_NAME')
    OTEL_TRACES_SAMPLER_ARG = os.environ.get('OTEL_TRACES_SAMPLER_ARG')
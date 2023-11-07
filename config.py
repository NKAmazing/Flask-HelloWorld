# Description: This file contains the configuration variables for the application

# Python imports
from dotenv import load_dotenv
import os

class Config():
    '''
    Class to load the configuration variables of the application
    '''

    def __init__(self):
        '''
        Initialize the class
        '''
        load_dotenv()

    # Load environment variables
    def load_env_variables(self):
        '''
        Load environment variables
        '''
        self.CONNECTION_STRING = os.environ.get('CONNECTION_STRING')
        self.OTEL_SERVICE_NAME = os.environ.get('OTEL_SERVICE_NAME')
        self.OTEL_TRACES_SAMPLER_ARG = os.environ.get('OTEL_TRACES_SAMPLER_ARG')
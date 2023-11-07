# Description: This is the main application file for the Flask application.

# Python imports
from main import create_app

# Create the Flask application
app = create_app()

# Push the application context
app.app_context().push()

if __name__ == "__main__":
    '''
    Start the Flask application.
    '''
    app.run(debug=True, port=5000, host='0.0.0.0')
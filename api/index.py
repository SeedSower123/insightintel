from app import app as application

# For Vercel, expose 'handler' for serverless use
def handler(environ, start_response):
    return application(environ, start_response)
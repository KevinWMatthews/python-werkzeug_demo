from werkzeug.wrappers import Response

SERVER_HOSTNAME = ''
SERVER_PORT = 5000

# Response() actually returns an application.
application = Response('Hello, World!')

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple(SERVER_HOSTNAME, SERVER_PORT, application)

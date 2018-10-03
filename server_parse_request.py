from werkzeug.wrappers import Request, Response

SERVER_HOSTNAME = ''
SERVER_PORT = 5000

# This is the standard method for parsing data from the Request
# and creating a response.
# Parsing the Request is very common, so Werkzeug provides a decorator for
# performing common tasks. See below.
def application_example(environ, start_response):
    request = Request(environ)
    response_body = 'Received request: {}'.format(request.url)
    response = Response(response_body, mimetype='text/plain')
    return response(environ, start_response)


# Every WSGI application uses environ and start_response in the same way.
# Werkzeug provides a decorator that initializes the Request and
# calls the start_response callback automagically.
# Wow.
@Request.application
def application(request):
    response_body = 'Received request: {}'.format(request.url)
    return Response(response_body, mimetype='text/plain')


if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple(SERVER_HOSTNAME, SERVER_PORT, application, use_debugger=True, use_reloader=True)

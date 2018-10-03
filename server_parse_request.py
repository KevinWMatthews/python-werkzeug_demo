from werkzeug.wrappers import Request, Response

SERVER_HOSTNAME = ''
SERVER_PORT = 5000

def application(environ, start_response):
    request = Request(environ)
    response_body = 'Received request: {}'.format(request.url)
    response = Response(response_body, mimetype='text/plain')
    return response(environ, start_response)

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple(SERVER_HOSTNAME, SERVER_PORT, application, use_debugger=True, use_reloader=True)

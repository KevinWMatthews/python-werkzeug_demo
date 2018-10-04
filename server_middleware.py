from werkzeug.wrappers import Request, Response

SERVER_HOSTNAME = ''
SERVER_PORT = 5000


@Request.application
def application(request):
    response_body = 'Hello, World!'
    return Response(response_body, mimetype='text/plain')


# Custom middleware
# I wonder if this could inherit from Response or BaseResponse.
class Middleware():
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        return self.app(environ, start_response)


app = Middleware(application)

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple(SERVER_HOSTNAME, SERVER_PORT, application, use_debugger=True, use_reloader=True)

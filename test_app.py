def app(environ, start_response):
    path = environ.get('PATH_INFO')
    data = '<h1>Hello World</h1>'

    data = data.encode('utf-8')
    start_response(
        '200 OK', [
            ('Content-Type', 'text/html'),
            ('Content-Length', str(len(data)))
        ]
    )

    return iter([data])

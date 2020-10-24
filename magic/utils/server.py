from typing import Iterable


def run(self, environ: dict, start_response) -> Iterable:
    types = {
        'css': 'text/css',
        'js': 'text/javascript',
        'html': 'text/html',
        'jpeg': 'video/jpeg',
        'jpg': 'video/jpeg',
        'png': 'image/png',
        'csv': 'text/csv',
        'md': 'text/markdown'

    }
    path = environ.get('PATH_INFO')
    data = self._route.get(path, self.e404)

    found = False
    for t in types:
        if str(path).lower().endswith(t):
            data = data[0](**environ).encode('utf-8')
            start_response(
                '200 OK', [
                    ('Content-Type', types.get(t)),
                    ('Content-Length', str(len(data)))
                ]
            )
            found = True
            break

    if not found:
        data = data[0](**environ).encode('utf-8')
        start_response(
            '200 OK', [
                ('Content-Type', 'text/html'),
                ('Content-Length', str(len(data)))
            ]
        )

    return iter([data])

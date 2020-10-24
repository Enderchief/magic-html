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


import os
import subprocess

path = './components/image_text.py'

with open(path) as f:
    file = f.read()

print(file)
x = subprocess.check_output(['pj', '-s', file]).decode('utf-8')
print(x)

spl = path.split('/')


spl = '/'.join(spl[0:-2])

with open(f'{spl}/test.js', 'w') as f:
    f.write(x)

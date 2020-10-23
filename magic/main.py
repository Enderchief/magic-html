from typing import Callable, Iterable

import re
import importlib


class Magic:
    """Magic object is the foundation for the framework
    :param name:
    :param path:
    :param modules:
    :param log:
    """
    def __init__(self, name: str, path: str = '/src', modules: list = None, log: bool = False):
        self.name = name
        self.path = path
        self._components = {}
        self._route = {}
        self.e404 = ''
        self.globals = {}
        self._log = log

        self.modules = [importlib.__import__(i) for i in modules] if modules else []

    def render_template(self, template_name: str, minify: bool = False, environ: dict = None) -> str:
        """
        reads .mHTML file and replaces the data for html elements defined in Magic._components
        :param template_name: file name at path "Magic.path / template_name"
        :param minify: minify html by removing newline and tabs
        :param environ: optional environment variables from gunicorn
        :return html_str:
        """
        modules = self.modules
        globals = self.globals

        with open(f'./{self.path}/{template_name}') as file:
            html_str = file.read()

            l_match = r'\{\{<([A-Za-z0-9_]+ *((attr="\{([\w\d\s\-_\'", :\[\]=+\-_])*\}")?(\/)))>\}\}'
            s_match = r'\{\{<([A-Za-z0-9_]+ *(\/))>\}\}'

            found = True
            while found:
                item = re.search(s_match, html_str)

                if item:
                    key = html_str[item.span()[0]:item.span()[1]]
                    key = key.replace('<', '').replace('>', '').replace('/', '').strip('{}').strip('{}')

                    html_str = html_str.replace(item.group(), self._components[key]())

                else:
                    item = re.search(l_match, html_str)
                    if item:
                        key = html_str[item.span()[0]:item.span()[1]].strip('{}').strip('{}')
                        new = key.split(' ')
                        key = new.pop(0).replace('<', '').replace('>', '').replace('/', '').strip('{}').strip('{}')
                        new = ' '.join(new)

                        kwargs = eval(
                            new[5:-1].replace('<', '').replace('>', '').replace('/', '').replace("'", '"').strip('"'))

                        html_str = html_str.replace(item.group(), self._components[key](**kwargs))
                    else:
                        found = False

        if minify:
            html_str = html_str.replace('\n', '').replace('\t', '')

        if environ:
            for k in environ.keys():
                get = environ.get(k)
                if type(get) == str:
                    html_str = html_str.replace('{{' + k + '}}', get.lstrip('/'))

        found = True
        while found:

            items = re.search(r'\{\{(.*)\}\}', html_str)
            if items:
                item = str(html_str[items.span()[0]:items.span()[1]])
                # print(item.strip('{}').strip('{}'))

                new = list(eval(i) for i in item.strip('{}').strip('{}').replace(';', '\n').split('|n|'))
                try:
                    new = (''.join(list(new)))
                except TypeError:
                    pass

                html_str = html_str.replace(item, new)
            else:
                found = False

        return html_str

    def compile(self, template_name: str) -> (str or Exception):
        try:
            with open(f'./{self.path}/{template_name}'.replace('.mhtml', '.html'), 'a') as file:
                file.write(self.render_template(template_name))
            return 'Success'
        except Exception as e:
            return e

    def def_global(self, kwargs: dict) -> None:
        print('DEF GLOBAL', kwargs)
        for k in kwargs:
            self.globals[k] = kwargs[k]

    def component(self, name: str):
        def get_func(func: Callable) -> Callable:
            self._components[name] = func
            return func

        return get_func

    def add_component(self, kwargs: dict) -> None:
        for k in kwargs:
            self.component(k)(kwargs[k].component)
        return None

    def route(self, route: str, *args: list, **kwargs: dict) -> Callable:
        def append_path(func):
            if route == '404':
                self.e404 = [func, args, kwargs]
            else:
                self._route[route] = [func, args, kwargs]

        return append_path

    def run(self, environ: dict, start_response) -> Iterable:
        path = environ.get('PATH_INFO')

        data = self._route.get(path, self.e404)

        if str(path).endswith('css'):
            data = data[0](**environ).encode('utf-8')
            start_response(
                '200 OK', [
                    ('Content-Type', 'text/css'),
                    ('Content-Length', str(len(data)))
                ]
            )
        else:
            data = data[0](**environ).encode('utf-8')
            start_response(
                '200 OK', [
                    ('Content-Type', 'text/html'),
                    ('Content-Length', str(len(data)))
                ]
            )

        return iter([data])

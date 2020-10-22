from magic import Magic

from components import (
    navbar,
    ordered_items,
    unordered_items,
    image_text,
    push_button,
    grid_item
)

app = Magic(__name__, modules=['math', 'random'], log=False)

components = {'Navbar': navbar,
              'OlList': ordered_items,
              'UlList': unordered_items,
              'ImgText': image_text,
              'PushButton': push_button,
              'GridItem': grid_item}

app.add_component(components)


@app.route('/')
def home(**kwargs):
    modules = app.modules
    app.globals['rand_num'] = list(modules[1].randint(1, 100) for _ in range(6))

    x = app.render_template('index.mhtml', minify=False, environ=kwargs)
    return x


@app.route('/test')
def test(**kwargs):
    return app.render_template('test.mhtml', minify=False, environ=kwargs)


@app.route('404')
def error(**kwargs):
    print(kwargs)
    return app.render_template('404.mhtml', environ=kwargs)


@app.route('/static/style.css')
def style(**kwargs):
    with open('src/static/style.css') as file:
        return file.read().replace('\n', '').replace('\t', '')


app.globals['test'] = 'hello world'


def create_app(*args):
    return app.run(*args)

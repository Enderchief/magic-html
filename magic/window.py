def _id(i: str) -> str:
    return f'document.getElementById("{i}");'


def _class_name(name: str) -> str:
    return f'document.getElementsByClassName("{name}");'


class Document:
    id = _id
    class_name = _class_name


def _assign(var_type: str = 'var'):
    def x(var: str):
        return f'{var_type} {var} = '

    return x


def get(var: str):
    return f'{var}'


class Method:
    var = _assign('var')
    let = _assign('let')
    const = _assign('const')


def component(**kwargs):

    site = kwargs.get('site')
    paths = kwargs.get('paths')

    paths = paths if paths else [1, 2, 3, 4]

    paths = [f'\n<a href="#"><li class="nav-item">{path}</li></a>' for path in paths]

    return (
        f'''
        <div class="navbar" aria-label="navigation bar">
            <ul class="nav">
                <li class="nav-item nav-main"><strong>{site}</strong></li>
                <div></div>
                {''.join(paths)}
            </ul>
        </div>
        '''
    ), __name__


def component(**kwargs):
    print(__name__, kwargs)

    content = kwargs.get('content')
    content = content.replace(' ', '+') if content else 'Placeholder+text'

    size = kwargs.get('size')
    size = f'{size}x{size}' if size else '128x128'

    return (
        f'''
        <div class="imgText">
            <img src="https://via.placeholder.com/{size}.png?text={content}"/>
            <div>{kwargs.get('text')}</div>
        </div>
        '''
    )
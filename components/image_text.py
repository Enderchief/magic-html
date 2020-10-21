
def component(**kwargs):
    print(__name__, kwargs)

    content = kwargs.get('content')
    content = content.replace(' ', '+') if content else 'Placeholder+text'

    return (
        f'''
        <div class="imgText">
            <img src="https://via.placeholder.com/3999x3999.png?text={content}"/>
            <div>{kwargs.get('text')}</div>
        </div>
        '''
    )

def component(**kwargs):

    content = kwargs['content']
    content = content.replace(' ', '+') if content else 'Placeholder+text'

    size = kwargs['size']
    size = f'{size}x{size}' if size else '128x128'

    return (
        f'''
<div class="imgText">
    <img src="https://via.placeholder.com/{size}.png?text={content}"/>
    <div>{kwargs['text']}</div>
</div>''')
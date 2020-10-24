def component(**kwargs):
    content = kwargs['content'] if ('content' in kwargs) else None
    content = content.replace(' ', '+') if content else 'Placeholder+text'

    size = kwargs['size'] if ('size' in kwargs) else None
    size = f'{size}x{size}' if size else '128x128'

    return (
        '<div class="imgText">\n'
        f'  <img src="https://via.placeholder.com/{size}.png?text={content}"/>\n'
        f'  <div>{kwargs["text"]}</div>\n'
        '</div>\n'), __name__



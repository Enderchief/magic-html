
def component(**kwargs):
    print(__name__, kwargs)

    if len(kwargs):
        items = list(f'<li>{i}</li>\n' for i in kwargs["items"])

    else:
        items = list(f'<li>{str(str(i * 2).__hash__())[:5]}</li>\n' for i in range(5))

    return ('<div class="olList">\n'
            f'\t\t\t<h3>{len(items)} {kwargs["compare"] if "compare" in kwargs.keys() else "Top things"}</h3>\n'
            '\t\t\t<ol>\n'
            '\t\t\t\t' +
            ('\t\t\t\t'.join(items)) +
            '\t\t\t</ol>\n'
            '\t\t</div>')
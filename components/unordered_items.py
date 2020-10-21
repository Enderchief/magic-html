
def component(**kwargs):
    print(__name__, kwargs)

    return ('<div class="ulList">\n'
            '\t\t\t<h3>This an unordered list</h3>\n'
            '\t\t\t<ul>\n'
            '\t\t\t\t<li>red</li>\n'
            '\t\t\t\t<li>green</li>\n'
            '\t\t\t\t<li>blue</li>\n'
            '\t\t\t</ul>\n'
            '\t\t</div>')

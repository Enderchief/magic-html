
def component(**kwargs):
    print(__name__, kwargs)

    cls = kwargs.get('class')

    return (
        '''
        <div class="CLASSNAME">
            {{<ImgText attr="{'text':'Hello this is text', 'content':'A grid webpage', 'size':'256'}"/>}}
        </div>
        '''
    ).replace('CLASSNAME', cls), __name__

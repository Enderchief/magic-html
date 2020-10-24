
def component(**kwargs):
    on_press = kwargs.get('onPress') if kwargs.get('onPress') else ''

    return (
        f'''
        <div class="pushBtn">
            <p>This is some text</p>
            <button onclick={on_press}()>Press me!</button>
        </div>
        '''
    ), __name__
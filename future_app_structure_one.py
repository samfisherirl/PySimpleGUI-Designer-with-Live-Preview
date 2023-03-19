import PySimpleGUI as sg

class PySimpleGUILayout:
    def __init__(self, layout=None):
        self.layout = layout or []
    
    def add_element(self, element_class, **kwargs):
        element = element_class(**kwargs)
        self.layout.append(element)
        return element.__dict__
    
    def add_row(self, *elements):
        column = sg.Column([list(elements)], size=(None, None))
        self.layout.append(column)
        return column
    
    def build(self):
        return self.layout

if __name__ == '__main__':
    layout_builder = PySimpleGUILayout()
    layout_builder.add_element(sg.Text, 'Row 1, Column 1')
    layout_builder.add_element(sg.Input, key='-IN-')
    layout_builder.add_element(sg.Button, 'Button 1')
    layout_builder.add_row(
        sg.Text('Row 2, Column 1'),
        sg.Input(key='-IN2-'),
        sg.Button('Button 2')
    )
    layout_builder.add_row(
        sg.Text('Row 3, Column 1'),
        sg.Input(key='-IN3-'),
        sg.Button('Button 3')
    )
    layout = layout_builder.build()
    window = sg.Window('Window Title', layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
    window.close()

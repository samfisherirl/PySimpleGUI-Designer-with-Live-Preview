import PySimpleGUI as sg

class PySimpleGUILayout:
    def __init__(self, layout=None):
        self.layout = layout or []
    
    def add_element(self, element_class, **kwargs):
        element = element_class(**kwargs)
        self.layout.append(element)
        return element.__dict__
    
    def build(self):
        return self.layout

if __name__ == '__main__':
    layout_builder = PySimpleGUILayout()
    layout_builder.add_element(sg.Button, button_text='Button 1')
    layout_builder.add_element(sg.Input, default_text='Default text')
    layout = layout_builder.build()
    window = sg.Window('Window Title', layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
    window.close()

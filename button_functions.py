'''these are the functions that will be used in the main function, each function is a button on the GUI'''

class Elements:
    def __init__(self):
        self.main = []
        self.container = []
        self.design = []
        self.organization = []
        self.info = []
        self.drawing = []
        self.other = []
        self.layouts = []

    def layout_append(self, obj_name, value):
        if hasattr(self, obj_name):
            obj = getattr(self, obj_name)
            obj.append(value)

    def return_layout(self):
        return self.layouts

    def return_list(self, obj_name):
        obj = getattr(self, obj_name)
        return obj

def layout(sg, make_button_row):
    Ele = Elements()
    # Makes a button for each string in the given list of strings
     
    layout = []     
    Ele.layout_append('layouts',[
        sg.Button(button_text="Delete Element",
                  button_color=("black", "darkred"),
                  key="DeleteElement"),
        sg.Button('Move Element Up ˄', key="MoveUp"),
        sg.Button('Move Element Down ˅', key="MoveDown"),
        sg.Button('~Theme~', key="Theme")
    ])

    Ele.layout_append('layouts', [sg.Text(text="Main Elements")])
    Ele.layout_append('layouts', make_button_row(Ele.main))

    Ele.layout_append('layouts', [sg.Text(text="Containers")])
    Ele.container = ["TabGroup", "Tab", "Frame", "Column"]
    Ele.layout_append('layouts', make_button_row(Ele.container))

    Ele.layout_append('layouts', [sg.Text(text="Separators")])
    Ele.design = ["HorizontalSeparator", "VerticalSeparator"]
    Ele.layout_append('layouts', make_button_row(Ele.design))

    Ele.layout_append('layouts', [sg.Text(text="Menus")])
    Ele.organization = ["Menu", "MenuButton", "OptionMenu", "ButtonMenu"]
    Ele.layout_append('layouts', make_button_row(Ele.organization))

    Ele.layout_append('layouts', [sg.Text(text="Structured Info")])
    Ele.info = ["Tree", "Table"]
    Ele.layout_append('layouts', make_button_row(Ele.info))

    Ele.layout_append('layouts', [sg.Text(text="Images/Drawing")])
    Ele.drawing = ["Image", "Graph", "Canvas"]
    Ele.layout_append('layouts', make_button_row(Ele.drawing))

    Ele.layout_append('layouts', [sg.Text(text="Others")])
    Ele.others = [
        "Slider", "Spin", "Multiline", "ProgressBar", "StatusBar"
    ]
    Ele.layout_append('layouts', layout)

    for i in layout:
        Ele.layout_append('layouts', i)
    return Ele



def get_theme():
        try:
            with open('theme.txt', 'r') as f:
                return f.read()
        except:
            return "DarkGrey4"

    # auto_load from file if it exists

def template_reader():
    try:
        f = open("autosave.txt")
        return f.read()
    except:
        print("There is no autosave file. Giving template layout.")
        return  "import PySimpleGUI as sg\n" \
            "sg.theme('DarkGrey4')\n" \
            "[" \
            "[sg.Text(text='This is a very basic PySimpleGUI layout')], " \
            "[sg.InputText()], " \
            "[sg.Button('Button', key='-ExampleKey-'), sg.Button(button_text='Exit')] " \
            "]"

def RESET():
    with open("autosave.txt", "w") as f:
        with open("default.txt", "r") as g:
            text = g.read()
            f.write(str(text))
            return text

def reset_error(sg, e):
        sg.popup_error(
            ("Error: " + str(e) if len(e.args) == 1 else "Error: " +
                str(e.args[0]) + "\n, in this place: " + str(e.args[1])) +
            "\n Importing cancelled or Error in importing (mistake in the text given)."
        )


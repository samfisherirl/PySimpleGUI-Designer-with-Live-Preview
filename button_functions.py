'''these are the functions that will be used in the main function, each function is a button on the GUI'''
class Elements:
    def __init__(self):
        self.layout_ = []
        self.key = ''

    def layout_append(self, *args):
        try:
            self.layout_.append(args)
        except:
            pass

    def return_layout(self):
        return [self.layout_]

    def return_list(self, obj_name):
        obj = getattr(self, obj_name)
        return obj

def layout(sg, make_button_row):
    Ele = Elements()
    # Makes a button for each string in the given list of strings
     
    layout = []      


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


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

def export_maker(theme, tree, importer):
    tree = define_default(tree)
    if importer:
        importer = "import PySimpleGUI as sg"
    else:
        importer = "from time import sleep"
    return f"""{importer}
sg.theme('{theme}')
layout = {tree}
window = sg.Window('Preview Window', layout, resizable=True, enable_close_attempted_event=True, location=sg.user_settings_get_entry('-location-', (None, None)))
while True:
    event, values = window.read()   
    # Read the event that happened and the values dictionary
    print(event, values)
    if event in ('Exit', sg.WINDOW_CLOSE_ATTEMPTED_EVENT):
        sg.user_settings_set_entry('-location-', window.current_location())  
        # The line of code to save the position before exiting
        break

window.close()
"""

def export_live(theme, tree):

    tree = define_default(tree)
    prelude = r"""

x = 1 
y = 1
def logger():
    x, y = window.current_location()
    with open(log, 'w') as f:
        f.write(f",{x},{y},")
        sleep(0.05)
        print('loggin')

def error_log(e):
    with open(er, 'w') as f:
        f.write(str(e))
try:
    with open(log, 'r') as f:
        xy = f.read()
        xy = xy.split(',')
        x = xy[1]
        y = xy[2]
        
except Exception as e:
    error_log(e)
    x='50'
    y='250'


def close_window():
    logger()
    # The line of code to save the position before exiting
    sleep(0.05)
    window.close()
"""
    ######################################


    val = f"""

{prelude}
sg.theme('{theme}')

layout = {tree}
window = sg.Window('Preview Window', layout, resizable=False, finalize=True, location=(x, y))

while True: 
    event, values = window.read(timeout=350)
    try:
        logger()
        print(event, values)
    except Exception as e:
        error_log(e)
    # Read the event that happened and the values dictionary
    if event == 'Exit':
        break


window.close()
"""
    return val


def define_default(tree):
    new_tree = ""
    for i in tree.splitlines():
        val = False
        if "InputText()" in i: val = "InputText()"
        if "InputText(\"\")" in i: val = "InputText(\"\")"
        if val:
            i = i.replace(val, r"InputText('default text')")
            val = False
        if "Button()" in i: val = "Button()"
        if "Button(\"\")" in i: val = "Button(\"\")"
        if val:
            i = i.replace(val, "Button(button_text=\"default text\")")
        new_tree = str(new_tree + i)
    return new_tree

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


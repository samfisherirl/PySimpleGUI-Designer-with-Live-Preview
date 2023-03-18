import PySimpleGUI as sg
from pathlib import Path
from time import sleep
import tkinter as tk

cwd = Path.cwd()
log = cwd / "log.txt"
er = cwd / "err.txt"


file = cwd / "test.py"
if not file.is_file():
	file = cwd / "eval" / "test.py"
with open(file, "r") as f:
	string = f.read()

exec(string)
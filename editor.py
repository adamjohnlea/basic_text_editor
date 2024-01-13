from tkinter.filedialog import askopenfilename, asksaveasfilename
from utils import update_status_label
import tkinter as tk


def open_file(window, text_editor, status_label):
    """
    Open a file and populate the text editor with its contents.

    :param window: The main application window.
    :param text_editor: The text editor widget to populate.
    :param status_label: The Tkinter Label widget that displays the status of the open operation.
    :return: None
    """
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt")])

    if not filepath:
        return

    text_editor.delete("1.0", tk.END)
    try:
        with open(filepath, "r") as input_file:
            text = input_file.read()
            text_editor.insert(tk.END, text)
        window.title(f"leaStudios Text Editor - {filepath}")

        update_status_label(status_label, f"File '{filepath}' opened successfully")

    except FileNotFoundError:
        update_status_label(status_label, f"File '{filepath}' not found")
    except Exception as e:
        update_status_label(status_label, f"Failed to open file '{filepath}'. Error: {str(e)}")


def save_file(window, text_editor, status_label):
    """
    Saves the contents of the text editor to a file.

    :param window: The Tkinter window object.
    :param text_editor: The Tkinter Text widget that contains the text to be saved.
    :param status_label: The Tkinter Label widget that displays the status of the save operation.
    :return: None
    """
    filepath = asksaveasfilename(defaultextension="txt", filetypes=[("Text Files", "*.txt")])

    if not filepath:
        return
    try:
        with open(filepath, "w") as output_file:
            text = text_editor.get("1.0", tk.END)
            output_file.write(text)
        window.title(f"leaStudios Text Editor - {filepath}")

        update_status_label(status_label, f"File '{filepath}' saved successfully")

    except Exception as e:
        update_status_label(status_label, f"Failed to save file '{filepath}'. Error: {str(e)}")

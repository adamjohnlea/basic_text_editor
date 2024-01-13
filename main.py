import tkinter as tk
from editor import open_file, save_file
import platform


def main():
    """
    Main method for the leaStudios Text Editor.

    :return: None
    """
    window = tk.Tk()
    window.title("leaStudios Text Editor")
    window.rowconfigure(0, minsize=400, weight=1)
    window.columnconfigure(1, minsize=500, weight=1)

    text_editor = tk.Text(window, font=("Helvetica", 16))
    text_editor.grid(row=0, column=1, sticky="nsew")

    frame = tk.Frame(window, relief=tk.RAISED, bd=2)
    save_button = tk.Button(frame, text="Save", command=lambda: save_file(window, text_editor, status_label))
    open_button = tk.Button(frame, text="Open", command=lambda: open_file(window, text_editor, status_label))

    open_button.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
    save_button.grid(row=1, column=0, sticky="ew", padx=5)

    frame.grid(row=0, column=0, sticky="ns")

    # Create a status label
    status_label = tk.Label(window, text="", bd=1, relief=tk.SUNKEN, anchor=tk.W)
    status_label.grid(row=1, column=0, columnspan=2, sticky="we")

    open_shortcut = '<Command-o>' if platform.system() == 'Darwin' else '<Control-o>'
    save_shortcut = '<Command-s>' if platform.system() == 'Darwin' else '<Control-s>'
    window.bind(open_shortcut, lambda event: open_file(window, text_editor, status_label))
    window.bind(save_shortcut, lambda event: save_file(window, text_editor, status_label))

    window.mainloop()


if __name__ == '__main__':
    main()

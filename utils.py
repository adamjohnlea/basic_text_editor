def update_status_label(status_label, message):
    """
    Update the status label with a message and clear it after 3 seconds.

    :param status_label: The Tkinter Label widget that displays the status.
    :param message: The message to display.
    :return: None
    """
    status_label.config(text=message)
    status_label.after(3000, lambda: status_label.config(text=""))

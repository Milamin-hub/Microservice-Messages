import tkinter as tk
from socketio.exceptions import ConnectionError
import logging
import socketio


logging.basicConfig(level=logging.ERROR)


class ChatWindow:
    def __init__(self):
        self.sio = socketio.Client()
        self.sio.connect('http://localhost:5000')
        self.sio.on('message', self.receive_message)

        self.window = tk.Tk()
        self.window.title("Chat")
        self.window.geometry("600x400")

        self.username_label = tk.Label(self.window, text="Username: ")
        self.username_label.grid(row=0, column=0)

        self.username_entry = tk.Entry(self.window)
        self.username_entry.grid(row=0, column=1)

        self.chat_text = tk.Text(self.window)
        self.chat_text.grid(row=1, column=0, columnspan=2)

        self.message_entry = tk.Entry(self.window)
        self.message_entry.grid(row=2, column=0)

        self.send_button = tk.Button(self.window, text="Send", command=self.send_message)
        self.send_button.grid(row=2, column=1)

        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.window.mainloop()

    def send_message(self):
        username = self.username_entry.get()
        message = self.message_entry.get()
        data = {'username': username, 'message': message}
        self.sio.emit('message', data)
        self.message_entry.delete(0, 'end')

    def receive_message(self, data):
        username = data['username']
        message = data['message']
        self.chat_text.insert(tk.END, '{}: {}\n'.format(username, message))

    def on_closing(self):
        self.sio.disconnect()
        self.window.destroy()


if __name__ == '__main__':
    try:
        chat_window = ChatWindow()
    except ConnectionError:
        print("\033[91m" + "Connection error" + "\033[0m", 'Check your internet connection or Server temporarily unavailable')

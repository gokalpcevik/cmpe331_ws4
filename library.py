"""
    Stage: Development-01
    @author: Gökalp Çevik, 120202074
    @author: Mert Mengilli, 119202055
    @author: Ömercan Topalömer, 120202103

    
    Stage: Development-02
    @author: Arda Çelik, 119202051
    @authot: Giragos Başak, 119202045
"""

from tkinter import messagebox
import tkinter as tk
from tkinter import Button


# Test username and passwords
test_login_username = 'test'
test_login_password = 'test123'


class LoginWindow:
    # constructor
    def __init__(self):
        self.window = tk.Tk()

        self._initializeGUI()
        self._addGUIElementsToFrame()

        # start the GUI frame
        self.window.mainloop()

    """
        Initialize GUI elements. If it is necessary, you can add
        more elements.
        ! PLEASE RENAME THE OBJECTS ACCORDING TO THEIR PURPOSES !
        ! YOU CAN ADD MORE ELEMENTS IF IT IS NECESSARY !
    """
    def _initializeGUI(self):
        self.window.title('Library Login')
        self.lbl01 = tk.Label(text="Library Username")
        self.lbl02 = tk.Label(text="Password")

        self.txt01 = tk.Entry()
        self.txt02 = tk.Entry()

        self.btn01 = tk.Button(text="Login")

        self.btn01.bind("<Button-1>", self.handle_click)

    """
        Add GUI elements to the layout of the frame. If it is necessary,
        you can add more elements.
    """
    def _addGUIElementsToFrame(self):
        self.lbl01.grid(row=0, column=0, padx=10, pady=5)
        self.txt01.grid(row=0, column=1, padx=10, pady=5)

        self.lbl02.grid(row=1, column=0, padx=10, pady=5)
        self.txt02.grid(row=1, column=1, padx=10, pady=5)

        self.btn01.grid(row=2, column=0, padx=10, pady=5)

    def create_library_window(self):
        self.after_login_window = tk.Tk()
        self.after_login_window.geometry("640x480")
        self.after_login_window.title('Library')
        self.new_label = tk.Label(self.after_login_window,text="Successful!")
        self.new_button = Button(self.after_login_window, text="New Button")
        
        self.new_label.pack()
        self.new_button.pack()

    def validate_and_login_user(self, event):
        username = self.txt01.get()
        password = self.txt02.get()
        if(username == test_login_username and password == test_login_password):
          # After a successful login, we create a new 'page' or a window to show the library. 
          self.create_library_window()
          # Login window can now be destroyed
          self.window.destroy()
          messagebox.showinfo("Welcome!!", "Successfully logged in.")
          # Start the after login window main loop
          self.after_login_window.mainloop()

    """
        Action listener for the buttons. If "event.widget" is from
        one of the buttons, apply the related operation.
        :param event: action event for detecting which button is clicked
    """
    def handle_click(self, event):
        if(event.widget == self.btn01):
            self.validate_and_login_user(event)
        

# main method for testing the application
if __name__ == "__main__":
    LoginWindow()
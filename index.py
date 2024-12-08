import customtkinter

customtkinter.set_appearance_mode('system')

def nameButton(number):
    return 'Button ' + number

def createButtons(self, length):
    i = 1
    while i <= length:
        button = customtkinter.CTkButton(master=self, text=nameButton(str(i)), fg_color='green', 
        text_color='black',  corner_radius=4, height=16)
        button.pack(pady = 4, padx = 4, fill="x")
        i += 1

class MyFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        createButtons(self, 10)

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.my_frame = MyFrame(master=self, width=384, height=384)
        self.my_frame.grid(row=0, column=0, padx=0, pady=0)

app = App()

app.mainloop()

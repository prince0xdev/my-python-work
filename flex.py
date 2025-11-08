import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Apprendre le layout")
        self.geometry("500x500")
        ctk.set_appearance_mode('light')

        #create a row of 2 columns
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((0,1), weight=1)

        self.textbox = ctk.CTkTextbox(master=self)
        self.textbox.grid(row=0, column=0, padx=20, pady=(20, 0), sticky="nsew")

        self.textbox = ctk.CTkTextbox(master=self)
        self.textbox.grid(row=0, column=1, padx=20, pady=(20, 0), sticky="nsew")

if __name__ =="__main__":
    app = App()
    app.mainloop()
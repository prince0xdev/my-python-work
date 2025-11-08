import customtkinter as ctk

class App(ctk.CTk):
        def __init__(self):
            super().__init__()
            
            self.geometry("500x300")
            self.title("small example app")
            ctk.set_appearance_mode("light")
            self.minsize(300, 200)

            # create 2x2 grid system
            self.grid_rowconfigure(0, weight=1)
            self.grid_columnconfigure((0, 1, 2), weight=1)

            self.textbox = ctk.CTkTextbox(master=self)
            self.textbox.grid(row=0, column=0, columnspan=3, padx=20, pady=(20, 0), sticky="nsew")

            self.combobox = ctk.CTkComboBox(master=self, values=["Sample text 1", "Text"])
            self.combobox.grid(row=1, column=1, padx=20, pady=20, sticky="ew")

            self.button = ctk.CTkButton(master=self, command=self.button_callback)
            self.button.grid(row=1, column=0, padx=20, pady=20, sticky="ew")
            
            self.button = ctk.CTkButton(master=self, command=self.button_callback, text="Hello")
            self.button.grid(row=1, column=2, padx=20, pady=20, sticky="ew")

        def button_callback(self):
            self.textbox.insert("insert", self.combobox.get() + "\n")           
            self.combobox.set("")
            
        def format_remaining_time(second: str):
            return print(f"hello world {second}")

if __name__ == "__main__":
    app = App()
    app.mainloop()
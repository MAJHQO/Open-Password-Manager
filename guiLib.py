import flet as ft

def focusField(self):


        self.control.border_color="#FFDDA3"
                
        self.control.text_style=ft.TextStyle(color="#C1C2CF")

        self.control.label_style=ft.TextStyle(color="#C1C2CF")

        self.control.hint_style=ft.TextStyle(color="#C1C2CF")


    
def blurField(self):
         
        self.control.border_color="#C1C2CF"

        self.control.text_style=ft.TextStyle(color="#C1C2CF")

        self.control.label_style=ft.TextStyle(color="#C1C2CF")
        
        self.control.hint_style=ft.TextStyle(color="#C1C2CF")

        self.page.update()

    
def hoverButton(self):

        if (self.data=='true'):

            self.control.bgcolor="#E8D4BC"

        else:

            self.control.bgcolor="#D9D9D9"

        self.page.update()
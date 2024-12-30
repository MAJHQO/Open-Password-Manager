import flet as ft, sqlite3 as sq
import os, logging, bd, guiLib as gLib, hashlib, cryptoLib, pywin32_system32

from cryptography import fernet



logging.basicConfig(level=logging.INFO, filename="\SoftLog.txt", filemode="w")


def start(page: ft.Page):

    def unBlockSoft(self):

        #userKey=mainKeyField.content.value

        pass

    try:


        page.title="Open Password Manager"
        page.connection.page_name="start"

        page.horizontal_alignment=ft.CrossAxisAlignment.CENTER

        page.fonts={"Kufam":"Fonts\\Kufam.ttf"}

        page.bgcolor="#E4E6F3"
        page.window_height=670
        page.window_width=1200

        


        mainSoftName=ft.Row(controls=[

            ft.Image("Icons\\Logo.png", width=226, height=226,color=ft.colors.BLACK),
            ft.Text("Open Password Manager", size=35, color=ft.colors.BLACK)], 
            
            alignment=ft.MainAxisAlignment.CENTER)

        mainKeyField=ft.Column(controls=[

            ft.TextField(label="Мастер пароль", hint_text="Введите мастер-пароль",width=350,password=True,can_reveal_password=True, border_color="#C1C2CF",on_focus=gLib.focusField, max_lines=1, on_blur=gLib.blurField, text_style=ft.TextStyle(color="C1C2CF"))],
            
            spacing=20,  alignment=ft.MainAxisAlignment.CENTER)


        
        unLockButton=ft.Container(content=ft.ElevatedButton("Разблокировать" ,on_click=unBlockSoft, on_hover=gLib.hoverButton, bgcolor="#D9D9D9", color=ft.colors.BROWN_200, icon=ft.icons.LOCK_OPEN_ROUNDED, icon_color=ft.colors.WHITE), alignment=ft.Alignment(0,0))


        resertPassword=ft.ElevatedButton("Забыли мастер-пароль?", data="resetUserMPassword", bgcolor="#E4E6F3",color=ft.colors.BLACK26)


        page.add(mainSoftName, ft.Text(""), mainKeyField,  ft.Text(""),unLockButton, ft.Text(""),resertPassword)

    except Exception as ex:

        logging.error(f"[ERROR]: {ex}")



def startWithoutPass(page: ft.Page):\

    page.title="Open Password Manager"
    page.connection.page_name="startWithoutPass"

    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.vertical_alignment=ft.MainAxisAlignment.CENTER

    page.fonts={"Kufam":"Fonts\\Kufam.ttf"}

    page.bgcolor="#E4E6F3"
    page.window_height=670
    page.window_width=1200



    def createStorage(self):


        def  createMPassword(self):

            if (self.control.text=="Сгенерировать пароль"):

                cryptoLib.createMPassword(self)

                with open ("information")

            else:

                master_password=createPassTheme.controls[1].content.controls[2].value

                


        def changeButtonText(self):

            if (createPassTheme.controls[1][2].label==""):

                enterGenPassw.text="Сгенерировать пароль"

            else:

                enterGenPassw.text="Создать хранилище"

            
            self.page.update()



        page.clean()
        
        createPassTheme=ft.Row(controls=[

            ft.Image("Image\createPassLogo.svg", width=200, height=300),
            ft.Container(content=ft.Column(controls=[ft.Text("Создание хранилища",size=40,font_family="Kufam", color=ft.colors.BLACK),
                                                     ft.Text("Мастер-пароль является единственным ключом, который способен открыть ваше хранилище\nпаролей и осуществить расшивровку данных. В случае, если данный пароль будет утерян - мы не сможем его\nвосстановить.\n\nПри создании мастер-пароля для хранилища, рукомедуется использовать различные символы (@, %,!, & #), в\nсочетании с буквами и цифрами", size=14,color=ft.colors.BLACK),
                                                     ft.TextField(ft.TextField(label="Мастер-пароль", hint_text="Введите мастер-пароль",width=350, border_color="#C1C2CF",on_focus=gLib.focusField, max_lines=1, on_blur=gLib.blurField, on_change=changeButtonText ,password=True,can_reveal_password=True ,text_style=ft.TextStyle(color="C1C2CF")))
                                                     ], spacing=20), on_hover=gLib.focusField)], 
            
            alignment=ft.MainAxisAlignment.CENTER, spacing=70, vertical_alignment=ft.CrossAxisAlignment.CENTER)

        enterGenPassw=ft.ElevatedButton("Сгенерировать пароль" ,on_click=createMPassword, on_hover=gLib.hoverButton, bgcolor="#D9D9D9", color=ft.colors.BROWN_200, icon=ft.icons.PASSWORD, icon_color=ft.colors.WHITE)

        page.add(createPassTheme,enterGenPassw)


        page.update()
    
    try:


        page.clean()


        mainSoftName=ft.Row(controls=[

            ft.Image("Icons\\Logo.png", width=226, height=226,color=ft.colors.BLACK),
            ft.Text("Open Password Manager", size=35, color=ft.colors.BLACK)], 
            
            alignment=ft.MainAxisAlignment.CENTER, spacing=5)


        unLockButton=ft.Container(content=ft.ElevatedButton("Создать хранилище" ,on_click=createStorage, on_hover=gLib.hoverButton, bgcolor="#D9D9D9", color=ft.colors.BROWN_200, icon=ft.icons.PASSWORD, height=50, icon_color=ft.colors.WHITE), alignment=ft.Alignment(0,0))


        page.add(mainSoftName, ft.Text(""), unLockButton)

    except Exception as ex:

        logging.error(f"[ERROR]: {ex}")






if __name__=="__main__":

    if (os.path.exists("Config\\masterpassword.ini")==True):

        ft.app(target=start)

    else:

        ft.app(target=startWithoutPass)
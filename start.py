import cryptography.utils
import flet as ft, guiLib as gLib, config
import main, time, logging, datetime,bd
import os, logging, Lib

import hashlib



logging.basicConfig(level=logging.INFO, filename="userErrorLog.log", filemode="w")


def start(page: ft.Page):

    def unBlockSoft(self):

        master_password=mainKeyField.controls[0].value

        hashMPassword=hashlib.sha384(master_password.encode()).hexdigest()

        config.token=hashMPassword


        try:

            with open ("information.txt", "r") as file:

                encryptionKey_file=file.readline()

                keyFile=Lib.deecrypt(encryptionKey_file.encode())

                if(keyFile==hashMPassword):

                    main.main_menu(page)
                        
                else:

                    mainKeyField.controls[0].border_color=ft.colors.RED

                    page.update()

                    time.sleep(1.0)

                    mainKeyField.controls[0].border_color="#C1C2CF"

                    page.update()

                
                file.close()

        except Exception as ex:

            logging.error(f"[{datetime.datetime.now()}] :: Connection to database was not succussful, REASON: {ex}")

        

        

    try:

        page.clean()


        page.title="Open Password Manager"
        page.connection.page_name="start"

        page.horizontal_alignment=ft.CrossAxisAlignment.CENTER

        page.fonts={"Kufam":"Fonts\\Kufam.ttf", "Kufam_SemiBold": "Fonts\\Kufam-SemiBold.ttf"}

        page.bgcolor="#E4E6F3"
        page.window_height=670
        page.window_width=1200
        page.window_resizable=False

        


        mainSoftName=ft.Row(controls=[

            ft.Image("Icons\\Logo.png", width=226, height=226,color=ft.colors.BLACK),
            ft.Text("Open Password Manager", size=35, color=ft.colors.BLACK, font_family="Kufam_SemiBold")], 
            
            alignment=ft.MainAxisAlignment.CENTER)

        mainKeyField=ft.Column(controls=[

            ft.TextField(label="Мастер пароль", hint_text="Введите мастер-пароль",width=350,password=True,can_reveal_password=True, border_color="#C1C2CF",on_focus=gLib.focusField, max_lines=1, on_blur=gLib.blurField, text_style=ft.TextStyle(color="C1C2CF"))],
            
            spacing=20,  alignment=ft.MainAxisAlignment.CENTER)


        
        unLockButton=ft.Container(content=ft.ElevatedButton("Разблокировать" ,on_click=unBlockSoft, on_hover=gLib.hoverButton, bgcolor="#D9D9D9", color=ft.colors.BROWN_200, icon=ft.icons.LOCK_OPEN_ROUNDED, icon_color=ft.colors.WHITE), alignment=ft.Alignment(0,0))


        resertPassword=ft.ElevatedButton("Забыли мастер-пароль?", data="resetUserMPassword", bgcolor="#E4E6F3",color=ft.colors.BLACK26, on_click=forgetMPassword)


        page.add(mainSoftName, ft.Text(""), mainKeyField,  ft.Text(""),unLockButton, ft.Text(""),resertPassword)

        page.update()

    except Exception as ex:

        logging.error(f"[{datetime.datetime.now()}] :: Connection to database was not succussful, REASON: {ex}")



def startWithoutPass(page: ft.Page):


    def backPage(self):

        startWithoutPass(self.page)

        self.page.update()



    page.title="Open Password Manager"
    page.connection.page_name="startWithoutPass"

    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.vertical_alignment=ft.MainAxisAlignment.CENTER

    page.fonts={"Kufam":"Fonts\\Kufam.ttf", "Kufam_SemiBold": "Fonts\\Kufam-SemiBold.ttf"}

    page.bgcolor="#E4E6F3"
    page.window_height=670
    page.window_width=1200
    page.window_resizable=False



    def createStorage(self):


        def  createMPassword(self):

            if (self.control.text=="Сгенерировать пароль"):

                mPassword, token=Lib.createMPassword(self)

                self.page.controls[0].controls[1].content.controls[2].value=mPassword

                self.control.text="Создать хранилище"

                self.page.update()

                

            else:

                master_password=createPassTheme.controls[1].content.controls[2].value
                
                hashMPassword=hashlib.sha384(master_password.encode()).hexdigest()

                config.token=hashMPassword

                with open(".\\information.txt", "w") as file:

                    try:

                        file.writelines(Lib.encryption(hashMPassword))

                    except Exception as ex:

                        print(ex)

                
                bd.reqExecute("""Create table Web_Accounts(
                        ID INT PRIMARY KEY,
                        Login TEXT,
                        Password TEXT,
                        Service_Address TEXT)""")


                bd.reqExecute("""Create table Bank_Accounts(
                        ID INT PRIMARY KEY,
                        Number TEXT,
                        Date TEXT,
                        CVC INT,
                        Card_Owner TEXT,
                        PIN_Code INT,
                        Bank_Name TEXT,
                        Bank_URL TEXT)""")


                bd.reqExecute("""Create table Documents(
                        ID INT PRIMARY KEY,
                        Filename TEXT,
                        Format TEXT,
                        FileData TEXT,
                        PageCount INT)""")

                
                main.main_menu(page)

                return

                


        def changeButtonText(self):

            if (createPassTheme.controls[1].content.controls[2].value==""):

                enterGenPassw.text="Сгенерировать пароль"

            else:

                enterGenPassw.text="Создать хранилище"

            
            page.update()



        page.clean()
        
        createPassTheme=ft.Row(controls=[

            ft.Image("Image\createPassLogo.svg", width=200, height=300),
            ft.Container(content=ft.Column(controls=[ft.Text("Создание хранилища",size=40,font_family="Kufam", color=ft.colors.BLACK),
                                                     ft.Text("Мастер-пароль является единственным ключом, который способен открыть ваше хранилище\nпаролей и осуществить расшивровку данных. В случае, если данный пароль будет утерян - мы не сможем его\nвосстановить.\n\nПри создании мастер-пароля для хранилища, рукомедуется использовать различные символы (@, %,!, & #), в\nсочетании с буквами и цифрами", size=14,color=ft.colors.BLACK),
                                                     ft.TextField(label="Мастер-пароль", hint_text="Введите мастер-пароль",width=350, border_color="#C1C2CF",on_focus=gLib.focusField, max_lines=1, on_blur=gLib.blurField, on_change=changeButtonText ,password=True,can_reveal_password=True)
                                                     ], spacing=20), on_hover=gLib.focusField)], 
            
            alignment=ft.MainAxisAlignment.CENTER, spacing=70, vertical_alignment=ft.CrossAxisAlignment.CENTER)

        enterGenPassw=ft.ElevatedButton("Сгенерировать пароль" ,on_click=createMPassword, on_hover=gLib.hoverButton, bgcolor="#D9D9D9", color=ft.colors.BROWN_200, icon=ft.icons.PASSWORD, icon_color=ft.colors.WHITE)

        backButton=ft.ElevatedButton("Назад", on_click=backPage,on_hover=gLib.hoverButton, bgcolor="#D9D9D9", color=ft.colors.BROWN_200,width=60, data="BACKPAGE:ENTER")
        
        page.add(createPassTheme,ft.Row([enterGenPassw, backButton],spacing=30, width=400 ,alignment=ft.MainAxisAlignment.CENTER))

        page.controls[0].controls[1].content.controls[2].value=""

        page.update()
    
    try:


        page.clean()

        page.window_resizable=False


        mainSoftName=ft.Row(controls=[

            ft.Image("Icons\\Logo.png", width=226, height=226,color=ft.colors.BLACK),
            ft.Text("Open Password Manager", size=35, color=ft.colors.BLACK, font_family="Kufam_SemiBold")], 
            
            alignment=ft.MainAxisAlignment.CENTER, spacing=5)


        unLockButton=ft.Container(content=ft.ElevatedButton("Создать хранилище" ,on_click=createStorage, on_hover=gLib.hoverButton, bgcolor="#D9D9D9", color=ft.colors.BROWN_200, icon=ft.icons.PASSWORD, height=50, icon_color=ft.colors.WHITE), alignment=ft.Alignment(0,0))


        page.add(mainSoftName, ft.Text(""), unLockButton)

    except Exception as ex:

        logging.error(f"[ERROR]: {ex}")



def forgetMPassword(self):

    def backPage(self):

        if (self.control.data.split(":")[1]=="ENTER"): 

            start(self.page)
        
        else:

            startWithoutPass(self.page)


    def  createMPassword(me):

            if (self.control.text=="Сгенерировать пароль"):

                mPassword, token=Lib.createMPassword(self)

                me.page.controls[0].controls[1].content.controls[2].value=mPassword

                me.control.text="Создать хранилище"

                me.page.update()

                

            else:

                master_password=forgetPassTheme.controls[1].content.controls[2].value
                
                hashMPassword=hashlib.sha384(master_password.encode()).hexdigest()

                config.token=hashMPassword

                with open(".\\information.txt", "wb") as file:

                    file.writelines(Lib.encryption(hashMPassword))

                
                bd.reqExecute("""Create table Web_Accounts(
                        ID INT PRIMARY KEY,
                        Login TEXT,
                        Password TEXT,
                        Service_Address TEXT)""")


                bd.reqExecute("""Create table Bank_Accounts(
                        ID INT PRIMARY KEY,
                        Number TEXT,
                        Date TEXT,
                        CVC INT,
                        Card_Owner TEXT,
                        PIN_Code INT,
                        Bank_Name TEXT,
                        Bank_URL TEXT)""")


                bd.reqExecute("""Create table Documents(
                        ID INT PRIMARY KEY,
                        Filename TEXT,
                        Format TEXT,
                        FileData TEXT,
                        PageCount INT)""")

                

                main.main_menu(me.page)

                return


    def changeButtonText(me):

            if (forgetPassTheme.controls[1].content.controls[2].value==""):

                enterGenPassw.text="Сгенерировать пароль"

            else:

                enterGenPassw.text="Создать новое хранилище"

            
            me.page.update()


    def createMPassword_page(me):

        os.remove("userData.db")
        os.remove("information.txt")

        forgetPassTheme.controls[1].content.controls[0].value="Создание хранилища"
        
        forgetPassTheme.controls[1].content.controls[1].value="Мастер-пароль является единственным ключом, который способен открыть ваше хранилище\nпаролей и осуществить расшивровку данных. В случае, если данный пароль будет утерян - мы не сможем его\nвосстановить.\n\nПри создании мастер-пароля для хранилища, рукомедуется использовать различные символы (@, %,!, & #), в\nсочетании с буквами и цифрами"
        forgetPassTheme.controls[1].content.controls[1].size=14

        forgetPassTheme.controls[1].content.controls.append(ft.TextField(label="Мастер-пароль", hint_text="Введите мастер-пароль",width=350, border_color="#C1C2CF",on_focus=gLib.focusField, max_lines=1, on_blur=gLib.blurField, on_change=changeButtonText ,password=True,can_reveal_password=True))
        
        enterGenPassw.on_click=createMPassword
        backButton.data="BACKPAGE:START"
        
        me.page.update()
        

            


    self.page.clean()


    self.page.title="Open Password Manager"
    self.page.connection.page_name="startWithoutPass"

    self.page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    self.page.vertical_alignment=ft.MainAxisAlignment.CENTER

    self.page.fonts={"Kufam":"Fonts\\Kufam.ttf", "Kufam_SemiBold": "Fonts\\Kufam-SemiBold.ttf"}

    self.page.bgcolor="#E4E6F3"
    self.page.window_height=670
    self.page.window_width=1200
    self.page.window_resizable=False

        
    forgetPassTheme=ft.Row(controls=[

            ft.Image("Image\createPassLogo.svg", width=200, height=300),
            ft.Container(content=ft.Column(controls=[ft.Text("Восстановление мастер-пароля",size=40,font_family="Kufam", color=ft.colors.BLACK),
                                                     ft.Text("Мастер-пароль является единственным ключом, которым осуществляется открытие вашего хранилища и \nрасшифровку данных. В случае, если данный пароль был утерян - восстановить доступ к хранилищу невозможною.\n\nЖелаете ли создать новое хранилище?", size=16,color=ft.colors.BLACK),
                                                     ], spacing=20), on_hover=gLib.focusField)], 
            
            alignment=ft.MainAxisAlignment.CENTER, spacing=70, vertical_alignment=ft.CrossAxisAlignment.CENTER)

    enterGenPassw=ft.ElevatedButton("Создать новое хранилище" ,on_click=createMPassword_page, on_hover=gLib.hoverButton, bgcolor="#D9D9D9", color=ft.colors.BROWN_200, icon=ft.icons.PASSWORD, icon_color=ft.colors.WHITE)

    backButton=ft.ElevatedButton("Назад", on_click=backPage,on_hover=gLib.hoverButton, bgcolor="#D9D9D9", color=ft.colors.BROWN_200,width=60, data="BACKPAGE:ENTER")
    
    self.page.add(forgetPassTheme,ft.Row([enterGenPassw, backButton], spacing=30, width=400 ,alignment=ft.MainAxisAlignment.CENTER))

    self.page.update()




if __name__=="__main__":

    if (os.path.exists("userData.db")==True):

        ft.app(target=start)

    else:

        ft.app(target=startWithoutPass)


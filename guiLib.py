import flet as ft, bd,time, Lib, shutil, datetime, os

from main import logging
from flet import FilePickerResultEvent
from docx import Document
from striprtf.striprtf import rtf_to_text

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







def createWebAccountData(self):

        def dialogClose(my):
               
               self.page.close_dialog()

               self.page.update()

        
        def createWebAccount(my):

                check=False
               
                if (webURLField.value!=""):
                      
                        serviceURL=webURLField.value

                else:
                       
                        webURLField.border_color=ft.colors.RED

                        check=True


                if (loginField.value!=""):
                       
                       login=loginField.value

                else:
                       
                       loginField.border_color=ft.colors.RED

                       check=True

                
                if (passwordField.value!=""):
                       
                       password=passwordField.value

                else:
                       
                       passwordField.border_color=ft.colors.RED

                       check=True

                
                if (check==True):

                        self.page.update()

                        time.sleep(1)

                        webURLField.border_color=ft.colors.BLACK
                        loginField.border_color=ft.colors.BLACK
                        passwordField.border_color=ft.colors.BLACK

                        self.page.update()

                else:

                        bd.reqExecute(f"Insert Into Web_Accounts(ID, Login, Password, Service_Address) values ((Select COUNT(*) from Web_Accounts)+1, '{Lib.encryption(loginField.value)}', '{Lib.encryption(passwordField.value)}', '{Lib.encryption(webURLField.value)}')")


                        self.page.close_dialog()

                        self.page.update()



        webURLField=ft.TextField(hint_text="Например google.com", height=40)
        loginField=ft.TextField(hint_text="Логин")
        passwordField=ft.TextField(hint_text="Пароль", password=True)
        
        
        webAccount_Add=ft.AlertDialog(content=
                                
                                ft.Column([

                                    ft.Row([

                                        ft.Text("Веб-адрес сайта: ",size=15, color=ft.colors.BLACK, width=120),

                                        webURLField,

                                        ft.Text("", width=9),

                                        ft.IconButton(ft.icons.COPY, icon_size=24, icon_color=ft.colors.BLACK, padding=0, data="CopyURL_From_WebCreate")
                                        
                                    ], width=500),

                                    ft.Text("", height=13),

                                    ft.Container (content=
                                        
                                        ft.Column([
                                               
                                        
                                                ft.Text("",height=2),

                                            ft.Row([

                                                ft.Text("",width=3),

                                                ft.Text("Аккаунт", size=19,color=ft.colors.BLACK),

                                            ], alignment=ft.MainAxisAlignment.START),

                                            ft.Divider(thickness=1, color="#999595"),

                                            ft.Row([

                                                ft.Text("",width=3),

                                                ft.Text("Логин", size=15, color=ft.colors.BLACK),

                                                ft.Text("",width=60),

                                                loginField

                                            ]),

                                            
                                            ft.Row([

                                                ft.Text("",width=3),

                                                ft.Text("Пароль", size=15, color=ft.colors.BLACK),

                                                ft.Text("",width=50),

                                                passwordField,

                                                ft.IconButton(icon=ft.icons.KEY, icon_size=20, tooltip="Сгенерировать пароль"),

                                            ]),
                                            
                                    ],width=500), bgcolor="#D9D9D9", border_radius=14,width=500,height=220),
                                    

                                ], width=500, height=280), title=ft.Text("Добавление учетной записи"),title_text_style=ft.TextStyle(color=ft.colors.BLACK,size=20) , bgcolor="#E4E6F3",actions=[
                                        
                                        ft.ElevatedButton("Создать", bgcolor="#D9D9D9", color=ft.colors.BROWN_200,height=33,width=100, on_click=createWebAccount),
                                        ft.ElevatedButton("Отмена", bgcolor="#E4E6F3",height=33,width=100, on_click=dialogClose)

                                ]
                                
            )

        self.page.show_dialog(dialog=webAccount_Add)

        self.page.update()



def createBankAccountData(self):
       
        def dialogClose(self):
               
               self.page.close_dialog()
        
               self.page.window_height=680

               self.page.update()


        def createBankAccount(self):
                
                check=False
               
                if (cardNumber.value==''):
                      
                      cardNumber.border_color=ft.colors.RED

                      check=True

                if(cardOverDate.value==''):
                       
                       cardOverDate.border_color=ft.colors.RED

                       check=True

                if(cardOwner.value==''):
                       
                       cardOwner.border_color=ft.colors.RED

                       check=True

                if(cardCVC.value==''):
                       
                       cardCVC.border_color=ft.colors.RED

                       check=True

                if(cardBankName.value==''):
                       
                       cardBankName.border_color=ft.colors.RED

                       check=True

                if(cardPincode.value==''):
                       
                       cardPincode.border_color=ft.colors.RED

                if (check==False):

                        if (cardPincode.value=="" or cardPincode.value==None):

                                bd.reqExecute(f"Insert Into Bank_Accounts(ID, Number, Date, CVC, Card_Owner, PIN_Code, Bank_Name) values((Select COUNT(*) from Bank_Accounts)+1, '{Lib.encryption(cardNumber.value)}', '{Lib.encryption(cardOverDate.value)}', '{Lib.encryption(cardCVC.value)}', '{Lib.encryption(cardOwner)}', ' ', '{Lib.encryption(cardBankName.value)}')")

                        else:
                               
                                bd.reqExecute(f"Insert Into Bank_Accounts(ID, Number, Date, CVC, Card_Owner, PIN_Code, Bank_Name) values((Select COUNT(*) from Bank_Accounts)+1, '{Lib.encryption(cardNumber.value)}', '{Lib.encryption(cardOverDate.value)}', '{Lib.encryption(cardCVC.value)}', '{Lib.encryption(cardOwner)}', '{Lib.encryption(cardPincode.value)}', '{Lib.encryption(cardBankName.value)}')")

                        
                        self.page.close_dialog(bankAccount)
                        
                        self.page.update()

                        return
                
                else:
                
                    self.page.update()

                    time.sleep(1)

                    cardNumber.border_color=ft.colors.BLACK
                    cardOverDate.border_color=ft.colors.BLACK
                    cardOwner.border_color=ft.colors.BLACK
                    cardCVC.border_color=ft.colors.BLACK
                    cardBankName.border_color=ft.colors.BLACK
                    cardPincode.border_color=ft.colors.BLACK

                    self.page.update()





        cardNumber=ft.TextField(hint_text="Номер карты")
        cardOverDate=ft.TextField(hint_text="Дата окончания действия карты")
        cardOwner=ft.TextField(hint_text="Владелец карты (на английском)")
        cardCVC=ft.TextField(hint_text="CVC-код")
        cardBankName=ft.TextField(hint_text="Название банка (на любом языке)")

        cardPincode=ft.TextField(hint_text="Pin-код от карты")

        bankAccount=ft.AlertDialog(title=ft.Text("Банковские данные", color=ft.colors.BLACK), bgcolor="#E4E6F3" ,content=ft.Column(
                
               [
                        ft.Container(content=ft.Column(
                            [

                                ft.Text("",height=2),

                                ft.Row([
                                        
                                            ft.Text("", width=3),
                                
                                            ft.Text("Основные данные", size=19, color=ft.colors.BLACK),
                                ]),

                                ft.Divider(thickness=1, color="#999595"),

                                ft.Row([
                                        
                                        ft.Text("", width=3),
                                        
                                        ft.Text("Номер", size=15, color=ft.colors.BLACK),

                                        ft.Text("", width=60),

                                        cardNumber

                                ]),


                                ft.Row([
                                        
                                        ft.Text("", width=3),
                                        
                                        ft.Text("Дата", size=15, color=ft.colors.BLACK),

                                        ft.Text("", width=75),

                                        cardOverDate
                                ]),


                                ft.Row([
                                        
                                        ft.Text("", width=3),
                                        
                                        ft.Text("Имя Фамилия", size=15, color=ft.colors.BLACK),

                                        ft.Text("", width=10),

                                        cardOwner
                                ]),


                                ft.Row([
                                        
                                        ft.Text("", width=3),
                                        
                                        ft.Text("CVC", size=15, color=ft.colors.BLACK),

                                        ft.Text("", width=80),

                                        cardCVC
                                ]),


                                ft.Row([
                                        
                                        ft.Text("", width=3),
                                        
                                        ft.Text("Банк", size=15, color=ft.colors.BLACK),

                                        ft.Text("", width=75),

                                        cardBankName
                                ]),
                            
                            ]), width=500, height=370, bgcolor="#D9D9D9", border_radius=14),


                        ft.Container(ft.Column(
                               [
                                   
                                    ft.Text("",height=2),

                                    
                                    ft.Row([
                                             
                                                ft.Text("", width=3),
                                      
                                                ft.Text("Необязательные данные", size=19, color=ft.colors.BLACK)
                                      ]),

                                    ft.Divider(thickness=1, color="#999595"),


                                    ft.Row([
                                             
                                            ft.Text("", width=3),
                                      
                                            ft.Text("Pin-код", size=15, color=ft.colors.BLACK),

                                            ft.Text("", width=60),

                                        cardPincode

                                      ])
                               
                               ]), bgcolor="#D9D9D9", width=500, height=130, border_radius=14)

        ], height=570, width=470, horizontal_alignment=ft.CrossAxisAlignment.START), actions=[
                                        
                                        ft.ElevatedButton("Создать", bgcolor="#D9D9D9", color=ft.colors.BROWN_200,height=33,width=100, on_click=createBankAccount),
                                        ft.ElevatedButton("Отмена", bgcolor="#E4E6F3",height=33,width=100, on_click=dialogClose)

                                ])
        

        self.page.show_dialog(bankAccount)

        self.page.window_height=745

        self.page.update()



def addNoteData(self):
       
        def dialogClose(self):
               
               self.page.close_dialog()
               
               self.page.window_height=680

               self.page.update()

        
        def selectNoteFile(me: FilePickerResultEvent):

                if (me.files[0].name.split(".")[1] in ['txt', 'md', 'doc', 'docx', 'rtf']):
               
                        noteFile["Path"]=me.files[0].path
                        noteFile["SelectedFile"]=me.files[0].name

                        addNoteFile.content.controls[0].content.controls[2].value=f"Файл '{noteFile["SelectedFile"]}' успешно выбран\n\nНе забудьте удалить выбранный файл, с целью безопасности хранения текущего"
                        addNoteFile.content.controls[0].content.controls[2].text_align=ft.TextAlign.CENTER
                        
                        addNoteFile.content.controls[0].content.controls[0].src="Image\DownloadSuccess.png"

                        addNoteFile.content.controls[0].content.controls[0].width=3005
                        addNoteFile.content.controls[0].content.controls[0].height=300
                        
                        addNoteFile.actions[0].disabled=False

                        self.page.update()

                else:
                       
                        addNoteFile.content.controls[0].content.controls[2].value=f"Файл '{me.files[0].name}' не является подходящим по формату"
                        addNoteFile.content.controls[0].content.controls[2].text_align=ft.TextAlign.CENTER
                        
                        addNoteFile.content.controls[0].content.controls[0].src="Icons\Error.png"

                        addNoteFile.content.controls[0].content.controls[0].width=300
                        addNoteFile.content.controls[0].content.controls[0].height=300

                        self.page.update()

        
        def createNoteData(self):
               
                try:
                        fileData=""

                        with open (noteFile["Path"], 'r') as file:
                               
                               fileData=file.read()

                        with open (".\\Data\\"+noteFile["SelectedFile"], "w") as eFile:
                               
                               eFile.writelines(Lib.encryption(fileData))


                        if (noteFile["SelectedFile"].split(".")[1]=="txt"):

                                with open(noteFile["Path"], "r") as file:
                                       
                                        data=file.read()

                                        bd.reqExecute(f"Insert into Documents (ID, Filename, Format, Filedata,PageCount) values((Select COUNT(*) from Documents)+1, '{noteFile['SelectedFile'].split(".")[0]}', '{noteFile['SelectedFile'].split(".")[1]}', '{Lib.encryption(fileData)}', '{data}')")

                        elif(noteFile["SelectedFile"].split(".")[1]=="md"):
                               
                               with open(noteFile["Path"], "r", encoding="utf-8") as file:
                                       
                                        data=file.read()

                                        bd.reqExecute(f"Insert into Documents (ID, Filename, Format, Filedata,PageCount) values((Select COUNT(*) from Documents)+1, '{noteFile['SelectedFile'].split(".")[0]}', '{noteFile['SelectedFile'].split(".")[1]}', '{Lib.encryption(fileData)}', '{data}')")

                        elif(noteFile["SelectedFile"].split(".")[1] in ['doc', 'docx']):
                               
                                document=Document(".\\Todo.rtf")

                                data = ""

                                for para in document.paragraphs:
                                
                                        data+=para.text+"\n"

                                bd.reqExecute(f"Insert into Documents (ID, Filename, Format, Filedata,PageCount) values((Select COUNT(*) from Documents)+1, '{noteFile['SelectedFile'].split(".")[0]}', '{noteFile['SelectedFile'].split(".")[1]}', '{Lib.encryption(fileData)}', '{data}')")

                        elif(noteFile["SelectedFile"].split(".")[1]=="rtf"):
                               
                               with open(noteFile["Path"], "r") as file:
                                       
                                        data=file.read()

                                        bd.reqExecute(f"Insert into Documents (ID, Filename, Format, Filedata,PageCount) values((Select COUNT(*) from Documents)+1, '{noteFile['SelectedFile'].split(".")[0]}', '{noteFile['SelectedFile'].split(".")[1]}', '{Lib.encryption(fileData)}', '{rtf_to_text(data)}')")
                        
                        
                        self.page.close_dialog()

                        self.page.window_height=680

                        self.page.update()

                except Exception as ex:

                        logging.error(f"[{datetime.datetime.now()}] :: File can't copy in selected path, REASON: {ex}")






        noteFile={'Path':"", 'SelectedFile': ""}


        selectedNoteFile=ft.FilePicker(on_result=selectNoteFile)

        addNoteFile=ft.AlertDialog(title=ft.Text("Заметки", color=ft.colors.BLACK), bgcolor="#E4E6F3" ,content=ft.Column(
                
               [
                        ft.Container(content=ft.Column(
                            [
                                ft.Image("Image\Download.png", width=80, height=80),

                                ft.Text("",height=5),

                                ft.Text("Нажмите в данной области для загрузки файла", size=14, color="")
                            
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER), width=500, height=420, bgcolor=ft.colors.TRANSPARENT, border_radius=14, on_click=lambda a:selectedNoteFile.pick_files(allow_multiple=False, initial_directory=os.path.expanduser('~')+"\\Downloads"))

        ], height=570, width=470, horizontal_alignment=ft.CrossAxisAlignment.CENTER), actions=[
                                        
                                        ft.ElevatedButton("Создать", bgcolor="#D9D9D9", color=ft.colors.BROWN_200,height=33,width=100, on_click=createNoteData, disabled=True),
                                        ft.ElevatedButton("Отмена", bgcolor="#E4E6F3",height=33,width=100, on_click=dialogClose)

                                ])
        
        self.page.overlay.extend([selectedNoteFile])

        self.page.show_dialog(addNoteFile)

        self.page.window_height=745

        self.page.update()
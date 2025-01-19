import flet as ft, bd,time, Lib, shutil, datetime, os, keyboard

from main import logging
from flet import FilePickerResultEvent
from docx import Document
from striprtf.striprtf import rtf_to_text

def focusField(self):


        self.control.border_color="#C8CAD7"
                
        self.control.text_style=ft.TextStyle(color="#C1C2CF")

        self.control.label_style=ft.TextStyle(color="#C1C2CF")

        self.control.hint_style=ft.TextStyle(color="#C1C2CF")

        self.page.update()


    
def blurField(self):
         
        self.control.border_color="#C1C2CF"

        self.control.text_style=ft.TextStyle(color="#C1C2CF")

        self.control.label_style=ft.TextStyle(color="#C1C2CF")
        
        self.control.hint_style=ft.TextStyle(color="#C1C2CF")

        self.page.update()

    
def hoverButton(self):

        if (self.data=='true' and type(self.control)==ft.ElevatedButton):

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

                        Lib.updateUserCardList(self, self.page.controls[0].controls[2].content.controls[1].content, "web")

                        self.page.update()



        webURLField=ft.TextField(hint_text="Например google.com", height=40, multiline=False)
        loginField=ft.TextField(hint_text="Логин", multiline=False)
        passwordField=ft.TextField(hint_text="Пароль", password=True, can_reveal_password=True, multiline=False)
        
        
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

        def choiceBankURL(self):
        
                if (self.value=="Сбербанк"):
                       
                       return "https://online.sberbank.ru"
                
                elif (self.value=="Т-Банк"):
                       
                       return "https://id.tbank.ru/auth/step?cid=MI1ShJumXc1X"

                elif (self.value=="Альфа-Банк"):
                       
                       return "https://private.auth.alfabank.ru/passport/cerberus-mini-blue/dashboard-blue/username?response_type=code&client_id=click-web-adf&scope=openid%20click-web&acr_values=username&non_authorized_user=true"

                elif (self.value=="Газпромбанк"):
                       
                       return "https://ib.online.gpb.ru/"

                elif (self.value=="Россельхозбанк"):
                       
                       return "https://online.rshb.ru/cas-auth/index?forceAuth=true"

                elif (self.value=="Райффайзен Банк"):
                       
                       return "https://online.raiffeisen.ru/login/main"

                elif (self.value=="Росбанк"):
                       
                       return "https://online.rosbank.ru"

                elif (self.value=="Ак Барс Банк"):
                       
                       return "https://online.akbars.ru"


               
               
       
        def dialogClose(self):
               
               self.page.close_dialog()
        
               self.page.window_height=680

               self.page.update()


        def createBankAccount(self):
                
                check=False

                try:
                        for i in cardNumber.value:
                                
                                if (i!=" "):
                                
                                        int(i)

                        if (cardNumber.value==''):
                        
                                cardNumber.border_color=ft.colors.RED

                                check=True

                except Exception as ex: 

                        cardNumber.border_color=ft.colors.RED

                        check=True
                        

                try:

                        int(cardOverDate.value[0:2])
                        int(cardOverDate.value[3:])

                        if(cardOverDate.value==''):
                        
                                cardOverDate.border_color=ft.colors.RED

                                check=True
                        
                        if(int(cardOverDate.value.split("/")[0])>12 or int(cardOverDate.value.split("/")[0])<1):

                                cardOverDate.border_color=ft.colors.RED

                                check=True

                        if (int(cardOverDate.value.split("/")[1])>(datetime.datetime.now().year+7) or int(cardOverDate.value.split("/")[1])<22):

                                cardOverDate.border_color=ft.colors.RED

                                check=True

                except Exception as ex:

                        cardOverDate.border_color=ft.colors.RED

                        check=True


                if(Lib.strCheckOnEnglish(cardOwner.value)!=True and cardOwner.value==''):
                       
                       cardOwner.border_color=ft.colors.RED

                       check=True

                
                try:

                        int(cardCVC.value)

                        if(cardCVC.value==''):
                        
                                cardCVC.border_color=ft.colors.RED

                                check=True
                
                except Exception as ex:

                        cardCVC.border_color=ft.colors.RED

                        check=True
                        


                if(cardBankName.value==''):
                       
                       cardBankName.border_color=ft.colors.RED

                       check=True


                if (check==False):

                        bankURL=choiceBankURL(bankAccountURLControl)

                        if (cardPincode.value=="" or cardPincode.value==None):

                                bd.reqExecute(f"Insert Into Bank_Accounts(ID, Number, Date, CVC, Card_Owner, PIN_Code, Bank_Name, Bank_URL) values((Select COUNT(*) from Bank_Accounts)+1, '{Lib.encryption(cardNumber.value)}', '{Lib.encryption(cardOverDate.value)}', '{Lib.encryption(cardCVC.value)}', '{Lib.encryption(cardOwner.value)}', '0', '{Lib.encryption(cardBankName.value)}', '{bankURL}')")

                        else:
                               
                                bd.reqExecute(f"Insert Into Bank_Accounts(ID, Number, Date, CVC, Card_Owner, PIN_Code, Bank_Name, Bank_URL) values((Select COUNT(*) from Bank_Accounts)+1, '{Lib.encryption(cardNumber.value)}', '{Lib.encryption(cardOverDate.value)}', '{Lib.encryption(cardCVC.value)}', '{Lib.encryption(cardOwner.value)}', '{Lib.encryption(cardPincode.value)}', '{Lib.encryption(cardBankName.value)}'. '{bankURL}')")

                        
                        self.page.close_dialog()

                        Lib.updateUserCardList(self, self.page.controls[0].controls[2].content.controls[1].content, "bank")
                        
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

                    self.page.update()





        cardNumber=ft.TextField(hint_text="Номер карты", max_length=19, on_change=maskedTextFieldNumber, color=ft.colors.BLACK)
        cardOverDate=ft.TextField(hint_text="Дата окончания действия карты", max_length=5, on_change=maskedTextFieldDate, color=ft.colors.BLACK)
        cardOwner=ft.TextField(hint_text="Владелец карты (на английском)", color=ft.colors.BLACK)
        cardCVC=ft.TextField(hint_text="CVC-код", password=True,can_reveal_password=True, color=ft.colors.BLACK)
        cardBankName=ft.TextField(hint_text="Название банка (на любом языке)", color=ft.colors.BLACK)

        cardPincode=ft.TextField(hint_text="Pin-код от карты", password=True, can_reveal_password=True, color=ft.colors.BLACK)
        bankAccountURLControl=ft.Dropdown(width=190, options=[
               
               ft.dropdown.Option("Сбербанк"),
               ft.dropdown.Option("Т-Банк"),
               ft.dropdown.Option("Альфа-Банк"),
               ft.dropdown.Option("Газпромбанк"),
               ft.dropdown.Option("Россельхозбанк"),
               ft.dropdown.Option("Райффайзен Банк"),
               ft.dropdown.Option("Росбанк"),
               ft.dropdown.Option("Ак Барс Банк"),

        ], filled=True, fill_color="#E4E6F3", color=ft.colors.BLACK)

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

                                        ]),

                                        ft.Row([
                                             
                                                ft.Text("", width=3),
                                      
                                                ft.Text("Ссылка на личный кабинет", size=15, color=ft.colors.BLACK),

                                                ft.Text("", width=30),

                                                bankAccountURLControl


                                      ])
                               
                               ]), bgcolor="#D9D9D9", width=550, height=200, border_radius=14)

        ], height=670, width=470, horizontal_alignment=ft.CrossAxisAlignment.START), actions=[
                                        
                                        ft.ElevatedButton("Создать", bgcolor="#D9D9D9", color=ft.colors.BROWN_200,height=33,width=100, on_click=createBankAccount),
                                        ft.ElevatedButton("Отмена", bgcolor="#E4E6F3",height=33,width=100, on_click=dialogClose)

                                ], on_dismiss=dialogClose)
        

        self.page.show_dialog(bankAccount)

        self.page.window_height=820

        self.page.update()



def addNoteData(self):
       
        def dialogClose(self):
               
               self.page.close_dialog()
               
               self.page.window_height=680

               self.page.update()

        
        def selectNoteFile(me: FilePickerResultEvent):

                if (me.files[0].name.split('.')[1] in ['txt', 'md', 'doc', 'docx', 'rtf']):
               
                        noteFile["Path"]=me.files[0].path
                        noteFile['SelectedFile']=me.files[0].name

                        addNoteFile.content.controls[0].content.controls[2].value=f"Файл '{noteFile['SelectedFile']}' успешно выбран\n\nНе забудьте удалить выбранный файл, с целью безопасности хранения текущего"
                        addNoteFile.content.controls[0].content.controls[2].text_align=ft.TextAlign.CENTER
                        
                        addNoteFile.content.controls[0].content.controls[0].src="Image\DownloadSuccess.png"

                        addNoteFile.content.controls[0].content.controls[0].width=3005
                        addNoteFile.content.controls[0].content.controls[0].height=300
                        
                        addNoteFile.actions[0].disabled=False

                        self.page.update()

                else:
                       
                        addNoteFile.content.controls[0].content.controls[2].value=f"Файл '{me.files[0].name}' не является подходящим по формату"
                        addNoteFile.content.controls[0].content.controls[2].text_align=ft.TextAlign.CENTER
                        
                        addNoteFile.content.controls[0].content.controls[0].src="Image\DownloadError.png"

                        addNoteFile.content.controls[0].content.controls[0].width=300
                        addNoteFile.content.controls[0].content.controls[0].height=300

                        self.page.update()

        
        def createNoteData(self):
               
                try:

                        fileData=""

                        if (noteFile['SelectedFile'].split('.')[1]=="txt"):

                                with open (noteFile["Path"], 'r') as file:
                                
                                        fileData=file.read()

                                with open (".\\Data\\e"+noteFile['SelectedFile'], "w") as eFile:
                                
                                        eFile.writelines(Lib.encryption(fileData))

                                
                                with open(noteFile["Path"], "r") as file:
                                       
                                        data=file.read()

                                        bd.reqExecute(f"Insert into Documents (ID, Filename, Format, Filedata,PageCount) values((Select COUNT(*) from Documents)+1, '{Lib.encryption(noteFile['SelectedFile'].split('.')[0])}', '{Lib.encryption(noteFile['SelectedFile'].split('.')[1])}', '{Lib.encryption(fileData)}', '{data}')")

                        elif(noteFile['SelectedFile'].split('.')[1]=="md"):
                               
                                with open(noteFile["Path"], "r", encoding="utf-8") as file:
                                       
                                        fileData=file.read()

                                with open (".\\Data\\e"+noteFile['SelectedFile'], "w") as eFile:
                                
                                        eFile.writelines(Lib.encryption(fileData))
                                
                                        bd.reqExecute(f"Insert into Documents (ID, Filename, Format, Filedata,PageCount) values((Select COUNT(*) from Documents)+1, '{Lib.encryption(noteFile['SelectedFile'].split('.')[0])}', '{Lib.encryption(noteFile['SelectedFile'].split('.')[1])}', '{Lib.encryption(fileData)}', 0)")

                        elif(noteFile['SelectedFile'].split('.')[1] in ['doc', 'docx']):
                               
                                document=Document(noteFile["Path"])

                                for para in document.paragraphs:
                                
                                        fileData+=para.text+"\n"

                                with open (".\\Data\\e"+noteFile['SelectedFile'], "w") as eFile:
                                
                                        eFile.writelines(Lib.encryption(fileData))

                                        bd.reqExecute(f"Insert into Documents (ID, Filename, Format, Filedata,PageCount) values((Select COUNT(*) from Documents)+1, '{Lib.encryption(noteFile['SelectedFile'].split('.')[0])}', '{Lib.encryption(noteFile['SelectedFile'].split('.')[1])}', '{Lib.encryption(fileData)}', 0)")

                        
                        elif(noteFile['SelectedFile'].split('.')[1]=="rtf"):
                               
                                with open(noteFile["Path"], "r") as file:
                                       
                                        fileData=file.read()

                                
                                with open (".\\Data\\e"+noteFile['SelectedFile'], "w") as eFile:

                                        rtfData=rtf_to_text(fileData)
                                
                                        eFile.writelines(Lib.encryption(rtfData))
                                
                                        bd.reqExecute(f"Insert into Documents (ID, Filename, Format, Filedata,PageCount) values((Select COUNT(*) from Documents)+1, '{Lib.encryption(noteFile['SelectedFile'].split('.')[0])}', '{Lib.encryption(noteFile['SelectedFile'].split('.')[1])}', '{Lib.encryption(rtfData)}', 0)")
                        
                        
                        self.page.close_dialog()

                        Lib.updateUserCardList(self, self.page.controls[0].controls[1].content.controls[1].content, "note")

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

                                ft.Text("Нажмите в данной области для загрузки файла", size=14, color="#C1C2CF")
                            
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER), width=500, height=420, bgcolor=ft.colors.TRANSPARENT, border_radius=14, on_click=lambda a:selectedNoteFile.pick_files(allow_multiple=False, initial_directory=os.path.expanduser('~')+"\\Downloads"))

        ], height=570, width=470, horizontal_alignment=ft.CrossAxisAlignment.CENTER), actions=[
                                        
                                        ft.ElevatedButton("Создать", bgcolor="#D9D9D9", color=ft.colors.BROWN_200,height=33,width=100, on_click=createNoteData, disabled=True),
                                        ft.ElevatedButton("Отмена", bgcolor="#E4E6F3",height=33,width=100, on_click=dialogClose)

                                ])
        
        self.page.overlay.extend([selectedNoteFile])

        self.page.show_dialog(addNoteFile)

        self.page.window_height=745

        self.page.update()



def changeUserCardWeb(self):

        def dialogClose(my):
               
               self.page.close_dialog()

               self.page.update()

        
        def changeWebAccount(my):

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

                        
                        bd.reqExecute(f"Update Web_Accounts SET Login='{Lib.encryption(loginField.value)}', Password='{Lib.encryption(passwordField.value)}', Service_Address='{Lib.encryption(webURLField.value)}' where ID={dataForCompare.split(':')[0]}")

                        
                        self.page.close_dialog()

                        Lib.updateUserCardList(self, self.page.controls[0].controls[2].content.controls[1].content, "web")

                        self.page.update()



        webURLField=ft.TextField(hint_text="Например google.com", height=40, multiline=False, color=ft.colors.BLACK)
        loginField=ft.TextField(hint_text="Логин", multiline=False, color=ft.colors.BLACK)
        passwordField=ft.TextField(hint_text="Пароль", password=True, can_reveal_password=True, multiline=False, color=ft.colors.BLACK)

        dataForCompare=self.control.data
        
        result=bd.reqExecute("Select * from Web_Accounts")

        userArr=[]

        for i in result:

                userArr.append([str(i[0]), Lib.deecrypt(i[1]), Lib.deecrypt(i[2]), Lib.deecrypt(i[3])])

        
        for i in userArr:

                if (i[0]==dataForCompare.split(":")[0] and i[3]==dataForCompare.split(":")[1]):

                        webURLField.value=i[3]
                        loginField.value=i[1]
                        passwordField.value=i[2]
        
        
        webAccount_Change=ft.AlertDialog(content=
                                
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
                                    

                                ], width=500, height=280), title=ft.Text("Изменение учетной записи"),title_text_style=ft.TextStyle(color=ft.colors.BLACK,size=20) , bgcolor="#E4E6F3",actions=[
                                        
                                        ft.ElevatedButton("Изменить", bgcolor="#D9D9D9", color=ft.colors.BROWN_200,height=33,width=100, on_click=changeWebAccount),
                                        ft.ElevatedButton("Отмена", bgcolor="#E4E6F3",height=33,width=100, on_click=dialogClose)

                                ]
                                
            )
        


        self.page.show_dialog(dialog=webAccount_Change)

        self.page.update()



def changeUserCardBank(self):

        def choiceBankURL(self):
        
                if (self.value=="Сбербанк"):
                       
                       return "https://online.sberbank.ru"
                
                elif (self.value=="Т-Банк"):
                       
                       return "https://id.tbank.ru/auth/step?cid=MI1ShJumXc1X"

                elif (self.value=="Альфа-Банк"):
                       
                       return "https://private.auth.alfabank.ru/passport/cerberus-mini-blue/dashboard-blue/username?response_type=code&client_id=click-web-adf&scope=openid%20click-web&acr_values=username&non_authorized_user=true"

                elif (self.value=="Газпромбанк"):
                       
                       return "https://ib.online.gpb.ru/"

                elif (self.value=="Россельхозбанк"):
                       
                       return "https://online.rshb.ru/cas-auth/index?forceAuth=true"

                elif (self.value=="Райффайзен Банк"):
                       
                       return "https://online.raiffeisen.ru/login/main"

                elif (self.value=="Росбанк"):
                       
                       return "https://online.rosbank.ru"

                elif (self.value=="Ак Барс Банк"):
                       
                       return "https://online.akbars.ru"


               
               
       
        def dialogClose(self):
               
               self.page.close_dialog()
        
               self.page.window_height=680

               self.page.update()


        def createBankAccount(self):
                
                check=False

                try:
                        for i in cardNumber.value:
                                
                                if (i!=" "):
                                
                                        int(i)

                        if (cardNumber.value==''):
                        
                                cardNumber.border_color=ft.colors.RED

                                check=True

                except Exception as ex: 

                        cardNumber.border_color=ft.colors.RED

                        check=True
                        

                try:

                        int(cardOverDate.value[0:2])
                        int(cardOverDate.value[3:])

                        if(cardOverDate.value==''):
                        
                                cardOverDate.border_color=ft.colors.RED

                                check=True
                        
                        if(int(cardOverDate.value.split("/")[0])>12 or int(cardOverDate.value.split("/")[0])<1):

                                cardOverDate.border_color=ft.colors.RED

                                check=True

                        if (int(cardOverDate.value.split("/")[1])>(datetime.datetime.now().year+7) or int(cardOverDate.value.split("/")[1])<22):

                                cardOverDate.border_color=ft.colors.RED

                                check=True

                except Exception as ex:

                        cardOverDate.border_color=ft.colors.RED

                        check=True


                if(Lib.strCheckOnEnglish(cardOwner.value)!=True and cardOwner.value==''):
                       
                       cardOwner.border_color=ft.colors.RED

                       check=True

                
                try:

                        int(cardCVC.value)

                        if(cardCVC.value==''):
                        
                                cardCVC.border_color=ft.colors.RED

                                check=True
                
                except Exception as ex:

                        cardCVC.border_color=ft.colors.RED

                        check=True
                        


                if(cardBankName.value==''):
                       
                       cardBankName.border_color=ft.colors.RED

                       check=True


                if (check==False):

                        bankURL=choiceBankURL(bankAccountURLControl)

                        if (cardPincode.value=="" or cardPincode.value==None):

                                bd.reqExecute(f"Update Bank_Accounts SET Number='{Lib.encryption(cardNumber.value)}', Date='{Lib.encryption(cardOverDate.value)}', CVC='{Lib.encryption(cardCVC.value)}', Card_Owner='{Lib.encryption(cardOwner.value)}', PIN_Code='0', Bank_Name='{Lib.encryption(cardBankName.value)}', Bank_URL='{bankURL}' where ID={int(dataForCompare.split(':')[0])}")

                        else:
                               
                                bd.reqExecute(f"Update Bank_Accounts SET Number='{Lib.encryption(cardNumber.value)}', Date='{Lib.encryption(cardOverDate.value)}', CVC='{Lib.encryption(cardCVC.value)}', Card_Owner='{Lib.encryption(cardOwner.value)}', PIN_Code='{Lib.encryption(cardPincode.value)}', Bank_Name='{Lib.encryption(cardBankName.value)}', Bank_URL='{bankURL}' where ID={int(dataForCompare.split(':')[0])}")

                        
                        self.page.close_dialog()

                        Lib.updateUserCardList(self, self.page.controls[0].controls[2].content.controls[1].content, "bank")
                        
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

                    self.page.update()





        cardNumber=ft.TextField(hint_text="Номер карты", max_length=19, on_change=maskedTextFieldNumber, color=ft.colors.BLACK)
        cardOverDate=ft.TextField(hint_text="Дата окончания действия карты", max_length=5, on_change=maskedTextFieldDate, color=ft.colors.BLACK)
        cardOwner=ft.TextField(hint_text="Владелец карты (на английском)", color=ft.colors.BLACK)
        cardCVC=ft.TextField(hint_text="CVC-код", password=True,can_reveal_password=True, color=ft.colors.BLACK)
        cardBankName=ft.TextField(hint_text="Название банка (на любом языке)", color=ft.colors.BLACK)

        cardPincode=ft.TextField(hint_text="Pin-код от карты", password=True, can_reveal_password=True, color=ft.colors.BLACK)
        bankAccountURLControl=ft.Dropdown(width=190, options=[
               
               ft.dropdown.Option("Сбербанк"),
               ft.dropdown.Option("Т-Банк"),
               ft.dropdown.Option("Альфа-Банк"),
               ft.dropdown.Option("Газпромбанк"),
               ft.dropdown.Option("Россельхозбанк"),
               ft.dropdown.Option("Райффайзен Банк"),
               ft.dropdown.Option("Росбанк"),
               ft.dropdown.Option("Ак Барс Банк"),

        ], filled=True, fill_color="#E4E6F3", color=ft.colors.BLACK)


        dataForCompare=self.control.data
        
        result=bd.reqExecute("Select * from Bank_Accounts")

        userArr=[]

        for i in result:

                userArr.append([str(i[0]), Lib.deecrypt(i[1]), Lib.deecrypt(i[2]), Lib.deecrypt(i[3]), Lib.deecrypt(i[4]), Lib.deecrypt(i[5]), Lib.deecrypt(i[6]), i[7]])

        
        for i in userArr:

                if (i[0]==dataForCompare.split(":")[0] and i[1]==dataForCompare.split(":")[1]):

                        cardNumber.value=i[1]
                        cardOverDate.value=i[2]
                        cardOwner.value=i[4]
                        cardCVC.value=i[3]
                        cardBankName.value=i[6]
                        cardPincode.value=i[5]


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

                                        ]),

                                        ft.Row([
                                             
                                                ft.Text("", width=3),
                                      
                                                ft.Text("Ссылка на личный кабинет", size=15, color=ft.colors.BLACK),

                                                ft.Text("", width=30),

                                                bankAccountURLControl


                                      ])
                               
                               ]), bgcolor="#D9D9D9", width=550, height=200, border_radius=14)

        ], height=670, width=470, horizontal_alignment=ft.CrossAxisAlignment.START), actions=[
                                        
                                        ft.ElevatedButton("Изменить", bgcolor="#D9D9D9", color=ft.colors.BROWN_200,height=33,width=100, on_click=createBankAccount),
                                        ft.ElevatedButton("Отмена", bgcolor="#E4E6F3",height=33,width=100, on_click=dialogClose)

                                ], on_dismiss=dialogClose)
        

        self.page.show_dialog(bankAccount)

        self.page.window_height=820

        self.page.update()





def maskedTextFieldNumber(self):

        if (keyboard.is_pressed("Backspace")==False):
       
                if(len(self.control.value) in [4,9,14]):
                
                        self.control.value+=" "

        self.page.update()



def maskedTextFieldDate(self):

        if (keyboard.is_pressed("Backspace")==False):

                if (len(self.control.value)==1 and self.control.value!="0"):
                
                        self.control.value="0"+self.control.value+"/"
        
                elif(len(self.control.value)==2):
                
                        self.control.value+="/"

        self.page.update()

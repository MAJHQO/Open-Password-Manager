import string,config as config,flet as ft, typing, logging, datetime,bd, requests, guiLib,base64,pyperclip,time

from random import randint
from cryptography.fernet import Fernet





def createMPassword(self):

    passLen=randint(10,25)

    mPassword=""

    lettersPassword_arr=list(string.ascii_letters)
    numberPassword_arr=list(string.digits)
    symbolPassword_arr=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


    for i in range(1,passLen+1):

        if (i%2==0):

            mPassword+=lettersPassword_arr[randint(0, len(lettersPassword_arr))]
        

        elif (i%2==1):

            if(i%3==1):

                mPassword+=numberPassword_arr[randint(0,len(numberPassword_arr))]

            else:

                mPassword+=symbolPassword_arr[randint(0,len(symbolPassword_arr))]


    return mPassword,config.fernet_token



def encryption(data: str, InitializationToken:bool=False) -> bytes:
    
    """
    data: string data for encryption
    """

    try:

        key=base64.urlsafe_b64encode(config.token.encode()[0:32])

        fernetObj=Fernet(key)
    
        result=fernetObj.encrypt(data.encode())

        if (InitializationToken==True):

            return result.decode(), config.token.decode()
    
        else:

            return result.decode()
    
    except Exception as ex:

        print(ex)

    


def deecrypt(data: bytes)->str:
    """
    data: bytes data for decryption
    """

    try:

        key=base64.urlsafe_b64encode(config.token.encode()[0:32])

        fernetObj=Fernet(key)
    
        result=fernetObj.decrypt(data)

        return result.decode()
    
    except Exception as ex:

        print(ex)



def updateUserCardList(obj, cardList: ft.ListView, updatePage=""):

    try:

        if (obj.data=="0" or updatePage=='all'):

                    cardList.controls.clear()
                    cardList.controls.append(ft.Row([]))

                    
                    obj.page.controls[0].controls[2].content.controls[0].content.controls[0].value=" Главная"
                    obj.page.update()

                    
                    result=bd.reqExecute("Select * from Web_Accounts")

                    countElementIndex=0

                    totalDict={'ID':"",'Login': "", 'Password': "", "Service Name": ""}

                    for i in range (0,len(result)):

                        if (len(cardList.controls[countElementIndex].controls)<=4):

                            totalDict["ID"]=str(result[i][0])
                            totalDict["Login"]=deecrypt(result[i][1].encode())
                            totalDict["Password"]=deecrypt(result[i][2].encode())
                            totalDict["Service Name"]=deecrypt(result[i][3].encode())

                            userCard=createUserCard('web', totalDict)

                            cardList.controls[countElementIndex].controls.append(userCard)

                        else:

                            cardList.controls.append(ft.Row())
                            
                            countElementIndex+=1


                    result=bd.reqExecute("Select * from Bank_Accounts")

                    totalDict={'ID':"",'Number': "", 'Date': "", "CVC": "", 'Bank Name': "", 'Bank URL': ""}

                    for i in range (0,len(result)):

                        if (len(cardList.controls[countElementIndex].controls)<=4):

                            totalDict["ID"]=str(result[i][0])
                            totalDict["Number"]=deecrypt(result[i][1].encode())
                            totalDict["Date"]=deecrypt(result[i][2].encode())
                            totalDict["CVC"]=deecrypt(result[i][3].encode())
                            totalDict["Bank Name"]=deecrypt(result[i][6].encode())
                            totalDict["Bank URL"]=result[i][7]

                            userCard=createUserCard('bank', totalDict)

                            cardList.controls[countElementIndex].controls.append(userCard)

                        else:

                            cardList.controls.append(ft.Row())
                            
                            countElementIndex+=1

                
                    result=bd.reqExecute("Select * from Documents")

                    totalDict={'ID':"",'Filename': "", 'Format': "", "FileData": ""}

                    for i in range (0,len(result)):

                        if (len(cardList.controls[countElementIndex].controls)<=4):

                            totalDict["ID"]=str(result[i][0])
                            totalDict["Filename"]=deecrypt(result[i][1].encode())
                            totalDict["Format"]=deecrypt(result[i][2].encode())
                            totalDict["FileData"]=deecrypt(result[i][3].encode())

                            userCard=createUserCard('note', totalDict)

                            cardList.controls[countElementIndex].controls.append(userCard)

                        else:

                            cardList.controls.append(ft.Row())
                            
                            countElementIndex+=1


        elif (obj.data=="1" or updatePage=='web'):

                cardList.controls.clear()
                cardList.controls.append(ft.Row([]))

                obj.page.controls[0].controls[2].content.controls[0].content.controls[0].value=" Аккаунты"

                obj.page.update()

                result=bd.reqExecute("Select * from Web_Accounts")

                countElementIndex=0

                totalDict={'ID':"",'Login': "", 'Password': "", "Service Name": ""}

                for i in range (0,len(result)):

                    if (len(cardList.controls[countElementIndex].controls)<=4):

                        totalDict["ID"]=str(result[i][0])
                        totalDict["Login"]=deecrypt(result[i][1].encode())
                        totalDict["Password"]=deecrypt(result[i][2].encode())
                        totalDict["Service Name"]=deecrypt(result[i][3].encode())

                        userCard=createUserCard('web', totalDict)

                        cardList.controls[countElementIndex].controls.append(userCard)

                    else:

                        cardList.controls.append(ft.Row())
                        
                        countElementIndex+=1


        elif (obj.data=="2" or updatePage=='bank'):

            result=bd.reqExecute("Select * from Bank_Accounts")

            cardList.controls.clear()
            cardList.controls.append(ft.Row([]))

            obj.page.controls[0].controls[2].content.controls[0].content.controls[0].value=" Банковские данные"
            obj.page.update()

            countElementIndex=0

            totalDict={'ID':"",'Number': "", 'Date': "", "CVC": "", 'Bank Name': "", 'Bank URL': ""}

            for i in range (0,len(result)):

                if (len(cardList.controls[countElementIndex].controls)<=4):

                    totalDict["ID"]=str(result[i][0])
                    totalDict["Number"]=deecrypt(result[i][1].encode())
                    totalDict["Date"]=deecrypt(result[i][2].encode())
                    totalDict["CVC"]=deecrypt(result[i][3].encode())
                    totalDict["Bank Name"]=deecrypt(result[i][6].encode())
                    totalDict["Bank URL"]=result[i][7]

                    userCard=createUserCard('bank', totalDict)

                    cardList.controls[countElementIndex].controls.append(userCard)

                else:

                    cardList.controls.append(ft.Row())
                    
                    countElementIndex+=1


        elif (obj.data=="3" or updatePage=='note'):

            result=bd.reqExecute("Select * from Documents")

            cardList.controls.clear()
            cardList.controls.append(ft.Row([]))

            obj.page.controls[0].controls[2].content.controls[0].content.controls[0].value=" Заметки"
            obj.page.update()

            countElementIndex=0

            totalDict={'ID':"",'Filename': "", 'Format': "", "FileData": ""}

            for i in range (0,len(result)):

                if (len(cardList.controls[countElementIndex].controls)<=4):

                    totalDict["ID"]=str(result[i][0])
                    totalDict["Filename"]=deecrypt(result[i][1].encode())
                    totalDict["Format"]=deecrypt(result[i][2].encode())
                    totalDict["FileData"]=deecrypt(result[i][3].encode())

                    userCard=createUserCard('note', totalDict)

                    cardList.controls[countElementIndex].controls.append(userCard)

                else:

                    cardList.controls.append(ft.Row())
                    
                    countElementIndex+=1

    except Exception as ex:

        pass



def createUserCard(type: str, data: dict[str,typing.Any]) -> ft.Card:

    """
    type: One of type data in app ('web', 'bank', 'note')
    
    data: 
        
        - If data type 'web': dict should consist of these key like {'ID',Login', 'Password', 'Service Name' (URL)}
        - If  data type 'bank': should consist of these key like {'ID','Number', 'Date', 'CVC', 'Bank Name', 'Bank URL'}
        - If  data type 'note': should consist of these key like {'ID','Filename', 'Format', 'FileData'}
    """


    def openLinkButton(self):
               
        if (self.control.data.split(":")[0]=="OPENLINK"):

            url=self.control.data.split("OPENLINK:")[1]

            if (url.find("https://")==-1):

                self.page.launch_url("https://"+url)

            else:

                self.page.launch_url(url)

        
        elif(self.control.data.split(":")[0]=="COPY"):

            pass





    if (type.lower()=='web'):

        if ("Login" in data.keys() and "Password" in data.keys() and "Service Name" in data.keys()):

            login=data['Login']
            password=""
            serviceURL=data['Service Name']

            if ("www." in data['Service Name']):

                serviceURL=data['Service Name'].split("www.")[1]

            elif ("https://" in data['Service Name']):

                serviceURL=data['Service Name'].split("https://")[1]

            
            if ("/" in serviceURL):

                serviceURL=serviceURL.split("/")[0]


            for i in range(0, len(data['Password'])):

                password+="•"

            
            #serviceIcon=ft.Container(content=ft.Image(url))

            
            card=ft.Card(content=
                                                                
                ft.Column(width=250, height=300, controls=[
                    
                    ft.Row(width=270, height=40, controls=[
                                                                                                                
                        ft.CupertinoListTile(title=ft.Text(serviceURL.split(".")[0], color=ft.colors.BLACK, font_family="Kufam_SemiBold"), subtitle=ft.Text(serviceURL, color=ft.colors.BLACK, size=14), leading=ft.CircleAvatar(foreground_image_url="https://"+serviceURL+"/favicon.ico", bgcolor=ft.colors.TRANSPARENT, max_radius=14, radius=14),width=210, padding=0),
                                                                
                        ft.Column([
                                                                    
                                ft.IconButton(icon=ft.icons.SETTINGS, icon_size=16, icon_color=ft.colors.WHITE, padding=0,on_click=guiLib.changeUserCardWeb, data=data['ID']+":"+data['Service Name'])],
                                    horizontal_alignment=ft.CrossAxisAlignment.START, width=30, height=50)],
                                    alignment=ft.MainAxisAlignment.CENTER, vertical_alignment=ft.CrossAxisAlignment.CENTER, spacing=0
                        ), 

                    ft.Divider(),

                    ft.Text(""),
                                                                                        
                    ft.Container(content=
                                                                        
                    ft.Row([

                        ft.Text("",width=4),
                                                                                                                    
                        ft.Text(width=150, height=23,value=login,disabled=True, color=ft.colors.BLACK, size=15, text_align=ft.TextAlign.START),
                        ft.Text("", width=30),
                        ft.IconButton(ft.icons.COPY, icon_size=18, icon_color=ft.colors.BLACK, padding=0, data="Login:"+data['Login'], on_click=copyInBufferCard)

                    ], spacing=0,vertical_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.START, width=400), bgcolor=ft.colors.TRANSPARENT, border=ft.border.all(0.7,ft.colors.BLACK), width=227, border_radius=14),
                                                                                                            

                    ft.Container(content=
                                                                                
                        ft.Row([

                            ft.Text("",width=4),

                            ft.Text(width=150, height=28,value=password,disabled=True, color=ft.colors.BLACK, size=15, text_align=ft.TextAlign.START),
                            ft.Text("", width=30),
                            ft.IconButton(ft.icons.COPY, icon_size=18, icon_color=ft.colors.BLACK, padding=0, data="Password:"+data['Password'], on_click=copyInBufferCard)

                        ], spacing=0, vertical_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.START), bgcolor=ft.colors.TRANSPARENT, border=ft.border.all(0.7,ft.colors.BLACK), width=227, border_radius=14),

                    ft.Text(""),

                    ft.ElevatedButton("Перейти на сайт",icon=ft.icons.LINK, bgcolor="#CAC8C8", width=180, color=ft.colors.BLACK, data="OPENLINK:"+serviceURL, on_click=openLinkButton)

                                                                                                            
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER), color="#D9D9D9", shadow_color=ft.colors.BLACK,shape=ft.RoundedRectangleBorder(14)
                
            )
    

            #print (requests.get(f"https://{serviceURL}/favicon.ico").content.find("404 Not Found"))

            try:
        
                if (str(requests.get(f"https://{serviceURL}/favicon.ico").content).find("404 Not Found")==-1):

                    return card
                
                else:

                    card.content.controls[0].controls[0].leading=ft.CircleAvatar(foreground_image_url="https://i.pinimg.com/736x/94/9b/4a/949b4a6abbc47da3905dd3ce46cac226.jpg", bgcolor=ft.colors.TRANSPARENT, max_radius=20,radius=20)

                    return card
                
            except Exception as ex:

                card.content.controls[0].controls[0].leading=ft.CircleAvatar(foreground_image_url="https://i.pinimg.com/736x/94/9b/4a/949b4a6abbc47da3905dd3ce46cac226.jpg", bgcolor=ft.colors.TRANSPARENT, max_radius=20,radius=20)

                return card

        else:

            logging.error(f"[{datetime.datetime.now()}] :: There is not one or more dictation keys")



    elif (type.lower()=='bank'):

        if ("Number" in data.keys() and "CVC" in data.keys() and "Date" in data.keys() and "Bank Name" in data.keys() and "Bank URL" in data.keys()):

            allnumber=data['Number']
            number=""
            cvcCode=""

            i=0
            
            while (i<len(allnumber)):

                if (i == 0):

                    number+=allnumber[i:4]

                    i+=3

                elif(i == 14):

                    number+=allnumber[15:]

                    break

                else:

                    if (allnumber[i:i+1]==" "):

                        number+=" "

                    else:
                        
                        number+="•"
                
                i+=1

            for i in range(0, len(data['CVC'])):

                cvcCode+="•"  

            
            
            card = ft.Card(content=
                                                                        
                        ft.Column(width=250, height=300, controls=[
                            
                            ft.Row(width=270, height=40, controls=[
                                                                                                                        
                                ft.CupertinoListTile(title=ft.Text(data['Bank Name'], color=ft.colors.BLACK, font_family="Kufam_SemiBold"), leading=ft.Image("Icons\MastercardLogo.png", border_radius=14), width=210, padding=0),
                                                                        
                                ft.Column([
                                                                            
                                        ft.IconButton(icon=ft.icons.SETTINGS, icon_size=16, icon_color=ft.colors.WHITE, padding=0, data=data['ID']+":"+data['Number'], on_click=guiLib.changeUserCardBank)],
                                            horizontal_alignment=ft.CrossAxisAlignment.START, width=30, height=50)],
                                            alignment=ft.MainAxisAlignment.CENTER, vertical_alignment=ft.CrossAxisAlignment.CENTER, spacing=0
                                ), 

                            ft.Divider(),

                            ft.Text(""),
                                                                                                
                            ft.Container(content=
                                                                                
                                ft.Row([
                                                                                                                                
                                    ft.Text(width=170, height=38,value=number,disabled=True, color=ft.colors.BLACK, size=15, text_align=ft.TextAlign.CENTER, font_family="Kufam_SemiBold"),
                                    ft.Text("", width=20),
                                    ft.IconButton(ft.icons.COPY, icon_size=18, icon_color=ft.colors.BLACK, padding=0, data="Number:"+data['Number'], on_click=copyInBufferCard)

                                ], spacing=0,vertical_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.START), bgcolor=ft.colors.TRANSPARENT, border=ft.border.all(0.7,ft.colors.BLACK), width=227, border_radius=14, alignment=ft.Alignment(0.0, 0.0)),
                                                                                                                    

                            ft.Container(content=
                                                                                        
                                ft.Row([

                                    ft.Text("", width=25),

                                    ft.Text(value=data['Date'],disabled=True, color=ft.colors.BLACK, size=15, text_align=ft.TextAlign.CENTER, font_family="Kufam_SemiBold"),
                                    ft.Text("", width=4),
                                    ft.IconButton(ft.icons.COPY, icon_size=18, icon_color=ft.colors.BLACK, padding=0,data="OverDate:"+data['Date'], on_click=copyInBufferCard),

                                    ft.Text("", width=40),

                                    ft.Text(cvcCode,disabled=True, color=ft.colors.BLACK, size=15, text_align=ft.TextAlign.CENTER),
                                    ft.Text("", width=4),
                                    ft.IconButton(ft.icons.COPY, icon_size=18, icon_color=ft.colors.BLACK, padding=0, data="CVC:"+data['CVC'], on_click=copyInBufferCard)

                                ], spacing=0, vertical_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.START), bgcolor=ft.colors.TRANSPARENT, width=227),


                            ft.Text(""),

                            ft.ElevatedButton("Перейти на сайт",icon=ft.icons.LINK, bgcolor="#CAC8C8", width=180, color=ft.colors.BLACK, data="OPENLINK:"+data['Bank URL'], on_click=openLinkButton)

                                                                                                                    
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER), color="#D9D9D9", shadow_color=ft.colors.BLACK,shape=ft.RoundedRectangleBorder(14)
                        
                )
                
     
            
            if (data['Number'][1:2]=="2"):

                card.content.controls[0].controls[0].leading=ft.Image("Icons\MirLogo.png",border_radius=14)

            elif (data['Number'][1:2]=="4"):

                card.content.controls[0].controls[0].leading=ft.Image("Icons\VisaLogo.png",border_radius=14)

            elif(data['Number'][1:2]=="5"):

                card.content.controls[0].controls[0].leading=ft.Image("Icons\MastercardLogo.png",border_radius=14)

            
            return card
        
        else:

            logging.error(f"[{datetime.datetime.now()}] :: There is not one or more dictation keys")



    
    elif (type.lower()=='note'):

        if ("Filename" in data.keys() and "Format" in data.keys()):
                
                filedata=data["FileData"]
                
                
                if (data['Format'] in ["docx", 'rtf']):
                
                    return ft.Card(content=
                                                                    
                        ft.Column(width=250, height=300, controls=[
                            
                            ft.Row(width=270, height=40, controls=[

                                ft.Text("", width=10),

                                ft.CircleAvatar(foreground_image_src="Icons\\Notes.jpg", max_radius=14,radius=14),

                                ft.Text("", width=45),
                                                                                                                        
                                ft.Text(data["Filename"], size=15, color=ft.colors.BLACK, width=75, max_lines=1, font_family="Kufam_SemiBold"),

                                ft.Text("", width=40),
                                                                        
                                ft.PopupMenuButton(icon=ft.icons.SETTINGS, icon_size=20, icon_color=ft.colors.WHITE, padding=0, data=data['ID']+":"+data['Filename'])
                                
                                ], alignment=ft.MainAxisAlignment.START, vertical_alignment=ft.CrossAxisAlignment.CENTER, spacing=0
                                ), 

                            ft.Divider(),

                            #ft.Text(""),
                                                                                                
                            ft.Container(content=ft.Image("Image\WordFileIcon.png"), width=230, height=160, padding=0, bgcolor=ft.colors.TRANSPARENT),

                            ft.Row([ft.IconButton(ft.icons.COPY, icon_size=24, icon_color=ft.colors.BLACK, padding=0, data=data["FileData"], on_click=copyInBufferCard)], alignment=ft.MainAxisAlignment.CENTER)

                                                                                                                    
                            ], horizontal_alignment=ft.CrossAxisAlignment.START), color="#D9D9D9", shadow_color=ft.colors.BLACK,shape=ft.RoundedRectangleBorder(14)
                        
                )

                else:

                    return ft.Card(content=
                                                                    
                        ft.Column(width=250, height=300, controls=[
                            
                            ft.Row(width=270, height=40, controls=[

                                ft.Text("", width=10),

                                ft.CircleAvatar(foreground_image_src="Icons\\Notes.jpg", max_radius=14,radius=14),

                                ft.Text("", width=45),
                                                                                                                        
                                ft.Text(data["Filename"], size=15, color=ft.colors.BLACK, width=75, max_lines=1, font_family="Kufam_SemiBold"),

                                ft.Text("", width=40),
                                                                        
                                ft.PopupMenuButton(icon=ft.icons.SETTINGS, icon_size=20, icon_color=ft.colors.WHITE, padding=0)
                                
                                ], alignment=ft.MainAxisAlignment.START, vertical_alignment=ft.CrossAxisAlignment.CENTER, spacing=0
                                ), 

                            ft.Divider(),

                            #ft.Text(""),
                                                                                                
                            ft.Container(content=ft.Image("Image\\NotesFileIcon.png"), width=230, height=160, padding=0, bgcolor=ft.colors.TRANSPARENT),

                            ft.Row([ft.IconButton(ft.icons.COPY, icon_size=24, icon_color=ft.colors.BLACK, padding=0, data=data["FileData"])], alignment=ft.MainAxisAlignment.CENTER)

                                                                                                                    
                            ], horizontal_alignment=ft.CrossAxisAlignment.START), color="#D9D9D9", shadow_color=ft.colors.BLACK,shape=ft.RoundedRectangleBorder(14)
                        
                )

            
        else:

                logging.error(f"[{datetime.datetime.now()}] :: There is not one or more dictation keys")


def strCheckOnEnglish(text:str):

    check=False

    english_ACSI_upper=[65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90]

    #english_ACSI_lower=[97,98,99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110,111, 112, 113, 114, 115, 116 ,117, 118, 119, 120, 121]

    for i in text:

        if (ord(i) in english_ACSI_upper):

            check=True

        else:

            check=False

    return check


def copyInBufferCard(self):

    if (self.control.data.split(":")[0]=="Number"):

        pyperclip.copy(self.control.data.split(":")[1])

        self.control.icon_color=ft.colors.GREEN_300
        self.page.update()

        time.sleep(1)

        self.control.icon_color=ft.colors.BLACK
        self.page.update()

        

    elif (self.control.data.split(":")[0]=="OverDate"):

        pyperclip.copy(self.control.data.split(":")[1])

        self.control.icon_color=ft.colors.GREEN_300
        self.page.update()

        time.sleep(1)

        self.control.icon_color=ft.colors.BLACK
        self.page.update()

    elif (self.control.data.split(":")[0]=="CVC"):

        pyperclip.copy(self.control.data.split(":")[1])

        self.control.icon_color=ft.colors.GREEN_300
        self.page.update()

        time.sleep(1)

        self.control.icon_color=ft.colors.BLACK
        self.page.update()

    elif (self.control.data.split(":")[0]=="Login"):

        pyperclip.copy(self.control.data.split(":")[1])

        self.control.icon_color=ft.colors.GREEN_300
        self.page.update()

        time.sleep(1)

        self.control.icon_color=ft.colors.BLACK
        self.page.update()

    elif (self.control.data.split(":")[0]=="Password"):

        pyperclip.copy(self.control.data.split(":")[1])

        self.control.icon_color=ft.colors.GREEN_300
        self.page.update()

        time.sleep(1)

        self.control.icon_color=ft.colors.BLACK
        self.page.update()
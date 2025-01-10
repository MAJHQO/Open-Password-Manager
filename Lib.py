import string,config,os,flet as ft, typing, logging, datetime

from random import randint
from cryptography.fernet import Fernet

ferNet=None

if (os.path.exists("information.txt")==True):

        with open("information.txt", "r") as file:

            config.fernet_token=file.readlines()[1]

            ferNet=Fernet(config.fernet_token.encode())

else:

    pKey=Fernet.generate_key()

    ferNet=Fernet(pKey)

    config.fernet_token=pKey



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



def encryption(data: str, Initialization_Fernet_Token:bool) -> bytes:
    
    """
    data: string data for encryption
    """

    try:
    
        key=ferNet.encrypt(data.encode())

    except Exception as ex:

        print(ex)

    if (Initialization_Fernet_Token==True):

        return key.decode(), config.fernet_token.decode()
    
    else:

        return key.decode()

    


def deecrypt(data: bytes)->str:
    """
    data: bytes data for decryption
    """

    try:

        data=ferNet.decrypt(data)

    except Exception as ex:

        print(ex)

    return data.decode()




def createUserCard(type: str, data: dict[str,typing.Any]) -> ft.Card:

    """
    type: One of type data in app ('web', 'bank', 'doc')
    
    data: 
        
        - If data type 'web': dict should consist of these key like {'Login', 'Password', 'Service Name' (URL)}
        - If  data type 'bank': should consist of these key like {'Number', 'Date', 'CVC', 'Bank Name', 'Bank URL'}
        - If  data type 'doc': should consist of these key like {'Filename', 'Format', 'Photo'(In Bytes), 'PageCount' (if file is PDF, PPTX, DOCX)}
    """

    if (type.lower()=='web'):

        if ("Login" in data.keys() and "Password" in data.keys() and "Service Name" in data.keys()):

            login=data['Login']
            password=data['Password']
            serviceName=""

            if (data['Service Name'] in "www."):

                serviceName=data['Service Name'].split("www.")[1]
                serviceName=serviceName.split(serviceName)[0]

            else:

                serviceName=serviceName.split(serviceName)[0]

            for i in range(0, len(password)):

                password[i]="•"

                                                
            return ft.Card(content=
                                                                
                ft.Column(width=250, height=300, controls=[
                    
                    ft.Row(width=270, height=40, controls=[
                                                                                                                
                        ft.CupertinoListTile(title=ft.Text(data, color=ft.colors.BLACK), subtitle=ft.Text(serviceName, color=ft.colors.BLACK, size=14), leading=ft.Image("Icons\\userCardLogo.ico"), width=210, padding=0),
                                                                
                        ft.Column([
                                                                    
                                ft.PopupMenuButton(icon=ft.icons.SETTINGS, icon_size=16, icon_color=ft.colors.WHITE, padding=0),],
                                    horizontal_alignment=ft.CrossAxisAlignment.START, width=30, height=50)],
                                    alignment=ft.MainAxisAlignment.CENTER, vertical_alignment=ft.CrossAxisAlignment.CENTER, spacing=0
                        ), 

                    ft.Divider(),

                    ft.Text(""),
                                                                                        
                    ft.Container(content=
                                                                        
                    ft.Row([
                                                                                                                    
                        ft.Text(width=150, height=28,value=login,disabled=True, color=ft.colors.BLACK, size=15, text_align=ft.TextAlign.CENTER),
                        ft.Text("", width=35),
                        ft.IconButton(ft.icons.COPY, icon_size=18, icon_color=ft.colors.BLACK, padding=0, data=data['Login'])

                    ], spacing=0,vertical_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.START), bgcolor=ft.colors.TRANSPARENT, border=ft.border.all(0.7,ft.colors.BLACK), width=227, border_radius=14),
                                                                                                            

                    ft.Container(content=
                                                                                
                        ft.Row([

                            ft.Text(width=150, height=28,value=password,disabled=True, color=ft.colors.BLACK, size=15, text_align=ft.TextAlign.CENTER),
                            ft.Text("", width=35),
                            ft.IconButton(ft.icons.COPY, icon_size=18, icon_color=ft.colors.BLACK, padding=0, data=data['Password'])

                        ], spacing=0, vertical_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.START), bgcolor=ft.colors.TRANSPARENT, border=ft.border.all(0.7,ft.colors.BLACK), width=227, border_radius=14),

                    ft.Text(""),

                    ft.ElevatedButton("Перейти на сайт",icon=ft.icons.LINK, bgcolor="#CAC8C8", width=180, color=ft.colors.BLACK, data="Open websiste: "+data['Service Name'])

                                                                                                            
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER), color="#D9D9D9", shadow_color=ft.colors.BLACK,shape=ft.RoundedRectangleBorder(14)
                
        )
    
        else:

            logging.error(f"[{datetime.datetime.now()}] :: There is not one or more dictation keys")


    elif (type.lower()=='bank'):

        if ("Number" in data.keys() and "CVC" in data.keys() and "Date" in data.keys() and "Bank Name" in data.keys() and "Bank URL" in data.keys()):

            number=""
            cvcCode=data['CVC']

            
            for i in range(0, len(data['Number'])):

                if (i in [0,1,2,3]):

                    number+=data['Number'][i]

                elif(i in [len(data['Number'])-1, len(data['Number'])-2]):

                    number+=data['Number'][i]

                else:

                    number+="•"

            for i in range(0, len(0, len(data['CVC']))):

                cvcCode[i]="•"  
            

            card = ft.Card(content=
                                                                    
                    ft.Column(width=250, height=300, controls=[
                        
                        ft.Row(width=270, height=40, controls=[
                                                                                                                    
                            ft.CupertinoListTile(title=ft.Text(data['Bank Name'], color=ft.colors.BLACK), leading=ft.Image("Icons\MirLogo.png", border_radius=40), width=210, padding=0),
                                                                    
                            ft.Column([
                                                                        
                                    ft.PopupMenuButton(icon=ft.icons.SETTINGS, icon_size=16, icon_color=ft.colors.WHITE, padding=0),],
                                        horizontal_alignment=ft.CrossAxisAlignment.START, width=30, height=50)],
                                        alignment=ft.MainAxisAlignment.CENTER, vertical_alignment=ft.CrossAxisAlignment.CENTER, spacing=0
                            ), 

                        ft.Divider(),

                        ft.Text(""),
                                                                                            
                        ft.Container(content=
                                                                            
                            ft.Row([
                                                                                                                            
                                ft.Text(width=150, height=28,value=data['Number'],disabled=True, color=ft.colors.BLACK, size=15, text_align=ft.TextAlign.CENTER),
                                ft.Text("", width=35),
                                ft.IconButton(ft.icons.COPY, icon_size=18, icon_color=ft.colors.BLACK, padding=0)

                            ], spacing=0,vertical_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.START), bgcolor=ft.colors.TRANSPARENT, border=ft.border.all(0.7,ft.colors.BLACK), width=227, border_radius=14),
                                                                                                                

                        ft.Container(content=
                                                                                    
                            ft.Row([

                                ft.Text("", width=25),

                                ft.Text(value=data['Date'],disabled=True, color=ft.colors.BLACK, size=15, text_align=ft.TextAlign.CENTER),
                                ft.Text("", width=4),
                                ft.IconButton(ft.icons.COPY, icon_size=18, icon_color=ft.colors.BLACK, padding=0),

                                ft.Text("", width=40),

                                ft.Text(data['CVC'],disabled=True, color=ft.colors.BLACK, size=15, text_align=ft.TextAlign.CENTER),
                                ft.Text("", width=4),
                                ft.IconButton(ft.icons.COPY, icon_size=18, icon_color=ft.colors.BLACK, padding=0)

                            ], spacing=0, vertical_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.START), bgcolor=ft.colors.TRANSPARENT, width=227),


                        ft.Text(""),

                        ft.ElevatedButton("Перейти на сайт",icon=ft.icons.LINK, bgcolor="#CAC8C8", width=180, color=ft.colors.BLACK, data="Open website: "+data['Bank URL'])

                                                                                                                
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER), color="#D9D9D9", shadow_color=ft.colors.BLACK,shape=ft.RoundedRectangleBorder(14)
                    
            )


            if (data["Number"][0]=="2"):

                card.content.controls[0].controls[0].leading=ft.Image("Icons\MirLogo.png", border_radius=40)

            elif (data["Number"][0]=="4"):

                card.content.controls[0].controls[0].leading=ft.Image("Icons\VisaLogo.png", border_radius=40)

            elif(data["Number"][0]=="5"):

                card.content.controls[0].controls[0].leading=ft.Image("Icons\MastercardLogo.png", border_radius=40)

            
            return card
        
        else:

            logging.error(f"[{datetime.datetime.now()}] :: There is not one or more dictation keys")



    
    elif (type.lower()=='note'):

        if ("Filename" in data.keys() and "Format" in data.keys()):
                
                #Реализовать открытие и чтение текста из файла

                return ft.Card(content=
                                                                
                    ft.Column(width=250, height=300, controls=[
                        
                        ft.Row(width=270, height=40, controls=[

                            ft.Text("", width=10),

                            ft.Image("Icons\\Notes.jpg", border_radius=100, width=31,height=31),

                            ft.Text("", width=45),
                                                                                                                    
                            ft.Text("ToDo List", size=17, color=ft.colors.BLACK, width=75),

                            ft.Text("", width=40),
                                                                    
                            ft.PopupMenuButton(icon=ft.icons.SETTINGS, icon_size=20, icon_color=ft.colors.WHITE, padding=0)
                            
                            ], alignment=ft.MainAxisAlignment.START, vertical_alignment=ft.CrossAxisAlignment.CENTER, spacing=0
                            ), 

                        ft.Divider(),

                        #ft.Text(""),
                                                                                            
                        ft.Container(content=
                                                                            
                            ft.Text(value=ft.Markdown(value="asd").value,size=13,color=ft.colors.BLACK, selectable=True).value, width=210, height=140, padding=0, bgcolor=ft.colors.TRANSPARENT
                            
                            ),

                        ft.Row([ft.IconButton(ft.icons.COPY, icon_size=24, icon_color=ft.colors.BLACK, padding=0, data="asd")], alignment=ft.MainAxisAlignment.CENTER)

                                                                                                                
                        ], horizontal_alignment=ft.CrossAxisAlignment.START), color="#D9D9D9", shadow_color=ft.colors.BLACK,shape=ft.RoundedRectangleBorder(14)
                    
            )

            
        else:

                logging.error(f"[{datetime.datetime.now()}] :: Photo data type isn't Byte")
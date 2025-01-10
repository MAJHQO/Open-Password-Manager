import flet as ft, bd,time

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

        def dialogClose(self):
               
               self.page.close_dialog(webAccount_Add)

               self.page.update()

        
        def createWebAccount(self):
               
                serviceURL=""
                login=""
                password=""

                check=False
               
                if (webURLField.value!=None):
                      
                        serviceURL=webURLField.value

                else:
                       
                        webURLField.border_color=ft.colors.RED

                        check=True


                if (loginField.value!=None):
                       
                       login=loginField.value

                else:
                       
                       loginField.border_color=ft.colors.RED

                       check=True

                
                if (passwordField.value!=None):
                       
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

                        self.page.close_banner(webAccount_Add)

                        self.page.update()



        webURLField=ft.TextField(hint_text="Например google.com", height=40)
        loginField=ft.TextField(hint_text="Логин")
        passwordField=ft.TextField(hint_text="Пароль")
        
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

                                                ft.Text("",width=0),

                                                ft.IconButton(icon=ft.icons.PASSWORD_SHARP, icon_size=25, tooltip="Показать пароль"),

                                                passwordField,

                                                ft.IconButton(icon=ft.icons.KEY, icon_size=20, tooltip="Сгенерировать пароль"),

                                            ]),
                                            
                                    ],width=500), bgcolor="#D9D9D9", border_radius=14,width=500,height=220),
                                    

                                ], width=500, height=280), title=ft.Text("Добавление учетной записи"),title_text_style=ft.TextStyle(color=ft.colors.BLACK,size=20) , bgcolor="#E4E6F3",actions=[
                                        
                                        ft.ElevatedButton("Создать", bgcolor="#D9D9D9", color=ft.colors.BROWN_200,height=33,width=100, on_click=createWebAccount),
                                        ft.ElevatedButton("Отмена", bgcolor="#E4E6F3",height=33,width=100)

                                ]
                                
            )

        self.page.show_dialog(dialog=webAccount_Add)
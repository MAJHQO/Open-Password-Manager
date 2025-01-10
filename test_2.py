import flet as ft


def test(page:ft.Page):

    def clickButton(self):

        self.open(webAccount_Add)

        self.update()

    def dialogClose(dialog: ft.AlertDialog, page: ft.Page):
       
       page.close_dialog(dialog)

       page.update()


    def saveUserData(self):

        serviceURL=""
        login=""
        password=""

        if (self.page.controls[0].content.controls[0].controls[1].value!=None):

            serviceURL=self.page.controls[0].content.controls[0].controls[1].value

        else:

            self.page.controls[0].content.controls[0].controls[1].border_color=ft.colors.RED

        
        if (self.page.controls[0].content.controls[2].content.controls[2].controls[3].value != None):

            login=self.page.controls[0].content.controls[2].content.controls[2].controls[3].value

        else:

            self.page.controls[0].content.controls[2].content.controls[2].controls[3].border_color=ft.colors.RED

        
        if (self.page.controls[0].content.controls[2].content.controls[3].controls[3].value != None):

            password=self.page.controls[0].content.controls[2].content.controls[3].controls[3].value

        else:

            self.page.controls[0].content.controls[2].content.controls[3].controls[3].border_color=ft.colors.RED

        self.page.update()

        #time.sleep(1)

        self.page.controls[0].content.controls[0].controls[1].border_color=ft.colors.BLACK
        self.page.controls[0].content.controls[2].content.controls[2].controls[3].border_color=ft.colors.BLACK
        self.page.controls[0].content.controls[2].content.controls[3].controls[3].border_color=ft.colors.BLACK

        self.page.update()

        self.page.close_banner(webAccount_Add)
        
        self.page.update()

        print(serviceURL,login,password)






    webAccount_Add=ft.AlertDialog(content=
                                
                                ft.Column([

                                    ft.Row([

                                        ft.Text("Веб-адрес сайта: ",size=15, color=ft.colors.BLACK, width=120),

                                        ft.TextField(hint_text="Например google.com", height=40),

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

                                                ft.TextField(hint_text="Логин"),

                                            ]),

                                            
                                            ft.Row([

                                                ft.Text("",width=3),

                                                ft.Text("Пароль", size=15, color=ft.colors.BLACK),

                                                ft.Text("",width=0),

                                                ft.IconButton(icon=ft.icons.PASSWORD_SHARP, icon_size=25, tooltip="Показать пароль"),

                                                ft.TextField(hint_text="Пароль"),

                                                ft.IconButton(icon=ft.icons.KEY, icon_size=20, tooltip="Сгенерировать пароль"),

                                            ]),
                                            
                                    ],width=500), bgcolor="#D9D9D9", border_radius=14,width=500,height=220),
                                    

                                ], width=500, height=280), title=ft.Text("Добавление учетной записи"),title_text_style=ft.TextStyle(color=ft.colors.BLACK,size=20) , bgcolor="#E4E6F3",actions=[
                                        
                                        ft.ElevatedButton("Создать", bgcolor="#D9D9D9", color=ft.colors.BROWN_200,height=33,width=100, on_click=saveUserData),
                                        ft.ElevatedButton("Отмена", bgcolor="#E4E6F3",height=33,width=100, on_click= lambda dlg: dialogClose(dlg.control,page))

                                ]
                                
            )


    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Please confirm"),
        content=ft.Text("Do you really want to delete all those files?"),
        actions=[
            ft.TextButton("Yes"),
            ft.TextButton("No"),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=lambda e: print("Modal dialog dismissed!"),)
    
    page.add(webAccount_Add,ft.ElevatedButton("Open dialog", on_click=lambda a: clickButton(page)))



ft.app(test)
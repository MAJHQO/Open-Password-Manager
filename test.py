import flet as ft, requests,json



def test_page(page:ft.Page):

    page.window_height=750
    page.window_width=1200

    cardListView=ft.ListView(spacing=10)

    mainCardContainer=ft.Container(width=1200, height=750, bgcolor=ft.colors.TRANSPARENT,content=ft.Row(controls=[], spacing=10) ,alignment=ft.Alignment(-1.0,-1.0))

    noteText=ft.Text("""1. Генерация пользовательских карточек с базовыми проверками, **кроме заметок**
  2. Создание отдельных окон (по категориям) добавления пользовательских карточек и занесение введенных данных в бд
  3. Создание навигации по приложению:
	  - Главное меню (Все записи)
	  - Аккаунты
	  - Банковские данные
	  - Заметки
  4. Актуализация кнопки "Добавить" и ее подпунктов в главном меню
  5. Добавление нового функционала в генерацию карточки "Заметки":
	  - Открытие нужного файла, чтение и копирование ограниченного кол-ва информации в карточку (ограничение по кол-ву символов)
  6. Реализация алгоритмов шифрования (при записи) и расшифрования (при чтении) пользовательских данных с бд
  7. Изучение Windows API и реализация ограничения доступа к информационной директории +шифрование самих данных на уровне ОС""", size=11, color=ft.colors.BLACK)
    
    plch=ft.Card(content=
                                                                
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
                                                                            
                            ft.Text(value=ft.Markdown(value=noteText).value,size=13,color=ft.colors.BLACK, selectable=True).value, width=210, height=140, padding=0, bgcolor=ft.colors.TRANSPARENT
                            
                            ),

                        ft.Row([ft.IconButton(ft.icons.COPY, icon_size=24, icon_color=ft.colors.BLACK, padding=0, data=noteText)], alignment=ft.MainAxisAlignment.CENTER)

                                                                                                                
                        ], horizontal_alignment=ft.CrossAxisAlignment.START), color="#D9D9D9", shadow_color=ft.colors.BLACK,shape=ft.RoundedRectangleBorder(14)
                    
            )
    
    mainCardContainer.content.controls.append(plch)
    mainCardContainer.content.controls.append(plch)

    page.add(mainCardContainer)


ft.app(target=test_page)



# ft.Card(content=ft.Column(width=250, height=300, controls=[
                    
#                     ft.Row(width=270, height=35, controls=[
#                         ft.CupertinoListTile(title=ft.Text("Google"), subtitle=ft.Text("https://google.com/account"), leading=ft.Image("Icons\\userCardLogo.ico"), width=210, padding=0),
#                         ft.Column([
#                             ft.PopupMenuButton(icon=ft.icons.SETTINGS, icon_size=16, icon_color=ft.colors.WHITE, padding=0),

#                         ], horizontal_alignment=ft.CrossAxisAlignment.START, width=30, height=50)
                        
#                     ], alignment=ft.MainAxisAlignment.CENTER, vertical_alignment=ft.CrossAxisAlignment.CENTER, spacing=0), 

#                     ft.Divider(),

#                     ft.Text(""),
 
#                     ft.Container(content=ft.Row([
#                         ft.TextField(label="Логин", width=200, height=50, value="There was be Kevin", bgcolor=ft.colors.BLACK, disabled=True),
#                         ft.IconButton(ft.icons.COPY, icon_size=15, icon_color=ft.colors.WHITE, padding=0)
#                     ], spacing=0), width=240, height=50, bgcolor=ft.colors.BLACK, padding=0, border_radius=2),
                    
#                     #ft.TextField(label="Логин", width=200, height=50, value="There was be Kevin"),
#                     ft.TextField(label="Пароль", width=200, height=50, password=True, value="There was be Kevin"),

#                     ft.Text(""),

#                     ft.ElevatedButton("Перейти на сайт",icon=ft.icons.LINK, bgcolor=ft.colors.TRANSPARENT, width=180)

                    
#                 ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
#                 )
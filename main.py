import flet as ft, sqlite3 as sq
import os, logging, bd, guiLib as gLib, hashlib, Lib, pywin32_system32



def main_menu(page:ft.Page):

    def pageChange(self):

        Lib.updateUserCardList(self, cardListView)





    page.clean()

    page.title="Open Password Manager"
    page.connection.page_name="Main Menu"

    page.fonts={"Kufam":"Fonts\\Kufam.ttf", "Kufam_SemiBold": "Fonts\\Kufam-SemiBold.ttf"}

    page.bgcolor="#E4E6F3"
    page.window_height=680
    page.window_width=1312


    cardListView=ft.ListView(controls=[ft.Row([])], expand=1)


    leftElementContainer=ft.Container(content=ft.Column([
        ft.Text("   OPEN", size=35, font_family="Kufam_SemiBold", color=ft.colors.BLACK), 
        ft.Text("      password manager", size=18, color=ft.colors.BLACK,font_family="Kufam_SemiBold"), 
        
        ft.Text(""), 
        
        ft.NavigationRail(label_type=ft.NavigationRailLabelType.ALL, group_alignment=-0.9 , indicator_color="#B0ADAD" , width=220,height=500, bgcolor="#D9D9D9", unselected_label_text_style=ft.TextStyle(color="#333333", size=15), selected_label_text_style=ft.TextStyle(color=ft.colors.BLACK, size=15), selected_index=0, destinations=[
        
            ft.NavigationDestination(label="Все записи", icon=ft.icons.NOTES, selected_icon=ft.Icons.NOTES_ROUNDED), 
            ft.NavigationDestination(label="\tАккаунты", icon=ft.icons.ACCOUNT_TREE_OUTLINED,selected_icon=ft.Icons.ACCOUNT_TREE_ROUNDED),
            ft.NavigationDestination(label="Банковские данные", icon=ft.icons.CREDIT_CARD_OUTLINED, selected_icon=ft.icons.CREDIT_CARD_ROUNDED),
            ft.NavigationDestination(label="Заметки", icon=ft.icons.NOTE_SHARP)], on_change=pageChange)
        
            ]),
        
        alignment=ft.Alignment(-1.0,0.0), bgcolor="#D9D9D9", width=220, height=500)
    
    topElementContainer=ft.Container(content=
                                     
                                    ft.Column([

                                        ft.Container(content=ft.Column([

                                            ft.Text(" Главная", size=23, color=ft.colors.BLACK, font_family="Kufam_SemiBold"),
                                        
                                        
                                            ft.PopupMenuButton(content=ft.Row([

                                                ft.Image("Icons\plus.svg", color=ft.colors.WHITE, width=27,height=27), 
                                                ft.Text("Добавить", size=15, color=ft.colors.WHITE), 
                                                ft.Image("Icons\chevron-down.svg", width=27, height=27,color=ft.colors.WHITE)
                                                
                                                ], width=150, alignment=ft.MainAxisAlignment.START), items=[
                                                    ft.PopupMenuItem("Аккаунт",data="Account", on_click=gLib.createWebAccountData),
                                                    ft.PopupMenuItem("Банковские данные",data="Bank Data", on_click=gLib.createBankAccountData),
                                                    ft.PopupMenuItem("Заметки",data="Notes", on_click=gLib.addNoteData)
                                                ], shadow_color=ft.colors.BLACK, bgcolor="#B0ADAD", padding=0),

                                        ], width=1050, height=100), width=1050, height=100, bgcolor="#D9D9D9"),


                                        ft.Container(content=cardListView, width=1050, height=550, bgcolor=ft.colors.TRANSPARENT)
                                        


                                        ]), bgcolor=ft.colors.TRANSPARENT, height=500,width=1050

    )
    
    
    #mainElementContainer=ft.Container(content=ft.Row(),bgcolor=ft.colors.RED, width=650, height=500, alignment=ft.Alignment(0.6,0.4),padding=0)

    page.add(ft.Row([leftElementContainer, ft.Text("", width=5), topElementContainer], spacing=0, vertical_alignment=ft.CrossAxisAlignment.START))

    #ft.Column([mainElementContainer], height=750, width=1200,alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.START)

    page.update()



def account_menu(page: ft.Page):

    pass
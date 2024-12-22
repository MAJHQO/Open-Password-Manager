import flet as ft, sqlite3 as sq,os, logging,bd

logging.basicConfig(level=logging.INFO, filename="\SoftLog.txt", filemode="w")


def start(page: ft.Page):

    def focusField(self):

        if (hasattr(self.control, "border_color")):

            self.control.border_color="#354733"

        else:

           # self.control.bgcolor="#354733"

           pass

        page.update()

    def unBlockSoft(self):

        #userKey=mainKeyField.content.value

        pass

    try:


        page.title=" "
        page.connection.page_name="start"

        page.fonts={"Kufam":"Fonts\Kufam.ttf"}

        page.bgcolor="#E4E6F3"
        page.window_height=670
        page.window_width=1200

        mainSoftName=ft.Row(controls=[ft.Container(ft.Image("Icons\Logo.png", width=226, height=226,color=ft.colors.BLACK), alignment=ft.Alignment(0, 0)),ft.Container(ft.Text("Open Password Manager", size=35, color=ft.colors.BLACK), alignment=ft.Alignment(0,1))])

        mainKeyField=ft.Container(content=ft.TextField(label="Мастер пароль", hint_text="Введите мастер-пароль",width=300, on_blur=focusField),alignment=ft.Alignment(0,0))

        enterButton=ft.Container(content=ft.ElevatedButton("Разблокировать", on_click=unBlockSoft, on_hover=focusField,bgcolor=ft.colors.TRANSPARENT, color="#354733"), alignment=ft.alignment.center)

        page.add(mainSoftName)

    except Exception as ex:

        logging.error(f"[ERROR]: {ex}")






if __name__=="__main__":

    ft.app(target=start)

    logging.info("")
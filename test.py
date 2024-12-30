import flet as ft



def test(page:ft.Page):

    page.add(ft.Row([ft.ElevatedButton("ra"), ft.Text("as")]))

ft.app(test)
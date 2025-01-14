import requests, flet as ft


def test_page(page: ft.Page):

    page.add(ft.CircleAvatar(foreground_image_url="https://www.amazon.com/favicon.ico"), ft.CircleAvatar(foreground_image_url="https://github.com/favicon.ico"))


ft.app(target=test_page)
    

import flet as ft, time, Lib, bd, os, shutil, datetime

from start import logging

from flet import FilePickerResultEvent, FilePicker

def addNoteData(self):
       
        def dialogClose(self):
               
               self.page.close_dialog()
               
               self.page.window_height=680

               self.page.update()

        
        def selectNoteFile(me: FilePickerResultEvent):
               
                noteFile["Path"]=me.files[0].path
                noteFile["SelectedFile"]=me.files[0].name

                addNoteFile.content.controls[0].content.controls[2].value=f"Файл '{noteFile["SelectedFile"]}' успешно выбран\n\nНе забудьте удалить выбранный файл, с целью безопасности хранения текущего"
                addNoteFile.content.controls[0].content.controls[2].text_align=ft.TextAlign.CENTER
                
                addNoteFile.content.controls[0].content.controls[0].src="Image\DownloadSuccess.png"

                addNoteFile.content.controls[0].content.controls[0].width=300
                addNoteFile.content.controls[0].content.controls[0].height=300
                
                addNoteFile.actions[0].disabled=False

                self.page.update()
        
        def createNoteData(self):
               
                try:
                        shutil.copy(noteFile["Path"], ".\\Data")

                        bd.reqExecute("Insert into")

                        self.page.close_dialog()

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

                                ft.Text("Нажмите в данной области для загрузки файла", size=14, color="")
                            
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER), width=500, height=420, bgcolor=ft.colors.TRANSPARENT, border_radius=14, on_click=lambda a:selectedNoteFile.pick_files(allow_multiple=False, initial_directory=os.path.expanduser('~')+"\\Downloads"))

        ], height=570, width=470, horizontal_alignment=ft.CrossAxisAlignment.CENTER), actions=[
                                        
                                        ft.ElevatedButton("Создать", bgcolor="#D9D9D9", color=ft.colors.BROWN_200,height=33,width=100, on_click=createNoteData, disabled=True),
                                        ft.ElevatedButton("Отмена", bgcolor="#E4E6F3",height=33,width=100, on_click=dialogClose)

                                ])
        
        self.page.overlay.extend([selectedNoteFile])

        self.page.show_dialog(addNoteFile)

        self.page.window_height=745

        self.page.update()



def test_page(page:ft.Page):
       
       page.add(ft.ElevatedButton("Open dialog", on_click=addNoteData))


ft.app(test_page)
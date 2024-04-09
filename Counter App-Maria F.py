#code
import flet as ft
# To understand how to center buttons: https://www.youtube.com/watch?v=-mZP91Y3naY&list=PL4KX3oEgJcfdiE-S3qLqATrsMg2Nddosx


def main(page: ft.Page):

    # Page configuration
    page.title = "Counter APP"
    page.window_height = 400
    page.window_width = 250
    page.window_max_height = page.window_height
    page.window_max_width = page.window_width
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    img = ft.Image(src=f"pet/pet.png")
    page.window_center()

    # Components configuration
    counter = ft.Text(value=0, size=50)

    def decrease_number(e):
        counter.value = counter.value - 1
        page.update()

    def increase_number(e):
        counter.value = counter.value + 1
        page.update()

    btn_d = ft.FloatingActionButton(text="-", on_click=decrease_number)
    btn_i = ft.FloatingActionButton(text="+", on_click=increase_number)

    # Adding components to page.
    page.add(
        ft.Row([counter], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row(
            [btn_d, btn_i], alignment=ft.MainAxisAlignment.CENTER
        ), img )
    page.update()


ft.app(target=main)

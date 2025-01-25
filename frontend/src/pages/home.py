import flet as ft

def HomePage(page: ft.Page):
    return ft.View(
        "/",
        controls=[
            ft.Text("Bem-vindo à Página Inicial!", size=30),
            ft.ElevatedButton("Ir para Página 1", on_click=lambda _: page.go("/page1")),
            ft.ElevatedButton("Ir para Página 2", on_click=lambda _: page.go("/page2")),
        ],
    )
import flet as ft

def Page2(page: ft.Page):
    return ft.View(
        "/page2",
        controls=[
            ft.Text("Você está na Página 2", size=30),
            ft.ElevatedButton("Voltar ao Início", on_click=lambda _: page.go("/")),
            ft.ElevatedButton("Ir para Página 1", on_click=lambda _: page.go("/page1")),
        ],
    )
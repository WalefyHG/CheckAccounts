import flet as ft
import requests


def Page1(page: ft.Page):
    
    response = requests.get("http://localhost:8000/api/teste/")
    
    
    return ft.View(
        "/page1",
        controls=[
            ft.Text("Você está na Página 1", size=30),
            ft.Text(response.content, size=30),
            ft.ElevatedButton("Voltar ao Início", on_click=lambda _: page.go("/")),
            ft.ElevatedButton("Ir para Página 2", on_click=lambda _: page.go("/page2")),
        ],
    )

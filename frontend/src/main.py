import flet as ft
from pages.home import HomePage
from pages.page1 import Page1
from pages.page2 import Page2

def main(page: ft.Page):

    def route_change(route):
        page.views.clear()
        match page.route:
            case "/":
                page.views.append(HomePage(page))
            case "/page1":
                page.views.append(Page1(page))
            case "/page2":
                page.views.append(Page2(page))
            case _:
                page.go("/")
        page.update()

    
    def view_pop(view):
        page.views.pop()
        if page.views:
            page.go(page.views[-1].route)


    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go("/") 

ft.app(target=main)

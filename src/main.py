import flet
import flet as ft
from flet import (
    Page, View,
    RouteChangeEvent,
    ViewPopEvent,
)

from views.log_in import login
from views.dashboard import dashboard

# Template
def main(page: Page) -> None:
    page.title = "Regista"

    page.window.height = 802
    page.window.width = 1245

    page.fonts = {
        "medium": "font/sky-medium.ttf",
        "regular": "font/sky-regular.ttf"
    }

    def route_change(e: RouteChangeEvent) -> None:
        # print(page.views)
        page.views.clear()
        # view home
        page.views.append(login(page))

        if page.route == "/dashboard":
            page.views.append(dashboard(page))

        #if page.route == "/page2":
        #    page.views.append(page_two(page))

        #if page.route == "/page3":
        #    page.views.append(page_three(page))

        page.update()

    def view_pop(e: ViewPopEvent) -> None:
        page.views.pop()
        top_view: View = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.go(page.route)


if __name__ == '__main__':
    ft.app(target=main)

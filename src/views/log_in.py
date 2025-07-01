import flet as ft
from flet import (
    Page,
    CupertinoTextField,
    View,
    Text,
    Container,
    FontWeight,
    Column,
    padding,
    MainAxisAlignment
)

from shared.themes import *

def login(page: Page) -> View:
    return View(
        route="/",
        bgcolor=green_shade_400,
        # padding=padding.symmetric(vertical=50, horizontal=100),
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        vertical_alignment=MainAxisAlignment.CENTER,
        controls=[
            Column(
                controls=[
                    Text(
                        value="regista",
                        size=120,
                        weight=FontWeight.W_400,
                        font_family="medium",
                        color=white
                    ),
                    Container(
                        height=1,
                        bgcolor=lower_white,
                        width=400
                    ),
                    Column(
                        width=300,
                        spacing=15,
                        controls=[
                            Column(height=20),
                            # User ID Input
                            CupertinoTextField(
                                placeholder_text="User ID",
                                placeholder_style=ft.TextStyle(
                                    font_family="regular",
                                    color="#90A4AE",
                                    size=18
                                ),
                                text_style=ft.TextStyle(
                                    font_family="medium",
                                    color=green_shade_400,
                                    size=18
                                ),
                                padding=ft.padding.symmetric(vertical=10, horizontal=20),
                                border=ft.border.all(width=1, color="#E0E0E0"),
                                border_radius=25
                            ),
                            # Passcode Input
                            CupertinoTextField(
                                placeholder_text="Passcode",
                                placeholder_style=ft.TextStyle(
                                    font_family="regular",
                                    color="#90A4AE",
                                ),
                                text_style=ft.TextStyle(
                                    font_family="regular",
                                    color=green_shade_400,
                                ),
                                padding=ft.padding.symmetric(vertical=10, horizontal=20),
                                border=ft.border.all(width=1, color="#E0E0E0"),
                                border_radius=25,
                                password=True
                            ),
                            Column(height=20),
                            Container(
                                content=Text(
                                    value="Log In",
                                    font_family="medium",
                                    size=16,
                                    color=white
                                ),
                                border=ft.border.all(width=1, color="#f5f5f7"),
                                on_click=lambda _: page.go("/dashboard"),
                                bgcolor=green_shade_300,
                                border_radius=25,
                                padding=ft.padding.symmetric(vertical=10, horizontal=40)
                            ),
                        ]
                    ),
                    Column(height=40),
                    Column(
                        spacing=0,
                        controls=[
                            Container(
                                content=Text(
                                    value="Report a Problem",
                                    font_family="medium",
                                    color=white
                                )
                            ),
                            Container(
                                content=Text(
                                    value="v0.1.0",
                                    font_family="regular",
                                    color=white
                                )
                            ),
                        ]
                    )
                ]
            ),
        ],
    )

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
    MainAxisAlignment,
    CrossAxisAlignment
)

from shared.themes import *
from components.buttons import *

def login(page: Page) -> View:
    return View(
        route="/",
        bgcolor=green_shade_400,
        # padding=padding.symmetric(vertical=50, horizontal=100),
        horizontal_alignment=CrossAxisAlignment.CENTER,
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
                            CustomTextField(texthint="User ID", show_password=False),
                            # Passcode Input
                            CustomTextField(texthint="Passcode", show_password=True),
                            Column(height=5),
                            CTAButton(text="Log In", animate=True, on_click=lambda _: page.go("/dashboard")),
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

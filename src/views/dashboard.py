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
    FontWeight,
    Row
)

from typing import Optional

from shared.themes import *


class CardButton(Container):
    def __init__(
        self,
        header: Optional[str] = None,
        desc: Optional[str] = None
        ):
        super().__init__()
        self.header = "Top Text" if header is None else header
        self.desc = "Bottom Text" if desc is None else desc

        self.content=Column(
            alignment=MainAxisAlignment.CENTER,
            spacing=5,
            controls=[
                Text(
                    value=self.header,
                    font_family="medium",
                    size=16,
                    color=white
                ),
                Text(
                    value=self.desc,
                    font_family="regular",
                    size=14,
                    color=white
                ),
            ]
        )
    
        self.border=ft.border.all(width=1, color="#f5f5f7")
        self.padding=padding.only(left=25)
        self.bgcolor="#08270A"
        self.border_radius=15
        self.height=100
        self.width=180


class TextInfo(Row):
    def __init__(self, head: str, tail: str):
        super().__init__()
        
        self.head = "Top text" if head is None else head
        self.tail = "Bottom text" if tail is None else tail

        self.controls = [
            Text(value=self.head, font_family="regular", color=white, size=18),
            Text(value=self.tail, font_family="medium", color=white, size=18),
        ]


def dashboard(page: Page) -> View:
    return View(
        route="/dashboard",
        padding=padding.symmetric(horizontal=150),
        bgcolor=green_shade_400,
        controls=[
            Column(height=60),
            # user image and name
            Row(
                controls=[
                    Container(
                        content=Text(
                            value="Go Back",
                            font_family="medium",
                            size=14,
                            color=white
                        ),
                        border=ft.border.all(width=1, color="#f5f5f7"),
                        bgcolor=green_shade_300,
                        border_radius=25,
                        padding=ft.padding.symmetric(vertical=10, horizontal=25),
                        on_click=lambda _: page.go("/login")
                    ),
                    Row(
                        controls=[
                            Container(
                                height=45,
                                width=45,
                                border_radius=25,
                                bgcolor=green_shade_300,
                                border=ft.border.all(width=1, color="#f5f5f7"),
                            ),
                            Text(
                                value="mirageOS",
                                font_family="regular",
                                size=16,
                                color=white
                            )
                        ]
                    ),
                ]
            ),
            # time, seconds, location name
            Row(
                spacing=20,
                controls=[
                    Text(
                        value="06:45",
                        font_family="regular",
                        size=180,
                        color=white
                    ),
                    Column(
                        spacing=0,
                        controls=[
                            Text(
                                value="34",
                                font_family="medium",
                                size=55,
                                color=white,
                            ),
                            Text(
                                value="Greater Accra\nGhana",
                                font_family="regular",
                                size=18,
                                color=white,
                                style=ft.TextStyle(
                                    height=1
                                )
                            ),
                        ]
                    )
                ]
            ),
            # line
            Container(
                height=1,
                bgcolor=lower_white,
                width=600
            ),
            Column(height=15),
            # today is Monday, June 24, 2025
            Row(
                controls=[
                    Text(
                        value="Today is ",
                        font_family="regular",
                        color=white,
                        size=30
                    ),
                    # Today
                    Text(
                        value="Monday",
                        font_family="regular",
                        color=green_shade_200,
                        size=30
                    ),
                    # Date
                    Text(
                        value="June 24, 2025",
                        font_family="medium",
                        color=white,
                        size=30
                    ),
                ]
            ),
            Column(height=25),
            # Cards [Clock card, activity logs, notifications, analytics]
            Row(
                spacing=20,
                controls=[
                    CardButton(header="Clock Card", desc="Clock In or Out"),
                    CardButton(header="Activity Logs", desc="Check your activity logs"),
                    CardButton(header="Notifications", desc="Your alerts & reminders"),
                    CardButton(header="Analytics", desc="Breakdown of working hours"),
                ]
            ),
            Column(height=40),
            # status (Clocked In), Last clock in, last clock out, system synced time
            Row(
                spacing=40,
                controls=[
                    Row(
                        controls=[
                            Text(value="Status", color=white, size=18, font_family="regular"),
                            Container(
                                content=Text(
                                    value="Clocked In",
                                    font_family="medium",
                                    size=16,
                                    color=white
                                ),
                                border=ft.border.all(width=1, color="#f5f5f7"),
                                bgcolor=green_shade_300,
                                border_radius=25,
                                padding=ft.padding.symmetric(vertical=10, horizontal=25)
                            ),
                        ]
                    ),
                    Container(height=20, width=2, bgcolor=lower_white),
                    Row(
                        spacing=40,
                        controls=[
                            TextInfo(head="header", tail="tailer"),
                            TextInfo(head="header", tail="tailer"),
                            TextInfo(head="header", tail="tailer"),
                        ]
                    ),
                ]
            ),
        ],
    )

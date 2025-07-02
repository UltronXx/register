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
    Row,
    ControlEvent
)

from typing import Optional

from shared.themes import *
from components.buttons import *


def dashboard(page: Page) -> View:
    return View(
        route="/dashboard",
        padding=padding.symmetric(horizontal=150),
        bgcolor=green_shade_400,
        controls=[
            Column(height=20),
            # user image and name
            Row(
                controls=[
                    CTAButton(text="Back", animate=True, on_click=lambda e: page.go("/login")),
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
                                    height=1.5
                                )
                            ),
                        ]
                    )
                ]
            ),
            # today is Monday, June 24, 2025
            Row(
                controls=[
                    Text(
                        value="Today is ",
                        font_family="regular",
                        color=white,
                        size=18
                    ),
                    # Today
                    Text(
                        value="Monday",
                        font_family="medium",
                        color=green_shade_200,
                        size=18
                    ),
                    # Date
                    Text(
                        value="June 24, 2025",
                        font_family="medium",
                        color=white,
                        size=18
                    ),
                ]
            ),
            Column(height=15),
            # line
            Container(
                height=1,
                bgcolor=lower_white,
                width=600
            ),
            Column(height=25),
            # Cards [Clock card, activity logs, notifications, analytics]
            Row(
                spacing=20,
                controls=[
                    FolderButton(folder_name="Clock Card", on_click=lambda e: print()),
                    FolderButton(folder_name="Activity Logs", on_click=lambda e: print()),
                    FolderButton(folder_name="Notifications", on_click=lambda e: print()),
                    FolderButton(folder_name="Analytics", on_click=lambda e: print()),
                    # CardButton(header="Clock Card", desc="Clock In or Out"),
                    # CardButton(header="Activity Logs", desc="Check your activity logs"),
                    # CardButton(header="Notifications", desc="Your alerts & reminders"),
                    # CardButton(header="Analytics", desc="Breakdown of working hours"),
                ]
            ),
            Column(height=20),
            # status (Clocked In), Last clock in, last clock out, system synced time
            Row(
                spacing=40,
                controls=[
                    Row(
                        controls=[
                            Text(value="Status", color=white, size=14, font_family="regular"),
                            CTAButton(text="Clocked In", animate=True),
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

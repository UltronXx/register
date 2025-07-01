import flet as ft
from flet import (
    Container,
    Row,
    Column,
    Text,
    MainAxisAlignment,
    border,
    padding,
    ControlEvent,
    AnimationCurve,
    Animation,
    CupertinoTextField,
    TextStyle
)

from typing import Optional, Any

from shared.themes import *

class CustomTextField(CupertinoTextField):
    def __init__(
      self,
      texthint: Optional[str] = None,
      show_password: Optional[bool] = None
      ):
      super().__init__()

      self.texthint = "Text Hint" if texthint is None else texthint
      self.show_password = False if show_password is None else show_password

      self.placeholder_text = self.texthint
      self.password = self.show_password

      self.placeholder_style = TextStyle(
          font_family="regular",
          color="#90A4AE",
          size=14
      )
      
      self.text_style=TextStyle(
          font_family="semibold",
          color=green_shade_400,
          size=14
      )
      self.padding=padding.symmetric(vertical=10, horizontal=20)
      self.border=border.all(width=1, color="#E0E0E0")
      self.border_radius=25



class CTAButton(Container):
    def __init__(
        self,
        text: Optional[str] = None,
        animate: Optional[bool] = None,
        on_click: Optional[Any] = None
        ):
      super().__init__(on_click=on_click)

      self.text = "CTA Button" if text is None else text
      self.animate = False if animate is None else animate
      
      self.content=Text(
            value=self.text,
            font_family="semibold",
            size=14,
            color=white
      )

      self.border = border.all(width=1, color="#f5f5f7")
      self.bgcolor = green_shade_300
      self.border_radius = 25
      self.padding = padding.symmetric(vertical=10, horizontal=20)



class CardButton(Container):
    def __init__(
        self,
        header: Optional[str] = None,
        desc: Optional[str] = None
        ):
        super().__init__()
        self.header = "Top Text" if header is None else header
        self.desc = "Bottom Text" if desc is None else desc

        self.content = Column(
            alignment=MainAxisAlignment.CENTER,
            spacing=5,
            controls=[
                Text(
                    value=self.header,
                    font_family="semibold",
                    size=14,
                    color=white
                ),
                Text(
                    value=self.desc,
                    font_family="regular",
                    size=12,
                    color=white
                ),
            ]
        )
    
        self.border = border.all(width=1, color="#f5f5f7")
        self.padding = padding.only(left=25)
        self.bgcolor = "#08270A"
        self.border_radius = 15
        self.height = 150
        self.width = 220

        self.scale = 1
        self.animate_scale = Animation(duration=100, curve=AnimationCurve.EASE_IN)

        self.on_hover = self.animate_hover

        # on hover
    def animate_hover(self, e: ControlEvent) -> None:
        self.scale = 1.05 if self.scale == 1 else 1
        self.update()



class TextInfo(Row):
    def __init__(self, head: str, tail: str):
        super().__init__()
        
        self.head = "Top text" if head is None else head
        self.tail = "Bottom text" if tail is None else tail

        self.controls = [
            Text(value=self.head, font_family="regular", color=white, size=14),
            Text(value=self.tail, font_family="semibold", color=white, size=14),
        ]

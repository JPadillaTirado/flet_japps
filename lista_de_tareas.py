import flet
from flet import *
from datetime import datetime
import sqlite3

class FormContainer(UserControl):
    def __init__(self):
        super().__init__()

    def build(self):
        return Container(
            width=280, 
            height=80,
            bgcolor="bluegrey500",
            opacity=1,
            border_radius=40,
            margin=margin.only(left=-20, right=-20),
            animate=animation.Animation(400,"decelerate"),
            animate_opacity=200,
            padding=padding.only(top=45, bottom=45),
        )





def main(page: Page):
    page.horizonal_alignment = "center"
    page.vertical_alignment = "center"

    def CreateToDoTask():
        pass

    _main_column_ = Column(
        scroll="hidden",
        expand=True,
        alignment=MainAxisAlignment.START,
        controls=[
            Row(
                alignment=MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    Text(
                        "Lista de tareas", size=20, weight="bold", color="White"),
                        IconButton(
                            icons.ADD_CIRCLE_ROUNDED,
                            icon_size=19,
                            on_click=lambda e: CreateToDoTask(e),
                        ),
                ],
            ),
            Divider(height=8, color="White"),
        ],
    
    )
    page.add(
        Container(
            width=1500,
            height=800,
            margin=-10,
            bgcolor="bluegrey900",
            alignment=alignment.center,
            content=Row(
                alignment=MainAxisAlignment.CENTER,
                vertical_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    Container(
                        width=280,
                        height=600,
                        bgcolor="#0f0f0f",
                        border_radius=40,
                        border= border.all(0.5, "white"),
                        padding=padding.only (top=35, left=20, right=20),
                        clip_behavior=ClipBehavior.HARD_EDGE,
                        content= Column(
                            alignment=MainAxisAlignment.CENTER,
                            expand=True,
                            controls=[
                                _main_column_,
                            FormContainer()
                            ],
                        ),
                    )
                ],
            ),
        )
    )
    page.update()
    form = page.controls[0].content.controls[0].content.controls[1].controls[0]

if __name__ == "__main__":
    flet.app(target=main)
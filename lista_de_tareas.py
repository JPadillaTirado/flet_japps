import flet
from flet import *
from datetime import datetime
import sqlite3

def main(page: Page):
    page.horizonal_alignment = "center"
    page.vertical_alignment = "center"

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
                        width=200,
                        height=600,
                        bgcolor="#0f0f0f",
                        border_radius=40,
                        border= border.all(0.5, "white"),
                        padding=padding.only (top=35, left=20, right=20)
                        clip_behavior=ClipBehavior.HARD_EDGE
                        content= collumn(
                            alignment=MainAxisAlignment.CENTER,
                            expand=True,
                            controls=[
                                main_column_,
                            ]
                        )
                    )
                ]
            )
        )
    )
    page.update()
    pass


if __name__ == "__main__":
    flet.app(target=main)
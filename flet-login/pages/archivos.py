from pages.login import *
import flet as ft
from flet import *
def build_archivos_container(page):
    conexion_obj = Conexion()

    archivos_container = Container(
        Column(
            controls=[
                Row([
                    Container(
                        content=ElevatedButton(
                            content=Text(
                                'Volver',
                                color='white',
                                weight='w500',
                            ),
                            width=180,
                            bgcolor='#2C3E50',
                            on_click=lambda _: page.go('/home')
                        )
                    ),
                    Container(
                        content=Text(
                            'ARCHIVOS', size=55, weight='bold', color='ffffff'
                        ),
                    ),
                ]),
                ElevatedButton(
                    content=Text(
                        'Subir Archivo',
                        color='white',
                        weight='w500',
                    ),
                    width=180,
                    bgcolor='#2C3E50',
                    #on_click=lambda _: 
                )
            ],
        ),
        padding=ft.padding.only(150),
    )
    return archivos_container
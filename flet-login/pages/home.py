from pages.login import *
import flet as ft
from flet import *
import math
def build_home_container(page):
    conexion_obj = Conexion()
    
    home_container = Container(
        Column(
            controls=[
                Row([
                    Text('H A R D       ', size=55, weight='bold', color='ffffff'), Text('  ', size=30, weight='bold', color='#2C3E50'), 
                    ElevatedButton(
                        content=Text(
                            'Cerrar Sesión',
                            color='white',
                            weight='w500'
                        ),
                        width=180,
                        bgcolor='#2C3E50',
                        on_click=lambda _: page.go('/')
                    )     
                ]),
                ElevatedButton(
                    content=Text(
                        'Archivos',
                        color='white',
                        weight='w500'
                    ),
                    width=180,
                    bgcolor='#2C3E50',
                    on_click=lambda _: page.go('/files')
                )
            ],
        ),
        padding=ft.padding.only(150),
        gradient=SweepGradient(
                center=ft.alignment.center,
                start_angle=0.0,
                end_angle=math.pi * 2,
                colors=[
                    "#07117E",
                    "#E404FF",
                    "#0024FF",
                    "#72E3FF",
                    "#07117E",
                ],
                stops=[0.0, 0.25, 0.5, 0.75, 1.0],
            ),
    )
    return home_container
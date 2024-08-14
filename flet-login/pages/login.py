from utils.conexion import *
import re
import flet as ft
from flet import *
import math

#waos

def build_login_container(page):
    conexion_obj = Conexion()
    def validar_login():
        def close_banner(e):
            page.banner.open = False
            page.update()
        def show_banner_click():
            page.banner.open = True
            page.update()
        
        email = email_textfield.content.value
        password = password_textfield.content.value

        if email == "" or password == "":
            page.banner = ft.Banner(
                bgcolor=ft.colors.RED,
                leading=ft.Icon(ft.icons.WARNING_AMBER_ROUNDED, color=ft.colors.AMBER, size=40),
                content=ft.Text(
                    "¡Error! Debe llenar todos los campos.",
                ),
                actions=[
                    ft.TextButton("Aceptar", on_click=close_banner),
                ],
            )
            show_banner_click()
            return
        
        if not conexion_obj.validar_password(password):
            page.banner = ft.Banner(
                bgcolor=ft.colors.RED,
                leading=ft.Icon(ft.icons.WARNING_AMBER_ROUNDED, color=ft.colors.AMBER, size=40),
                content=ft.Text(
                    "¡Error! La contraseña es incorrecta.",
                ),
                actions=[
                    ft.TextButton("Aceptar", on_click=close_banner),
                ],
            )
            show_banner_click()
            return
        if not conexion_obj.correo_existente(email):
            page.banner = ft.Banner(
                bgcolor=ft.colors.RED,
                leading=ft.Icon(ft.icons.WARNING_AMBER_ROUNDED, color=ft.colors.AMBER, size=40),
                content=ft.Text(
                    "¡Error! El correo es incorrecto.",
                ),
                actions=[
                    ft.TextButton("Aceptar", on_click=close_banner),
                ],
            )
            show_banner_click()
            return

        if conexion_obj.correo_existente(email) and conexion_obj.validar_password(password):
            page.go('/home')
        else:
            page.go('/')

    email_textfield = Container(
        content=TextField(
        width=280,
        height=40,
        hint_text='Correo electrónico',
        border='underline',
        prefix_icon=ft.icons.EMAIL,
    ), padding=ft.padding.only(35, 10))
    password_textfield = Container(
        content=TextField(
        width=280,
        height=40,
        hint_text='Contraseña',
        border='underline',
        prefix_icon=ft.icons.LOCK,
        password=True,
        can_reveal_password=True,
    ), padding=ft.padding.only(35, 10))

    login_container = Container(
        Column(
            controls=[
                Text(
                    'Iniciar Sesión',
                    width=360,
                    size=25,
                    weight='w900',
                    text_align='center',
                ),
                email_textfield,
                password_textfield,
                Row([
                    Text('       '),
                    ElevatedButton(
                        content=Text(
                            'ENTRAR',
                            color='white',
                            weight='w500',
                        ),
                        width=280,
                        bgcolor='#000000',
                        on_click=lambda _: validar_login()
                    ),
                ]),
                Row([
                    Text('¿No tiene cuenta?', size=15),
                    TextButton('Crear una cuenta.', on_click= lambda _: page.go('/registro')),
                ],
                alignment=MainAxisAlignment.CENTER),
            ],
            alignment=MainAxisAlignment.CENTER,
            spacing=30,
        ),
        gradient=LinearGradient(["#037c6e","#025043"]),
        width=350,
        height=500,
        border_radius=5,
    )
    return login_container
from utils.conexion import *
from app import *
import flet as ft
from flet import *
import re

def build_registro_container(page):
    conexion_obj = Conexion()
    def on_key_down(self, key):
        if key == "C-c":
            return True
    def registrar():

        def close_banner(e):
            page.banner.open = False
            page.update()

        def show_banner_click():
            page.banner.open = True
            page.update()

        name = name_textfield.content.value
        email = email_textfield.content.value
        password = password_textfield.content.value
        confirm_password = confirm_password_textfield.content.value
        
        if name == "" or email == "" or password == "" or confirm_password == "":
            # Verificar que los campos estén llenos
            page.banner = ft.Banner(
                bgcolor=ft.colors.RED,
                leading=ft.Icon(ft.icons.WARNING_AMBER_ROUNDED, color=ft.colors.AMBER, size=40),
                content=ft.Text(
                    "¡Error! Todos los campos son obligatorios.",
                ),
                actions=[
                    ft.TextButton("Aceptar", on_click=close_banner),
                ],
            )
            show_banner_click()
            return
        if not re.match(r"^(?=.*[A-Z])(?=.*[!@#$%^&*()-+])(?=.{8,})\S+$", password):
            page.banner = ft.Banner(
                bgcolor=ft.colors.RED,
                leading=ft.Icon(ft.icons.WARNING_AMBER_ROUNDED, color=ft.colors.WHITE, size=40),
                content=ft.Text(
                    "¡Error! La contraseña debe tener al menos 8 caracteres, una mayúscula y un símbolo."
                ),
                actions=[
                    ft.TextButton("Aceptar", on_click=close_banner),
                ],
            )
            show_banner_click()
            return
        if conexion_obj.correo_existente(email):
            page.banner = ft.Banner(
                bgcolor=ft.colors.RED,
                leading=ft.Icon(ft.icons.WARNING_AMBER_ROUNDED, color=ft.colors.WHITE, size=40),
                content=ft.Text(
                    "¡Error! Este correo electrónico ya está registrado."
                ),
                actions=[
                    ft.TextButton("Aceptar", on_click=close_banner),
                ],
            )
            show_banner_click()
            return      
        if password != confirm_password:
            # Manejar el caso en que las contraseñas no coincidan
            page.banner = ft.Banner(
                bgcolor=ft.colors.RED,
                leading=ft.Icon(ft.icons.WARNING_AMBER_ROUNDED, color=ft.colors.WHITE, size=40),
                content=ft.Text(
                    "¡Error! Las contraseñas no coinciden."
                ),
                actions=[
                    ft.TextButton("Aceptar", on_click=close_banner),
                ],
            )
            show_banner_click()
            return
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            page.banner = ft.Banner(
                bgcolor=ft.colors.RED,
                leading=ft.Icon(ft.icons.WARNING_AMBER_ROUNDED, color=ft.colors.WHITE, size=40),
                content=ft.Text(
                    "¡Error! Ingrese un correo electrónico válido."
                ),
                actions=[
                    ft.TextButton("Aceptar", on_click=close_banner),
                ],
            )
            show_banner_click()
            return
        else:
            page.banner = ft.Banner(
                bgcolor=ft.colors.GREEN,
                leading=ft.Icon(ft.icons.CHECK_ROUNDED, color=ft.colors.WHITE, size=40),
                content=ft.Text(
                    "Bienvenido, " + name + "!"
                    ),
                actions=[
                    ft.TextButton("Aceptar", on_click=close_banner),
                ],
            )
            show_banner_click()
            conexion_obj.ejecutar_consulta(name, email, password)
            return
        
    name_textfield = Container(
        content=TextField(
        width=280,
        height=40,
        hint_text='Nombre de Usuario',
        border='underline',
        prefix_icon=ft.icons.VERIFIED_USER,
    ), padding=ft.padding.only(35, 10))
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
    ), padding=ft.padding.only(35, 10))
    confirm_password_textfield = Container(
        content=TextField(
        width=280,
        height=40,
        hint_text='Confirmar Contraseña',
        border='underline',
        prefix_icon=ft.icons.LOCK,
        password=True,
        can_reveal_password=True,
    ), padding=ft.padding.only(35, 10))

    registro_container = Container(
        Column(
            controls=[
                Text(
                    'Registrarse',
                    width=360,
                    size=25,
                    weight='w900',
                    text_align='center'
                ),
                name_textfield,
                email_textfield,
                password_textfield,
                confirm_password_textfield,
                Row([
                    Text('      '),
                    ElevatedButton(
                        content=Text(
                            'REGISTRAR',
                            color='white',
                            weight='w500'
                        ),
                        width=280,
                        bgcolor='#000000',
                        on_click=lambda _: registrar()
                    ),
                ]),
                Container(    
                    IconButton(
                        icon="arrow_back", icon_color='white',
                        width=40,
                        bgcolor='#000000',
                        on_click=lambda _: page.go("/"),
                    ),
                    padding=ft.padding.only(153, 10)
                ),
                Row([
                    ft.IconButton(
                        icon=ft.icons.FACEBOOK,
                        icon_color=ft.colors.BLACK,
                        icon_size=35,
                    ),
                    ft.IconButton(
                        icon=ft.icons.EMAIL,
                        icon_color=ft.colors.BLACK,
                        icon_size=35,
                    ),
                    ],
                    alignment=MainAxisAlignment.CENTER,
                    spacing=50,
                    )
            ],
            alignment=MainAxisAlignment.CENTER,
        ),
        gradient=LinearGradient(["#037c6e","#025043"]),
        width=350,
        height=500,
        border_radius=5,
    )

    return registro_container

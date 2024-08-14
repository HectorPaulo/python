from pages.login import *
from pages.home import *
from pages.registro import *
from pages.archivos import *
#_______________________________________________
def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.SYSTEM
    page.title = "H A R D   -   alpha"
    page.window_height = 600
    page.window_width = 800
    # Construir los contenedores
    registro_container = build_registro_container(page)
    login_container = build_login_container(page)
    home_container = build_home_container(page)
    archivos_container = build_archivos_container(page)
    # ___________-Saltos de Página-__________.
    def route_change(e: RouteChangeEvent) -> None:
        # ----------> Página de Logueo
        page.views.clear()
        if page.route == '/':
            page.views.append(
                View(
                    route='/',
                    controls=[login_container],
                    vertical_alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    spacing=40
                )
            )
        elif page.route == '/registro':
            page.views.append(
                View(
                    route='/registro',
                    controls=[registro_container],
                    vertical_alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    spacing=46
                )
            )
        elif page.route == '/home':
            page.views.append(
                View(
                    route='/home',
                    controls=[home_container],
                    vertical_alignment=MainAxisAlignment.CENTER,
                    #horizontal_alignment=CrossAxisAlignment.CENTER,
                    spacing=46
                )
            )
        elif page.route == '/archivos':
            page.views.append(
                View(
                    route='/archivos',
                    controls=[archivos_container],
                    vertical_alignment=MainAxisAlignment.CENTER,
                    #horizontal_alignment=CrossAxisAlignment.CENTER,
                    spacing=46
                )
            )
        page.update()

    def view_pop(e: ViewPopEvent) -> None:
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)
if __name__ == '__main__':
    ft.app(target=main)

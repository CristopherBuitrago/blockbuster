from tools.menus import *
from tools.utils import clean_screen

while True:
    clean_screen()
    op = menu_principal
    if op == 1: # ADMINISTRADOR DE GENEROS
        clean_screen()
        menu_genders()
    elif op == 2: # ADMINISTRADOR DE ACTORES
        clean_screen()
        menu_actors()
    elif op == 3: # ADMINISTRADOR DE FORMATOS
        clean_screen()
        menu_formats()
    elif op == 4: # GESTOR DE INFORMES
        clean_screen()
        menu_info()
    elif op == 5: # GESTOR DE PELICULAS
        clean_screen()
        menu_movies()
    elif op == 6: # SALIR
        clean_screen()
        print('Vuelva pronto!')
        break
    
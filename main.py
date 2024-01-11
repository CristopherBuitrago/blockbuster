from source.actores import create_actor, list_actors
from source.formatos import create_format, list_formats
from source.peliculas import create_movie, delete_actor_by_id, delete_movie_by_id, edit_movie, find_movie_by_id, list_all_movies
from tools.menus import *
from tools.utils import clean_screen
from source.generos import create_gender, list_genders

# general functions
def genders ():
    clean_screen()
    op = menu_genders()
    if op == 1: # CREAR GENERO
        clean_screen()
        create_gender()
    elif op == 2: # LISTAR GENERO
        clean_screen()
        list_genders()
    elif op == 3:
        print('Saliendo...')
def actors ():
    clean_screen()
    op = menu_actors()
    if op == 1:
        clean_screen()
        create_actor()
    elif op == 2:
        clean_screen()
        list_actors()
    elif op == 3:
        print('Saliendo...')
def format ():
    op = menu_formats
    if op == 1: # crear formato
        clean_screen()
        create_format()
    elif op == 2:
        clean_screen()
        list_formats()
    elif op == 3: # listar formatos
        print('Saliendo...')
def movies ():
    op = menu_movies()
    if op == 1: 
        clean_screen()
        create_movie()
    elif op == 2:
        clean_screen()
        edit_movie()
    elif op == 3:
        clean_screen()
        delete_movie_by_id()
    elif op == 4:
        clean_screen()
        delete_actor_by_id()
    elif op == 5:
        clean_screen()
        find_movie_by_id()
    elif op == 6:
        clean_screen()
        list_all_movies()
    elif op == 7:
        print('Saliendo...')
# START
while True:
    clean_screen()
    op = menu_principal()
    if op == 1: # ADMINISTRADOR DE GENEROS
        genders()
    elif op == 2: # ADMINISTRADOR DE ACTORES
        actors()
    elif op == 3: # ADMINISTRADOR DE FORMATOS
        clean_screen()
        format()
    elif op == 4: # GESTOR DE INFORMES
        clean_screen()
        menu_info()
    elif op == 5: # GESTOR DE PELICULAS
        clean_screen()
        movies()
    elif op == 6: # SALIR
        clean_screen()
        print('Vuelva pronto!')
        break


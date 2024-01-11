from tools.utils import option_valide

def menu_principal():  # principal main
    print('*************<SISTEMA GESTOR DE PELICULAS BLOCKBUSTER>************')
    print('* 1.------------------------------------ADMINISTRADOR DE GENEROS *')
    print('* 2.------------------------------------ADMINISTRADOR DE ACTORES *')
    print('* 3.-----------------------------------ADMINISTRADOR DE FORMATOS *')
    print('* 4.------------------------------------------GESTOR DE INFORMES *')
    print('* 5.---------------------------------------- GESTOR DE PELICULAS *')
    print('* 6.-------------------------------------------------------SALIR *')
    print('******************************************************************')
    op = option_valide('Choose: ', 1, 6)
    return op  # this line to return the user's choice

def menu_genders(): # genders main
    print('************<GESTOR DE GENEROS>************')
    print('* 1.-------------------------CREAR GENERO *')
    print('* 2.-----------------------LISTAR GENEROS *')
    print('* 3.--------------------------------SALIR *')
    print('*******************************************')
    op = option_valide('Choose: ',1,3)
    return op

def menu_actors(): # actors main
    print('************<GESTOR DE ACTORES>************')
    print('* 1.--------------------------CREAR ACTOR *')
    print('* 2.-------------------------LISTAR ACTOR *')
    print('* 3.--------------------------------SALIR *')
    print('*******************************************')
    op = option_valide('Choose: ',1,3)
    return op

def menu_formats (): # formats main
    print('************<GESTOR DE FORMATOS>************')
    print('* 1.------------------------CREAR FORMATOS *')
    print('* 2.-----------------------LISTAR FORMATOS *')
    print('* 3.---------------------------------SALIR *')
    print('*********************************************')
    op = option_valide('Choose: ',1,3)
    return op

def menu_info ():# main info
    print('****************************[GESTOR DE INFORMES]***************************')
    print('* 1.-------------------------LISTAR LAS PELICULAS DE UN GENERO ESPECIFICO *')
    print('* 2.----LISTAR LAS PELICULAS DONDE EL PROTAGONISTA SEA SILVESTER STALLONE *')
    print('* 3.------------------BUSCAR PELICULA Y MOSTRAR LA SINOPSIS Y LOS ACTORES *')
    print('* 4.----------------------------------------------------------------SALIR *')
    print('***************************************************************************')
    op = option_valide('Choose: ',1,4)
    return op

def menu_movies (): # main movies
    print('****************[GESTOR DE PELICULAS]***************')
    print('* 1.------------------------------AGREGAR PELICULA *')
    print('* 2.-------------------------------EDITAR PELICULA *')
    print('* 3.-----------------------------ELIMINAR PELICULA *')
    print('* 4.--------------------------------ELIMINAR ACTOR *')
    print('* 5.-------------------------------BUSCAR PELIUCLA *')
    print('* 6.--------------------LISTAR TODAS LAS PELICULAS *')
    print('* 7.-----------------------------------------SALIR *')
    print('****************************************************')
    op = option_valide('Choose: ',1,7)
    return op
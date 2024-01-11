from tools.utils import clean_screen,load_json, code_generator, save_json, key_to_continue

movie_list = load_json("peliculas")

def create_gender_movie():
    num_entry = 0
    genders = {}

    while True:
        try:
            name_gender = input('Ingrese el nombre del género: ')
            num_entry += 1

            code_gender = code_generator('G', num_entry, num_entry)

            if name_gender:
                for code in code_gender:
                    genders[code] = {
                        "id": code,
                        "nombre": name_gender
                    }

            another_entry = input('¿La película posee otro género? [y/n]: ')
            if another_entry.lower() != 'y':
                return genders
            else:
                clean_screen()

        except Exception as e:
            print(f"Error: {e}")

def create_actor_movie(): # create actor
    num_entry = 0
    actors = {}

    while True:
        try:
            # Solicitar el nombre del género
            name_actor = input('Ingrese el nombre del actor: ')
            rol = input('Ingrese el rol del actor: ')
            num_entry += 1

            # Código generador
            code_actor = code_generator('A', num_entry, num_entry)

            # Crear un diccionario con la información del género
            if name_actor:
                for code in code_actor:
                    actors[code] = {
                        "id": code,
                        "nombre": name_actor,
                        "rol": rol
                    }

            # Preguntar si quiere agregar otro género
            another_entry = input('¿Desea agregar otro actor? [y/n]: ')
            if another_entry.lower() == 'y':
                clean_screen()
            elif another_entry.lower() == 'n':
                return actors
            else:
                print('Opción no reconocida')
                break

        except Exception as e:
            print(f"Error: {e}")

def create_format_movie(): # create format
    num_entry = 0
    formats = {}

    while True:
        try:
            # Solicitar el nombre del género
            name_format = input('Ingrese el nombre del formato: ')
            num_entry += 1

            # Código generador
            code_format = code_generator('F', num_entry, num_entry)

            # Crear un diccionario con la información del género
            if name_format:
                for code in code_format:
                    formats[code] = {
                        "id": code,
                        "nombre": name_format
                    }

            # Preguntar si quiere agregar otro género
            another_entry = input('¿Desea agregar otro format? [y/n]: ')
            if another_entry.lower() == 'y':
                clean_screen()
            elif another_entry.lower() == 'n':
                return formats
            else:
                print('Opción no reconocida')
                break

        except Exception as e:
            print(f"Error: {e}")

def create_movie(): # create movie
    num_entry = 0
    pelicula_data = load_json('peliculas')

    if pelicula_data is None:
        pelicula_data = {"blockbuster": {"peliculas": {}}}

    pelicula_data = pelicula_data.get("blockbuster", {}).get("peliculas", {})

    while True:
        try:
            name_movie = input('Ingrese el nombre de la película: ')
            duration_movie = input('Ingrese la duración de la película: ')
            sinopsis = input("Ingrese la sinopsis de la película: ")
            gender = create_gender_movie()
            actors = create_actor_movie()
            formats = create_format_movie()

            num_entry += 1

            code_movie = code_generator('P', num_entry, num_entry)

            if name_movie:
                for code in code_movie:
                    pelicula_data[code] = {
                        "id": code,
                        "nombre": name_movie,
                        "duracion": duration_movie,
                        "sinopsis": sinopsis,
                        "genero": gender,
                        "actores": actors,
                        "formato": formats
                    }

                save_json({"blockbuster": {"peliculas": pelicula_data}}, 'peliculas')

                another_entry = input('Película agregada. ¿Desea agregar otra película? [y/n]: ')
                if another_entry.lower() == 'n':
                    break
                else:
                    clean_screen()

        except Exception as e:
            print(f"Error: {e}")

def edit_movie(): # edit movie
    pelicula_data = load_json('peliculas')

    if pelicula_data is None or "blockbuster" not in pelicula_data:
        print("No hay películas para editar.")
        key_to_continue()
        return

    pelicula_data = pelicula_data["blockbuster"]["peliculas"]

    try:
        identifier = input("Ingrese la ID o el nombre de la película que desea editar: ")

        if identifier not in pelicula_data:
            print("La película no existe.")
            key_to_continue()
            return

        movie_to_edit = pelicula_data[identifier]

        print("Información actual de la película:")
        for key, value in movie_to_edit.items():
            print(f"{key}: {value}")

        attribute_to_edit = input("Ingrese el nombre del atributo que desea editar (nombre, duracion, sinopsis, genero, actores, formato): ")

        if attribute_to_edit in movie_to_edit:
            new_value = input(f"Ingrese el nuevo valor para {attribute_to_edit}: ")
            movie_to_edit[attribute_to_edit] = new_value
        else:
            print("Atributo no válido.")
            key_to_continue()

        save_json({"blockbuster": {"peliculas": pelicula_data}}, 'peliculas')

        print("Película editada con éxito.")

    except Exception as e:
        print(f"Error: {e}")

def delete_movie_by_id(): # delete movie
    pelicula_data = load_json('peliculas')

    if pelicula_data is None or "blockbuster" not in pelicula_data:
        print("No hay películas para eliminar.")
        return

    pelicula_data = pelicula_data["blockbuster"]["peliculas"]

    try:
        identifier = input("Ingrese la ID de la película que desea eliminar: ")

        if identifier not in pelicula_data:
            print("La película no existe.")
            return

        confirmation = input(f"¿Está seguro de que desea eliminar la película con ID {identifier}? [y/n]: ")

        if confirmation.lower() == 'y':
            del pelicula_data[identifier]
            save_json({"blockbuster": {"peliculas": pelicula_data}}, 'peliculas')
            print("Película eliminada con éxito.")
            key_to_continue()
        else:
            print("Operación de eliminación cancelada.")

    except Exception as e:
        print(f"Error: {e}")

def find_movie_by_id(movie_id):
    peliculas_data = load_json('peliculas')

    if peliculas_data is None or "blockbluster" not in peliculas_data or "peliculas" not in peliculas_data["blockbluster"]:
        print("No hay películas para buscar.")
        return

    lista_peliculas = peliculas_data["blockbluster"]["peliculas"]

    for movie_code, movie_data in lista_peliculas.items():
        if movie_data["id"] == movie_id:
            print(f'Pelicula encontrada:')
            print(f'ID: {movie_data["id"]}')
            print(f'Nombre: {movie_data["nombre"]}')
            print(f'Duración: {movie_data["duracion"]}')
            print(f'Sinopsis: {movie_data["sinopsis"]}')
            print(f'Género: {movie_data["genero"]}')
            print(f'Actores: {movie_data["actores"]}')
            print(f'Formato: {movie_data["formato"]}')
            return

    print(f'No se encontró ninguna película con ID {movie_id}.')

def delete_actor_by_id():
    peliculas_data = load_json('peliculas')

    if peliculas_data is None or "blockbluster" not in peliculas_data or "actores" not in peliculas_data["blockbluster"]:
        print("No hay actores para eliminar.")
        key_to_continue()
        return

    actores_data = peliculas_data["blockbluster"]["actores"]

    try:
        identifier = input("Ingrese la ID del actor que desea eliminar: ")

        if identifier not in actores_data:
            print("El actor no existe.")
            return

        confirmation = input(f"¿Está seguro de que desea eliminar el actor con ID {identifier}? [y/n]: ")

        if confirmation.lower() == 'y':
            del actores_data[identifier]
            save_json(peliculas_data, 'peliculas')
            print("Actor eliminado con éxito.")
            key_to_continue()
        else:
            print("Operación de eliminación cancelada.")

    except Exception as e:
        print(f"Error: {e}")

def list_all_movies():
    peliculas_data = load_json('peliculas')

    if peliculas_data is None or "blockbluster" not in peliculas_data or "peliculas" not in peliculas_data["blockbluster"]:
        print("No hay películas para listar.")
        return

    lista_peliculas = peliculas_data["blockbluster"]["peliculas"]

    print(f'PELÍCULAS:')
    for movie_code, movie_data in lista_peliculas.items():
        print(f'{movie_code}: {movie_data["nombre"]}')
        print('----------------------------------')

# Llamada a la función list_all_movies
list_all_movies()

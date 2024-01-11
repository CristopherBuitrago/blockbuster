from tools.utils import clean_screen,load_json, code_generator, save_json, key_to_continue

actor_list = load_json("actores")

def create_actor(): # create actor
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

            # Salvar información en json
            save_json(actors, 'actores')

            # Mostrar el diccionario de géneros actualizado
            print("Diccionario de géneros actualizado:", actors)

            # Preguntar si quiere agregar otro género
            another_entry = input('¿Desea agregar otro actor? [y/n]: ')
            if another_entry.lower() == 'y':
                clean_screen()
            elif another_entry.lower() == 'n':
                break
            else:
                print('Opción no reconocida')
                break

        except Exception as e:
            print(f"Error: {e}")

def list_actors(): # list actor
    lista_actors = load_json('actores')
    print(f'ACTORES:')
    for actor_code, actor_data in lista_actors.items():
        print(f'{actor_code}: {actor_data["nombre"]}')
        print('----------------------------------')
    key_to_continue()
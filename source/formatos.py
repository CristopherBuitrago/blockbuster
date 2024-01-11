from tools.utils import clean_screen,load_json, code_generator, save_json, key_to_continue

format_list = load_json("formatos")

def create_format(): # create format
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

            # Salvar información en json
            save_json(formats, 'formatos')

            # Mostrar el diccionario de géneros actualizado
            print("Diccionario de géneros actualizado:", formats)

            # Preguntar si quiere agregar otro género
            another_entry = input('¿Desea agregar otro format? [y/n]: ')
            if another_entry.lower() == 'y':
                clean_screen()
            elif another_entry.lower() == 'n':
                break
            else:
                print('Opción no reconocida')
                break

        except Exception as e:
            print(f"Error: {e}")

def list_formats(): # list format
    lista_formats = load_json('formatos')
    print(f'formatos:')
    for format_code, format_data in lista_formats.items():
        print(f'{format_code}: {format_data["nombre"]}')
        print('----------------------------------')
    key_to_continue()
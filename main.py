from pokemon import PokemonDatabaseSystem
from time import sleep
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_user_input():
    print("Enter the name of the Pokemon you want to get information about (or type 'exit' to end):")
    return input().lower()

def display_pokemon_info(pokemon_info, user_input):
    clear_console()
    if pokemon_info:
        print("Pokemon Information:" + "\n")
        print("Name: " + user_input.capitalize())
        print("ID: " + str(pokemon_info['id']))
        print("Height: " + str(pokemon_info['height']))
        print("Weight: " + str(pokemon_info['weight']))
        print("Type: " + str(pokemon_info['type']))
        print("Base Stats: " + str(pokemon_info['base_stats']))
        print("Ability: " + str(pokemon_info['ability']))
        sleep(10)
    else:
        print("No information available for the specified Pokemon.")
        sleep(3)

def main():
    P = PokemonDatabaseSystem()

    clear_console()
    print("Welcome to the Pokemon API Getter!")
    sleep(3)

    while True:
        clear_console()

        user_input = get_user_input()
        if user_input == 'exit':
            break

        try:
            pokemon_info = P.get_pokemon_info(user_input)
            display_pokemon_info(pokemon_info, user_input)
        except Exception as ex:
            clear_console()
            print("Error: " + str(ex))
            sleep(3)

if __name__ == '__main__':
    main()

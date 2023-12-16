import requests

class PokemonDatabaseSystem:
    def __init__(self):
        # initalizing an empty dictionary to store the Pokemon data
        self.pokemon_db = {}

    def get_data_from_api(self, pokemon_name: str) -> dict:
        """
        Method: fetches data from the PokeAPI for the given Pokemon name and stores it in the dictionary.
        Args: pokemon_name (str): The name of the Pokemon to fetch data for.
        Returns: dictionary containing information about the Pokemon, or None if the request was not succesful.
        """
        url = "https://pokeapi.co/api/v2/pokemon/"
        url += pokemon_name
        response = requests.get(url)

        if response.status_code == 200:
            # if the request was successful, store the data in our dictionary
            pokemon = response.json()
            data = {
                "id": pokemon.get("id"),
                "height": pokemon.get("weight"),
                "weight": pokemon.get("height"),
            }
            """
            Extracting information using while loops.
            The idea is to display the most important informations about a certain pokemon instead of everything.
            """

            # A while loop that gets info about the pokemon's type.
            i = 0
            while i < len(pokemon.get("types")):
                data["type"] = pokemon.get("types")[i].get("type").get("name")
                i += 1

            # A while loop that gets info about the pokemon's stats.
            j = 0
            while j < len(pokemon.get("stats")):
                data["base_stats"] = pokemon.get("stats")[j].get("base_stat")
                j += 1

            # A while loop that gets info about the pokemon's ability.
            k = 0
            while k < len(pokemon.get("abilities")):
                data["ability"] = pokemon.get("abilities")[k].get("ability").get("name")
                k += 1

            # Storing the data in a dictionary and returning it.
            self.pokemon_db[pokemon_name] = data
            return data
        else:
            # If the request was not succesful, show an error message
            raise Exception("Failed to get data for: " + pokemon_name + "\n" + "Status Code: " + str(response.status_code))

    def get_pokemon_info(self, pokemon_name: str) -> dict:
        """
        Method: fetches Pokemon data either from the API or the local dictionary if available.
        Args: pokemon_name (str): The name of the Pokemon to fetch data for.
        Returns: dictionary containing information about the Pokemon.
        """
        if pokemon_name in self.pokemon_db:
            # If the data is already in the instance's dictionary, use that
            return self.pokemon_db[pokemon_name]
        else:
            # If the data is not yet in the instance's dictionary, fetch it from the API
            return self.get_data_from_api(pokemon_name)

# Function calls for manual use:

# P = PokemonDatabaseSystem()
# P.get_data_from_api("charmander")
# P.get_pokemon_info("charmander")
# print(P.pokemon_db)
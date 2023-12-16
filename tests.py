import unittest
from unittest.mock import patch, Mock
from pokemon import PokemonDatabaseSystem

class TestPokemonDatabaseSystem(unittest.TestCase):
    @patch('pokemon.requests.get')
    # Testing correctly getting data from the API
    def test_get_data_from_api(self, mock_requests_get):
        P = PokemonDatabaseSystem()

        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "id": 1,
            "weight": 85,
            "height": 7,
            "types": [{"type": {"name": "grass"}}],
            "stats": [{"base_stat": 45}],
            "abilities": [{"ability": {"name": "chlorophyll"}}]
        }
        mock_requests_get.return_value = mock_response

        data = P.get_data_from_api("bulbasaur")

        self.assertEqual(data, {
            "id": 1,
            "height": 85,
            "weight": 7,
            "type": "grass",
            "base_stats": 45,
            "ability": "chlorophyll"
        })
        self.assertEqual(P.pokemon_db["bulbasaur"], data)

    # Testing storing the data in a local dictionary
    def test_store_data_in_local_dictionary(self):
        P = PokemonDatabaseSystem()
        stored_data = {
            "id": 1,
            "weight": 0.7,
            "height": 7,
            "type": "grass",
            "base_stats": 45,
            "ability": "chlorophyll"
        }

        P.pokemon_db["bulbasaur"] = stored_data
        data = P.get_pokemon_info("bulbasaur")

        self.assertEqual(stored_data, data)

    @patch('pokemon.requests.get')
    # Testing fetching data from a local dictionary
    def test_extract_data_from_local_dictionary(self, mock_requests_get):
        P = PokemonDatabaseSystem()
        stored_data = {
            "id": 1,
            "weight": 0.7,
            "height": 7,
            "type": "grass",
            "base_stats": 45,
            "ability": "chlorophyll"
        }
        mock_response = mock_requests_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = stored_data

        P.pokemon_db["bulbasaur"] = stored_data
        data = P.get_pokemon_info("bulbasaur")

        mock_requests_get.assert_not_called()
        self.assertEqual(stored_data, data)

    @patch('pokemon.requests.get')
    # Testing raising an exception for a non existing pokemon
    def test_exception_for_non_existing_pokemon(self, mock_requests_get):
        P = PokemonDatabaseSystem()

        mock_response = mock_requests_get.return_value
        mock_response.status_code = 404

        with self.assertRaises(Exception) as checking:
            P.get_data_from_api("non_existing_pokemon")

        self.assertEqual(str(checking.exception), "Failed to get data for: non_existing_pokemon\nStatus Code: 404")

if __name__ == '__main__':
    unittest.main()
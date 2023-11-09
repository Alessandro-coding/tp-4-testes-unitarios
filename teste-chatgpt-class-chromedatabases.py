import unittest
from unittest.mock import MagicMock, patch
from bleachbit.Action import ChromeDatabases  # Importe a classe ChromeDatabases de seu módulo

class TestChromeDatabases(unittest.TestCase):

    @patch('bleachbit.Action.Special.delete_chrome_databases_db')
    @patch('bleachbit.Action.FileActionProvider.get_paths')
    def test_get_commands(self, mock_get_paths, mock_delete_chrome_databases_db):
        # Crie um objeto ChromeDatabases
        chrome_databases = ChromeDatabases(action_element=None)

        # Configure o mock para get_paths retornar uma lista de caminhos fictícios
        mock_get_paths.return_value = ['/path/to/database1', '/path/to/database2']

        # Chame o método get_commands()
        commands = list(chrome_databases.get_commands())

        # Verifique se o mock get_paths foi chamado
        mock_get_paths.assert_called_once()

        # Verifique se o método get_commands retorna os comandos esperados
        expected_commands = [
            Command.Function('/path/to/database1', mock_delete_chrome_databases_db, 'Clean file'),
            Command.Function('/path/to/database2', mock_delete_chrome_databases_db, 'Clean file')
        ]
        self.assertEqual(commands, expected_commands)

if __name__ == '__main__':
    unittest.main()

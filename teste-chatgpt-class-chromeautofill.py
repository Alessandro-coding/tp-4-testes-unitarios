import unittest
from unittest.mock import MagicMock, patch
from bleachbit.Action import ChromeAutofill  # Importe a classe ChromeAutofill de seu módulo

class TestChromeAutofill(unittest.TestCase):

    @patch('bleachbit.Action.Special.delete_chrome_autofill')
    @patch('bleachbit.Action.FileActionProvider.get_paths')
    def test_get_commands(self, mock_get_paths, mock_delete_chrome_autofill):
        # Crie um objeto ChromeAutofill
        chrome_autofill = ChromeAutofill(action_element=None)

        # Configure o mock para get_paths retornar uma lista de caminhos fictícios
        mock_get_paths.return_value = ['/path/to/autofill1', '/path/to/autofill2']

        # Chame o método get_commands()
        commands = list(chrome_autofill.get_commands())

        # Verifique se o mock get_paths foi chamado
        mock_get_paths.assert_called_once()

        # Verifique se o método get_commands retorna os comandos esperados
        expected_commands = [
            Command.Function('/path/to/autofill1', mock_delete_chrome_autofill, 'Clean file'),
            Command.Function('/path/to/autofill2', mock_delete_chrome_autofill, 'Clean file')
        ]
        self.assertEqual(commands, expected_commands)

if __name__ == '__main__':
    unittest.main()

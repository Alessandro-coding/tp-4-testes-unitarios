import unittest
from unittest.mock import patch, MagicMock
from blechbit.Action import AptAutoclean

class TestAptAutoclean(unittest.TestCase):

    @patch('blechbit.Action.FileUtilities.exe_exists')
    @patch('blechbit.Action.Command.Function')
    @patch('blechbit.Action.Unix.apt_autoclean')
    def test_get_commands(self, mock_apt_autoclean, mock_Command, mock_exe_exists):
        mock_exe_exists.return_value = True

        # Criar uma instância da classe AptAutoclean
        apt_autoclean = AptAutoclean(action_element=None, path_vars=None)

        # Chamar o método get_commands()
        commands = list(apt_autoclean.get_commands())

        # Verificar se os mocks foram chamados com os argumentos corretos
        mock_exe_exists.assert_called_with('apt-get')
        mock_apt_autoclean.assert_called_once_with()
        mock_Command.assert_called_once_with(None, mock_apt_autoclean.return_value, 'apt-get autoclean')

        # Verificar se o método retorna uma lista de comandos corretamente
        self.assertEqual(len(commands), 1)
        self.assertEqual(commands[0], mock_Command.return_value)

if __name__ == '__main__':
    unittest.main()

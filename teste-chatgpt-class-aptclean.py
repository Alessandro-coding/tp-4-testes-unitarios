import unittest
from unittest.mock import patch
from bleachbit.Action import AptClean  # Importe a classe AptClean de seu módulo

class TestAptClean(unittest.TestCase):

    @patch('bleachbit.Action.FileUtilities.exe_exists')
    @patch('bleachbit.Action.Command.Function')
    @patch('bleachbit.Action.Unix.apt_clean')
    def test_get_commands(self, mock_apt_clean, mock_Command, mock_exe_exists):
        mock_exe_exists.return_value = True

        # Criar uma instância da classe AptClean
        apt_clean = AptClean(action_element=None, path_vars=None)

        # Chamar o método get_commands()
        commands = list(apt_clean.get_commands())

        # Verificar se os mocks foram chamados com os argumentos corretos
        mock_exe_exists.assert_called_with('apt-get')
        mock_apt_clean.assert_called_once_with()
        mock_Command.assert_called_once_with(None, mock_apt_clean.return_value, 'apt-get clean')

        # Verificar se o método retorna uma lista de comandos corretamente
        self.assertEqual(len(commands), 1)
        self.assertEqual(commands[0], mock_Command.return_value)

if __name__ == '__main__':
    unittest.main()

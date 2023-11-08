import unittest
from unittest.mock import patch
from bleachbit.Action import AptAutoremove  # Importe a classe AptAutoremove de seu módulo

class TestAptAutoremove(unittest.TestCase):

    @patch('bleachbit.Action.FileUtilities.exe_exists')
    @patch('bleachbit.Action.Command.Function')
    @patch('bleachbit.Action.Unix.apt_autoremove')
    def test_get_commands(self, mock_apt_autoremove, mock_Command, mock_exe_exists):
        mock_exe_exists.return_value = True

        # Criar uma instância da classe AptAutoremove
        apt_autoremove = AptAutoremove(action_element=None, path_vars=None)

        # Chamar o método get_commands()
        commands = list(apt_autoremove.get_commands())

        # Verificar se os mocks foram chamados com os argumentos corretos
        mock_exe_exists.assert_called_with('apt-get')
        mock_apt_autoremove.assert_called_once_with()
        mock_Command.assert_called_once_with(None, mock_apt_autoremove.return_value, 'apt-get autoremove')

        # Verificar se o método retorna uma lista de comandos corretamente
        self.assertEqual(len(commands), 1)
        self.assertEqual(commands[0], mock_Command.return_value)

if __name__ == '__main__':
    unittest.main()

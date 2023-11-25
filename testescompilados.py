# A maneira que foi encontrada para rodar os testes
# Foi criar um arquivo .py dentro da pasta de testes do próprio software
# O comando para rodar os testes a seguir é:
# python3 -m unittest tests.Testeestudo1.TestAptAutoremove TestAptClean TestChromeAutoFill TestChromeDatabases TestCompiledSearch TestSplashThread
# Abaixo segue o resultado dos testes e quais foram executados:

############################## RESULTADO DOS TESTES   #############################################################

# gg@gg-VirtualBox:~/Downloads/bleachbit-master$ python3 -m unittest tests.Testeestudo1.TestAptAutoremove TestAptClean TestChromeAutoFill TestChromeDatabases TestCompiledSearch TestSplashThread
# FEEEEE
# ======================================================================
# ERROR: TestAptClean (unittest.loader._FailedTest)
# ----------------------------------------------------------------------
# ImportError: Failed to import test module: TestAptClean
# Traceback (most recent call last):
#   File "/usr/lib/python3.10/unittest/loader.py", line 154, in loadTestsFromName
#     module = __import__(module_name)
# ModuleNotFoundError: No module named 'TestAptClean'


# ======================================================================
# ERROR: TestChromeAutoFill (unittest.loader._FailedTest)
# ----------------------------------------------------------------------
# ImportError: Failed to import test module: TestChromeAutoFill
# Traceback (most recent call last):
#   File "/usr/lib/python3.10/unittest/loader.py", line 154, in loadTestsFromName
#     module = __import__(module_name)
# ModuleNotFoundError: No module named 'TestChromeAutoFill'


# ======================================================================
# ERROR: TestChromeDatabases (unittest.loader._FailedTest)
# ----------------------------------------------------------------------
# ImportError: Failed to import test module: TestChromeDatabases
# Traceback (most recent call last):
#   File "/usr/lib/python3.10/unittest/loader.py", line 154, in loadTestsFromName
#     module = __import__(module_name)
# ModuleNotFoundError: No module named 'TestChromeDatabases'


# ======================================================================
# ERROR: TestCompiledSearch (unittest.loader._FailedTest)
# ----------------------------------------------------------------------
# ImportError: Failed to import test module: TestCompiledSearch
# Traceback (most recent call last):
#   File "/usr/lib/python3.10/unittest/loader.py", line 154, in loadTestsFromName
#     module = __import__(module_name)
# ModuleNotFoundError: No module named 'TestCompiledSearch'


# ======================================================================
# ERROR: TestSplashThread (unittest.loader._FailedTest)
# ----------------------------------------------------------------------
# ImportError: Failed to import test module: TestSplashThread
# Traceback (most recent call last):
#   File "/usr/lib/python3.10/unittest/loader.py", line 154, in loadTestsFromName
#     module = __import__(module_name)
# ModuleNotFoundError: No module named 'TestSplashThread'


# ======================================================================
# FAIL: test_get_commands (tests.Testeestudo1.TestAptAutoremove)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "/usr/lib/python3.10/unittest/mock.py", line 1379, in patched
#     return func(*newargs, **newkeywargs)
#   File "/home/gg/Downloads/bleachbit-master/tests/Testeestudo1.py", line 28, in test_get_commands
#     mock_apt_autoremove.assert_called_once_with()
#   File "/usr/lib/python3.10/unittest/mock.py", line 940, in assert_called_once_with
#     raise AssertionError(msg)
# AssertionError: Expected 'apt_autoremove' to be called once. Called 0 times.

# ----------------------------------------------------------------------
# Ran 6 tests in 0.005s

############################## FIM DO RESULTADO DOS TESTES    #############################################################

FAILED (failures=1, errors=5)

import unittest
from unittest.mock import patch, MagicMock
from bleachbit.Action import *
from unittest.mock import patch, MagicMock
from threading import Event
from bleachbit.Windows import SplashThread
from bleachbit.DeepScan import CompiledSearch


#Testes estudo diciplina TEES
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

class TestSplashThread(unittest.TestCase): #Teste dessas 3 funções da classe, a de iniciar a classe, a de rodar a thread e a de fazer ela esperar com join.

    def test_start(self):
        splash_thread = SplashThread()
        splash_thread.start()
        self.assertTrue(splash_thread._splash_screen_started.is_set())

    def test_run(self):
        def mock_target():
            return "Mock Splash Screen Handle"

        splash_thread = SplashThread(target=mock_target)
        splash_thread.start()
        splash_thread.join()  # Espera até que a thread seja concluída

        self.assertEqual(splash_thread._splash_screen_handle, "Mock Splash Screen Handle")

    def test_join(self):
        splash_thread = SplashThread()
        splash_thread.start()
        splash_thread.join()
        self.assertFalse(splash_thread.is_alive())
class TestCompiledSearch(unittest.TestCase):          # 5 Testes da função match da classe CompiledSearch

    def test_match_with_regex(self):
        search_condition = SearchCondition(command='test', regex='file\d+\.txt')
        compiled_search = CompiledSearch(search_condition)

        result = compiled_search.match('/path/to/directory', 'file123.txt')

        self.assertEqual(result, '/path/to/directory/file123.txt')

    def test_match_with_nregex(self):
        search_condition = SearchCondition(command='test', nregex='ignore\d+\.txt')
        compiled_search = CompiledSearch(search_condition)

        result = compiled_search.match('/path/to/directory', 'ignore456.txt')

        self.assertIsNone(result)

    def test_match_with_wholeregex(self):
        search_condition = SearchCondition(command='test', wholeregex='subdir/file\d+\.txt')
        compiled_search = CompiledSearch(search_condition)

        result = compiled_search.match('/path/to/directory/subdir', 'file789.txt')

        self.assertEqual(result, '/path/to/directory/subdir/file789.txt')

    def test_match_with_nwholeregex(self):
        search_condition = SearchCondition(command='test', nwholeregex='exclude/subdir/file\d+\.txt')
        compiled_search = CompiledSearch(search_condition)

        result = compiled_search.match('/path/to/directory/exclude/subdir', 'file987.txt')

        self.assertIsNone(result)

    def test_match_no_conditions(self):
        search_condition = SearchCondition(command='test')
        compiled_search = CompiledSearch(search_condition)

        result = compiled_search.match('/path/to/directory', 'any_file.txt')

        self.assertEqual(result, '/path/to/directory/any_file.txt')


if __name__ == '__main__':
    unittest.main()

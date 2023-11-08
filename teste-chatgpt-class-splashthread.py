import unittest
from threading import Event
from bleachbit.windows import SplashThread 

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

if __name__ == '__main__':
    unittest.main()

# main.py
from gui import MainWindow
from logic import MainLogic

class AppController:
    def __init__(self):
        self.main_window = MainWindow()
        self.main_logic = MainLogic()

    def run(self):
        self.main_window.show()

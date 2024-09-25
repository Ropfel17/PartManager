import sys
from PySide6.QtWidgets import QApplication
from controller import AppController

def main():
    print("Program started")
    app = QApplication(sys.argv)
    
    controller = AppController()
    controller.run()

    sys.exit(app.exec())

# Der Einstiegspunkt in das Programm
if __name__ == "__main__":
    main()
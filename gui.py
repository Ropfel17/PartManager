# gui.py
from PySide6.QtWidgets import QMainWindow, QPushButton, QLineEdit, QLabel, QVBoxLayout, QWidget, QTabWidget, QHBoxLayout
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize

    
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setup_window()
        
    def setup_window(self):
        self.setWindowTitle("PartManager")
        self.setGeometry(100,100,800,600)
       # Hauptlayout für das Fenster
        main_layout = QHBoxLayout()

        # Tab Widget erstellen
        self.tab_widget = QTabWidget()
        self.tab_widget.setTabPosition(QTabWidget.West)  # Setze die Tabs an die linke Seite
        self.tab_widget.setIconSize(QSize(30, 30)) 

        # Tabs hinzufügen
        self.create_tabs()

        # Füge das Tab-Widget zum Hauptlayout hinzu
        main_layout.addWidget(self.tab_widget)

        # Erstelle ein zentrales Widget für das Hauptlayout
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def create_tabs(self):
        # Home-Tab
        home_tab = QWidget()
        home_layout = QVBoxLayout()
        home_layout.addWidget(QLabel("Willkommen auf der Home-Seite!"))
        home_tab.setLayout(home_layout)

        # All Parts-Tab
        all_parts_tab = QWidget()
        all_parts_layout = QVBoxLayout()
        all_parts_layout.addWidget(QLabel("Liste aller Teile:"))
        # Hier könnten weitere Widgets hinzugefügt werden (z.B. eine Tabelle)
        all_parts_tab.setLayout(all_parts_layout)

        # Add Part-Tab
        add_part_tab = QWidget()
        add_part_layout = QVBoxLayout()
        add_part_layout.addWidget(QLabel("Fügen Sie ein neues Teil hinzu:"))
        add_part_layout.addWidget(QLineEdit("Teilname"))  # Eingabefeld für den Teilname
        add_part_layout.addWidget(QPushButton("Teil hinzufügen"))  # Schaltfläche zum Hinzufügen
        add_part_tab.setLayout(add_part_layout)

        # Tabs in das Tab-Widget einfügen
        self.tab_widget.addTab(home_tab, QIcon("assets/home.png"),"")
        self.tab_widget.addTab(all_parts_tab, QIcon("assets/list.png"),"")
        self.tab_widget.addTab(add_part_tab, QIcon("assets/add.png"),"")

        



        

        


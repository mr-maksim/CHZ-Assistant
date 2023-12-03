import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from tkinter import filedialog


class App(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi('ui/main.ui', self)
        self.start_button.clicked.connect(self.start)
        self.open_button.clicked.connect(self.open)
        self.open_dir_button.clicked.connect(self.open_dir)

    def start(self):
        pass

    def open(self):
        filetypes = (('PDF', '*.pdf'),)
        filepath = filedialog.askopenfilename(
            multiple=True, title="Выбери файл(ы)", filetypes=filetypes)
        self.lcdNumber.display(len(filepath))

    def open_dir(self):
        directory = filedialog.askdirectory(
            title="Выберите папку", initialdir='/')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    print(1)
    sys.exit(app.exec())

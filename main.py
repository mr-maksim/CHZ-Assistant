import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from tkinter import filedialog
from pypdf import PdfMerger


class App(QMainWindow):

    def __init__(self, dir='', file='') -> None:
        self.directory = dir
        self.filepath = file
        super().__init__()
        uic.loadUi('ui/main.ui', self)
        self.start_button.clicked.connect(self.start)
        self.open_button.clicked.connect(self.open)
        self.open_dir_button.clicked.connect(self.open_dir)

    def start(self):
        print(self.filepath)
        merger = PdfMerger()

        for pdf in list(self.filepath):
            merger.append(pdf)
        merger.write(f"{self.directory}/result.pdf")
        merger.close()
        sys.exit(app.exec())

    def open(self):
        filetypes = (('PDF', '*.pdf'),)
        self.filepath = filedialog.askopenfilename(
            multiple=True, title="Выбери файл(ы)", filetypes=filetypes)
        self.lcdNumber.display(len(self.filepath))
        self.enabled_button()

    def open_dir(self):
        self.directory = filedialog.askdirectory(
            title="Выберите папку", initialdir='/')
        self.enabled_button()
        self.lineEdit.setText(self.directory)

    def enabled_button(self):
        if len(self.filepath) > 0 and self.directory:
            self.start_button.setEnabled(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec())

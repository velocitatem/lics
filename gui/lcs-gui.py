import argparse
from pyphonetics import RefinedSoundex
import pronouncing as pr
import pyperclip as pc
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

def modify_sentence(sentence):
    rs = RefinedSoundex()
    phrase = sentence

    def find_best_word(words, target):

        min_backup_distance = 5
        backup = target
        for word in words:
            distance = rs.distance(word, target)
            if distance < 1:
                return word
            elif distance < min_backup_distance:
                backup = word
                min_backup_distance = distance
        return backup

    sf = [find_best_word(pr.rhymes(word), word) for word in phrase.split(" ")]
    return " ".join(sf)

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 textbox - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 400
        self.height = 140
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
    
        # Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(280,40)
        
        # Create a button in the window
        self.button = QPushButton('Show text', self)
        self.button.move(20,80)
        
        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()
    
    @pyqtSlot()
    def on_click(self):
        textboxValue = self.textbox.text()
        cm = modify_sentence(textboxValue)
        pc.copy(cm)
        QMessageBox.question(self, 'Covert Message',  cm, QMessageBox.Ok, QMessageBox.Ok)
        self.textbox.setText("")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

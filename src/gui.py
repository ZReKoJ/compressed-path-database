import sys
import numpy as np

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        
        self.setWindowTitle("Compressed Path Databases")
        self.resize(800, 400)
        #self.showMaximized()

        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.menu_bar = None
        self.tableWidget = None

        self.addMenuBar()
        self.addTableWidget()

        layout.addWidget(self.menu_bar)
        layout.addWidget(self.tableWidget)

        self.actions = {}

    @pyqtSlot()
    def getfile(self):
        file_name = QFileDialog.getOpenFileName(self, 'Open file', 'D:/compressed-path-database/resources',"Image files (*.jpg *.png)")
        if ("open_file" in self.actions):
            self.actions.get("open_file")(file_name)

    def addMenuBar(self):
        self.menu_bar = QMenuBar()
        menu_file = self.menu_bar.addMenu("File")
        menu_file.addAction("Open", self.getfile)

    def addTableWidget(self, matrix=None):
        self.tableWidget = QTableWidget()
        self.tableWidget.itemChanged.connect(self.cellModify)
    
    def cellModify(self, item):
        print(item.row(), item.column(), item.text())

    def initTableData(self, data):
        self.tableWidget.itemChanged.disconnect()
        self.tableWidget.setRowCount(data.shape[0])
        self.tableWidget.setColumnCount(data.shape[1])
        for index, x in np.ndenumerate(data):
            self.tableWidget.setItem(index[0], index[1], QTableWidgetItem(str(x)))
        self.tableWidget.itemChanged.connect(self.cellModify)

    def addCallback(self, action_name, function):
        self.actions[action_name] = function

app = QApplication(sys.argv)
        
def createWindow():
    window = Window()
    window.show()
    return window

def start():
    sys.exit(app.exec_())
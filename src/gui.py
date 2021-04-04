import sys
import numpy as np

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MainWindow(QWidget):
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
        self.data = None
        self.images = []

    @pyqtSlot()
    def getfile(self):
        file_name = QFileDialog.getOpenFileName(self, 'Open file', 'D:/compressed-path-database/resources',"Image files (*.jpg *.png)")
        if ("open_file" in self.actions):
            self.actions.get("open_file")(file_name)

    def addMenuBar(self):
        self.menu_bar = QMenuBar()
        menu_file = self.menu_bar.addMenu("File")
        menu_file.addAction("Open", self.getfile)
        menu_print = self.menu_bar.addMenu("Print")
        menu_print.addAction("Matrix", self.printMatrix)

    def addTableWidget(self, matrix=None):
        self.tableWidget = QTableWidget()
        self.tableWidget.itemChanged.connect(self.cellModify)
    
    def cellModify(self, item):
        print(item.row(), item.column(), item.text())

    def printMatrix(self):
        image = ImageWindow(self.data)
        self.images.append(image)
        image.show()

    def initTableData(self, data):
        self.data = data
        self.tableWidget.itemChanged.disconnect()
        self.tableWidget.setRowCount(self.data.shape[0])
        self.tableWidget.setColumnCount(self.data.shape[1])
        for index, x in np.ndenumerate(self.data):
            self.tableWidget.setItem(index[0], index[1], QTableWidgetItem(str(x)))
        self.tableWidget.itemChanged.connect(self.cellModify)

    def addCallback(self, action_name, function):
        self.actions[action_name] = function

class ImageWindow(QWidget):
    def __init__(self, matrix):
        QWidget.__init__(self)
        
        self.setWindowTitle("Compressed Path Databases")
        self.resize(400, 400)
        #self.showMaximized()
                


        self.colors = {}
        self.colors["0"] = QColor(255, 255, 255, 255).rgb()
        self.colors["1"] = QColor(0, 0, 0, 0).rgb()
        

        self.label = QLabel()

        self.matrix = matrix
        self.print()

        self.grid = QGridLayout()
        self.grid.addWidget(self.label,1,1)
        self.setLayout(self.grid)

    def print(self): 
        image = QImage(self.matrix.shape[1],self.matrix.shape[0], QImage.Format_RGB888)

        for index, x in np.ndenumerate(self.matrix):
            image.setPixel(index[1], index[0], self.colors[str(x)])

        pix = QPixmap(image)
        self.label.setPixmap(pix.scaled(400, 400, Qt.KeepAspectRatio))

app = QApplication(sys.argv)
        
def createWindow():
    window = MainWindow()
    window.show()
    return window

def start():
    sys.exit(app.exec_())

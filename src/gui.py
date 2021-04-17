import sys
import numpy as np
from mappings import mapping as mp
import os
from algorithm import Algorithm

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        
        self.setWindowTitle("Compressed Path Databases")
        self.resize(800, 400)
        #self.showMaximized()

        mainLayout = QVBoxLayout()
        self.setLayout(mainLayout)

        secondaryLayout = QHBoxLayout()
        
        self.menu_bar = None
        self.tableWidget = None

        self.addMenuBar()
        self.addTableWidget()
        self.addTreeView()

        mainLayout.addWidget(self.menu_bar)
        mainLayout.addLayout(secondaryLayout)
        secondaryLayout.addWidget(self.tableWidget)
        secondaryLayout.addWidget(self.treeView)

        self.actions = {}
        self.data = None
        self.images = []

    @pyqtSlot()
    def getfile(self):
        file_name = QFileDialog.getOpenFileName(self, 'Open file', 'D:/compressed-path-database/resources',"Image files (*.jpg *.png)")
        if ("open_file" in self.actions):
            self.actions.get("open_file")(file_name[0])

    def addMenuBar(self):
        self.menu_bar = QMenuBar()
        menu_file = self.menu_bar.addMenu("File")
        menu_file.addAction("Open", self.getfile)
        menu_print = self.menu_bar.addMenu("Print")
        menu_print.addAction("Matrix", lambda : self.printMatrix(self.data["stream"]))
        menu_calculate = self.menu_bar.addMenu("Calculate")
        menu_calculate.addAction("Calc", lambda : self.calculate(self.data["stream"]))

    def calculate(self, data): 
        algorithm = Algorithm(data)

    def addTableWidget(self, matrix=None):
        self.tableWidget = QTableWidget()
        self.tableWidget.itemChanged.connect(self.cellModify)
    
    def addTreeView(self):
        view = QTreeView()
        model = QFileSystemModel()
        model.index(QDir.currentPath())
        view.setModel(model)
        view.setColumnWidth(0, 200)
        self.treeView = view

    def cellModify(self, item):
        self.data["stream"][item.row()][item.column()] = item.text()
        for image in self.images:
            image.update(self.data)

    def printMatrix(self, data):
        image = ImageWindow(data)
        self.images.append(image)
        image.show()

    def initTableData(self, data):
        self.data = data
        self.tableWidget.itemChanged.disconnect()
        self.tableWidget.setRowCount(self.data["stream"].shape[0])
        self.tableWidget.setColumnCount(self.data["stream"].shape[1])
        for index, x in np.ndenumerate(self.data["stream"]):
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
        for index, row in mp.iterrows():
            self.colors[str(row['id'])] = QColor(row['color'][0], row['color'][1], row['color'][2], 0).rgb()
        
        self.label = QLabel()
        self.grid = QGridLayout()
        self.grid.addWidget(self.label, 1, 1)
        self.setLayout(self.grid)

        self.update(matrix)

    def update(self, matrix):
        self.matrix = matrix
        self.print()

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

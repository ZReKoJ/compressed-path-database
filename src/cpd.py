import map_reader
import gui
import os

window = None
matrix = None

def openFileFunction(filename):
    basename = os.path.basename(os.path.normpath(filename))
    matrix = map_reader.imageToMatrix(filename, 300, 200)
    window.initTableData({
        "filename": basename,
        "stream": matrix
    })

if __name__ == "__main__":
    window = gui.createWindow()

    window.addCallback("open_file", openFileFunction)

    openFileFunction('D:/compressed-path-database/resources/labyrinth_2.png')

    gui.start()
import map_reader
import gui

window = None
matrix = None

def openFileFunction(filename):
    matrix = map_reader.imageToMatrix(filename, 300, 200)
    window.initTableData(matrix)

if __name__ == "__main__":
    window = gui.createWindow()

    window.addCallback("open_file", openFileFunction)

    openFileFunction('D:/compressed-path-database/resources/labyrinth_2.png')

    gui.start()
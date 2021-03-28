import map_reader
import gui

window = None
matrix = None

def openFileFunction(filename):
    matrix = map_reader.imageToMatrix(filename[0], 20, 20)
    window.initTableData(matrix)

if __name__ == "__main__":
    window = gui.createWindow()
    window.addCallback("open_file", openFileFunction)

    gui.start()
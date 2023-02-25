import sqlite3
from PyQt5 import QtWidgets, uic
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('main.ui', self)

        self.load_data()

    def load_data(self):
        conn = sqlite3.connect('coffee.sqlite')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM coffee')
        result = cursor.fetchall()

        table = self.findChild(QtWidgets.QTableWidget, 'tableWidget')
        table.setRowCount(len(result))

        for i, row in enumerate(result):
            for j, col in enumerate(row):
                item = QtWidgets.QTableWidgetItem()
                item.setText(str(col))
                table.setItem(i, j, item)

        conn.close()

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()

import sys
from PyQt6 import QtCore
from PyQt6.QtGui import QDragEnterEvent, QDropEvent, QPixmap
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QApplication, QHBoxLayout, QLabel, QTextEdit, QLineEdit
from PyQt6.QtWidgets import QPushButton
from PyQt6.QtCore import Qt, pyqtSlot
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout,QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Main window')

        # 创建窗口
        window = QWidget()
        window.setWindowTitle("我的第一个PyQt6应用")
        window.resize(300, 200)

        # 创建按钮
        button = QPushButton("点击我!")
        button.clicked.connect(lambda: print("按钮被点击了!"))

        # 创建布局并添加按钮
        layout = QVBoxLayout()
        layout.addWidget(button)
        window.setLayout(layout)

        self.setCentralWidget(window)
        self.show()


def main():


    # 创建应用程序对象
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()

    # # 创建窗口
    # window = QWidget()
    # window.setWindowTitle("我的第一个PyQt6应用")
    # window.resize(300, 200)
    #
    # # 创建按钮
    # button = QPushButton("点击我!")
    # button.clicked.connect(lambda: print("按钮被点击了!"))
    #
    # # 创建布局并添加按钮
    # layout = QVBoxLayout()
    # layout.addWidget(button)
    # window.setLayout(layout)
    #
    # # 显示窗口
    # window.show()

    # 进入应用主循环
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

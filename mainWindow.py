import atexit
import os
import signal
import subprocess
import sys
import threading
import time
from datetime import datetime
from os import kill
from subprocess import Popen, call
from tkinter import Checkbutton, Variable

import psutil
from PyQt5 import Qt, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QTreeWidgetItem, QTreeWidget, \
    QTreeWidgetItemIterator

from GUI_Project.ui_mainWindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.test)  # Select Tests
        self.ui.treeWidget.setHeaderHidden(True)
        self.ui.pushButton_2.clicked.connect(self.runTest)  # Run
        self.ui.pushButton_3.clicked.connect(self.updateLog)  # Refresh Logs
        self.ui.pushButton_4.clicked.connect(self.stopTest) # stop
        self.ui.pushButton_5.clicked.connect(self.selectAll)  # Select All Tests
        self.ui.pushButton_6.clicked.connect(self.deSelectAll)  # DeSelect All Tests


    def test(self):
        a = QFileDialog.getExistingDirectory(self, 'openFiles', 'C:/Users/Avi/Desktop/project')
        stra = os.listdir(a)
        for i in stra:
            if 'Test.js' in i:
                QTreeWidgetItem(self.ui.treeWidget, [i]).setCheckState(0, QtCore.Qt.Unchecked)

    def runTest(self):
        root = self.ui.treeWidget.invisibleRootItem()
        child_count = root.childCount()
        for i in range(child_count):
            item = root.child(i)
            if item.checkState(0):
                itemText = item.text(0)
                os.chdir("C:/Users/Avi/Desktop/project")

                p = Popen(['node', itemText])
                print(p)
                # while p.poll() is None:
                #     print("Still working...")
                #     time.sleep(0.1)
                # print(i)
                # if i == 2:
                    # p.terminate()
                    # p.kill()
                    # pobj = psutil.Process(p.pid)
                    # list children & kill them
                    # for c in pobj.children(recursive=True):
                    #     c.kill()
                    #     pobj.kill()
                    # os.killpg(os.getpgid(p.pid), signal.SIGTERM)
                print("its on!")
                # stdout = p.communicate()
                print("Run Test completed!")

    def realExec(self, itemText):
        proc = subprocess.Popen(['node', itemText])

        while proc.poll() is None:
            print("Still working...")
            time.sleep(0.1)

    def updateLog(self):
        print("start updateLog")
        currentDate = datetime.date(datetime.now())
        day = (str(currentDate)[9])
        month = (str(currentDate)[5: -3])
        year = (str(currentDate)[:4])
        self.ui.plainTextEdit.clear()
        root = self.ui.treeWidget.invisibleRootItem()
        child_count = root.childCount()
        for i in range(child_count):
            item = root.child(i)
            if item.checkState(0):
                itemText = item.text(0)
                renTest = itemText[:-3]
                os.chdir(f"C:/Users/Avi/Desktop/project/{day}.{month}.{year}")
                the_file = open(renTest + ".log")
                logFile = the_file.read()
                self.ui.plainTextEdit.insertPlainText(logFile)

    def selectAll(self):
        root = self.ui.treeWidget.invisibleRootItem()
        child_count = root.childCount()
        for i in range(child_count):
            item = root.child(i)
            item.setCheckState(0, QtCore.Qt.Checked)

    def deSelectAll(self):
        root = self.ui.treeWidget.invisibleRootItem()
        child_count = root.childCount()
        for i in range(child_count):
            item = root.child(i)
            item.setCheckState(0, QtCore.Qt.Unchecked)

    def stopTest(self, t):
        print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        print(t)
        # pobj = psutil.Process(p.pid)
        # for c in pobj.children(recursive=True):
        #     c.kill()
        #     pobj.kill()




app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())

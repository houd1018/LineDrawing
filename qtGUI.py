# Created by: PyQt5 UI code generator 5.11.3
#

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *


from Expression import DrawExp
from dda import DrawDDA
from midpoint import DrawMid
from Bresenham import DrawBre
from midpoint_circle import Drawcircle


##########################   GUI     ##############
class Ui_MainWindow(object):

    def drawExp(self, MainWindow):
        x0 = int(self.edit_Exp_x0.value())
        y0 = int(self.edit_Exp_y0.value())
        x1 = int(self.edit_Exp_x1.value())
        y1 = int(self.edit_Exp_y1.value())
        DrawExp(x0, y0, x1, y1)

    def drawdda(self, MainWindow):
        x0 = int(self.edit_dda_x0.value())
        y0 = int(self.edit_dda_y0.value())
        x1 = int(self.edit_dda_x1.value())
        y1 = int(self.edit_dda_y1.value())
        DrawDDA(x0, y0, x1, y1)

    def drawbre(self, MainWindow):
        x0 = int(self.edit_bre_x0.value())
        y0 = int(self.edit_bre_y0.value())
        x1 = int(self.edit_bre_x1.value())
        y1 = int(self.edit_bre_y1.value())
        DrawBre(x0, y0, x1, y1)

    def drawcircle(self, MainWindow):
        xc = int(self.edit_circle_xc.value())
        yc = int(self.edit_circle_yc.value())
        r = int(self.edit_circle_r.value())
        Drawcircle(xc, yc, r)

    def drawMid(self, MainWindow):
        xc = int(self.edit_Mid_xc.value())
        yc = int(self.edit_Mid_yc.value())
        rx = int(self.edit_Mid_rx.value())
        ry = int(self.edit_Mid_ry.value())
        DrawMid(xc, yc, rx, ry)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.centralwidget.setObjectName("centralwidget")

        self.Exp_but = QtWidgets.QPushButton(self.centralwidget)
        self.Exp_but.setGeometry(QtCore.QRect(540, 20, 161, 81))
        self.Exp_but.setObjectName("Exp_but")

        self.dda_but = QtWidgets.QPushButton(self.centralwidget)
        self.dda_but.setGeometry(QtCore.QRect(540, 130, 161, 81))
        self.dda_but.setObjectName("dda_but")

        self.bre_but = QtWidgets.QPushButton(self.centralwidget)
        self.bre_but.setGeometry(QtCore.QRect(540, 240, 161, 81))
        self.bre_but.setObjectName("bre_but")

        self.circle_but = QtWidgets.QPushButton(self.centralwidget)
        self.circle_but.setGeometry(QtCore.QRect(540, 460, 161, 81))
        self.circle_but.setObjectName("circle_but")

        self.Mid_but = QtWidgets.QPushButton(self.centralwidget)
        self.Mid_but.setGeometry(QtCore.QRect(540, 350, 161, 81))
        self.Mid_but.setObjectName("Mid_but")

        self.edit_Exp_x0 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.edit_Exp_x0.setGeometry(QtCore.QRect(250, 30, 62, 27))
        self.edit_Exp_x0.setObjectName("edit_Exp_x0")
        self.edit_Exp_y0 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.edit_Exp_y0.setGeometry(QtCore.QRect(340, 30, 62, 27))
        self.edit_Exp_y0.setObjectName("edit_Exp_y0")
        self.edit_Exp_x1 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.edit_Exp_x1.setGeometry(QtCore.QRect(250, 70, 62, 27))
        self.edit_Exp_x1.setObjectName("edit_Exp_x1")
        self.edit_Exp_y1 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.edit_Exp_y1.setGeometry(QtCore.QRect(340, 70, 62, 27))
        self.edit_Exp_y1.setObjectName("edit_Exp_y1")

        self.edit_dda_x0 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.edit_dda_x0.setGeometry(QtCore.QRect(250, 140, 62, 27))
        self.edit_dda_x0.setObjectName("edit_dda_x0")
        self.edit_dda_y0 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.edit_dda_y0.setGeometry(QtCore.QRect(340, 140, 62, 27))
        self.edit_dda_y0.setObjectName("edit_dda_y0")
        self.edit_dda_x1 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.edit_dda_x1.setGeometry(QtCore.QRect(250, 180, 62, 27))
        self.edit_dda_x1.setObjectName("edit_dda_x1")
        self.edit_dda_y1 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.edit_dda_y1.setGeometry(QtCore.QRect(340, 180, 62, 27))
        self.edit_dda_y1.setObjectName("edit_dda_y1")

        self.edit_bre_x0 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.edit_bre_x0.setGeometry(QtCore.QRect(250, 250, 62, 27))
        self.edit_bre_x0.setObjectName("edit_bre_x0")
        self.edit_bre_y0 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.edit_bre_y0.setGeometry(QtCore.QRect(340, 250, 62, 27))
        self.edit_bre_y0.setObjectName("edit_bre_y0")
        self.edit_bre_x1 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.edit_bre_x1.setGeometry(QtCore.QRect(250, 290, 62, 27))
        self.edit_bre_x1.setObjectName("edit_bre_x1")
        self.edit_bre_y1 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.edit_bre_y1.setGeometry(QtCore.QRect(340, 290, 62, 27))
        self.edit_bre_y1.setObjectName("edit_bre_y1")

        self.edit_circle_xc = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.edit_circle_xc.setGeometry(QtCore.QRect(250, 470, 62, 27))
        self.edit_circle_xc.setObjectName("edit_circle_xc")
        self.edit_circle_yc = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.edit_circle_yc.setGeometry(QtCore.QRect(340, 470, 62, 27))
        self.edit_circle_yc.setObjectName("edit_circle_yc")
        self.edit_circle_r = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.edit_circle_r.setGeometry(QtCore.QRect(250, 510, 62, 27))
        self.edit_circle_r.setObjectName("edit_circle_r")

        self.edit_Mid_xc = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.edit_Mid_xc.setGeometry(QtCore.QRect(250, 360, 62, 27))
        self.edit_Mid_xc.setObjectName("edit_Mid_xc")
        self.edit_Mid_yc = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.edit_Mid_yc.setGeometry(QtCore.QRect(340, 360, 62, 27))
        self.edit_Mid_yc.setObjectName("edit_Mid_yc")
        self.edit_Mid_rx = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.edit_Mid_rx.setGeometry(QtCore.QRect(250, 400, 62, 27))
        self.edit_Mid_rx.setObjectName("edit_Mid_rx")
        self.edit_Mid_ry = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.edit_Mid_ry.setGeometry(QtCore.QRect(340, 400, 62, 27))
        self.edit_Mid_ry.setObjectName("edit_Mid_ry")

        self.Exp_start = QtWidgets.QLabel(self.centralwidget)
        self.Exp_start.setGeometry(QtCore.QRect(50, 30, 160, 20))
        self.Exp_start.setObjectName("Exp_start")
        self.Exp_end = QtWidgets.QLabel(self.centralwidget)
        self.Exp_end.setGeometry(QtCore.QRect(50, 70, 160, 18))
        self.Exp_end.setObjectName("Exp_end")

        self.dda_start = QtWidgets.QLabel(self.centralwidget)
        self.dda_start.setGeometry(QtCore.QRect(50, 140, 160, 20))
        self.dda_start.setObjectName("dda_start")
        self.dda_end = QtWidgets.QLabel(self.centralwidget)
        self.dda_end.setGeometry(QtCore.QRect(50, 180, 160, 18))
        self.dda_end.setObjectName("dda_end")

        self.bre_start = QtWidgets.QLabel(self.centralwidget)
        self.bre_start.setGeometry(QtCore.QRect(50, 250, 160, 16))
        self.bre_start.setObjectName("bre_start")
        self.bre_end = QtWidgets.QLabel(self.centralwidget)
        self.bre_end.setGeometry(QtCore.QRect(50, 290, 160, 18))
        self.bre_end.setObjectName("bre_end")
        
        self.circle_midpoint = QtWidgets.QLabel(self.centralwidget)
        self.circle_midpoint.setGeometry(QtCore.QRect(50, 470, 160, 16))
        self.circle_midpoint.setObjectName("circle_midpoint")
        self.circle_r = QtWidgets.QLabel(self.centralwidget)
        self.circle_r.setGeometry(QtCore.QRect(50, 510, 160, 18))
        self.circle_r.setObjectName("circle_r")

        self.Mid_midpoint = QtWidgets.QLabel(self.centralwidget)
        self.Mid_midpoint.setGeometry(QtCore.QRect(50, 360, 160, 20))
        self.Mid_midpoint.setObjectName("Mid_midpoint")
        self.Mid_rxry = QtWidgets.QLabel(self.centralwidget)
        self.Mid_rxry.setGeometry(QtCore.QRect(50, 400, 160, 18))
        self.Mid_rxry.setObjectName("Mid_rxry")
        
   
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.edit_Exp_x0.setRange(int(-10000), int(10000))
        self.edit_Exp_x1.setRange(-10000, 10000)
        self.edit_Exp_y0.setRange(-10000, 10000)
        self.edit_Exp_y1.setRange(-10000, 10000)

        self.edit_Exp_x0.setValue(int(-10))
        self.edit_Exp_x1.setValue(-6)
        self.edit_Exp_y0.setValue(30)
        self.edit_Exp_y1.setValue(40)

        self.edit_dda_x0.setRange(int(-10000), int(10000))
        self.edit_dda_x1.setRange(-10000, 10000)
        self.edit_dda_y0.setRange(-10000, 10000)
        self.edit_dda_y1.setRange(-10000, 10000)

        self.edit_dda_x0.setValue(int(-10))
        self.edit_dda_x1.setValue(-6)
        self.edit_dda_y0.setValue(30)
        self.edit_dda_y1.setValue(40)

        self.edit_bre_x0.setRange(-10000, 10000)
        self.edit_bre_x1.setRange(-10000, 10000)
        self.edit_bre_y0.setRange(-10000, 10000)
        self.edit_bre_y1.setRange(-10000, 10000)

        self.edit_bre_x0.setValue(-10)
        self.edit_bre_x1.setValue(6)
        self.edit_bre_y0.setValue(30)
        self.edit_bre_y1.setValue(40)

        self.edit_circle_xc.setRange(-10000, 10000)
        self.edit_circle_yc.setRange(-10000, 10000)
        self.edit_circle_r.setRange(-10000, 10000)

        self.edit_circle_xc.setValue(12)
        self.edit_circle_yc.setValue(13)
        self.edit_circle_r.setValue(20)

        self.edit_Mid_xc.setRange(-10000, 10000)
        self.edit_Mid_yc.setRange(-10000, 10000)
        self.edit_Mid_rx.setRange(-10000, 10000)
        self.edit_Mid_ry.setRange(-10000, 10000)

        self.edit_Mid_xc.setValue(2)
        self.edit_Mid_yc.setValue(6)
        self.edit_Mid_rx.setValue(25)
        self.edit_Mid_ry.setValue(16)
        self.Exp_but.clicked.connect(self.drawExp)
        self.dda_but.clicked.connect(self.drawdda)
        self.bre_but.clicked.connect(self.drawbre)
        self.circle_but.clicked.connect(self.drawcircle)
        self.Mid_but.clicked.connect(self.drawMid)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Line Drawing Algorithm Demonstration"))
        self.Exp_but.setText(_translate("MainWindow", "Expression")) 
        self.dda_but.setText(_translate("MainWindow", "DDA"))  #
        self.bre_but.setText(_translate("MainWindow", "Bresenham"))  #
        self.circle_but.setText(_translate("MainWindow", "midpoint_circle"))  #
        self.Mid_but.setText(_translate("MainWindow", "midpoint"))  #
        self.Exp_start.setText(_translate("MainWindow", "Starting coordinates"))  #
        self.Exp_end.setText(_translate("MainWindow", "Ending coordinates"))  #
        self.dda_start.setText(_translate("MainWindow", "Starting coordinates"))  #
        self.dda_end.setText(_translate("MainWindow", "Ending coordinates"))  #
        self.bre_start.setText(_translate("MainWindow", "Starting coordinates"))  #
        self.bre_end.setText(_translate("MainWindow", "Ending coordinates"))  #
        self.Mid_midpoint.setText(_translate("MainWindow", "Starting coordinates"))  #
        self.Mid_rxry.setText(_translate("MainWindow", "Starting coordinates"))  #
        self.circle_midpoint.setText(_translate("MainWindow", "Center point"))  #
        self.circle_r.setText(_translate("MainWindow", "Radius"))  #


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

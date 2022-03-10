from mainWindow import *
from PyQt5 import QtCore, QtGui, QtWidgets
from  pyqtgraph.flowchart import Flowchart
from pyqtgraph import PlotWidget
import pyqtgraph as pg
import numpy as np

class extendWindow(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        
        
        self.setupUi(MainWindow)

        ## ------ Buttonfunctions ------ ##
        self.startButton.clicked.connect(self.func1)
        self.forceRead.setValue(3)
        self.forceRead.setMaximum(1000)
        

        #self.graphbutton = QtWidgets.QPushButton(self.stressWidget)
        #self.graphbutton.setObjectName('test')
        #self.graphbutton.setMinimumSize(QtCore.QSize(0, 25))
        #self.gridLayout_6.addWidget(self.graphbutton, 1, 1, 1, 1)
        #self.gridLayout_3.addWidget(self.saveGraphButton, 9, 0, 1, 1)
        #self.graphbutton.raise_()
        #self.startButton.clicked.connect(self.startButtonclicked)

        ## -------- Add graph ---------- ##
        ## Create flowchart, define input/output terminals
        #fc = Flowchart(terminals={
        #    'dataIn': {'io': 'in'},
        #    'dataOut': {'io': 'out'}    
        #})
        #w = fc.widget()
        #self.gridLayout_6.addWidget(w, 1, 1, 1, 1)
        ################################################
        self.graphWdiget = pg.PlotWidget()
        self.graphWdiget.setBackground(background= (33, 33, 33))
        self.graphWdiget.setRange(None, (0,100), (0,100), 0.1, True, True)
        pg.ViewBox.viewRect
        self.gridLayout_6.addWidget(self.graphWdiget, 1, 1, 1, 1)
        ###############################################
        #self.qView = pg.GraphicsView()
        

    def func1(self):
        i = self.forceRead.value() + 20
        self.forceRead.setValue(i)

        print(i)




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = extendWindow()
    MainWindow.show()
    sys.exit(app.exec_())
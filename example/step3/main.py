# -*- coding: utf-8 -*-
import sys
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile
from PySide2.QtWidgets import *

from maya.app.general.mayaMixin import MayaQWidgetBaseMixin

class SampleWindow(MayaQWidgetBaseMixin, QMainWindow):

	def __init__(self, parent=None):
		super(SampleWindow, self).__init__(parent)
		
		#execPath = os.path.dirname(os.path.abspath('__file__'))
		#execPath = os.path.dirname(__file__)
		#uiFilePath = os.path.join(execPath, "View/helloworld.ui");
		uiFilePath = "D:\workspace\Qt\HelloPySide\ui\helloworld.ui"

		file = QFile(uiFilePath)
		file.open(QFile.ReadOnly)

		loader = QUiLoader()
		self.UI = loader.load(file)
		self.setCentralWidget(self.UI)
		self.setWindowTitle(u'SampleWindow')

def main():
	app = QApplication.instance()
	ui = SampleWindow()
	ui.show()
	sys.exit(app.exec_())

main()


#uiFilePath = os.path.join(CURRENT_PATH, 'helloworld.ui')
#file = QFile(uiFilePath)
#file = QFile("D:\workspace\Qt\HelloPySide\View\helloworld.ui")
#file.open(QFile.ReadOnly)

#loader = QUiLoader()
#window = loader.load(file)

#window.show()

#sys.exit(app.exec_())

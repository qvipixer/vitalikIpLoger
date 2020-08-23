from PyQt5 import QtWidgets
from IpTracker import Ui_MainWindow
import sys
import requests
import datetime

data = datetime.datetime.now()
timeDataNow = data.strftime('%Y-%m-%d %H.%M.%S')

#print(timeDataNow)


# Запись в лог при старте программы

# Запись в лог при старте программы

class mywindow(QtWidgets.QMainWindow):
	def __init__(self):
		super(mywindow, self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.ui.pushButtonRefresh.clicked.connect(self.btnClickedRefresh)
		self.ui.pushButtonClose.clicked.connect(self.btnClickedClose)
		self.file = 'log_' + timeDataNow + '.csv'
		#self.file = 'log.txt'

		self.openFile = open(self.file,'a')
		self.openFile.write('Open loger;' + timeDataNow + '\n')
		self.openFile.close()

		self.openFile = open(self.file,'r')
		self.openFileRead = self.openFile.read()
		self.ui.textBrowser.setText(self.openFileRead)
		self.openFile.close()

		self.ui.labelTimeNow.setText(timeDataNow)


	def btnClickedRefresh(self):
		# Получение IP
		myIP = requests.get('https://ramziv.com/ip').text
		self.ui.labelcurrentIP.setText(myIP)
		# Получение IP

		data = datetime.datetime.now()
		timeDataNow = data.strftime('%Y-%m-%d %H.%M.%S')
		self.ui.labelTimeNow.setText(timeDataNow)

		# Запись в лог занчений
		self.openFile = open(self.file,'a')
		self.openFile.writelines(myIP + ';' + timeDataNow + '\n')
		self.openFile.close()
		# Запись в лог занчений

		self.openFile = open(self.file,'r')
		self.openFileRead = self.openFile.read()
		self.ui.textBrowser.setText(self.openFileRead)
		self.openFile.close()

	def btnClickedClose(self):
		self.openFile = open(self.file,'a')
		self.openFile.write('Stop loger;' + timeDataNow + '\n')
		self.openFile.close()
		sys.exit(app.exec())


app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())

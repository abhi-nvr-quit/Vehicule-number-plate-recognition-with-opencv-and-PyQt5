# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_listdata.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_list_dialog(object):
    def setupUi(self, list_dialog):
        list_dialog.setObjectName("list_dialog")
        list_dialog.resize(834, 573)
        self.tableWidget = QtWidgets.QTableWidget(list_dialog)
        self.tableWidget.setGeometry(QtCore.QRect(10, 110, 801, 451))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.edit_button = QtWidgets.QPushButton(list_dialog)
        self.edit_button.setGeometry(QtCore.QRect(520, 70, 75, 23))
        self.edit_button.setObjectName("edit_button")
        self.label_9 = QtWidgets.QLabel(list_dialog)
        self.label_9.setGeometry(QtCore.QRect(30, 10, 641, 31))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook")
        font.setPointSize(26)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label = QtWidgets.QLabel(list_dialog)
        self.label.setGeometry(QtCore.QRect(30, 70, 47, 13))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(list_dialog)
        self.lineEdit.setGeometry(QtCore.QRect(70, 70, 171, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.add_button = QtWidgets.QPushButton(list_dialog)
        self.add_button.setGeometry(QtCore.QRect(440, 70, 75, 23))
        self.add_button.setObjectName("add_button")
        self.delete_button = QtWidgets.QPushButton(list_dialog)
        self.delete_button.setGeometry(QtCore.QRect(600, 70, 75, 23))
        self.delete_button.setObjectName("delete_button")
        self.lcdNumber = QtWidgets.QLCDNumber(list_dialog)
        self.lcdNumber.setGeometry(QtCore.QRect(710, 40, 64, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lcdNumber.setFont(font)
        self.lcdNumber.setObjectName("lcdNumber")
        self.refresh_button = QtWidgets.QPushButton(list_dialog)
        self.refresh_button.setGeometry(QtCore.QRect(350, 70, 75, 23))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("."), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.refresh_button.setIcon(icon)
        self.refresh_button.setShortcut("")
        self.refresh_button.setObjectName("refresh_button")
        self.search_button = QtWidgets.QPushButton(list_dialog)
        self.search_button.setGeometry(QtCore.QRect(260, 70, 75, 23))
        self.search_button.setObjectName("search_button")

        self.retranslateUi(list_dialog)
        QtCore.QMetaObject.connectSlotsByName(list_dialog)

    def retranslateUi(self, list_dialog):
        _translate = QtCore.QCoreApplication.translate
        list_dialog.setWindowTitle(_translate("list_dialog", "LIST OF DATA"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("list_dialog", "1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("list_dialog", "PLate Number"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("list_dialog", "Mark"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("list_dialog", "Color"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("list_dialog", "Assurance"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("list_dialog", "Technique"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("list_dialog", "Owner Name"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("list_dialog", "Owner CNI"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("list_dialog", "Phone"))
        self.edit_button.setText(_translate("list_dialog", "Edit"))
        self.label_9.setText(_translate("list_dialog", "LIST OF DATA IN THE DATABASE"))
        self.label.setText(_translate("list_dialog", "Search"))
        self.add_button.setText(_translate("list_dialog", "ADD"))
        self.delete_button.setText(_translate("list_dialog", "Delete"))
        self.refresh_button.setText(_translate("list_dialog", "Refresh"))
        self.search_button.setText(_translate("list_dialog", "Search"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    list_dialog = QtWidgets.QDialog()
    ui = Ui_list_dialog()
    ui.setupUi(list_dialog)
    list_dialog.show()
    sys.exit(app.exec_())


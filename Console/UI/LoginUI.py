# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginForm(object):
    def setupUi(self, LoginForm):
        LoginForm.setObjectName("LoginForm")
        LoginForm.setWindowModality(QtCore.Qt.ApplicationModal)
        LoginForm.resize(352, 232)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logo/UI/Resources/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        LoginForm.setWindowIcon(icon)
        self.username = QtWidgets.QLineEdit(LoginForm)
        self.username.setGeometry(QtCore.QRect(110, 70, 211, 31))
        self.username.setPlaceholderText("")
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(LoginForm)
        self.password.setGeometry(QtCore.QRect(110, 120, 211, 31))
        self.password.setInputMask("")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setPlaceholderText("")
        self.password.setObjectName("password")
        self.title = QtWidgets.QLabel(LoginForm)
        self.title.setGeometry(QtCore.QRect(30, 20, 291, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setWordWrap(False)
        self.title.setObjectName("title")
        self.label_username = QtWidgets.QLabel(LoginForm)
        self.label_username.setGeometry(QtCore.QRect(30, 70, 72, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label_username.setFont(font)
        self.label_username.setObjectName("label_username")
        self.label_password = QtWidgets.QLabel(LoginForm)
        self.label_password.setGeometry(QtCore.QRect(30, 120, 72, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label_password.setFont(font)
        self.label_password.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_password.setObjectName("label_password")
        self.login_button = QtWidgets.QPushButton(LoginForm)
        self.login_button.setGeometry(QtCore.QRect(30, 170, 291, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.login_button.setFont(font)
        self.login_button.setObjectName("login_button")

        self.retranslateUi(LoginForm)
        self.login_button.clicked.connect(LoginForm.login)
        QtCore.QMetaObject.connectSlotsByName(LoginForm)

    def retranslateUi(self, LoginForm):
        _translate = QtCore.QCoreApplication.translate
        LoginForm.setWindowTitle(_translate("LoginForm", "PYCM Login"))
        self.username.setText(_translate("LoginForm", "admin"))
        self.password.setText(_translate("LoginForm", "123456"))
        self.title.setText(_translate("LoginForm", "PYCM 登录"))
        self.label_username.setText(_translate("LoginForm", "用户名："))
        self.label_password.setText(_translate("LoginForm", "密　码："))
        self.login_button.setText(_translate("LoginForm", "登录"))
        self.login_button.setShortcut(_translate("LoginForm", "Return"))
import Resources_rc

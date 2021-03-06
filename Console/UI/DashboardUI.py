# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DashboardUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DashboardForm(object):
    def setupUi(self, DashboardForm):
        DashboardForm.setObjectName("DashboardForm")
        DashboardForm.resize(1304, 779)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logo/UI/Resources/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DashboardForm.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(DashboardForm)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.setSpacing(10)
        self.main_layout.setObjectName("main_layout")
        self.frame_header = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_header.sizePolicy().hasHeightForWidth())
        self.frame_header.setSizePolicy(sizePolicy)
        self.frame_header.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_header.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_header.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_header.setObjectName("frame_header")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_header)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(8)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.toggle_broadcast = QtWidgets.QPushButton(self.frame_header)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggle_broadcast.sizePolicy().hasHeightForWidth())
        self.toggle_broadcast.setSizePolicy(sizePolicy)
        self.toggle_broadcast.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.toggle_broadcast.setFont(font)
        self.toggle_broadcast.setCheckable(True)
        self.toggle_broadcast.setChecked(False)
        self.toggle_broadcast.setObjectName("toggle_broadcast")
        self.horizontalLayout.addWidget(self.toggle_broadcast)
        self.remote_spy = QtWidgets.QPushButton(self.frame_header)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.remote_spy.sizePolicy().hasHeightForWidth())
        self.remote_spy.setSizePolicy(sizePolicy)
        self.remote_spy.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.remote_spy.setFont(font)
        self.remote_spy.setCheckable(True)
        self.remote_spy.setObjectName("remote_spy")
        self.horizontalLayout.addWidget(self.remote_spy)
        self.remote_command = QtWidgets.QPushButton(self.frame_header)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.remote_command.sizePolicy().hasHeightForWidth())
        self.remote_command.setSizePolicy(sizePolicy)
        self.remote_command.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.remote_command.setFont(font)
        self.remote_command.setObjectName("remote_command")
        self.horizontalLayout.addWidget(self.remote_command)
        self.file_transfer = QtWidgets.QPushButton(self.frame_header)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.file_transfer.sizePolicy().hasHeightForWidth())
        self.file_transfer.setSizePolicy(sizePolicy)
        self.file_transfer.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.file_transfer.setFont(font)
        self.file_transfer.setObjectName("file_transfer")
        self.horizontalLayout.addWidget(self.file_transfer)
        self.main_layout.addWidget(self.frame_header)
        self.frame_body = QtWidgets.QFrame(self.centralwidget)
        self.frame_body.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_body.setObjectName("frame_body")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_body)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.desktop_widget_container = QtWidgets.QWidget(self.frame_body)
        self.desktop_widget_container.setObjectName("desktop_widget_container")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.desktop_widget_container)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.desktop_layout = QtWidgets.QListWidget(self.desktop_widget_container)
        self.desktop_layout.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked)
        self.desktop_layout.setProperty("showDropIndicator", False)
        self.desktop_layout.setDragEnabled(False)
        self.desktop_layout.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.desktop_layout.setDefaultDropAction(QtCore.Qt.IgnoreAction)
        self.desktop_layout.setSelectionMode(QtWidgets.QAbstractItemView.ContiguousSelection)
        self.desktop_layout.setIconSize(QtCore.QSize(240, 135))
        self.desktop_layout.setMovement(QtWidgets.QListView.Free)
        self.desktop_layout.setResizeMode(QtWidgets.QListView.Adjust)
        self.desktop_layout.setViewMode(QtWidgets.QListView.IconMode)
        self.desktop_layout.setObjectName("desktop_layout")
        self.verticalLayout_2.addWidget(self.desktop_layout)
        self.horizontalLayout_3.addWidget(self.desktop_widget_container)
        self.log_widget_container = QtWidgets.QWidget(self.frame_body)
        self.log_widget_container.setObjectName("log_widget_container")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.log_widget_container)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.log_area = QtWidgets.QTextEdit(self.log_widget_container)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(10)
        self.log_area.setFont(font)
        self.log_area.setReadOnly(True)
        self.log_area.setObjectName("log_area")
        self.verticalLayout_3.addWidget(self.log_area)
        self.action_buttons_layout = QtWidgets.QHBoxLayout()
        self.action_buttons_layout.setObjectName("action_buttons_layout")
        self.send_message_button = QtWidgets.QPushButton(self.log_widget_container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.send_message_button.sizePolicy().hasHeightForWidth())
        self.send_message_button.setSizePolicy(sizePolicy)
        self.send_message_button.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.send_message_button.setObjectName("send_message_button")
        self.action_buttons_layout.addWidget(self.send_message_button)
        self.clear_log_area = QtWidgets.QPushButton(self.log_widget_container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clear_log_area.sizePolicy().hasHeightForWidth())
        self.clear_log_area.setSizePolicy(sizePolicy)
        self.clear_log_area.setObjectName("clear_log_area")
        self.action_buttons_layout.addWidget(self.clear_log_area)
        self.verticalLayout_3.addLayout(self.action_buttons_layout)
        self.horizontalLayout_3.addWidget(self.log_widget_container)
        self.horizontalLayout_3.setStretch(0, 8)
        self.main_layout.addWidget(self.frame_body)
        self.main_layout.setStretch(0, 1)
        self.main_layout.setStretch(1, 30)
        self.verticalLayout.addLayout(self.main_layout)
        DashboardForm.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(DashboardForm)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1304, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.services_operation_menu = QtWidgets.QMenu(self.menu)
        self.services_operation_menu.setObjectName("services_operation_menu")
        DashboardForm.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(DashboardForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBar.sizePolicy().hasHeightForWidth())
        self.toolBar.setSizePolicy(sizePolicy)
        self.toolBar.setMinimumSize(QtCore.QSize(0, 0))
        self.toolBar.setBaseSize(QtCore.QSize(0, 0))
        self.toolBar.setStyleSheet("height: 20px")
        self.toolBar.setMovable(False)
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.toolBar.setObjectName("toolBar")
        DashboardForm.addToolBar(QtCore.Qt.BottomToolBarArea, self.toolBar)
        self.client_sort = QtWidgets.QAction(DashboardForm)
        self.client_sort.setObjectName("client_sort")
        self.client_select_all = QtWidgets.QAction(DashboardForm)
        self.client_select_all.setObjectName("client_select_all")
        self.start_all_services_menu = QtWidgets.QAction(DashboardForm)
        self.start_all_services_menu.setObjectName("start_all_services_menu")
        self.stop_all_services_menu = QtWidgets.QAction(DashboardForm)
        self.stop_all_services_menu.setObjectName("stop_all_services_menu")
        self.restart_all_services_menu = QtWidgets.QAction(DashboardForm)
        self.restart_all_services_menu.setObjectName("restart_all_services_menu")
        self.exit_menu = QtWidgets.QAction(DashboardForm)
        self.exit_menu.setObjectName("exit_menu")
        self.client_scroll_in = QtWidgets.QAction(DashboardForm)
        self.client_scroll_in.setObjectName("client_scroll_in")
        self.client_scroll_out = QtWidgets.QAction(DashboardForm)
        self.client_scroll_out.setObjectName("client_scroll_out")
        self.remote_shutdown_menu = QtWidgets.QAction(DashboardForm)
        self.remote_shutdown_menu.setObjectName("remote_shutdown_menu")
        self.remote_reboot_menu = QtWidgets.QAction(DashboardForm)
        self.remote_reboot_menu.setObjectName("remote_reboot_menu")
        self.services_operation_menu.addAction(self.start_all_services_menu)
        self.services_operation_menu.addAction(self.stop_all_services_menu)
        self.services_operation_menu.addAction(self.restart_all_services_menu)
        self.menu.addAction(self.services_operation_menu.menuAction())
        self.menu.addAction(self.exit_menu)
        self.menubar.addAction(self.menu.menuAction())
        self.toolBar.addAction(self.client_sort)
        self.toolBar.addAction(self.client_select_all)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.client_scroll_in)
        self.toolBar.addAction(self.client_scroll_out)

        self.retranslateUi(DashboardForm)
        self.client_select_all.triggered.connect(self.desktop_layout.selectAll)
        self.client_sort.triggered.connect(self.desktop_layout.doItemsLayout)
        self.exit_menu.triggered.connect(DashboardForm.close)
        self.client_scroll_in.triggered.connect(DashboardForm.client_scroll_in)
        self.client_scroll_out.triggered.connect(DashboardForm.client_scroll_out)
        self.send_message_button.clicked.connect(DashboardForm.send_message)
        self.toggle_broadcast.clicked['bool'].connect(DashboardForm.toggle_broadcast)
        self.remote_command.clicked.connect(DashboardForm.remote_command)
        self.clear_log_area.clicked.connect(self.log_area.clear)
        self.remote_spy.clicked['bool'].connect(DashboardForm.toggle_remote_spy)
        QtCore.QMetaObject.connectSlotsByName(DashboardForm)

    def retranslateUi(self, DashboardForm):
        _translate = QtCore.QCoreApplication.translate
        DashboardForm.setWindowTitle(_translate("DashboardForm", "PYCM Dashboard"))
        self.toggle_broadcast.setText(_translate("DashboardForm", "屏幕广播"))
        self.remote_spy.setText(_translate("DashboardForm", "远程监控"))
        self.remote_command.setText(_translate("DashboardForm", "远程命令"))
        self.file_transfer.setText(_translate("DashboardForm", "文件传输"))
        self.send_message_button.setText(_translate("DashboardForm", "发送消息"))
        self.clear_log_area.setText(_translate("DashboardForm", "清除日志"))
        self.menu.setTitle(_translate("DashboardForm", "系统"))
        self.services_operation_menu.setTitle(_translate("DashboardForm", "服务"))
        self.toolBar.setWindowTitle(_translate("DashboardForm", "toolBar"))
        self.client_sort.setText(_translate("DashboardForm", "自动排列"))
        self.client_sort.setToolTip(_translate("DashboardForm", "自动排列学生端"))
        self.client_select_all.setText(_translate("DashboardForm", "选择全部"))
        self.client_select_all.setToolTip(_translate("DashboardForm", "选择全部学生端"))
        self.start_all_services_menu.setText(_translate("DashboardForm", "启动所有服务"))
        self.stop_all_services_menu.setText(_translate("DashboardForm", "停止所有服务"))
        self.restart_all_services_menu.setText(_translate("DashboardForm", "重启所有服务"))
        self.exit_menu.setText(_translate("DashboardForm", "退出"))
        self.client_scroll_in.setText(_translate("DashboardForm", "放大图标"))
        self.client_scroll_in.setToolTip(_translate("DashboardForm", "放大客户端图标"))
        self.client_scroll_out.setText(_translate("DashboardForm", "缩小图标"))
        self.client_scroll_out.setToolTip(_translate("DashboardForm", "缩小客户端图标"))
        self.remote_shutdown_menu.setText(_translate("DashboardForm", "远程关机"))
        self.remote_reboot_menu.setText(_translate("DashboardForm", "远程重启"))
import Resources_rc

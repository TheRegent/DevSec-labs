from PyQt5 import QtCore, QtWidgets


class GUI(object):

    def base(self, window):
        window.resize(720, 720)
        window.setWindowTitle("Labwork #1")

        self.rooter = QtWidgets.QRadioButton(window)
        self.rooter.setGeometry(QtCore.QRect(80, 40, 81, 16))
        self.rooter.setText("Root")

        self.user = QtWidgets.QRadioButton(window)
        self.user.setGeometry(QtCore.QRect(80, 60, 81, 16))
        self.user.setText("User")

        self.choice = QtWidgets.QLabel(window)
        self.choice.setGeometry(QtCore.QRect(80, 10, 221, 21))
        self.choice.setText("Choose a role:")

        self.start_but = QtWidgets.QPushButton(window)
        self.start_but.setGeometry(QtCore.QRect(500, 10, 201, 105))
        self.start_but.setText("Start")



        self.pwd_lable = QtWidgets.QLabel(window)
        self.pwd_lable.setGeometry(QtCore.QRect(10, 160, 51, 31))
        self.pwd_lable.setText("pwd")

        self.pwd_entry = QtWidgets.QLineEdit(window)
        self.pwd_entry.setGeometry(QtCore.QRect(70, 160, 571, 31))

        self.pwd_but = QtWidgets.QPushButton(window)
        self.pwd_but.setGeometry(QtCore.QRect(648, 160, 71, 31))
        self.pwd_but.setText("pwd")



        self.ls_label = QtWidgets.QLabel(window)
        self.ls_label.setGeometry(QtCore.QRect(10, 220, 21, 21))
        self.ls_label.setText("ls")

        self.ls_entry = QtWidgets.QLineEdit(window)
        self.ls_entry.setGeometry(QtCore.QRect(70, 210, 571, 31))

        self.ls_but = QtWidgets.QPushButton(window)
        self.ls_but.setGeometry(QtCore.QRect(648, 210, 71, 31))
        self.ls_but.setText("ls")



        self.label_cd = QtWidgets.QLabel(window)
        self.label_cd.setGeometry(QtCore.QRect(10, 270, 31, 21))
        self.label_cd.setText("cd")

        self.cd_but = QtWidgets.QPushButton(window)
        self.cd_but.setGeometry(QtCore.QRect(648, 260, 71, 31))
        self.cd_but.setText("cd")

        self.cd_entry = QtWidgets.QLineEdit(window)
        self.cd_entry.setGeometry(QtCore.QRect(70, 260, 571, 31))



        self.label_mkdir = QtWidgets.QLabel(window)
        self.label_mkdir.setGeometry(QtCore.QRect(10, 320, 71, 20))
        self.label_mkdir.setText("mkdir")

        self.mkdir_entry = QtWidgets.QLineEdit(window)
        self.mkdir_entry.setGeometry(QtCore.QRect(70, 310, 571, 31))
        self.mkdir_entry.setText("")

        self.mkdir_but = QtWidgets.QPushButton(window)
        self.mkdir_but.setGeometry(QtCore.QRect(648, 310, 71, 31))
        self.mkdir_but.setText("mkdir")



        self.label_vi = QtWidgets.QLabel(window)
        self.label_vi.setGeometry(QtCore.QRect(10, 470, 21, 20))
        self.label_vi.setText("vi")

        self.vi_entry = QtWidgets.QLineEdit(window)
        self.vi_entry.setGeometry(QtCore.QRect(70, 460, 571, 31))
        self.vi_entry.setText("")

        self.vi_but = QtWidgets.QPushButton(window)
        self.vi_but.setGeometry(QtCore.QRect(648, 460, 71, 31))
        self.vi_but.setText("vi")



        self.label_rmfile = QtWidgets.QLabel(window)
        self.label_rmfile.setGeometry(QtCore.QRect(10, 370, 71, 20))
        self.label_rmfile.setText("rmfile")

        self.rmfile_entry = QtWidgets.QLineEdit(window)
        self.rmfile_entry.setGeometry(QtCore.QRect(70, 360, 571, 31))
        self.rmfile_entry.setText("")

        self.rmfile_but = QtWidgets.QPushButton(window)
        self.rmfile_but.setGeometry(QtCore.QRect(648, 360, 71, 31))
        self.rmfile_but.setText("rmfile")



        self.rmdir_but = QtWidgets.QPushButton(window)
        self.rmdir_but.setGeometry(QtCore.QRect(648, 410, 71, 31))
        self.rmdir_but.setText("rmdir")

        self.rmdir_entry = QtWidgets.QLineEdit(window)
        self.rmdir_entry.setGeometry(QtCore.QRect(70, 410, 571, 31))
        self.rmdir_entry.setText("")

        self.label_rmdir = QtWidgets.QLabel(window)
        self.label_rmdir.setGeometry(QtCore.QRect(10, 420, 71, 20))
        self.label_rmdir.setText("rmdir")



        self.vi_txt_entry = QtWidgets.QPlainTextEdit(window)
        self.vi_txt_entry.setGeometry(QtCore.QRect(10, 500, 701, 181))
        self.vi_txt_entry.setPlainText("")

        self.blocker = QtWidgets.QRadioButton(window)
        self.blocker.setGeometry(QtCore.QRect(80, 80, 161, 16))
        self.blocker.setCheckable(True)
        self.blocker.setChecked(True)
        self.blocker.setText("Blocked user")

        self.label_root = QtWidgets.QLabel(window)
        self.label_root.setGeometry(QtCore.QRect(270, 30, 291, 21))
        self.label_root.setText("# Root has all rights (rwx)")

        self.label_user = QtWidgets.QLabel(window)
        self.label_user.setGeometry(QtCore.QRect(270, 50, 301, 21))
        self.label_user.setText("# User has limited rights (r-x)")

        self.label_blocked_user = QtWidgets.QLabel(window)
        self.label_blocked_user.setGeometry(QtCore.QRect(270, 70, 321, 21))
        self.label_blocked_user.setText("# Blocked user has not rights (---)")

        self.finish_but = QtWidgets.QPushButton(window)
        self.finish_but.setGeometry(QtCore.QRect(10, 690, 701, 25))
        self.finish_but.setText("End")

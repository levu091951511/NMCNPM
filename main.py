from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets
from Handle.quanlynhankhauhandle  import Main
from Handle.signinHandle import SignIn
from Service.ConnetDB import MY_DB
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
db = MY_DB()
# result_user = db.select_NguoiDung_MatKhau()
from Service import globals


class UIMAINHK_NK():
    def __init__(self):
        self.mainUI = QMainWindow()
        self.main = Main(self.mainUI) 
        # self.main.setup()
        # self.main.pushButton_23.clicked.connect(self.main.KhaiBaoNhanKhauHandle)
        self.signinUI = QMainWindow()
        self.signin = SignIn(self.signinUI)
        self.signinUI.show()
        self.signin.pushButton_login.clicked.connect(lambda: self.checkFields())
        self.main.pushButton.clicked.connect(self.Logout)

        
        # self.mainUI.show()

    def checkFields(self):
        textUser = ""
        textPassword = ""

        def showMessage(message):
            self.signin.frame_error.show()
            self.signin.label_error.setText(message)

        # CHECK USER
        if not self.signin.lineEdit_user.text():
            textUser = " User Empyt. "
            self.signin.lineEdit_user.setStyleSheet(self.signin.styleLineEditError)
        else:
            textUser = self.signin.lineEdit_user.text()
            self.signin.lineEdit_user.setStyleSheet(self.signin.styleLineEditOk)

        # CHECK PASSWORD
        if not self.signin.lineEdit_password.text():
            textPassword = " Password Empyt. "
            self.signin.lineEdit_password.setStyleSheet(self.signin.styleLineEditError)
        else:
            textPassword = self.signin.lineEdit_password.text()
            self.signin.lineEdit_password.setStyleSheet(self.signin.styleLineEditOk)

        if not self.signin.lineEdit_user.text() and not self.signin.lineEdit_password.text():
            text = "User Empyt && Password Empyt"
            showMessage(text)
            self.signin.frame_error.setStyleSheet(self.signin.stylePopupError)

        else:
            # CHECK FIELDS
            result_user = db.select_NguoiDung_MatKhau(textUser, textPassword)
            if result_user.fetchall() == []:
                text = "Tên Đăng Nhập Hoặc Mật Khẩu Không Đúng"
                showMessage(text)
                # print(textUser, textPassword)
                self.signin.frame_error.setStyleSheet(self.signin.stylePopupError)
            else:
                globals.username = textUser
                globals.password = textPassword
                self.main.setup()   
                text = " Login OK. "
                showMessage(text)
                self.signin.frame_error.setStyleSheet(self.signin.stylePopupOk)
                self.signinUI.hide()
                self.mainUI.show()
    def Logout(self):
        question = QMessageBox.question(self.main.tab_7, "Thông Báo", "Bạn chắc chắn muốn đăng xuất ?  ")
        if question == QMessageBox.Yes:
            QMessageBox.information(self.main.tab_7, "Thông Báo", "Đã Đăng Xuất")
            self.mainUI.hide()
            self.signinUI.show()
        

        
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UIMAINHK_NK()
    sys.exit(app.exec_())
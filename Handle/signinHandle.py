from View.UI.dangnhap import Ui_Signin

class SignIn(Ui_Signin):
    def __init__(self, ui_signin):
        self.setupUi(ui_signin)
        self.frame_error.hide()

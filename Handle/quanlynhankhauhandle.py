from View.UI.quanlynhankhauui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from Service.ConnetDB import MY_DB
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import time
import datetime
from Service import globals


'''
Class Main chứa các hàm xử lý các tab
+ Tên Người Lập Trình: Lê Quang Vũ
+ Ngày Đã Lưu: 11/2/2023
+ Tên Dự Án: BTL-CNPM
+ Tên Giáo Viên: Trịnh Thành Trung
+ Tên Môn Học: Công Nghệ Phần Mềm
+ Người Giúp Đỡ: Lê Nguyên Khang
+ mô tả:
    - chương trình gồm các hàm xử lý các tab: (NguoiDung_Handler, KhaiBaoNhanKhauHandle...)
    - Kết nối cơ sở dữ liệu để truy vấn các thao tác hiển thị, thêm, sửa, xóa thông tin
    - xử lý các nút bấm trên giao diện để hiển thị các tab và thao tác các chức năng
'''

class Main(Ui_MainWindow):
    def __init__(self, ui_main):
        self.setupUi(ui_main)
        self.ui_main = ui_main
        self.getMS = None
        self.getName = None
        self.nguoidunghientai = None
        self.pushButton_24.clicked.connect(lambda: self.frame_8.setEnabled(True))
        self.tableWidget_17.setHorizontalHeaderLabels(["Từ Ngày", "Đến Ngày", "Chỗ Ở", "Nghề Nghiệp", "Nơi Làm Việc", "Ghi Chú"])
        self.tableWidget_20.setHorizontalHeaderLabels(["Ngày", "TATS", "Hình Thức", "Mức Độ", "Thời Gian", "Cơ Quan Xử Lý", "Ngày Lưu", "Ghi Chú"])
        self.tableWidget_18.setHorizontalHeaderLabels(["Từ Ngày", "Đến Ngày", "Chỗ Ở", "Nghề Nghiệp", "Nơi Làm Việc", "Tiền Án"])
        self.tableWidget_18.setEnabled(True)
        self.comboBox_4.setEnabled(True)
        self.tableWidget_3.setHorizontalHeaderLabels(["Nhân Khẩu", "Số Hộ Khẩu", "Chỗ Ở", "Nghề Nghiệp", "QH Với Chủ Hộ", "Tiền Án"])
        self.tableWidget_3.setEnabled(True)
        self.tableWidget_5.setHorizontalHeaderLabels(["Số Hộ Khẩu", "Họ Tên", "Ngày Sinh", "Nơi Sinh", "Nơi ĐKHKTT", "Số CCCD", "Quan Hệ Với chủ hộ"])
        self.tableWidget_21.setHorizontalHeaderLabels(["Số Hộ Khẩu", "Họ Tên", "Ngày Sinh", "Nơi Sinh", "Nơi ĐKHKTT", "Số CCCD", "Quan Hệ Với chủ hộ"])
        self.tableWidget_6.setHorizontalHeaderLabels(["Số Hộ Khẩu", "Họ Tên", "Ngày Sinh", "Nơi Sinh", "Nơi ĐKHKTT", "Số CCCD", "Quan Hệ Với chủ hộ"])
        self.tableWidget_8.setHorizontalHeaderLabels(['Mã Nhân Khẩu', 'Họ Tên'])
        self.tableWidget_9.setHorizontalHeaderLabels(["Từ Ngày", "Đến Ngày", "Chỗ Ở", "Nghề Nghiệp", "Nơi Làm Việc", "Ghi Chú"])
        self.tableWidget_12.setHorizontalHeaderLabels(['Số Hộ Khẩu', 'Họ Tên Chủ Hộ'])
        self.tableWidget_13.setHorizontalHeaderLabels(["Mã Nhân Khẩu", "Họ Tên", "Ngày Sinh", "Nơi Sinh", "Nơi ĐKHKTT", "Số CCCD", "Quan Hệ Với chủ hộ"])
        self.tableWidget_15.setHorizontalHeaderLabels(["Mã Nhân Khẩu", "Họ Tên", "Ngày Sinh", "Nơi Sinh", "Nơi ĐKHKTT", "Số CCCD", "Quan Hệ Với chủ hộ"])
        self.tableWidget_2.setHorizontalHeaderLabels(["Mã Nhân Khẩu", "Họ Tên", "Ngày Sinh", "Nơi Sinh", "Nơi ĐKHKTT", "Số CCCD"])
        self.tableWidget_16.setHorizontalHeaderLabels(["Mã Nhân Khẩu", "Họ Tên", "Ngày Sinh", "Nơi Sinh", "Nơi ĐKHKTT", "Số CCCD"])
        self.tableWidget_11.setHorizontalHeaderLabels(["Mã Chủ Hộ", "Họ Tên Chủ Hộ", "Địa Chỉ", "Ngày Lập"])
        self.MaNK = []
        self.MaHK = []
        self.MaKS = []
        self.chucvu_user = "Tổ Trưởng"

        # =======================================================================================================
        # sử lý các nút bấm trên giao diện
        self.pushButton_23.clicked.connect(self.KhaiBaoNhanKhauHandle)
        self.pushButton_33.clicked.connect(self.KhaiSinhMoiHandle)
        self.pushButton_3.clicked.connect(self.NguoiDung_Handler)
        self.pushButton_5.clicked.connect(self.KhaiMoiHoKhau)
        # self.pushButton_5.clicked.connect(self.KhaiTu)

        self.pushButton_14.clicked.connect(self.exit)
        self.tabWidget_2.tabCloseRequested.connect(self.CloseTab)
        self.pushButton_2.clicked.connect(self.DoiMatKhau_Handle)
        # self.pushButton_5.clicked.connect(self.tab_KhaiBaoHoKhau)
        self.pushButton_8.clicked.connect(self.TamTru_Handler)
        self.pushButton_63.clicked.connect(self.TamVang_Handler)
        self.pushButton_7.clicked.connect(self.ChuyenDi_Handler)
        self.pushButton_6.clicked.connect(self.NhapKhau_Handle)
        self.pushButton_69.clicked.connect(self.TachKhau_Handle)
        self.pushButton_9.clicked.connect(self.ThongTinNhanKhau_Handler)
        self.pushButton_11.clicked.connect(self.ThongTinHoKhau_Handler)
        self.pushButton_12.clicked.connect(self.TimKiemNhanKhau)
        self.pushButton_13.clicked.connect(self.TimKiemHoKhau_Handler)
        self.pushButton_33.clicked.connect(self.KhaiSinhMoiHandle)
        self.pushButton_64.clicked.connect(self.ThongKe_Handler)
        self.pushButton_65.clicked.connect(self.KhaiTu_Handler)
        self.pushButton_71.clicked.connect(self.NhaVanHoaHandler)
        self.pushButton_78.clicked.connect(lambda: self.tabWidget_3.addTab(self.tab_26, "Thông Tin Sự Kiện"))
        self.pushButton_79.clicked.connect(lambda: self.tabWidget_3.addTab(self.tab_25, "Thông Tin Cơ Sở Vật Chất"))
                
        # ==========================================================================================================

        
    # lấy dữ liêu các bảng ========================================================================================
    def GetData(self, table, MaHK = None, MaNK = None, MaKS = None, HoTenKhaiSinh = None, DiaChi = None, GioiTinh = None):
        self.db = MY_DB()
        if table == "HoKhau":
            if MaHK is not None:
                self.result = self.db.select_all_HoKhau(MaHK, None, None)
            elif HoTenKhaiSinh is not None:
                self.result = self.db.select_all_HoKhau(None, HoTenKhaiSinh, None)
            elif DiaChi is not None:
                self.result = self.db.select_all_HoKhau(None, None, DiaChi)
            else:
                self.result = self.db.select_all_HoKhau()

        elif table == "NhanKhau":
            if MaHK is not None:
                self.result = self.db.select_all_NhanKhau(MaHK, None, None, None, None, None)
            elif MaNK is not None:
                self.result = self.db.select_all_NhanKhau(None, MaNK, None, None, None, None)
            elif MaKS is not None:
                self.result = self.db.select_all_NhanKhau(None, None, MaKS, None, None, None)
            elif HoTenKhaiSinh is not None:
                self.result = self.db.select_all_NhanKhau(None, None, None, HoTenKhaiSinh, None, None)
            elif DiaChi is not None:
                self.result = self.db.select_all_NhanKhau(None, None, None, None, DiaChi, None)
            elif GioiTinh is not None:
                self.result = self.db.select_all_NhanKhau(None, None, None, None, None, GioiTinh)
            else:
                self.result = self.db.select_all_NhanKhau(None, None, None, None, None, None)

        elif table == "KhaiSinh":
            if MaKS is not None:
                self.result = self.db.select_all_KhaiSinh(MaKS, None, None, None)
            elif HoTenKhaiSinh is not None:
                self.result = self.db.select_all_KhaiSinh(None, HoTenKhaiSinh, None, None)
            elif DiaChi is not None:
                self.result = self.db.select_all_KhaiSinh(None, None, DiaChi, None)
            elif GioiTinh is not None:
                self.result = self.db.select_all_KhaiSinh(None, None, None, GioiTinh)
            else:
                self.result = self.db.select_all_KhaiSinh(None, None, None, None)

        elif table == "KhaiBao":
            if MaNK is not None:
                self.result = self.db.select_all_NhanKhau(MaNK)
            else:
                self.result = self.db.select_all_NhanKhau(None)

        elif table == "TamTru":
            if MaNK is not None:
                self.result = self.db.select_all_TamTru(MaNK)
            else:
                self.result = self.db.select_all_Tamtru(None)   

        elif table == "TienAnTienSu":
            if MaNK is not None:
                self.result = self.db.select_all_TienAnTienSu(MaNK)
            else:
                self.result = self.db.select_all_TienAnTienSu(None)   

        elif table == "TamVang":
            if MaNK is not None:
                self.result = self.db.select_all_TamVang(MaNK)
            else:
                self.result = self.db.select_all_TamVang(None)

        return self.result

    # setup all tab ==========================================================================================
    # set dữ liệu, thông tin ban đầu cho các tab
    def setup(self):
        self.db = MY_DB()
        result_select_hokhau = self.GetData("HoKhau")
        for row_num, row_data in enumerate(result_select_hokhau):
            for col_num, col_data in enumerate(row_data):
                if col_num == 0:
                    self.MaHK.append(col_data)
                    self.comboBox.addItem(col_data)
                    self.comboBox_11.addItem(col_data)
        
        result_select_nhankhau = self.GetData("NhanKhau")
        for row_num, row_data in enumerate(result_select_nhankhau):
            for col_num, col_data in enumerate(row_data):
                if col_num == 0:
                    self.MaNK.append(col_data)
                    self.comboBox_7.addItem(col_data)
                    self.comboBox_8.addItem(col_data)
                    self.comboBox_10.addItem(col_data)
                    self.comboBox_12.addItem(col_data)
                    self.comboBox_13.addItem(col_data)
                    self.comboBox_19.addItem(col_data)
                    self.comboBox_6.addItem(col_data)
 
        result_select_khaisinh = self.GetData("KhaiSinh")
        for row_num, row_data in enumerate(result_select_khaisinh):
            for col_num, col_data in enumerate(row_data):
                if col_num == 0:
                    self.MaKS.append(col_data)
                    self.comboBox_9.addItem(col_data)
        self.result_NguoiDungHienTai = self.db.ThongTinNguoiDung(globals.username, globals.password)
        self.nguoidunghientai = self.result_NguoiDungHienTai.fetchall()[0]
        self.label_7.setText("Quản lý:" + self.nguoidunghientai[1])
        self.label_8.setText(str(time.strftime("         %Y/%m/%d - %H:%M:%S:%p")))

        user = self.db.ThongTinNguoiDung(globals.username, globals.password).fetchall()[0]
        self.chucvu_user = user[5]
        
    
    # TAB NGƯỜI DÙNG =================================================================================
    def NguoiDung_Handler(self):
        if self.chucvu_user == "Tổ Trưởng":
            # self.setupUi(self.ui_main)
            i = self.tabWidget_2.addTab(self.tab_5, "Người Dùng")
            self.tabWidget_2.setCurrentIndex(i)
            # khao báo cơ sở dữ liệu
            self.db = MY_DB()
            print(globals.username)
            self.result = self.db.ThongTinNguoiDung(globals.username, globals.password)

            # setub cho tab người dùng
            for row_num, row_data in enumerate(self.result):
                for col_num, col_data in enumerate(row_data):
                    if col_num == 0:
                        self.mSLineEdit.setText(col_data)
                        self.getMS = col_data
                    elif col_num == 1:
                        self.hTNLineEdit.setText(col_data)
                        self.getName = col_data
                    elif col_num == 2:
                        self.userNameLineEdit.setText(col_data)
                    elif col_num == 3:
                        if col_data == self.radioButton.text():
                            self.radioButton.nextCheckState()
                        elif col_data == self.radioButton_2.text():
                            self.radioButton_2.nextCheckState()
                    elif col_num == 4:
                        self.emailLineEdit.setText(col_data)
                    elif col_num == 5:
                        self.chCVLineEdit.setText(col_data)
                    elif col_num == 6:
                        self.quyNHNLineEdit.setText(col_data)
                    elif col_num == 7:
                        date = col_data.split("-")
                        d = QDate(int(date[0]), int(date[1]), int(date[2]))
                        self.dateEdit.setDate(d)
                    elif col_num == 8:
                        self.aChLineEdit.setText(col_data)
                    elif col_num == 9:
                        self.iNThoILineEdit.setText(col_data)

                    # self.tableWidget.setItem(row_num, col_num, QtWidgets.QTableWidgetItem(""))
                    self.tableWidget.setItem(row_num, col_num, QtWidgets.QTableWidgetItem(str(col_data)))
                    self.tableWidget.setHorizontalHeaderLabels(["Mã Số", "Họ Tên", "UserName", "Giới Tính", "Email", "Chức Vụ", "quyền hạn", "ngày sinh", "địa chỉ", "Số Điện Thoại"])

            self.result = self.db.select_all_user()
            for row_num, row_data in enumerate(self.result):
                for col_num, col_data in enumerate(row_data):
                    # self.tableWidget.setItem(row_num, col_num, QtWidgets.QTableWidgetItem(""))
                    self.tableWidget.setItem(row_num, col_num, QtWidgets.QTableWidgetItem(str(col_data)))
                    self.tableWidget.setHorizontalHeaderLabels(["Mã Số", "Họ Tên", "UserName","Giới Tính", "Email", "Chức Vụ", "quyền hạn", "ngày sinh", "địa chỉ", "Số Điện Thoại"])

            def LuuNguoiDung():
                self.db = MY_DB()
                ms = self.mSLineEdit.text()
                name = self.hTNLineEdit.text()
                username = self.userNameLineEdit.text()
                sex = "Nữ"
                if self.radioButton.isChecked():
                    sex = "Nam"
                email = self.emailLineEdit.text()
                chucvu = self.chCVLineEdit.text()
                quyenhan = self.quyNHNLineEdit.text()
                ngaysinh = self.dateEdit.date()
                ngaysinh = str(ngaysinh.toPyDate())
                diachi = self.aChLineEdit.text()
                sodienthoai = self.iNThoILineEdit.text()
                if self.getMS == ms:
                    self.db.updateSqliteTable_User(ms, name, username, sex, email, chucvu, quyenhan, str(ngaysinh), diachi, sodienthoai)
                else:
                    self.db.insertSqliteTable_User(ms, name, username, sex, email, chucvu, quyenhan, str(ngaysinh), diachi, sodienthoai)
                self.NguoiDung_Handler()
            
            # nếu click vào nút lưu thì update người dùng
            self.pushButton_16.clicked.connect(LuuNguoiDung)

            def XoaNguoiDung(self): 
                pass
        else:
            QMessageBox.information(self.tab_7, "Thông Báo", "Không có quyền hạn truy cập chức năng")

    # =================================================================================================================
    # Hàm sử lý chức năng đổi mật khẩu
    def DoiMatKhau_Handle(self):
        i = self.tabWidget_2.addTab(self.tab_18, "Đổi Mật Khẩu")
        # self.dict.update(i: "Đổi Mật Khẩu")
        self.tabWidget_2.setCurrentIndex(i)
        result_select_NguoiDung_MatKhau = self.db.select_NguoiDung_MatKhau(globals.username, globals.password).fetchall()[0]
        print(result_select_NguoiDung_MatKhau)

        def NhapMatKhauCu():
            matkhaucu = self.mTKhUCLineEdit.text()
            if result_select_NguoiDung_MatKhau[1] == matkhaucu:
                return True
            else:
                return False
        def update_matkhau():
            if NhapMatKhauCu() and self.mTKhUMILineEdit.text() == self.nhPLIMTKhULineEdit.text():
                self.db.update_matkhau(self.nhPLIMTKhULineEdit.text(), result_select_NguoiDung_MatKhau[0])
                QMessageBox.information(self.tab_18, "Thông Báo", "Đổi Mật Khẩu Thành Công")
            else:
                QMessageBox.information(self.tab_18, "Thông Báo", "Đổi Mật Khẩu Thất Bại ")

        self.pushButton_51.clicked.connect(update_matkhau)

    # xử lý tab khai báo nhân khẩu ============================================================================        
    def KhaiBaoNhanKhauHandle(self):
        if self.chucvu_user == "Tổ Trưởng":
            i = self.tabWidget_2.addTab(self.tab_8, "Khai Báo Nhân Khẩu")
            self.tabWidget_2.setCurrentIndex(i)
            self.db = MY_DB()
            self.frame_5.setEnabled(True)
            MaNK = self.comboBox_7.currentText()
            MaHK = self.comboBox.currentText()

            def get_thong_tin_ho_khau():
                mahk = self.comboBox.currentText()
                result_select_all_HoKhau_NhanKhau_maHK = self.db.select_all_HoKhau_NhanKhau_maHK(str(mahk))
                result = result_select_all_HoKhau_NhanKhau_maHK.fetchall()[0]
                self.hTNLineEdit_2.setText(result[0])
                date = result[1].split("-")
                d = QDate(int(date[0]), int(date[1]), int(date[2]))
                self.dateEdit_5.setDate(d)
                if result[2] == self.radioButton_3.text():
                    self.radioButton_5.nextCheckState()
                elif result[2] == self.radioButton_4.text():
                    self.radioButton_6.nextCheckState()
                self.nghNghiPLineEdit_3.setText(result[3])
                self.chLineEdit_2.setText(result[4])
                
            # kiem tra khi bam nut tiep tuc MaNK
            def check():
                mank = self.comboBox_7.currentText()
                result_select_nhankhau_MaNK = self.GetData("NhanKhau",None, mank, None, None, None, None)
                if result_select_nhankhau_MaNK.fetchall() == []:
                    self.frame_11.setEnabled(True)
                    self.frame_12.setEnabled(True)
                    self.comboBox.setEnabled(False)
                    self.comboBox_7.setEnabled(False)
                else:
                    self.frame_11.setEnabled(False)
                    self.frame_12.setEnabled(False)
                    QMessageBox.information(self.tab_18, "Thông Báo", "Mã hộ khẩu hoặc nhân khẩu đã tồn tại, vui lòng nhập mã khác")

            def check_2():
                mahk = self.comboBox.currentText()
                mank = self.comboBox_7.currentText()
                MaKS = self.comboBox_9.currentText()
                HoTen = self.hTNKhaiSinhLineEdit.text()
                TenGoiKhac = self.tNGIKhCLineEdit.text()
                sex = "Nữ"
                if self.radioButton_3.isChecked():
                    sex = "Nam"
                date = self.dateEdit_2.date()
                date = str(date.toPyDate())
                NoiSinh = self.nISinhLineEdit.text()
                QueQuan = self.quQuNLineEdit.text()
                ChoOHienNay  =self.chHiNNayLineEdit.text()
                DanToc = self.comboBox_2.currentText()
                TonGiao = self.comboBox_3.currentText()
                QuocTich = self.quCTChLineEdit_2.text()
                SoCCCD = self.sCCCDLineEdit.text()
                NoiCap = self.nICPLineEdit.text()
                NoiDKHKTT = self.nIKHKTTLineEdit.text()
                TrinhDoHocVan = self.trNhHCVNLineEdit.text()
                NgheNghiep = self.nghNghiPLineEdit.text()
                DauVet = self.dUVTDHNhLineEdit.text()
                GhiChu = self.ghiChLineEdit.text()
                CanBoDH = self.cNBHNgDNLineEdit.text()
                NguoiKhai = self.ngIKhaiLineEdit.text()
                NgayKhai = self.ngYKhaiLineEdit.text()
                result_select_hokhau_MaHK = self.GetData("HoKhau", mahk, None, None, None, None, None)
                result_select_nhankhau_MaNK = self.GetData("NhanKhau",None, mank, None, None, None, None)
                # print(result_select_nhankhau_MaNK.fetchall())    
                if result_select_nhankhau_MaNK.fetchall() == [] and HoTen and sex and date and NoiSinh and QueQuan and ChoOHienNay and DanToc and QuocTich and NoiDKHKTT and CanBoDH and NguoiKhai and NgayKhai != "":
                    if insert_nhankhau():
                        self.frame_5.setEnabled(True)
                        self.frame_11.setEnabled(False)
                        self.frame_12.setEnabled(False)
                        self.pushButton_31.setEnabled(False)
                    else:
                        self.frame_11.setEnabled(True)
                        self.frame_12.setEnabled(True)
                        self.frame_5.setEnabled(False)
                        self.comboBox.setEditable(True)
                        self.comboBox_7.setEditable(True)
                        QMessageBox.information(self.tab_18, "", "Lưu Không Thành Công")
                else:
                    self.frame_11.setEnabled(True)
                    self.frame_12.setEnabled(True)
                    self.frame_5.setEnabled(False)
                    self.comboBox.setEditable(True)
                    self.comboBox_7.setEditable(True)
                    QMessageBox.information(self.tab_18, "", "vui lòng kiểm tra lại thông tin")

            self.pushButton_15.clicked.connect(check)
            self.pushButton_15.clicked.connect(get_thong_tin_ho_khau)
            self.pushButton_66.clicked.connect(check)

            def KiemTraKhaiSinh(MaKS):
                result_select_khaisinh = self.GetData("KhaiSinh", None, None, MaKS, None, None, None)
                if result_select_khaisinh is not None:
                    QMessageBox.information(self.tab_18, "", "đã có khai sinh, tiến hành chỉnh sửa thông tin")
                    for row_num, row_data in enumerate(result_select_khaisinh):
                        for col_num, col_data in enumerate(row_data):
                            if col_num == 1:
                                self.hTNKhaiSinhLineEdit.setText(col_data)
                            elif col_num == 2:
                                self.tNGIKhCLineEdit.setText(col_data)
                            elif col_num == 3:
                                if col_data == self.radioButton_3.text():
                                    self.radioButton_3.nextCheckState()
                                elif col_data == self.radioButton_4.text():
                                    self.radioButton_4.nextCheckState()
                            elif col_num == 4:
                                date = col_data.split("-")
                                print(date)
                                d = QDate(int(date[0]), int(date[1]), int(date[2]))
                                self.dateEdit_2.setDate(d)
                            elif col_num == 5:
                                self.nISinhLineEdit.setText(col_data)
                            elif col_num == 6:
                                self.quQuNLineEdit.setText(col_data)
                            elif col_num == 7:
                                self.chHiNNayLineEdit.setText(col_data)
                            elif col_num == 8:
                                self.comboBox_2.addItem(col_data)
                            elif col_num == 9:
                                self.comboBox_3.addItem(col_data)
                            elif col_num == 10:
                                self.quCTChLineEdit_2.setText(col_data)
            
            def insert_nhankhau():
                MaHK = self.comboBox.currentText()
                MaNK = self.comboBox_7.currentText()
                MaKS = self.comboBox_9.currentText()
                HoTen = self.hTNKhaiSinhLineEdit.text()
                TenGoiKhac = self.tNGIKhCLineEdit.text()
                sex = "Nữ"
                if self.radioButton_3.isChecked():
                    sex = "Nam"
                date = self.dateEdit_2.date()
                date = str(date.toPyDate())
                NoiSinh = self.nISinhLineEdit.text()
                QueQuan = self.quQuNLineEdit.text()
                ChoOHienNay  =self.chHiNNayLineEdit.text()
                DanToc = self.comboBox_2.currentText()
                TonGiao = self.comboBox_3.currentText()
                QuocTich = self.quCTChLineEdit_2.text()
                SoCCCD = self.sCCCDLineEdit.text()
                NoiCap = self.nICPLineEdit.text()
                NoiDKHKTT = self.nIKHKTTLineEdit.text()
                TrinhDoHocVan = self.trNhHCVNLineEdit.text()
                NgheNghiep = self.nghNghiPLineEdit.text()
                DauVet = self.dUVTDHNhLineEdit.text()
                GhiChu = self.ghiChLineEdit.text()
                CanBoDH = self.cNBHNgDNLineEdit.text()
                NguoiKhai = self.ngIKhaiLineEdit.text()
                NgayKhai = self.ngYKhaiLineEdit.text()
                QuanHe = self.comboBox_4.currentText()
                data_nhankhau = (MaNK, MaKS, MaHK, HoTen, TenGoiKhac, sex, date, NoiSinh, QueQuan, ChoOHienNay, DanToc, TonGiao, QuocTich, 
                SoCCCD, NoiCap, NoiDKHKTT, TrinhDoHocVan, NgheNghiep, DauVet, QuanHe, "", "", "", "", "", NguoiKhai, CanBoDH, NgayKhai)

            self.pushButton_19.clicked.connect(lambda:KiemTraKhaiSinh(self.comboBox_9.currentText()))
            self.pushButton_31.clicked.connect(check_2)

            def CapNhatThongTinDaLuu_NhanKhau(MaNK):
                result_capnhat = self.db.select_all_NhanKhau(None, MaNK, None, None, None, None)
                result_tienantiensu_mank = self.db.select_all_TienAnTienSu(MaNK)
                tienan = result_tienantiensu_mank.fetchall()[0][3]
                for row_num, row_data in enumerate(result_capnhat):
                    for col_num, col_data in enumerate(row_data):
                        if col_num == 2:
                            self.tableWidget_3.setItem(row_num, 1, QtWidgets.QTableWidgetItem(str(col_data)))
                        elif col_num == 3:
                            self.tableWidget_3.setItem(row_num, 0, QtWidgets.QTableWidgetItem(str(col_data)))
                        elif col_num == 9:
                            self.tableWidget_3.setItem(row_num, 2, QtWidgets.QTableWidgetItem(str(col_data)))
                        elif col_num == 17:
                            self.tableWidget_3.setItem(row_num, 3, QtWidgets.QTableWidgetItem(str(col_data)))
                        else:
                            self.tableWidget_3.setItem(row_num, 4, QtWidgets.QTableWidgetItem(str(self.comboBox_4.currentText())))
                            self.tableWidget_3.setItem(row_num, 5, QtWidgets.QTableWidgetItem(tienan))
            
            def get_KhaiBao_and_TienAnTienSu(MaNK):
                self.db = MY_DB()
                # result_khaibao = self.db.select_all_KhaiBao(None)
                result_khaobao_mank = self.db.select_all_KhaiBao(MaNK)
                # result_tienantiensu = self.db.select_all_TienAnTienSu(None)
                result_tienantiensu_mank = self.db.select_all_TienAnTienSu(MaNK)

                # dien vao bang tab khai bao
                for row_num, row_data in enumerate(result_khaobao_mank):
                    for col_num, col_data in enumerate(row_data):
                        if col_num == 0 or col_num == 1:
                            continue
                        else:
                            self.tableWidget_17.setItem(row_num, col_num - 2, QtWidgets.QTableWidgetItem(str(col_data)))
                            if col_num < 7:
                                self.tableWidget_18.setItem(row_num, col_num - 2, QtWidgets.QTableWidgetItem(str(col_data)))
                        
                for row_num, row_data in enumerate(result_tienantiensu_mank):
                    for col_num, col_data in enumerate(row_data):
                        if col_num == 0 or col_num == 1:
                            continue
                        else:
                            self.tableWidget_20.setItem(row_num, col_num - 2, QtWidgets.QTableWidgetItem(str(col_data)))
                            if col_num == 3:
                                self.tableWidget_18.setItem(row_num, col_num + 2, QtWidgets.QTableWidgetItem(str(col_data)))
                                self.tableWidget_18.setItem(row_num, col_num + 2, QtWidgets.QTableWidgetItem(str(col_data)))
            self.pushButton_22.clicked.connect(lambda:CapNhatThongTinDaLuu_NhanKhau(self.comboBox_7.currentText()))
            self.pushButton_21.clicked.connect(lambda: self.KhaiBaoHandle(self.comboBox_7.currentText())) 
            self.pushButton_21.clicked.connect(lambda:get_KhaiBao_and_TienAnTienSu(self.comboBox_7.currentText()))
        else:
            QMessageBox.information(self.tab_7, "Thông Báo", "Không có quyền hạn truy cập chức năng")
    # xử lý tab khai sinh ======================================================================================
    def KhaiSinhMoiHandle(self):
        if self.chucvu_user == "Tổ Trưởng":
            i = self.tabWidget_2.addTab(self.tab_19, "Khai Sinh Mới")
            self.tabWidget_2.setCurrentIndex(i)
            self.db = MY_DB()
            def insert_khaisinh():
                MaKS = self.hTNKhaiSinhLineEdit_10.text()
                HoTen = self.hTNKhaiSinhLineEdit_9.text()
                TenGoiKhac = self.tNGIKhCLineEdit_4.text()
                sex = "Nữ"
                if self.radioButton_21.isChecked():
                    sex = "Nam"
                date = self.dateEdit_22.date()
                date = str(date.toPyDate())
                NoiSinh = self.nISinhLineEdit_6.text()
                QueQuan = self.quQuNLineEdit_6.text()
                ChoOHienNay = self.chHiNNayLineEdit_5.text()
                DanToc = self.comboBox_16.currentText()
                TonGiao = self.comboBox_17.currentText()
                QuocTich = self.quCTChLineEdit_5.text()
                HoTenBo = self.sCCCDLineEdit_5.text()
                NamSinhBo = self.dateEdit_7.date()
                NamSinhBo = str(NamSinhBo.toPyDate())
                if NamSinhBo == "2000-01-01":
                    NamSinhBo = ""
                HoTenMe = self.hTNCAMLineEdit.text()
                NamsinhMe = self.dateEdit_9.date()
                NamsinhMe = str(NamsinhMe.toPyDate())
                if NamsinhMe == "2000-01-01":
                    NamsinhMe = ""
                DauVet = self.dUVTDHNhLineEdit_4.text()
                GhiChu = self.ghiChLineEdit_12.text()
                NguoiKhai = self.ngIKhaiLineEdit_4.text()
                CanBoDH = self.cNBHNgDNLineEdit_4.text()
                NgayKhai = self.ngYKhaiLineEdit_4.text()
                
                data_khaisinh = (MaKS, HoTen, TenGoiKhac, sex, date, NoiSinh, QueQuan, ChoOHienNay, DanToc,
                TonGiao, QuocTich, HoTenBo, NamSinhBo, HoTenMe, NamsinhMe, DauVet, GhiChu, NguoiKhai, CanBoDH, NgayKhai)
                self.db.insertSqliteTable_KhaiSinh(data_khaisinh)

            
            def check_MaKS():
                maks_box  = self.hTNKhaiSinhLineEdit_10.text()
                result_select_khaisinh = self.GetData("KhaiSinh", None, None, maks_box, None, None, None)
                # print(result_select_khaisinh.fetchall())
                if result_select_khaisinh.fetchall() == []:
                    self.pushButton_58.setEnabled(True)
                    print("mã khai sinh hợp lý")
                else:
                    self.pushButton_58.setEnabled(False)
                    print("Mã Khai sinh đã tồn tại, vui lòng nhập mã khai sinh khác")

            self.pushButton_56.clicked.connect(lambda: check_MaKS())
            self.pushButton_58.clicked.connect(lambda: insert_khaisinh())
        else:
            QMessageBox.information(self.tab_7, "Thông Báo", "Không có quyền hạn truy cập chức năng")

    # xử lý tab Khai báo =================================================================================
    def KhaiBaoHandle(self, mank):
        self.db = MY_DB()
        i = self.tabWidget_2.addTab(self.tab_6, "Khai Báo")
        # self.dict.update(i: "Tạm Trú / Tạm Vắng")
        self.tabWidget_2.setCurrentIndex(i)
        # mank = self.comboBox_7.currentText()
        self.label_66.setText("Thông Tin Khai Báo Nhân Khẩu:" + mank)
        def khaibao():
            TuNgay = self.dateEdit_20.date()
            TuNgay = str(TuNgay.toPyDate())
            DenNgay = self.dateEdit_21.date()
            DenNgay = str(DenNgay.toPyDate())
            ChoO = self.chLineEdit_7.text()
            NgheNghiep = self.nghNghiPLineEdit_11.text()
            NoiLamViec = self.nILMViCLineEdit_5.text()
            GhiChu = self.ghiChLineEdit_11.text()
            
            data_khaibao = ("", mank, TuNgay, DenNgay, ChoO, NgheNghiep, NoiLamViec, GhiChu)
            self.db.insertSqliteTable_KhaiBao(data_khaibao)
    
        def tienantiensu():
            Ngay = self.dateEdit_17.date()
            Ngay = str(Ngay.toPyDate())
            TienAnTienSu = self.nILMViCLineEdit_6.text()
            HinhThuc = self.ghiChLineEdit_13.text()
            MucDo = self.mCLineEdit.text()
            ThoiGianXuLy = self.nILMViCLineEdit_8.text()
            CoQuanXuLy = self.nILMViCLineEdit_7.text()
            NgayLuu = self.dateEdit_20.date()
            NgayLuu = str(NgayLuu.toPyDate())
            GhiChu = self.ghiChLineEdit_3.text()

            data_tienantiensu = ("", mank, Ngay, TienAnTienSu, HinhThuc, MucDo, ThoiGianXuLy, CoQuanXuLy, NgayLuu, GhiChu)
            self.db.insertSqliteTable_TienAnTienSu(data_tienantiensu)

        self.pushButton_55.clicked.connect(khaibao)
        self.pushButton_55.clicked.connect(tienantiensu)

    
    # xử lý tab đăng ký hộ khẩu===============================================================================================
    def KhaiMoiHoKhau(self):
        if self.chucvu_user == "Tổ Trưởng":
            i= self.tabWidget_2.addTab(self.tab_10, "Đăng Ký Hộ Khẩu")
            # self.dict.update(i: "Khai Báo Hộ Khẩu")
            self.tabWidget_2.setCurrentIndex(i)
            
            def KiemTraHoKhau():
                MaHK = self.sHKhULineEdit_2.text()
                result_select_hokhau_MaHK = self.GetData("HoKhau",MaHK, None, None, None, None, None)
                if result_select_hokhau_MaHK.fetchall() == []:
                    print("tiến hành thêm mới hộ khẩu")
                    
                    self.frame_8.setEnabled(True)
                    self.frame_25.setEnabled(True)
                    self.sHKhULineEdit_2.setEnabled(False)
                    self.label_31.setText(self.sHKhULineEdit_2.text())

                else:
                    self.frame_8.setEnabled(False)
                    self.frame_25.setEnabled(False)
                    print("mã hộ khẩu đã tồn tại")
            
            def KiemTraNhanKhau():
                MaNK = self.hTNKhaiSinhLineEdit_15.text()
                result_select_nhankhau_MaNK = self.GetData("NhanKhau",None, MaNK, None, None, None, None)
                MaHK = self.sHKhULineEdit_2.text()
                result_select_HoKhau__MaHK = self.GetData("HoKhau",MaHK, None, None, None, None, None)
                # print(result_select_nhankhau_MaNK.fetchall())
                if result_select_nhankhau_MaNK.fetchall() == []:
                    print("mã nhân khẩu hợp lệ")
                    self.pushButton_53.clicked.connect(KiemTraKhaiSinh)
                else:
                    MaHK = self.sHKhULineEdit_2.text()
                    MaNK = self.hTNKhaiSinhLineEdit_15.text()
                    result_select_nhankhau_MaNK_MaHK = self.GetData("NhanKhau",MaHK, MaNK, None, None, None, None)
                    result_select_nhankhau_MaNK = self.GetData("NhanKhau",None, MaNK, None, None, None, None)
                    if result_select_nhankhau_MaNK_MaHK.fetchall() == []:
                        MaNK = self.hTNKhaiSinhLineEdit_15.text()
                        result_select_nhankhau_MaNK = self.GetData("NhanKhau",None, MaNK, None, None, None, None)
                        for row_num, row_data in enumerate(result_select_nhankhau_MaNK):
                            for col_num, col_data in enumerate(row_data):
                                if col_num == 1:
                                    self.hTNKhaiSinhLineEdit_12.setText(col_data)
                                elif col_num == 3:
                                    self.hTNKhaiSinhLineEdit_13.setText(col_data) 
                                elif col_num == 4:
                                    self.tNGIKhCLineEdit_5.setText(col_data)
                                elif col_num == 5:
                                    if col_data == self.radioButton_3.text():
                                        self.radioButton_19.nextCheckState()
                                    elif col_data == self.radioButton_4.text():
                                        self.radioButton_20.nextCheckState()
                                elif col_num == 6:
                                    date = col_data.split("-")
                                    print(date)
                                    d = QDate(int(date[0]), int(date[1]), int(date[2]))
                                    self.dateEdit_5.setDate(d)
                                elif col_num == 7:
                                    self.nISinhLineEdit_5.setText(col_data)
                                elif col_num == 8:
                                    self.quQuNLineEdit_5.setText(col_data)
                                elif col_num == 9:
                                    self.chHiNNayLineEdit_6.setText(col_data)
                                elif col_num == 10:
                                    self.comboBox_15.addItem(col_data)
                                elif col_num == 11:
                                    self.comboBox_18.addItem(col_data)
                                elif col_num == 12:
                                    self.quCTChLineEdit_3.setText(col_data)
                                elif col_num == 13:
                                    self.sCCCDLineEdit_6.setText(col_data)
                                elif col_num == 14:
                                    self.nICPLineEdit_6.setText(col_data)
                                elif col_num == 15:
                                    self.nIKHKTTLineEdit_3.setText(col_data)
                                elif col_num == 16:
                                    self.trNhHCVNLineEdit_3.setText(col_data)
                                elif col_num == 17:
                                    self.nghNghiPLineEdit_5.setText(col_data)
                                elif col_num == 18:
                                    self.dUVTDHNhLineEdit_3.setText(col_data)
                                elif col_num == 24:
                                    self.ghiChLineEdit_4.setText(col_data)
                                elif col_num == 25:
                                    self.ngIKhaiLineEdit_3.setText(col_data)
                                elif col_num == 26:
                                    self.cNBHNgDNLineEdit_3.setText(col_data)
                                    
                                elif col_num == 27:
                                    date = col_data.split("-")
                                    print(date)
                                    d = QDate(int(date[0]), int(date[1]), int(date[2]))
                                    self.dateEdit_18.setDate(d)
                    else:
                        print("mã nhân khẩu đã tồn tại trong hộ khẩu:", result_select_nhankhau_MaNK.fetchall()[0][2])
                    

            def KiemTraKhaiSinh():
                MaKS = self.hTNKhaiSinhLineEdit_12.text()
                result_select_khaisinh_MaKS = self.GetData("KhaiSinh",None, None, MaKS, None, None, None)
                # print(result_select_nhankhau_MaNK.fetchall())
                if result_select_khaisinh_MaKS.fetchall() == []:
                    print("Không Có Mã Khai Sinh")
                else:
                    MaKS = self.hTNKhaiSinhLineEdit_12.text()
                    result_select_nhankhau_MaKS = self.GetData("NhanKhau",None, None, MaKS, None, None, None).fetchall()
                    # print(result_select_nhankhau_MaKS)
                    if result_select_nhankhau_MaKS == []:
                        MaKS = self.hTNKhaiSinhLineEdit_12.text()
                        result_select_khaisinh_MaKS = self.GetData("KhaiSinh",None, None, MaKS, None, None, None)
                        for row_num, row_data in enumerate(result_select_khaisinh_MaKS):
                            for col_num, col_data in enumerate(row_data):
                                if col_num == 1:
                                    self.hTNKhaiSinhLineEdit_13.setText(col_data) 
                                elif col_num == 2:
                                    self.tNGIKhCLineEdit_5.setText(col_data)
                                elif col_num == 3:
                                    if col_data == self.radioButton_19.text():
                                        self.radioButton_19.nextCheckState()
                                    elif col_data == self.radioButton_20.text():
                                        self.radioButton_20.nextCheckState()
                                elif col_num == 4:
                                    date = col_data.split("-")
                                    print(date)
                                    d = QDate(int(date[0]), int(date[1]), int(date[2]))
                                    self.dateEdit_15.setDate(d)
                                elif col_num == 5:
                                    self.nISinhLineEdit_5.setText(col_data)
                                elif col_num == 6:
                                    self.quQuNLineEdit_5.setText(col_data)
                                elif col_num == 7:
                                    self.chHiNNayLineEdit_6.setText(col_data)
                                elif col_num == 8:
                                    self.comboBox_15.addItem(col_data)
                                elif col_num == 9:
                                    self.comboBox_18.addItem(col_data)
                                elif col_num == 10:
                                    self.quCTChLineEdit_3.setText(col_data)
                                elif col_num == 15:
                                    self.dUVTDHNhLineEdit_3.setText(col_data)
                                elif col_num == 16:
                                    self.ghiChLineEdit_4.setText(col_data)
                                elif col_num == 17:
                                    self.ngIKhaiLineEdit_3.setText(col_data)
                                elif col_num == 18:
                                    self.cNBHNgDNLineEdit_3.setText(col_data)
                            
                                elif col_num == 19:
                                    date = col_data.split("-")
                                    print(date)
                                    d = QDate(int(date[0]), int(date[1]), int(date[2]))
                                    self.dateEdit_18.setDate(d)
                                
                    else:
                        print("Mã khai sinh đã có trong hộ khẩu:", result_select_nhankhau_MaKS[0][2])
                    
                
            
            def insert_chuho():
                self.db = MY_DB()
                mahk = self.sHKhULineEdit_2.text()
                machuho = self.hTNKhaiSinhLineEdit_15.text()
                maks = self.hTNKhaiSinhLineEdit_12.text()
                HoTenKhaiSinh = self.hTNKhaiSinhLineEdit_13.text()
                TenGoiKhac = self.tNGIKhCLineEdit_5.text()
                sex = "Nữ"
                if self.radioButton_19.isChecked():
                    sex = "Nam"
                date = self.dateEdit_15.date()
                date = str(date.toPyDate())
                NoiSinh = self.nISinhLineEdit_5.text()
                QueQuan = self.quQuNLineEdit_5.text()
                ChoOHienNay = self.chHiNNayLineEdit_6.text()
                DanToc = self.comboBox_15.currentText()
                TonGiao = self.comboBox_16.currentText()
                QuocTich = self.quCTChLineEdit_3.text()
                SoCCCD = self.sCCCDLineEdit_6.text()
                NoiCap = self.nICPLineEdit_6.text()
                NoiDKHKTT = self.nIKHKTTLineEdit_3.text()
                TrinhDoHocVan = self.trNhHCVNLineEdit_3.text()
                NgheNghiep = self.nghNghiPLineEdit_5.text()
                DauVet = self.dUVTDHNhLineEdit_3.text()
                TienAnTienSu = self.tiNNTiNSLineEdit.text()
                GhiChu = self.ghiChLineEdit_4.text()
                NguoiKhai = self.ngIKhaiLineEdit_3.text()
                CanBoDH = self.cNBHNgDNLineEdit_3.text()
                date_khai = self.dateEdit_15.date()
                date_khai = str(date_khai.toPyDate())

                data_chuho = (mahk, machuho, HoTenKhaiSinh, ChoOHienNay, date_khai,None ,None ,CanBoDH)
                data_nhankhau = (machuho, maks, mahk, HoTenKhaiSinh, TenGoiKhac, sex, date, NoiSinh, QueQuan, ChoOHienNay, DanToc, TonGiao, QuocTich, 
                SoCCCD, NoiCap, NoiDKHKTT, TrinhDoHocVan, NgheNghiep, DauVet, "Chủ hộ", "", "", "", "", "", NguoiKhai, CanBoDH, date_khai)
                if self.db.insertSqliteTable_HoKhau(data_chuho) and self.db.insertSqliteTable_NhanKhau(data_nhankhau):
                    self.frame_10.setEnabled(True)
                    self.pushButton_27.setEnabled(False)
                    self.frame_8.setEnabled(False)
                    self.frame_25.setEnabled(False)
                else:
                    self.frame_10.setEnabled(False)
                    self.pushButton_27.setEnabled(True)
                    self.frame_8.setEnabled(True)
                    self.frame_25.setEnabled(True)  

            def update_chuho():
                self.db = MY_DB()
                mahk = self.sHKhULineEdit_2.text()
                machuho = self.hTNKhaiSinhLineEdit_15.text()
                maks = self.hTNKhaiSinhLineEdit_12.text()
                HoTenKhaiSinh = self.hTNKhaiSinhLineEdit_13.text()
                TenGoiKhac = self.tNGIKhCLineEdit_5.text()
                sex = "Nữ"
                if self.radioButton_19.isChecked():
                    sex = "Nam"
                date = self.dateEdit_15.date()
                date = str(date.toPyDate())
                NoiSinh = self.nISinhLineEdit_5.text()
                QueQuan = self.quQuNLineEdit_5.text()
                ChoOHienNay = self.chHiNNayLineEdit_6.text()
                DanToc = self.comboBox_15.currentText()
                TonGiao = self.comboBox_16.currentText()
                QuocTich = self.quCTChLineEdit_3.text()
                SoCCCD = self.sCCCDLineEdit_6.text()
                NoiCap = self.nICPLineEdit_6.text()
                NoiDKHKTT = self.nIKHKTTLineEdit_3.text()
                TrinhDoHocVan = self.trNhHCVNLineEdit_3.text()
                NgheNghiep = self.nghNghiPLineEdit_5.text()
                DauVet = self.dUVTDHNhLineEdit_3.text()
                TienAnTienSu = self.tiNNTiNSLineEdit.text()
                GhiChu = self.ghiChLineEdit_4.text()
                NguoiKhai = self.ngIKhaiLineEdit_3.text()
                CanBoDH = self.cNBHNgDNLineEdit_3.text()
                date_khai = self.dateEdit_15.date()
                date_khai = str(date_khai.toPyDate())

                data_chuho = (mahk, machuho, HoTenKhaiSinh, ChoOHienNay, date_khai,None ,None ,CanBoDH)
                data_nhankhau = (machuho, maks, mahk, HoTenKhaiSinh, TenGoiKhac, sex, date, NoiSinh, QueQuan, ChoOHienNay, DanToc, TonGiao, QuocTich, 
                SoCCCD, NoiCap, NoiDKHKTT, TrinhDoHocVan, NgheNghiep, DauVet, "Chủ hộ", "", "", "", "", "", NguoiKhai, CanBoDH, date_khai)
                if self.db.updateSqliteTable_NhanKhau(mahk, machuho) and self.db.updateSqliteTable_HoKhau(mahk, machuho):
                    self.frame_10.setEnabled(True)
                    self.pushButton_27.setEnabled(False)
                    self.frame_8.setEnabled(False)
                    self.frame_25.setEnabled(False)
                else:
                    self.frame_10.setEnabled(False)
                    self.pushButton_27.setEnabled(True)
                    self.frame_8.setEnabled(True)
                    self.frame_25.setEnabled(True)               

            self.pushButton_24.clicked.connect(KiemTraHoKhau)
            self.pushButton_59.clicked.connect(KiemTraNhanKhau)
            
            MaNK = self.hTNKhaiSinhLineEdit_15.text()
            result_select_nhankhau_MaNK = self.GetData("NhanKhau",None, MaNK, None, None, None, None)
            if result_select_nhankhau_MaNK.fetchall() == []:
                self.pushButton_27.clicked.connect(insert_chuho)
                print("insert_chuho")
            else: 
                self.pushButton_27.clicked.connect(update_chuho)
                print("update_chuho")
            self.frame_10.setEnabled(True)
            self.pushButton_26.clicked.connect(lambda: self.KhaiBaoHandle(self.hTNKhaiSinhLineEdit_15.text()))

        else:
            QMessageBox.information(self.tab_7, "Thông Báo", "Không có quyền hạn truy cập chức năng")

    # thao tác nhập khẩu ========================================================================================
    def NhapKhau_Handle(self):
        if self.chucvu_user == "Tổ Trưởng":
            i = self.tabWidget_2.addTab(self.tab_11, "Nhập Khẩu")    
            self.tabWidget_2.setCurrentIndex(i)

            def KiemTraNhanKhau():
                MaNK = self.comboBox_8.currentText()
                result_select_nhankhau_MaNK = self.GetData("NhanKhau",None, MaNK, None, None, None, None)
                # print(result_select_nhankhau_MaNK.fetchall())
                # self.tableWidget_5.setEnabled(True)
                if result_select_nhankhau_MaNK.fetchall() == []:
                    print("mã nhân khẩu không có trong hệ thống")
                else:
                    MaNK = self.comboBox_8.currentText()
                    result_select_nhankhau_MaNK = self.GetData("NhanKhau",None, MaNK, None, None, None, None)
                    for row_num, row_data in enumerate(result_select_nhankhau_MaNK):
                        for col_num, col_data in enumerate(row_data):
                            if col_num == 2:
                                self.tableWidget_5.setItem(row_num, 0, QtWidgets.QTableWidgetItem(str(col_data)))
                            elif col_num == 3:
                                self.tableWidget_5.setItem(row_num, 1, QtWidgets.QTableWidgetItem(str(col_data)))
                        
                            elif col_num == 6:
                                self.tableWidget_5.setItem(row_num, 2, QtWidgets.QTableWidgetItem(str(col_data)))
                            elif col_num == 7:
                                self.tableWidget_5.setItem(row_num, 3, QtWidgets.QTableWidgetItem(str(col_data)))
                            elif col_num == 13:
                                self.tableWidget_5.setItem(row_num, 5, QtWidgets.QTableWidgetItem(str(col_data)))
                            elif col_num == 15:
                                self.tableWidget_5.setItem(row_num, 4, QtWidgets.QTableWidgetItem(str(col_data)))
                            elif col_num == 19:
                                self.tableWidget_5.setItem(row_num, 6, QtWidgets.QTableWidgetItem(str(col_data)))

            def nhapkhau():
                self.db = MY_DB()
                hokhau = self.comboBox_11.currentText()
                nhankhau = self.comboBox_8.currentText()
                self.db.updateSqliteTable_NhanKhau(hokhau, nhankhau)
                self.db.updateSqliteTable_HoKhau(hokhau, nhankhau)

            self.pushButton_34.clicked.connect(KiemTraNhanKhau)
            
            self.pushButton_54.clicked.connect(nhapkhau)
            self.pushButton_35.clicked.connect(self.KhaiMoiHoKhau)
        else:
            QMessageBox.information(self.tab_7, "Thông Báo", "Không có quyền hạn truy cập chức năng")

    # thao tác tách khẩu ===========================================================================================================
    
    def TachKhau_Handle(self):
        if self.chucvu_user == "Tổ Trưởng":
            i = self.tabWidget_2.addTab(self.tab_23, "Tách Khẩu")
            self.tabWidget_2.setCurrentIndex(i)

            def KiemTraNhanKhau():
                MaNK = self.comboBox_8.currentText()
                result_select_nhankhau_MaNK = self.GetData("NhanKhau",None, MaNK, None, None, None, None)
                self.hTNKhaiSinhLineEdit_15.setText(MaNK)
                self.hTNKhaiSinhLineEdit_15.setEnabled(False)
                if result_select_nhankhau_MaNK.fetchall() == []:
                    print("mã nhân khẩu không có trong hệ thống")
                else:
                    MaNK = self.comboBox_8.currentText()
                    result_select_nhankhau_MaNK = self.GetData("NhanKhau",None, MaNK, None, None, None, None)
                    for row_num, row_data in enumerate(result_select_nhankhau_MaNK):
                        for col_num, col_data in enumerate(row_data):
                            if col_num == 2:
                                self.tableWidget_21.setItem(row_num, 0, QtWidgets.QTableWidgetItem(str(col_data)))
                            elif col_num == 3:
                                self.tableWidget_21.setItem(row_num, 1, QtWidgets.QTableWidgetItem(str(col_data)))
                            elif col_num == 6:
                                self.tableWidget_21.setItem(row_num, 2, QtWidgets.QTableWidgetItem(str(col_data)))
                            elif col_num == 7:
                                self.tableWidget_21.setItem(row_num, 3, QtWidgets.QTableWidgetItem(str(col_data)))
                            elif col_num == 13:
                                self.tableWidget_21.setItem(row_num, 5, QtWidgets.QTableWidgetItem(str(col_data)))
                            elif col_num == 15:
                                self.tableWidget_21.setItem(row_num, 4, QtWidgets.QTableWidgetItem(str(col_data)))
                            elif col_num == 19:
                                self.tableWidget_21.setItem(row_num, 6, QtWidgets.QTableWidgetItem(str(col_data)))

            self.pushButton_67.clicked.connect(KiemTraNhanKhau)
            self.pushButton_68.clicked.connect(self.KhaiMoiHoKhau)
        else:
            QMessageBox.information(self.tab_7, "Thông Báo", "Không có quyền hạn truy cập chức năng")
        
    # chuyển đi ===========================================================================================
    def ChuyenDi_Handler(self):
        if self.chucvu_user == "Tổ Trưởng":
            self.db = MY_DB()
            i = self.tabWidget_2.addTab(self.tab_12, "Chuyển Đi")
            self.tabWidget_2.setCurrentIndex(i)
            def KiemTraNhanKhau():
                MaNK = self.comboBox_12.currentText()
                result_select_nhankhau_MaNK = self.GetData("NhanKhau",None, MaNK, None, None, None, None)
                self.hTNKhaiSinhLineEdit_15.setText(MaNK)
                self.hTNKhaiSinhLineEdit_15.setEnabled(False)
                if result_select_nhankhau_MaNK.fetchall() == []:
                    print("mã nhân khẩu không có trong hệ thống")
                else:
                    MaNK = self.comboBox_12.currentText()
                    result_select_nhankhau_MaNK = self.GetData("NhanKhau",None, MaNK, None, None, None, None)
                    for row_num, row_data in enumerate(result_select_nhankhau_MaNK):
                        for col_num, col_data in enumerate(row_data):
                            if col_num == 2:
                                self.tableWidget_6.setItem(row_num, 0, QtWidgets.QTableWidgetItem(str(col_data)))
                            elif col_num == 3:
                                self.tableWidget_6.setItem(row_num, 1, QtWidgets.QTableWidgetItem(str(col_data)))
                            elif col_num == 6:
                                self.tableWidget_6.setItem(row_num, 2, QtWidgets.QTableWidgetItem(str(col_data)))
                            elif col_num == 7:
                                self.tableWidget_6.setItem(row_num, 3, QtWidgets.QTableWidgetItem(str(col_data)))
                            elif col_num == 13:
                                self.tableWidget_6.setItem(row_num, 5, QtWidgets.QTableWidgetItem(str(col_data)))
                            elif col_num == 15:
                                self.tableWidget_6.setItem(row_num, 4, QtWidgets.QTableWidgetItem(str(col_data)))
                            elif col_num == 19:
                                self.tableWidget_6.setItem(row_num, 6, QtWidgets.QTableWidgetItem(str(col_data)))

            def insert_chuyendi():
                MaNK = self.comboBox_12.currentText()
                result_select_nhankhau_MaNK = self.GetData("NhanKhau",None, MaNK, None, None, None, None)
                NoiDi = result_select_nhankhau_MaNK.fetchall()[0][15]
                print(NoiDi)
                NoiDen = self.nIILineEdit.text()
                NgayDi = self.dateEdit_10.date()
                NgayDi = str(NgayDi.toPyDate()) 
                GhiChu = self.lDoLineEdit.text()
                NgayDen = self.dateEdit_11.date()
                NgayDen = str(NgayDen.toPyDate()) 
                
                self.db.updateSqliteTable_NhanKhau_ChuyenDi(NgayDi, NoiDi, NgayDen, GhiChu, NoiDen, MaNK)
            
            self.pushButton_36.clicked.connect(KiemTraNhanKhau)
            self.pushButton_37.clicked.connect(insert_chuyendi)
        
        else:
            QMessageBox.information(self.tab_7, "Thông Báo", "Không có quyền hạn truy cập chức năng")

    # tạm trú ==================================================================================================
    def TamTru_Handler(self):
        if self.chucvu_user == "Tổ Trưởng":
            i = self.tabWidget_2.addTab(self.tab_13, "Tạm Trú")
            # self.dict.update(i: "Tạm Trú / Tạm Vắng")
            self.tabWidget_2.setCurrentIndex(i)
            def KiemTraNhanKhau():
                MaNK = self.comboBox_13.currentText()
                result_select_nhankhau_MaNK = self.GetData("NhanKhau",None, MaNK, None, None, None, None)
                self.hTNKhaiSinhLineEdit_15.setText(MaNK)
                self.hTNKhaiSinhLineEdit_15.setEnabled(False)
                # print(result_select_nhankhau_MaNK.fetchall())
                # self.tableWidget_5.setEnabled(True)
                if result_select_nhankhau_MaNK.fetchall() == []:
                    print("mã nhân khẩu không có trong hệ thống")
                else:
                    MaNK = self.comboBox_13.currentText()
                    result_select_nhankhau_MaNK = self.GetData("NhanKhau",None, MaNK, None, None, None, None)
                    for row_num, row_data in enumerate(result_select_nhankhau_MaNK):
                        for col_num, col_data in enumerate(row_data):
                            if col_num == 2:
                                self.tableWidget_7.setItem(row_num, 0, QtWidgets.QTableWidgetItem(str(col_data)))
                            elif col_num == 3:
                                self.tableWidget_7.setItem(row_num, 1, QtWidgets.QTableWidgetItem(str(col_data)))
                            elif col_num == 6:
                                self.tableWidget_7.setItem(row_num, 2, QtWidgets.QTableWidgetItem(str(col_data)))
                            elif col_num == 7:
                                self.tableWidget_7.setItem(row_num, 3, QtWidgets.QTableWidgetItem(str(col_data)))
                            elif col_num == 13:
                                self.tableWidget_7.setItem(row_num, 5, QtWidgets.QTableWidgetItem(str(col_data)))
                            elif col_num == 15:
                                self.tableWidget_7.setItem(row_num, 4, QtWidgets.QTableWidgetItem(str(col_data)))
                            elif col_num == 19:
                                self.tableWidget_7.setItem(row_num, 6, QtWidgets.QTableWidgetItem(str(col_data)))

            def insert_tamtru():
                MaNK = MaNK = self.comboBox_13.currentText()
                TuNgay = self.dateEdit_12.date()
                TuNgay = str(TuNgay.toPyDate())

                DenNgay = self.dateEdit_19.date()
                DenNgay = str(DenNgay.toPyDate())
                GhiChu = self.ghiChLineEdit_6.text()

                NgayLap = self.dateEdit_12.date()
                NgayLap = str(NgayLap.toPyDate())

                self.db.insertSqliteTable_TamTru(MaNK, TuNgay, DenNgay, GhiChu, NgayLap)
            self.pushButton_38.clicked.connect(KiemTraNhanKhau)
            self.pushButton_39.clicked.connect(insert_tamtru)
        else:
            QMessageBox.information(self.tab_7, "Thông Báo", "Không có quyền hạn truy cập chức năng")

    # tạm vắng ===============================================================================================
    def TamVang_Handler(self):
        if self.chucvu_user == "Tổ Trưởng":
            i = self.tabWidget_2.addTab(self.tab_20, "Tạm Vắng")
            self.tabWidget_2.setCurrentIndex(i)
            def KiemTraNhanKhau():
                MaNK = self.comboBox_19.currentText()
                result_select_nhankhau_MaNK = self.GetData("NhanKhau",None, MaNK, None, None, None, None)
                self.hTNKhaiSinhLineEdit_15.setText(MaNK)
                self.hTNKhaiSinhLineEdit_15.setEnabled(False)
                if result_select_nhankhau_MaNK.fetchall() == []:
                    print("mã nhân khẩu không có trong hệ thống")
                else:
                    MaNK = self.comboBox_19.currentText()
                    result_select_nhankhau_MaNK = self.GetData("NhanKhau",None, MaNK, None, None, None, None)
                    for row_num, row_data in enumerate(result_select_nhankhau_MaNK):
                        for col_num, col_data in enumerate(row_data):
                            if col_num == 2:
                                self.tableWidget_14.setItem(row_num, 0, QtWidgets.QTableWidgetItem(str(col_data)))
                            elif col_num == 3:
                                self.tableWidget_14.setItem(row_num, 1, QtWidgets.QTableWidgetItem(str(col_data)))
                            elif col_num == 6:
                                self.tableWidget_14.setItem(row_num, 2, QtWidgets.QTableWidgetItem(str(col_data)))
                            elif col_num == 7:
                                self.tableWidget_14.setItem(row_num, 3, QtWidgets.QTableWidgetItem(str(col_data)))
                            elif col_num == 13:
                                self.tableWidget_14.setItem(row_num, 5, QtWidgets.QTableWidgetItem(str(col_data)))
                            elif col_num == 15:
                                self.tableWidget_14.setItem(row_num, 4, QtWidgets.QTableWidgetItem(str(col_data)))
                            elif col_num == 19:
                                self.tableWidget_14.setItem(row_num, 6, QtWidgets.QTableWidgetItem(str(col_data)))

            def insert_tamvang():
                MaNK = self.comboBox_19.currentText()
                TuNgay = self.dateEdit_19.date()
                TuNgay = str(TuNgay.toPyDate())

                DenNgay = self.dateEdit_8.date()
                DenNgay = str(DenNgay.toPyDate())
                NoiTamTru = self.nITMTrLineEdit.text()
                GhiChu = self.ghiChLineEdit_9.text()
                NgayLap = self.dateEdit_23.date()
                NgayLap = str(NgayLap.toPyDate())

                self.db.insertSqliteTable_TamVang(MaNK, TuNgay, DenNgay, NoiTamTru, GhiChu, NgayLap)

            self.pushButton_60.clicked.connect(KiemTraNhanKhau)
            self.pushButton_61.clicked.connect(insert_tamvang)
        else:
            QMessageBox.information(self.tab_7, "Thông Báo", "Không có quyền hạn truy cập chức năng")
            
    # tab_thông tin nhân khẩu =================================================================================
    def ThongTinNhanKhau_Handler(self):
        if self.chucvu_user == "Tổ Trưởng":
            i = self.tabWidget_2.addTab(self.tab_14, "Thông Tin Nhân Khẩu")
            self.tabWidget_2.setCurrentIndex(i)
            result_select_nhankhau = self.db.select_all_NhanKhau()
            for row_num, row_data in enumerate(result_select_nhankhau):
                for col_num, col_data in enumerate(row_data):
                    if col_num == 0:
                        self.tableWidget_8.setItem(row_num, 0, QtWidgets.QTableWidgetItem(str(col_data)))
                    elif col_num == 3:
                        self.tableWidget_8.setItem(row_num, 1, QtWidgets.QTableWidgetItem(str(col_data)))

            def hienthi():
                for i in range(self.tableWidget_9.rowCount()):
                    for j in range(self.tableWidget_9.columnCount()):
                        self.tableWidget_9.setItem(i, j, QtWidgets.QTableWidgetItem(""))
                self.frame_16.setEnabled(False)

                row = self.tableWidget_8.currentRow()
                MaNK = self.tableWidget_8.item(row, 0).text()
                result_select_nhankhau_MaNK = self.db.select_all_NhanKhau(None, MaNK, None, None, None, None)
                for row_num, row_data in enumerate(result_select_nhankhau_MaNK):
                    for col_num, col_data in enumerate(row_data):
                        if col_num == 2:
                            self.sHKLineEdit.setText(col_data)
                        if col_num == 3:
                            self.hTNKhaiSinhLineEdit_8.setText(col_data) 
                        elif col_num == 4:
                            self.tNGIKhCNUCLineEdit.setText(col_data)
                        elif col_num == 5:
                            if col_data == self.radioButton_11.text():
                                self.radioButton_11.nextCheckState()
                            elif col_data == self.radioButton_12.text():
                                self.radioButton_12.nextCheckState()
                        elif col_num == 6:
                            date = col_data.split("-")
                            print(date)
                            d = QDate(int(date[0]), int(date[1]), int(date[2]))
                            self.dateEdit_14.setDate(d)
                        elif col_num == 7:
                            self.nISinhLineEdit_4.setText(col_data)
                        elif col_num == 8:
                            self.quQuNLineEdit_4.setText(col_data)
                        elif col_num == 9:
                            self.chHiNNayLineEdit_4.setText(col_data)
                        elif col_num == 10:
                            self.comboBox_14.addItem(col_data)
                        elif col_num == 11:
                            self.tNGiOLineEdit.setText(col_data)
                        elif col_num == 12:
                            self.quCTChLineEdit_4.setText(col_data)
                        elif col_num == 13:
                            self.sCCCDLineEdit_4.setText(col_data)
                        elif col_num == 14:
                            self.nICPLineEdit_4.setText(col_data)
                        elif col_num == 15:
                            self.nINgKKhaiSinhLineEdit.setText(col_data)
                        elif col_num == 16:
                            self.trNhLineEdit.setText(col_data)
                        elif col_num == 17:
                            self.nghNghiPLineEdit_7.setText(col_data)
                        elif col_num == 18:
                            self.dUVTLineEdit.setText(col_data)
                        elif col_num == 24:
                            self.ghiChLineEdit_7.setText(col_data)
            
                result_khaobao_mank = self.db.select_all_KhaiBao(MaNK)
                for row_num, row_data in enumerate(result_khaobao_mank):
                    for col_num, col_data in enumerate(row_data):
                        if col_num != 0 and col_num != 1:
                            self.tableWidget_9.setItem(row_num, col_num-2, QtWidgets.QTableWidgetItem(str(col_data)))
                
                def chinhsuanhankhau():
                    self.frame_16.setEnabled(True)

                self.pushButton_40.clicked.connect(chinhsuanhankhau)
            self.tableWidget_8.currentItemChanged.connect(hienthi)  
            # self.pushButton_70.clicked.connect(hienthi) 
        else:
            QMessageBox.information(self.tab_7, "Thông Báo", "Không có quyền hạn truy cập chức năng")
        
    # tab_thông tin hộ khẩu ===============================================================================================
    def ThongTinHoKhau_Handler(self):
        if self.chucvu_user == "Tổ Trưởng":
            i = self.tabWidget_2.addTab(self.tab_17, "Thông Tin Hộ Khẩu")
            self.tabWidget_2.setCurrentIndex(i)
            result_select_hokhau = self.db.select_all_HoKhau()
            for row_num, row_data in enumerate(result_select_hokhau):
                for col_num, col_data in enumerate(row_data):
                    if col_num == 0:
                        self.tableWidget_12.setItem(row_num, 0, QtWidgets.QTableWidgetItem(str(col_data)))
                    elif col_num == 2:
                        self.tableWidget_12.setItem(row_num, 1, QtWidgets.QTableWidgetItem(str(col_data)))
            def hienthi():
                for i in range(self.tableWidget_13.rowCount()):
                    for j in range(self.tableWidget_13.columnCount()):
                        self.tableWidget_13.setItem(i, j, QtWidgets.QTableWidgetItem(""))
                self.frame_23.setEnabled(False)

                row = self.tableWidget_12.currentRow()
                MaHK = self.tableWidget_12.item(row, 0).text()
                result_select_hokhau_MaHK = self.db.select_all_HoKhau(MaHK, None, None)
                for row_num, row_data in enumerate(result_select_hokhau_MaHK):
                    for col_num, col_data in enumerate(row_data):
                        if col_num == 0:
                            self.sHKhULineEdit.setText(col_data)
                        elif col_num == 2:
                            self.hTNChHLineEdit.setText(col_data)
                        elif col_num == 3:
                            self.aChLineEdit_2.setText(col_data)
                        elif col_num == 4:
                            self.ngYNgKLineEdit.setText(col_data)
                        elif col_num == 6:
                            self.ghiChLineEdit_8.setText(col_data)

                result_select_nhankhau_MaHK = self.db.select_all_NhanKhau(MaHK, None, None, None, None, None)
                for row_num, row_data in enumerate(result_select_nhankhau_MaHK):
                    for col_num, col_data in enumerate(row_data):
                        if col_num == 0:
                            self.tableWidget_13.setItem(row_num, 0, QtWidgets.QTableWidgetItem(str(col_data)))
                        elif col_num == 3:
                            self.tableWidget_13.setItem(row_num, 1, QtWidgets.QTableWidgetItem(str(col_data)))
                        elif col_num == 6:
                            self.tableWidget_13.setItem(row_num, 2, QtWidgets.QTableWidgetItem(str(col_data)))
                        elif col_num == 7:
                            self.tableWidget_13.setItem(row_num, 3, QtWidgets.QTableWidgetItem(str(col_data)))
                        elif col_num == 13:
                            self.tableWidget_13.setItem(row_num, 5, QtWidgets.QTableWidgetItem(str(col_data)))
                        elif col_num == 15:
                            self.tableWidget_13.setItem(row_num, 4, QtWidgets.QTableWidgetItem(str(col_data)))
                        elif col_num == 19:
                            self.tableWidget_13.setItem(row_num, 6, QtWidgets.QTableWidgetItem(str(col_data)))
                
                def chinhsuahokhau():
                    self.frame_23.setEnabled(True)
                
                self.pushButton_47.clicked.connect(chinhsuahokhau)
            self.tableWidget_12.currentItemChanged.connect(hienthi)
        
        else:
            QMessageBox.information(self.tab_7, "Thông Báo", "Không có quyền hạn truy cập chức năng")
    # thao tác tìm kiếm nhân khẩu =====================================================================

    def TimKiemNhanKhau(self):
        i = self.tabWidget_2.addTab(self.tab_15, "Tìm Kiếm Nhân Khẩu")
        self.tabWidget_2.setCurrentIndex(i)

        def TimKiemNhanKhau_MaKS(MaKS):
            result_select_all_NhanKhau_MaKS = self.db.select_all_NhanKhau(None, None, MaKS)
            for row_num, row_data in enumerate(result_select_all_NhanKhau_MaKS):
                for col_num, col_data in enumerate(row_data):
                    if col_num == 0:
                        self.tableWidget_10.setItem(row_num, 0, QtWidgets.QTableWidgetItem(str(col_data)))
                    elif col_num == 3:
                        self.tableWidget_10.setItem(row_num, 1, QtWidgets.QTableWidgetItem(str(col_data)))
                    elif col_num == 6:
                        self.tableWidget_10.setItem(row_num, 2, QtWidgets.QTableWidgetItem(str(col_data)))
                    elif col_num == 7:
                        self.tableWidget_10.setItem(row_num, 3, QtWidgets.QTableWidgetItem(str(col_data)))
                    elif col_num == 13:
                        self.tableWidget_10.setItem(row_num, 5, QtWidgets.QTableWidgetItem(str(col_data)))
                    elif col_num == 15:
                        self.tableWidget_10.setItem(row_num, 4, QtWidgets.QTableWidgetItem(str(col_data)))
                    elif col_num == 19:
                        self.tableWidget_10.setItem(row_num, 6, QtWidgets.QTableWidgetItem(str(col_data)))
        def TimKiemNhanKhau_HoTen(HoTen):
            result_select_all_NhanKhau_HoTen = self.db.select_all_NhanKhau(None, None, None, HoTen)
            for row_num, row_data in enumerate(result_select_all_NhanKhau_HoTen):
                for col_num, col_data in enumerate(row_data):
                    if col_num == 0:
                        self.tableWidget_10.setItem(row_num, 0, QtWidgets.QTableWidgetItem(str(col_data)))
                    elif col_num == 3:
                        self.tableWidget_10.setItem(row_num, 1, QtWidgets.QTableWidgetItem(str(col_data)))
                    elif col_num == 6:
                        self.tableWidget_10.setItem(row_num, 2, QtWidgets.QTableWidgetItem(str(col_data)))
                    elif col_num == 7:
                        self.tableWidget_10.setItem(row_num, 3, QtWidgets.QTableWidgetItem(str(col_data)))
                    elif col_num == 13:
                        self.tableWidget_10.setItem(row_num, 5, QtWidgets.QTableWidgetItem(str(col_data)))
                    elif col_num == 15:
                        self.tableWidget_10.setItem(row_num, 4, QtWidgets.QTableWidgetItem(str(col_data)))
                    elif col_num == 19:
                        self.tableWidget_10.setItem(row_num, 6, QtWidgets.QTableWidgetItem(str(col_data)))

        def TimKiemNhanKhau_NoiSinh(NoiSinh):
            result_select_all_NhanKhau_NoiSinh = self.db.select_all_NhanKhau(None, None, None, None, NoiSinh)
            for row_num, row_data in enumerate(result_select_all_NhanKhau_NoiSinh):
                for col_num, col_data in enumerate(row_data):
                    if col_num == 0:
                        self.tableWidget_10.setItem(row_num, 0, QtWidgets.QTableWidgetItem(str(col_data)))
                    elif col_num == 3:
                        self.tableWidget_10.setItem(row_num, 1, QtWidgets.QTableWidgetItem(str(col_data)))
                    elif col_num == 6:
                        self.tableWidget_10.setItem(row_num, 2, QtWidgets.QTableWidgetItem(str(col_data)))
                    elif col_num == 7:
                        self.tableWidget_10.setItem(row_num, 3, QtWidgets.QTableWidgetItem(str(col_data)))
                    elif col_num == 13:
                        self.tableWidget_10.setItem(row_num, 5, QtWidgets.QTableWidgetItem(str(col_data)))
                    elif col_num == 15:
                        self.tableWidget_10.setItem(row_num, 4, QtWidgets.QTableWidgetItem(str(col_data)))
                    elif col_num == 19:
                        self.tableWidget_10.setItem(row_num, 6, QtWidgets.QTableWidgetItem(str(col_data)))

        def TimKiemNhanKhau():
            
            for i in range(self.tableWidget_10.rowCount()):
                for j in range(self.tableWidget_10.columnCount()):
                    self.tableWidget_10.setItem(i, j, QtWidgets.QTableWidgetItem(""))

            if self.radioButton_13.isChecked():
                TimKiemNhanKhau_MaKS(self.lineEdit.text())
            elif self.radioButton_14.isChecked():
                TimKiemNhanKhau_HoTen(self.lineEdit_2.text())
            elif self.radioButton_15.isChecked():
                TimKiemNhanKhau_NoiSinh(self.lineEdit_3.text())
            else:
                QMessageBox.information(self.tab_15, "", "Please select")
                
        self.pushButton_45.clicked.connect(TimKiemNhanKhau)

            
    # thao tác tìm kiếm hộ khẩu ==========================================================================================
    def TimKiemHoKhau_Handler(self):
        i = self.tabWidget_2.addTab(self.tab_16, "Tìm Kiếm Hộ Khẩu")
        self.tabWidget_2.setCurrentIndex(i)
        
        def TimKiemHoKhau_MaHK(SoHK):
            result_select_HoKhau__MaHK = self.db.select_all_HoKhau(SoHK)
            for row_num, row_data in enumerate(result_select_HoKhau__MaHK):
                for col_num, col_data in enumerate(row_data):
                    if col_num == 1:
                        self.tableWidget_11.setItem(row_num, 0, QtWidgets.QTableWidgetItem(str(col_data)))
                    elif col_num == 2:
                        self.tableWidget_11.setItem(row_num, 1, QtWidgets.QTableWidgetItem(str(col_data)))
                    elif col_num == 3:
                        self.tableWidget_11.setItem(row_num, 2, QtWidgets.QTableWidgetItem(str(col_data)))
                    elif col_num == 4:
                        self.tableWidget_11.setItem(row_num, 3, QtWidgets.QTableWidgetItem(str(col_data)))

        def TimKiemHoKhau_HoTenChuHo(HoTen):
            result_select_HoKhau__HoTen = self.db.select_all_HoKhau(None, HoTen)
            for row_num, row_data in enumerate(result_select_HoKhau__HoTen):
                for col_num, col_data in enumerate(row_data):
                    if col_num == 1:
                        self.tableWidget_11.setItem(row_num, 0, QtWidgets.QTableWidgetItem(str(col_data)))
                    elif col_num == 2:
                        self.tableWidget_11.setItem(row_num, 1, QtWidgets.QTableWidgetItem(str(col_data)))
                    elif col_num == 3:
                        self.tableWidget_11.setItem(row_num, 2, QtWidgets.QTableWidgetItem(str(col_data)))
                    elif col_num == 4:
                        self.tableWidget_11.setItem(row_num, 3, QtWidgets.QTableWidgetItem(str(col_data)))

        def TimKiemHoKhau_DiaChi(DiaChi):
            result_select_HoKhau__DiaChi = self.db.select_all_HoKhau(None, None, DiaChi)
            for row_num, row_data in enumerate(result_select_HoKhau__DiaChi):
                for col_num, col_data in enumerate(row_data):
                    if col_num == 1:
                        self.tableWidget_11.setItem(row_num, 0, QtWidgets.QTableWidgetItem(str(col_data)))
                    elif col_num == 2:
                        self.tableWidget_11.setItem(row_num, 1, QtWidgets.QTableWidgetItem(str(col_data)))
                    elif col_num == 3:
                        self.tableWidget_11.setItem(row_num, 2, QtWidgets.QTableWidgetItem(str(col_data)))
                    elif col_num == 4:
                        self.tableWidget_11.setItem(row_num, 3, QtWidgets.QTableWidgetItem(str(col_data)))


        def TimKiemHoKhau():
            for i in range(self.tableWidget_11.rowCount()):
                for j in range(self.tableWidget_11.columnCount()):
                    self.tableWidget_11.setItem(i, j, QtWidgets.QTableWidgetItem(""))

            if self.radioButton_16.isChecked():
                TimKiemHoKhau_MaHK(self.lineEdit_4.text())
            elif self.radioButton_17.isChecked():
                TimKiemHoKhau_HoTenChuHo(self.lineEdit_5.text())
            elif self.radioButton_18.isChecked():
                TimKiemHoKhau_DiaChi(self.lineEdit_6.text())
            else:
                print("Please select")

        self.pushButton_46.clicked.connect(TimKiemHoKhau)

    # thống kê ===================================================================================================
    def ThongKe_Handler(self):
        i = self.tabWidget_2.addTab(self.tab_21, "Thống kê")
        self.tabWidget_2.setCurrentIndex(i)
        self.comboBox_5.addItem("Giới Tính")
        self.comboBox_5.addItem("Địa Chỉ")

        def ThongKe_DiaChi(DiaChi):
            result_ThongKe_DiaChi = self.db.select_all_NhanKhau(None, None, None, None, DiaChi)
            for row_num, row_data in enumerate(result_ThongKe_DiaChi):
                for col_num, col_data in enumerate(row_data):
                    if col_num == 0:
                        self.tableWidget_15.setItem(row_num, 0, QtWidgets.QTableWidgetItem(str(col_data)))
                    elif col_num == 3:
                        self.tableWidget_15.setItem(row_num, 1, QtWidgets.QTableWidgetItem(str(col_data)))
                    elif col_num == 6:
                        self.tableWidget_15.setItem(row_num, 2, QtWidgets.QTableWidgetItem(str(col_data)))
                    elif col_num == 7:
                        self.tableWidget_15.setItem(row_num, 3, QtWidgets.QTableWidgetItem(str(col_data)))
                    elif col_num == 13:
                        self.tableWidget_15.setItem(row_num, 5, QtWidgets.QTableWidgetItem(str(col_data)))
                    elif col_num == 15:
                        self.tableWidget_15.setItem(row_num, 4, QtWidgets.QTableWidgetItem(str(col_data)))
                    elif col_num == 19:
                        self.tableWidget_15.setItem(row_num, 6, QtWidgets.QTableWidgetItem(str(col_data)))

        def ThongKe_GioiTinh(GioiTinh):
            result_ThongKe_GioiTinh = self.db.select_all_NhanKhau(None, None, None, None, None, GioiTinh)
            for row_num, row_data in enumerate(result_ThongKe_GioiTinh):
                for col_num, col_data in enumerate(row_data):
                    if col_num == 0:
                        self.tableWidget_15.setItem(row_num, 0, QtWidgets.QTableWidgetItem(str(col_data)))
                    elif col_num == 3:
                        self.tableWidget_15.setItem(row_num, 1, QtWidgets.QTableWidgetItem(str(col_data)))
                    elif col_num == 6:
                        self.tableWidget_15.setItem(row_num, 2, QtWidgets.QTableWidgetItem(str(col_data)))
                    elif col_num == 7:
                        self.tableWidget_15.setItem(row_num, 3, QtWidgets.QTableWidgetItem(str(col_data)))
                    elif col_num == 13:
                        self.tableWidget_15.setItem(row_num, 5, QtWidgets.QTableWidgetItem(str(col_data)))
                    elif col_num == 15:
                        self.tableWidget_15.setItem(row_num, 4, QtWidgets.QTableWidgetItem(str(col_data)))
                    elif col_num == 19:
                        self.tableWidget_15.setItem(row_num, 6, QtWidgets.QTableWidgetItem(str(col_data)))
        def ThongKe():
            if self.comboBox_5.currentText() == "Địa Chỉ":
                ThongKe_DiaChi(self.lineEdit_7.text())
            elif self.comboBox_5.currentText() == "Giới Tính":
                ThongKe_GioiTinh(self.lineEdit_7.text())
        
        self.pushButton_62.clicked.connect(ThongKe)

    # khai tử =====================================================================================================
    def KhaiTu_Handler(self):
        if self.chucvu_user == "Tổ Trưởng":
            i = self.tabWidget_2.addTab(self.tab_22, "Khai Tử")
            self.tabWidget_2.setCurrentIndex(i)
            
            def KiemTraNhanKhauNguoiKhai():
                MaNKNguoiKhai = self.lineEdit_8.text()
                result_select_all_NhanKhau_MaNK = self.db.select_all_NhanKhau(None, MaNKNguoiKhai)
                for row_num, row_data in enumerate(result_select_all_NhanKhau_MaNK):
                    for col_num, col_data in enumerate(row_data):
                        if col_num == 0:
                            self.tableWidget_2.setItem(row_num, 0, QtWidgets.QTableWidgetItem(str(col_data)))
                        elif col_num == 3:
                            self.tableWidget_2.setItem(row_num, 1, QtWidgets.QTableWidgetItem(str(col_data)))
                        elif col_num == 6:
                            self.tableWidget_2.setItem(row_num, 2, QtWidgets.QTableWidgetItem(str(col_data)))
                        elif col_num == 7:
                            self.tableWidget_2.setItem(row_num, 3, QtWidgets.QTableWidgetItem(str(col_data)))
                        elif col_num == 13:
                            self.tableWidget_2.setItem(row_num, 5, QtWidgets.QTableWidgetItem(str(col_data)))
                        elif col_num == 15:
                            self.tableWidget_2.setItem(row_num, 4, QtWidgets.QTableWidgetItem(str(col_data)))

            def KiemTraNhanKhauNguoiChet():
                MaNKNguoiChet = self.lineEdit_9.text()
                result_select_all_NhanKhau_MaNK = self.db.select_all_NhanKhau(None, MaNKNguoiChet)
                for row_num, row_data in enumerate(result_select_all_NhanKhau_MaNK):
                    for col_num, col_data in enumerate(row_data):
                        if col_num == 0:
                            self.tableWidget_16.setItem(row_num, 0, QtWidgets.QTableWidgetItem(str(col_data)))
                        elif col_num == 3:
                            self.tableWidget_16.setItem(row_num, 1, QtWidgets.QTableWidgetItem(str(col_data)))
                        elif col_num == 6:
                            self.tableWidget_16.setItem(row_num, 2, QtWidgets.QTableWidgetItem(str(col_data)))
                        elif col_num == 7:
                            self.tableWidget_16.setItem(row_num, 3, QtWidgets.QTableWidgetItem(str(col_data)))
                        elif col_num == 13:
                            self.tableWidget_16.setItem(row_num, 5, QtWidgets.QTableWidgetItem(str(col_data)))
                        elif col_num == 15:
                            self.tableWidget_16.setItem(row_num, 4, QtWidgets.QTableWidgetItem(str(col_data)))

            self.pushButton_28.clicked.connect(KiemTraNhanKhauNguoiKhai)
            self.pushButton_32.clicked.connect(KiemTraNhanKhauNguoiChet)

            def insert_KhaiTu():
                MaNKNguoiKhai = self.lineEdit_8.text()
                MaNKNguoiChet = self.lineEdit_9.text()
                ngaykhai = self.dateEdit.date()
                ngaykhai = str(ngaykhai.toPyDate())

                ngaychet = self.dateEdit.date()
                ngaychet = str(ngaychet.toPyDate())
                lydochet = self.lDoChTLineEdit.text()
                data = (MaNKNguoiChet, MaNKNguoiKhai, ngaykhai, ngaychet, lydochet)
                self.db.insert_KhaiTu(data)
            
            self.pushButton_52.clicked.connect(insert_KhaiTu)
        else:
            QMessageBox.information(self.tab_7, "Thông Báo", "Không có quyền hạn truy cập chức năng")

    # =========================================================================================================================
    # tab quản lý nhà văn hóa ================================================================================================= 
    def NhaVanHoaHandler(self):
        self.db = MY_DB()
        i = self.tabWidget_2.addTab(self.tab_24, "Quản Lý Nhà Văn Hóa")
        self.tabWidget_2.setCurrentIndex(i)
        self.tableWidget_22.setHorizontalHeaderLabels(["Người ĐK", "SĐT", "Mã SK", "Tên SK", "Ngày BĐ", "Ngày KT", "CSVC Đã Dùng", "Tổng Chi Phí"])
        self.tableWidget_23.setHorizontalHeaderLabels(["Mã CSVC", "Tên", "Giá Cho Thuê", "Số Lượng"])
        self.frame_31.setEnabled(False)

        result_select_all_CSVC = self.db.select_all_CSVC()
        for row_num, row_data in enumerate(result_select_all_CSVC):
            ten = ""
            sl = 0
            for col_num, col_data in enumerate(row_data):
                
                if col_num == 1:
                    ten = col_data
                elif col_num == 3:
                    sl = col_data
            self.comboBox_22.addItem(ten + "(" + str(sl) + " cái)")
        

        def select_all_CTCSVC(MASK):
            list_csvc = []
            
            result_select_all_CTCSVC = self.db.select_all_CTCSVC(MASK, None)
            for row_num, row_data in enumerate(result_select_all_CTCSVC):
                list_ctcsvc = ""
                for col_num, col_data in enumerate(row_data):
                    if col_num == 1:
                        list_ctcsvc = list_ctcsvc + col_data
                    elif col_num == 2:
                        list_ctcsvc = list_ctcsvc + "(" + str(col_data) + ")"
                list_csvc.append(list_ctcsvc)
            return list_csvc


        result_select_all_SUKIEN = self.db.select_all_SUKIEN(None)
        for row_num, row_data in enumerate(result_select_all_SUKIEN):
            str_ctcsvc = ""
            for col_num, col_data in enumerate(row_data):
                # print(col_data)
                if col_num == 1:
                    self.tableWidget_22.setItem(row_num, 0, QtWidgets.QTableWidgetItem(str(col_data)))
                elif col_num == 2:
                    self.tableWidget_22.setItem(row_num, 1, QtWidgets.QTableWidgetItem(str(col_data)))
                elif col_num == 3:
                    self.comboBox_20.addItem(col_data)
                    self.tableWidget_22.setItem(row_num, 2, QtWidgets.QTableWidgetItem(str(col_data)))
                    for datas in select_all_CTCSVC(col_data):
                        str_ctcsvc = str_ctcsvc + datas + ","
                    str_ctcsvc = str_ctcsvc.strip(",")
                    self.tableWidget_22.setItem(row_num, 6, QtWidgets.QTableWidgetItem(str_ctcsvc))
                    tongtien = self.db.TongTien(col_data).fetchall()[0]
                    self.tableWidget_22.setItem(row_num, 7, QtWidgets.QTableWidgetItem(str(tongtien[2]) + "VND"))
                elif col_num == 4:
                    self.tableWidget_22.setItem(row_num, 3, QtWidgets.QTableWidgetItem(str(col_data)))
                elif col_num == 5:
                    self.tableWidget_22.setItem(row_num, 4, QtWidgets.QTableWidgetItem(str(col_data)))
                elif col_num == 6:
                    self.tableWidget_22.setItem(row_num, 5, QtWidgets.QTableWidgetItem(str(col_data)))

        def insert_sukien():
            self.db = MY_DB()
            self.frame_31.setEnabled(True)
            self.frame_30.setEnabled(False)
            self.pushButton_85.clicked.connect(KiemTraNhanKhau)
            self.pushButton_73.clicked.connect(lambda:  add_csvc())
            self.pushButton_86.clicked.connect(KiemTraSuKien)
            
            def insert():
                MANGUOIDK = self.comboBox_6.currentText()
                TEN = self.hTNNgIKLineEdit.text()
                SDT = self.sTLineEdit.text()
                MASK = self.comboBox_20.currentText()
                TENSK = self.tNSKiNLineEdit.text()
                NGAYBD = self.dateTimeEdit_2.dateTime()
                NGAYBD = str(NGAYBD.toPyDateTime()) 
                NGAYKT = self.dateTimeEdit.dateTime()
                NGAYKT = str(NGAYKT.toPyDateTime())

                list_CSVC = []
                csvcs = self.lineEdit_10.text().split(", ")
                for csvc in csvcs:
                    csvc = csvc.split("(")
                    TenCSVC  = csvc[0].strip()
                    MACSVC = self.db.select_all_CSVC(None, TenCSVC).fetchall()[0][0]
                    soluong = csvc[1].strip(")")
                    list_CSVC.append((MACSVC, int(soluong)))
        
                list_sukien  = (MANGUOIDK, TEN, SDT, MASK, TENSK, NGAYBD, NGAYKT)
                if KiemTraNgay():
                    check_insert = True
                    for list_ctcsvc in list_CSVC:
                        lst_insert =  tuple([MASK] + list(list_ctcsvc))
                        if self.db.insert_ctcsvc(lst_insert) is not True:
                            check_insert = False
                    if self.db.insert_sukien(list_sukien) and check_insert:
                        QMessageBox.information(self.tab_24, "Thông Báo", "Lưu Thành Công")
                        self.NhaVanHoaHandler()
                    else:
                        QMessageBox.information(self.tab_24, "Thông Báo", "Lưu Không Thành Công")

                else:
                    QMessageBox.information(self.tab_24, "Thông Báo", "Ngày bị trùng")

            # list_sukien  = (MANGUOIDK, TEN, SDT, MASK, TENSK, NGAYBD, NGAYKT)
            self.pushButton_74.clicked.connect(lambda: insert())
        
        def add_csvc():
            lst_csvc = self.lineEdit_10.text()
            csvc = self.comboBox_22.currentText().split("(")[0]
            soluong = self.spinBox_3.text()
            if lst_csvc != "":
                lst_csvc = lst_csvc + ", " + csvc + "(" + soluong + ")"
            else:
                lst_csvc = lst_csvc + csvc + "(" + soluong + ")"
            self.lineEdit_10.setText(lst_csvc)
            return lst_csvc
    
        def KiemTraNhanKhau():
            MaNK = self.comboBox_6.currentText()
            result_select_nhankhau_MaNK = self.GetData("NhanKhau",None, MaNK, None, None, None, None)
            for row_num, row_data in enumerate(result_select_nhankhau_MaNK):
                for col_num, col_data in enumerate(row_data):
                    if col_num == 3:
                        self.hTNNgIKLineEdit.setText(col_data)
        def KiemTraSuKien():
            MASK = self.comboBox_20.currentText()
            result_select_all_SuKien = self.db.select_all_SUKIEN(MASK)
            if result_select_all_SuKien.fetchall() != []:
                QMessageBox.information(self.tab_24, "Thông Báo", "Mã Sự Kiện Đã Tồn Tại")
            else:
                self.frame_30.setEnabled(True)

        self.pushButton_75.clicked.connect(insert_sukien)

        def KiemTraNgay():
            NGAYBD = self.dateTimeEdit_2.dateTime()
            NGAYBD = str(NGAYBD.toPyDateTime()) 
            NGAYKT = self.dateTimeEdit.dateTime()
            NGAYKT = str(NGAYKT.toPyDateTime())
            date_BD_form = NGAYBD.split()[0]
            time_BD_form = NGAYBD.split()[1]

            date_KT_form = NGAYKT.split()[0]
            time_KT_form = NGAYKT.split()[1]

            NGAYBD_SQL = []
            NGAYKT_SQL = []

            result_select_all_SUKIEN = self.db.select_all_SUKIEN()
            for row_num, row_data in enumerate(result_select_all_SUKIEN):
                for col_num, col_data in enumerate(row_data):
                    if col_num == 5:
                        NGAYBD_SQL.append(col_data)
                    elif col_num == 6:
                        NGAYKT_SQL.append(col_data)
            for i in range(int(len(NGAYBD_SQL))):
                date_BD = NGAYBD_SQL[i].split()[0]
                time_BD = NGAYBD_SQL[i].split()[1]

                date_KT = NGAYKT_SQL[i].split()[0]
                time_KT = NGAYKT_SQL[i].split()[1]

                ischeck = datetime.datetime(year=int(date_BD.split("-")[0]),month=int(date_BD.split("-")[1]),day=int(date_BD.split("-")[2]),hour=int(time_BD.split(":")[0]), minute = int(time_BD.split(":")[1]), second = int(time_BD.split(":")[2])) <= datetime.datetime(year=int(date_BD_form.split("-")[0]),month=int(date_BD_form.split("-")[1]),day=int(date_BD_form.split("-")[2]),hour=int(time_BD_form.split(":")[0]), minute = int(time_BD_form.split(":")[1]), second = int(time_BD_form.split(":")[2])) <= datetime.datetime(year=int(date_KT.split("-")[0]),month=int(date_KT.split("-")[1]),day=int(date_KT.split("-")[2]),hour=int(time_KT.split(":")[0]), minute = int(time_KT.split(":")[1]), second = int(time_KT.split(":")[2])) or datetime.datetime(year=int(date_BD.split("-")[0]),month=int(date_BD.split("-")[1]),day=int(date_BD.split("-")[2]),hour=int(time_BD.split(":")[0]), minute = int(time_BD.split(":")[1]), second = int(time_BD.split(":")[2])) <= datetime.datetime(year=int(date_KT_form.split("-")[0]),month=int(date_KT_form.split("-")[1]),day=int(date_KT_form.split("-")[2]),hour=int(time_KT_form.split(":")[0]), minute = int(time_KT_form.split(":")[1]), second = int(time_KT_form.split(":")[2])) <= datetime.datetime(year=int(date_KT.split("-")[0]),month=int(date_KT.split("-")[1]),day=int(date_KT.split("-")[2]),hour=int(time_KT.split(":")[0]), minute = int(time_KT.split(":")[1]), second = int(time_KT.split(":")[2]))
                if ischeck:
                    return False
            return True

        def sua_sk():
            self.frame_31.setEnabled(True)
            self.pushButton_73.clicked.connect(lambda:  add_csvc())
            def hienthi():
                row = self.tableWidget_22.currentRow()
                MASK = self.tableWidget_22.item(row, 2).text()
                # csvc_dadung = self.tableWidget_22.item(row, 6).text()
                # self.lineEdit_10.setText(csvc_dadung)

                csvcs = self.tableWidget_22.item(row, 6).text().split(",")
                print(csvcs)
                string_ctcsvc = ""
                for csvc in csvcs:
                    csvc = csvc.split("(")
                    MACSVC  = csvc[0].strip()
                    TenCSVC = self.db.select_all_CSVC(MACSVC, None).fetchall()[0][1]
                    soluong = csvc[1].strip(")")
                    if string_ctcsvc != "":
                        string_ctcsvc = string_ctcsvc + ", " + TenCSVC + "(" + soluong + ")"
                    else:
                        string_ctcsvc = string_ctcsvc + TenCSVC + "(" + soluong + ")"
                string_ctcsvc.strip(",")
                self.lineEdit_10.setText(string_ctcsvc)
                    
                result_select_all_SUKIEN = self.db.select_all_SUKIEN(MASK)
                for row_num, row_data in enumerate(result_select_all_SUKIEN):
                    for col_num, col_data in enumerate(row_data):
                        if col_num == 0:
                            self.comboBox_6.setCurrentText(col_data)
                        elif col_num == 1:
                            self.hTNNgIKLineEdit.setText(col_data)
                        elif col_num == 2:
                            self.sTLineEdit.setText(col_data)
                        elif col_num == 3:
                            self.comboBox_20.setCurrentText(col_data)
                        elif col_num == 4:
                            self.tNSKiNLineEdit.setText(col_data)
                        elif col_num == 5:
                            datetime = col_data.split()
                            date = datetime[0].split("-")
                            time = datetime[1].split(":")
                            d = QDateTime(int(date[0]), int(date[1]), int(date[2]), int(time[0]), int(time[1]), int(time[2]))
                            self.dateTimeEdit_2.setDateTime(d)
                        elif col_data == 6:
                            datetime = col_data.split()
                            date = datetime[0].split("-")
                            time = datetime[1].split(":")
                            d = QDateTime(int(date[0]), int(date[1]), int(date[2]), int(time[0]), int(time[1]), int(time[2]))
                            self.dateTimeEdit.setDateTime(d)
                            
            self.tableWidget_22.currentItemChanged.connect(hienthi)

            def update_sukien():
                MANGUOIDK = self.comboBox_6.currentText()
                TEN = self.hTNNgIKLineEdit.text()
                SDT = self.sTLineEdit.text()
                MASK = self.comboBox_20.currentText()
                TENSK = self.tNSKiNLineEdit.text()
                NGAYBD = self.dateTimeEdit_2.dateTime()
                NGAYBD = str(NGAYBD.toPyDateTime()) 
                NGAYKT = self.dateTimeEdit.dateTime()
                NGAYKT = str(NGAYKT.toPyDateTime())

                if KiemTraNgay():
                    list_CSVC = []
                    csvcs = self.lineEdit_10.text().split(", ")
                    for csvc in csvcs:
                        csvc = csvc.split("(")
                        TenCSVC  = csvc[0].strip()
                        MACSVC = self.db.select_all_CSVC(None, TenCSVC).fetchall()[0][0]
                        soluong = csvc[1].strip(")")
                        list_CSVC.append((MACSVC, int(soluong)))
                    check_update = True
                    for list_ctcsvc in list_CSVC:
                        if self.db.update_ctcsvc(list_ctcsvc[1], MASK, MACSVC) is not True:
                            check_update = False
                    
                    if self.db.update_sukien(MANGUOIDK, TEN ,SDT, TENSK, NGAYBD, NGAYKT, MASK) and check_update:
                        QMessageBox.information(self.tab_24, "Thông Báo", "Đã sửa")
                        self.NhaVanHoaHandler()
                    else:
                        QMessageBox.information(self.tab_24, "Thông Báo", "Lưu không thành công")
                else:
                    QMessageBox.information(self.tab_24, "Thông Báo", "Trùng ngày với sự kiện khác")
            self.pushButton_74.clicked.connect(update_sukien)

        self.pushButton_76.clicked.connect(sua_sk)

        def xoasukien():
            question = QMessageBox.question(self.tab_24, "Thông Báo", "Bạn chắc chắn muốn xóa lựa chọn ?  ")
            if question == QMessageBox.Yes:
                row = self.tableWidget_22.currentRow()
                MASK = self.tableWidget_22.item(row, 3).text()
                if self.db.xoasukien(MASK):
                    QMessageBox.information(self.tab_24, "Thông Báo", "Đã Xóa Lựa Chọn")
                    self.NhaVanHoaHandler()
                else:
                    QMessageBox.information(self.tab_24, "Thông Báo", "Xóa Thất Bại")
        self.pushButton_77.clicked.connect(xoasukien)

        # CƠ SỞ VẬT CHẤT
        self.comboBox_23.setEnabled(False)
        self.frame_32.setEnabled(False)
        result_select_all_CSVC = self.db.select_all_CSVC()
        for row_num, row_data in enumerate(result_select_all_CSVC):
            for col_num, col_data in enumerate(row_data):
                self.tableWidget_23.setItem(row_num, col_num, QtWidgets.QTableWidgetItem(str(col_data)))

        def themcosovatchat():
            self.comboBox_23.setEnabled(True)
            def KiemTraCSVC():
                MACSVC = self.comboBox_23.currentText()
                result_csvc = self.db.select_all_CSVC(MACSVC)
                if result_csvc.fetchall() == []:
                    self.frame_32.setEnabled(True)
                else:
                    QMessageBox.information(self.tab_26, "Thông Báo", "Mã Cơ Sở Vật Chất Đã Tồn Tại  ")  

            def Insert_CSVC():
                MACSVC = self.comboBox_23.currentText()
                TENCSVC = self.tNSKiNLineEdit_2.text()
                SOLUONG = self.spinBox.text()
                GIA = self.spinBox_2.text() 

                data_csvc = (MACSVC, TENCSVC, GIA, SOLUONG)
                if self.db.insert_csvc(data_csvc):
                    QMessageBox.information(self.tab_26, "Thông Báo", "Lưu Thành Công")
                else:
                    QMessageBox.information(self.tab_26, "Thông Báo", "Lưu Không Thành Công")
            
            self.pushButton_84.clicked.connect(KiemTraCSVC)
            self.pushButton_83.clicked.connect(Insert_CSVC)

        self.pushButton_72.clicked.connect(themcosovatchat)

        def suacosovatchat():
            self.frame_32.setEnabled(True)
            def hienthi():
                row = self.tableWidget_23.currentRow()
                MACSVC = self.tableWidget_23.item(row, 0).text()
                    
                result_select_all_CSVC = self.db.select_all_CSVC(MACSVC)
                for row_num, row_data in enumerate(result_select_all_CSVC):
                    for col_num, col_data in enumerate(row_data):
                        if col_num == 0:
                            self.comboBox_23.setCurrentText(col_data)
                        elif col_num == 1:
                            self.tNSKiNLineEdit_2.setText(col_data)
                        elif col_num == 2:
                            self.spinBox.setSpecialValueText(col_data)
                        elif col_num == 3:
                            self.spinBox_2.setSpecialValueText(col_data)


            def update_csvc():
                question = QMessageBox.question(self.tab_26, "Thông Báo", "Bạn chắc chắn muốn thay đổi ?  ")
                if question == QMessageBox.Yes:
                    MACSVC = self.comboBox_23.currentText()
                    TENCSVC = self.tNSKiNLineEdit_2.text()
                    SOLUONG = self.spinBox.text()
                    GIA = self.spinBox_2.text()  

                    if self.db.update_csvc(TENCSVC, GIA, SOLUONG, MACSVC):
                        QMessageBox.information(self.tab_26, "Thông Báo", "Lưu Thành Công")
                        self.NhaVanHoaHandler()
                    else:
                        QMessageBox.information(self.tab_26, "Thông Báo", "Lưu Không Thành Công")

            self.tableWidget_23.currentItemChanged.connect(hienthi)
            self.pushButton_83.clicked.connect(update_csvc)

        self.pushButton_80.clicked.connect(suacosovatchat)
        
        def xoacosovatchat():
            question = QMessageBox.question(self.tab_26, "Thông Báo", "Bạn chắc chắn muốn xóa lựa chọn ?  ")
            if question == QMessageBox.Yes:
                row = self.tableWidget_23.currentRow()
                MACSVC = self.tableWidget_23.item(row, 0).text()
                if self.db.xoacosovatchat(MACSVC):
                    QMessageBox.information(self.tab_26, "Thông Báo", "Đã Xóa Lựa Chọn")
                    self.NhaVanHoaHandler()
                else:
                    QMessageBox.information(self.tab_26, "Thông Báo", "Xóa Thất Bại")
        self.pushButton_81.clicked.connect(xoacosovatchat)

            
    def exit(self):
        exit(0)
    def addTab(self):
        self.tab_new = QtWidgets.QWidget()
        self.tab_new.setObjectName("tab_new")
        self.tabWidget_2.addTab(self.tab_new, "Tab New")

    def CloseTab(self):
        self.tabWidget_2.removeTab(self.tabWidget_2.currentIndex())

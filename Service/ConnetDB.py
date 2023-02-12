import sqlite3
import hashlib

class MY_DB():
    def __init__(self):
        self.conn = sqlite3.connect('../BTL-CNPM/Service/database.db')
        self.cur = self.conn.cursor()

    def select_all_user(self):
        self.sql_select = """ SELECT User.MS, User.'Họ Tên',DangNhap.UserName, User.'Giới Tính', User.Email, User.'Chức Vụ',
        User.'Quyền Hạn', User.'Ngày Sinh', User.'Địa Chỉ', User.'Điện Thoại' FROM User, DangNhap
        WHERE User.MS = DangNhap.MS
            """
        self.result = self.conn.execute(self .sql_select)
        return self.result

    def updateSqliteTable_User(self, MS, Name, UserName, Sex, Email, Chucvu, quyenhan, ngaysinh, diachi, dienthoai):
        try:
            sql_update_query = """Update User SET 'Họ Tên' = ?, 'Giới Tính' = ?, 'Email' = ?, 
            'Chức Vụ' = ?, 'Quyền Hạn' = ?, 'Ngày Sinh' = ?, 'Địa Chỉ' = ?, 'Điện Thoại' = ? WHERE MS = ?"""
            data = (Name, Sex, Email, Chucvu, quyenhan, ngaysinh, diachi, dienthoai, MS)
            self.cur.execute(sql_update_query, data)
            sql_update_dangnhap = """Update DangNhap Set UserName = ? WHERE MS = ?"""
            self.cur.execute(sql_update_dangnhap, (UserName, MS))
            self.conn.commit()
            print("Record Updated successfully")
            self.cur.close()

        except sqlite3.Error as error:
            print("Failed to update sqlite table", error)
        finally:
            if self.conn:
                self.conn.close()
                print("The sqlite connection is closed")

    def updateSqliteTable_NhanKhau(self, MaHK, MaNK):
        try:
            sql_update_query = """Update NhanKhau SET 'MaHK' = ?, QuanHeVoiChuHo = 'Chủ Hộ' WHERE MaNK = ?"""

            self.cur.execute(sql_update_query, (MaHK, MaNK))
            self.conn.commit()
            print("Record Updated successfully")
            # self.cur.close()
            return True

        except sqlite3.Error as error:
            print("Failed to update sqlite table", error)
            return False
        finally:
            if self.conn:
                
                print("The sqlite connection is closed")

    def updateSqliteTable_NhanKhau_ChuyenDi(self, NgayDi, NoiDi, NgayDen, LyDoChuyenDen, NoiDKHKTT, MaNK):
        try:
            sql_update_query = """Update NhanKhau SET 'NgayChuyenDen' = ?, LyDoChuyeDen = ?, 
            NgayChuyenDi = ?, NoiChuyenDi = ?, NoiDKHKTT = ? WHERE MaNK = ?"""
            self.cur.execute(sql_update_query, (NgayDen, LyDoChuyenDen, NgayDi, NoiDi, NoiDKHKTT, MaNK))
            self.conn.commit()
            print("Record Updated successfully")
            # self.cur.close()
            return True

        except sqlite3.Error as error:
            print("Failed to update sqlite table", error)
            return False
        finally:
            if self.conn:
                
                print("The sqlite connection is closed")

    def updateSqliteTable_HoKhau(self, MaHK, MaNK):
        try:
            sql_update_query = """Update HoKhau SET 'MaHK' = ? WHERE 'MaChuHo' = ?"""
            self.cur.execute(sql_update_query, (MaHK, MaNK))
            self.conn.commit()
            print("Record Updated successfully")
            # self.cur.close()
            return True

        except sqlite3.Error as error:
            print("Failed to update sqlite table", error)
            return False
        finally:
            if self.conn:
                
                print("The sqlite connection is closed")

    def update_matkhau(self, MatKhauMoi, NguoiDung):
        try:
            sql_update_query = """Update DangNhap SET PassWord = ? WHERE UserName = ?"""
            self.cur.execute(sql_update_query, (MatKhauMoi, NguoiDung))
            self.conn.commit()
            print("Record Updated successfully")
            # self.cur.close()
            return True

        except sqlite3.Error as error:
            print("Failed to update sqlite table", error)
            return False
        finally:
            if self.conn:
                
                print("The sqlite connection is closed")

    def update_sukien(self, MaNguoiDK, TenNguoiDK, SDT, TenSK, ThoiGianBatDau, ThoiGianKetThuc, MaSK):
        try:
            sql_update_query = """Update SUKIEN SET MaNguoiDK = ? , TenNguoiDK = ?, SDT = ?, TENSK = ?,ThoiGianBatDau = ?, ThoiGianKetThuc = ? WHERE MASK = ?"""
            self.cur.execute(sql_update_query, (MaNguoiDK, TenNguoiDK, SDT, TenSK, ThoiGianBatDau, ThoiGianKetThuc, MaSK))
            self.conn.commit()
            print("Record Updated successfully")
            # self.cur.close()
            return True

        except sqlite3.Error as error:
            print("Failed to update sqlite table", error)
            return False
        finally:
            if self.conn:
                print("The sqlite connection is closed")

    def update_csvc(self, TenCSVC, Gia, SoLuong, MACSVC):
        try:
            sql_update_query = """Update CSVC SET TENCSVC = ? , GIA = ?, SOLUONGHIENCO = ? WHERE MACSVC = ?"""
            self.cur.execute(sql_update_query, (TenCSVC, Gia, SoLuong, MACSVC))
            self.conn.commit()
            print("Record Updated successfully")
            # self.cur.close()
            return True
        except sqlite3.Error as error:
            print("Failed to update sqlite table", error)
            return False
        finally:
            if self.conn:
                print("The sqlite connection is closed")
    
    def update_ctcsvc(self, SoLuong, MASK, MACSVC):
        try:
            sql_update_query = """Update CTCSVC SET SOLUONGTHUE = ? WHERE MASK = ? AND MACSVC = ?"""
            self.cur.execute(sql_update_query, (SoLuong, MASK, MACSVC))
            self.conn.commit()
            print("Record Updated successfully")
            # self.cur.close()
            return True
        except sqlite3.Error as error:
            print("Failed to update sqlite table", error)
            return False
        finally:
            if self.conn:
                print("The sqlite connection is closed")


    def select_NguoiDung_MatKhau(self, Username, Password):
        sql_select_DangNhap = """ SELECT DangNhap.UserName, DangNhap.PassWord FROM DangNhap 
                            WHERE DangNhap.UserName = ? AND DangNhap.Password = ?"""
        self.result = self.conn.execute(sql_select_DangNhap, (Username, Password))
        return self.result


    def insertSqliteTable_User(self, MS, Name, UserName, Sex, Email, Chucvu, quyenhan, ngaysinh, diachi, dienthoai):
        try:
            sql_insert_query = """INSERT INTO User VALUES (?, ?, ?, ? ,? ,?, ?, ? ,?)"""
            data = (MS, Name, Sex, Email, Chucvu, quyenhan, ngaysinh, diachi, dienthoai)
            self.cur.execute(sql_insert_query, data)
            sql_insert_dangnhap = """INSERT INTO DangNhap VALUES(?, "1")"""
            self.cur.execute(sql_insert_dangnhap, (UserName,))
            self.conn.commit()
        except sqlite3.Error as error:
            print("Failed to update sqlite table", error)
        finally:
            if self.conn:
                self.conn.close()
                print("The sqlite connection is closed")


    def ThongTinNguoiDung(self, Username, Password):
        sql_select_TTNguoidung = """ SELECT User.MS, User.'Họ Tên',DangNhap.UserName, User.'Giới Tính', User.Email, User.'Chức Vụ',
        User.'Quyền Hạn', User.'Ngày Sinh', User.'Địa Chỉ', User.'Điện Thoại' FROM User, DangNhap
        WHERE User.MS = DangNhap.MS
            AND DangNhap.UserName = ?
            AND DangNhap.Password = ?
            """
        self.result = self.conn.execute(sql_select_TTNguoidung, (Username, Password))
        return self.result

    def select_all_HoKhau(self, MaHK = None, HoTenKhaiSinh = None, DiaChi = None):
        if MaHK is not None:
            sql_select_all_HoKhau_MaHK = """SELECT * FROM HoKhau WHERE MaHK = ?"""
            result = self.conn.execute(sql_select_all_HoKhau_MaHK, (MaHK,))
        elif HoTenKhaiSinh is not None:
            sql_select_all_HoKhau_HoTen = """SELECT * FROM HoKhau WHERE HoTenChuHo = ?"""
            result = self.conn.execute(sql_select_all_HoKhau_HoTen, (HoTenKhaiSinh,))
        elif DiaChi is not None:
            sql_select_all_HoKhau_DiaChi = """SELECT * FROM HoKhau WHERE DiaChi = ?"""
            result = self.conn.execute(sql_select_all_HoKhau_DiaChi, (DiaChi,))
        else:
            sql_select_all_HoKhau = """SELECT * FROM HoKhau"""
            result = self.conn.execute(sql_select_all_HoKhau)
        return result
        
        

    def select_all_NhanKhau(self, MaHK = None, MaNK = None, MaKS = None, HoTenKhaiSinh = None, DiaChi = None, GioiTinh = None):
        if MaHK is not None:
            sql_select_all_NhanKhau_MaHK = """SELECT * FROM NhanKhau WHERE MaHK = ?"""
            result = self.conn.execute(sql_select_all_NhanKhau_MaHK, (MaHK,))
        elif MaNK is not None:
            sql_select_all_NhanKhau_MaNK = """SELECT * FROM NhanKhau WHERE MaNK = ?"""
            result = self.conn.execute(sql_select_all_NhanKhau_MaNK, (MaNK,))
        elif MaKS is not None:
            sql_select_all_NhanKhau_MaKS = """SELECT * FROM NhanKhau WHERE MaKS = ?"""
            result = self.conn.execute(sql_select_all_NhanKhau_MaKS, (MaKS,))
        elif HoTenKhaiSinh is not None:
            sql_select_all_NhanKhau_HoTenKhaiSinh = """SELECT * FROM NhanKhau WHERE HoTen = ?"""
            result = self.conn.execute(sql_select_all_NhanKhau_HoTenKhaiSinh, (HoTenKhaiSinh,))
        elif DiaChi is not None:
            sql_select_all_NhanKhau_DiaChi = """SELECT * FROM NhanKhau WHERE NoiSinh = ?"""
            result = self.conn.execute(sql_select_all_NhanKhau_DiaChi, (DiaChi,))
        elif GioiTinh is not None:
            sql_select_all_NhanKhau_GioiTinh = """SELECT * FROM NhanKhau WHERE GioiTinh = ?"""
            result = self.conn.execute(sql_select_all_NhanKhau_GioiTinh, (GioiTinh,))
        elif MaHK is not None and MaNK is not None:
            sql_select_all_NhanKhau_MaNK_MaHK = """SELECT * FROM NhanKhau WHERE MaNK = ? AND MaHK = ?"""
            result = self.conn.execute(sql_select_all_NhanKhau_MaNK_MaHK, (MaNK, MaHK))
        else:
            sql_select_all_NhanKhau = """SELECT * FROM NhanKhau"""
            result = self.conn.execute(sql_select_all_NhanKhau)    

        return result

    def select_all_KhaiSinh(self, MaKS = None, HoTenKhaiSinh = None, DiaChi = None, GioiTinh = None ):
        if MaKS is not None:
            sql_select_all_KhaiSinh_MaKS = """SELECT * FROM KhaiSinh WHERE MaKS = ?"""
            result = self.conn.execute(sql_select_all_KhaiSinh_MaKS, (MaKS,))
        elif HoTenKhaiSinh is not None:
            sql_select_all_KhaiSinh_HoTenKhaiSinh = """SELECT * FROM KhaiSinh WHERE TenKhaiSinh = ?"""
            result = self.conn.execute(sql_select_all_KhaiSinh_HoTenKhaiSinh, (HoTenKhaiSinh,))
        elif DiaChi is not None:
            sql_select_all_KhaiSinh_DiaChi = """SELECT * FROM KhaiSinh WHERE DiaChi = ?"""
            result = self.conn.execute(sql_select_all_KhaiSinh, (DiaChi,))
        elif GioiTinh is not None:
            sql_select_all_KhaiSinh_GioiTinh = """SELECT * FROM KhaiSinh WHERE GioiTinh = ?"""
            result = self.conn.execute(sql_select_all_KhaiSinh_GioiTinh, (GioiTinh,))
        else:
            sql_select_all_KhaiSinh = """SELECT * FROM KhaiSinh"""
            result = self.conn.execute(sql_select_all_KhaiSinh)

        return result

    def select_all_KhaiBao(self, MaNK = None):
        if MaNK is not None:
            sql_select_all_KhaiBao_MaNK = """SELECT * FROM KhaiBao WHERE MaNK = ?"""
            result = self.conn.execute(sql_select_all_KhaiBao_MaNK, (MaNK,))
        else:
            sql_select_all_KhaiBao = """SELECT * FROM KhaiBao"""
            result = self.conn.execute(sql_select_all_KhaiBao)
        return result

    def select_all_Tamtru(self, MaNK = None):
        if MaNK is not None:
            sql_select_all_TamTru_MaNK = """SELECT * FROM TamTru WHERE MaNK = ?"""
            result = self.conn.execute(sql_select_all_TamTru_MaNK, (MaNK,))
        else:
            sql_select_all_TamTru = """SELECT * FROM TamTru"""
            result = self.conn.execute(sql_select_all_TamTru)
        return result

    def select_all_TamVang(self, MaNK =None):
        if MaNK is not None:
            sql_select_all_TamVang_MaNK = """SELECT * FROM TamVang WHERE MaNK = ?"""
            result = self.conn.execute(sql_select_all_TamVang_MaNK, (MaNK,))
        else:
            sql_select_all_TamVang = """SELECT * FROM TamVang"""
            result = self.conn.execute(sql_select_all_TamVang)
        return result
    
    def select_all_TienAnTienSu(self, MaNK =None):
        if MaNK is not None:
            sql_select_all_TienAnTienSu_MaNK = """SELECT * FROM TienAnTienSu WHERE MaNK = ?"""
            result = self.conn.execute(sql_select_all_TienAnTienSu_MaNK, (MaNK,))
        else:
            sql_select_all_TienAnTienSu = """SELECT * FROM TienAnTienSu"""
            result = self.conn.execute(sql_select_all_TienAnTienSu)
        return result

    def select_all_HoKhau_NhanKhau_maHK(self, maHK):
        select_all_HoKhau_NhanKhau_mahk = """SELECT HoKhau.HoTenChuHo, NhanKhau.NgaySinh, NhanKhau.GioiTinh, NhanKhau.NgheNghiep, NhanKhau.ChoOHienNay
        FROM HoKhau, NhanKhau WHERE HoKhau.MaChuHo = NhanKhau.MaNK AND HoKhau.MaHK = ?"""
        result = self.conn.execute(select_all_HoKhau_NhanKhau_mahk, (maHK,))
        return result

    def select_all_SUKIEN(self, MaSK = None):
        if MaSK is not None:
            sql_select_all_SUKIEN_MaSK = """SELECT * FROM SUKIEN WHERE MaSK = ?"""
            result = self.conn.execute(sql_select_all_SUKIEN_MaSK, (MaSK,))
        else:
            sql_select_all_SUKIEN = """SELECT * FROM SUKIEN"""
            result = self.conn.execute(sql_select_all_SUKIEN)
        return result

    def select_all_CSVC(self, MaCSVC =None, Ten = None):
        if MaCSVC is not None:
            sql_select_all_CSVC_MaCSVC = """SELECT * FROM CSVC WHERE MaCSVC = ?"""
            result = self.conn.execute(sql_select_all_CSVC_MaCSVC, (MaCSVC,))
        elif Ten is not None:
            sql_select_all_CSVC_Ten = """SELECT * FROM CSVC WHERE TENCSVC = ?"""
            result = self.conn.execute(sql_select_all_CSVC_Ten, (Ten,))
        else:
            sql_select_all_CSVC = """SELECT * FROM CSVC"""
            result = self.conn.execute(sql_select_all_CSVC)
        return result
    
    def select_all_CTCSVC(self, MaSK =None, MaCSVC = None):
        if MaSK is not None:
            sql_select_all_CTCSVC_MaSK = """SELECT * FROM CTCSVC WHERE MaSK = ?"""
            result = self.conn.execute(sql_select_all_CTCSVC_MaSK, (MaSK,))
        elif MaCSVC is not None:
            sql_select_all_CTCSVC_MaCSVC = """SELECT * FROM CTCSVC WHERE MaCSVC = ?"""
            result = self.conn.execute(sql_select_all_CTCSVC_MaCSVC, (MaCSVC,))
        else:
            sql_select_all_CTCSVC = """SELECT * FROM CTCSVC"""
            result = self.conn.execute(sql_select_all_CTCSVC)
        return result

    def TongTien(self, MaSK):
        sql = """SELECT SUKIEN.MASK, SUKIEN.TENSK, SUM(CTCSVC.SOLUONGTHUE*CSVC.GIA)
                FROM CTCSVC, CSVC, SUKIEN 
                WHERE CTCSVC.MACSVC = CSVC.MACSVC AND CTCSVC.MASK = SUKIEN.MASK AND SUKIEN.MASK = ?
                GROUP BY SUKIEN.MASK, SUKIEN.TENSK"""
        result = self.conn.execute(sql, (MaSK,))
        return result

    # Thêm Dữ Liệu vào bảng NhanKhau
    def insertSqliteTable_NhanKhau(self, list_nhankhau):
        try:
            sql_insert_query = """INSERT INTO NhanKhau VALUES (?, ?, ?, ? ,? ,?, ?, ? ,?, ?, ?, ?, ?, ? ,? ,?, ?, ? ,?, ?, ?, ?, ?, ? ,? ,?, ?, ?)"""
            data = tuple(list_nhankhau)
            self.cur.execute(sql_insert_query, data)
            self.conn.commit()
            return True
        except sqlite3.Error as error:
            print("Failed to update sqlite table", error)
            return False
        finally:
            if self.conn:
                # self.conn.close()
                print("The sqlite connection is closed")

    # Thêm Dữ liệu vào bảng KhaiSinh
    def insertSqliteTable_KhaiSinh(self, list_khaisinh):
        try:
            sql_insert_query = """INSERT INTO KhaiSinh VALUES (?, ?, ?, ?, ?, ? ,? ,?, ?, ? ,?, ?, ?, ?, ?, ? ,? ,?, ?, ?)"""
            data = tuple(list_khaisinh)
            self.cur.execute(sql_insert_query, data)
            self.conn.commit()
        except sqlite3.Error as error:
            print("Failed to update sqlite table", error)
        finally:
            if self.conn:
                # self.conn.close()
                print("The sqlite connection is closed")

    # Thêm Dữ liệu vào bảng KhaiBao
    def insertSqliteTable_KhaiBao(self, list_khaibao):
        try:
            sql_insert_query = """INSERT INTO KhaiBao VALUES (?, ?, ? ,? ,?, ?, ?, ?)"""
            data = tuple(list_khaibao)
            self.cur.execute(sql_insert_query, data)
            self.conn.commit()
        except sqlite3.Error as error:
            print("Failed to update sqlite table", error)
        finally:
            if self.conn:
                # self.conn.close()
                print("The sqlite connection is closed")

    #thêm dữ liệu vào bảng tiền án 
    def insertSqliteTable_TienAnTienSu(self, list_tienantiensu):
        try:
            sql_insert_query = """INSERT INTO TienAnTienSu VALUES (?, ?, ? ,? ,?, ?, ?, ?, ?, ?)"""
            data = tuple(list_tienantiensu)
            self.cur.execute(sql_insert_query, data)
            self.conn.commit()
        except sqlite3.Error as error:
            print("Failed to update sqlite table", error)
        finally:
            if self.conn:
                # self.conn.close()
                print("The sqlite connection is closed")

    #thêm dữ liệu vào bảng hộ khẩu 
    def insertSqliteTable_HoKhau(self, list_hokhau):
        try:
            sql_insert_query = """INSERT INTO HoKhau VALUES (?, ?, ? ,? ,?, ?, ?, ?)"""
            data = tuple(list_hokhau)
            self.cur.execute(sql_insert_query, data)
            self.conn.commit()
            return True
        except sqlite3.Error as error:
            print("Failed to update sqlite table", error)
            return False
        finally:
            if self.conn:
                # self.conn.close()
                print("The sqlite connection is closed")

    def insertSqliteTable_TamTru(self, MaNK, TuNgay, DenNgay, GhiChu, NgayLap):
        try:
            sql_insert_query = """INSERT INTO TamTru VALUES (?, ?, ? ,? ,?)"""
            data = (MaNK, TuNgay, DenNgay, GhiChu, NgayLap)
            self.cur.execute(sql_insert_query, data)
            self.conn.commit()
            return True
        except sqlite3.Error as error:
            print("Failed to update sqlite table", error)
            return False
        finally:
            if self.conn:
                # self.conn.close()
                print("The sqlite connection is closed")

    def insertSqliteTable_TamVang(self, MaNK, TuNgay, DenNgay, NoiTamTru, GhiChu, NgayLap):
        try:
            sql_insert_query = """INSERT INTO TamVang VALUES (?, ?, ? ,? , ?, ?)"""
            data = (MaNK, TuNgay, DenNgay,NoiTamTru, GhiChu, NgayLap)
            self.cur.execute(sql_insert_query, data)
            self.conn.commit()
            return True
        except sqlite3.Error as error:
            print("Failed to update sqlite table", error)
            return False
        finally:
            if self.conn:
                # self.conn.close()
                print("The sqlite connection is closed")

    def insert_KhaiTu(self, list_KhaiTu):
        try:
            sql_insert_query = """INSERT INTO KhaiTu VALUES (?, ?, ? ,? , ?)"""
            data = tuple(list_KhaiTu)
            self.cur.execute(sql_insert_query, data)
            self.conn.commit()
            return True
        except sqlite3.Error as error:
            print("Failed to update sqlite table", error)
            return False
        finally:
            if self.conn:
                # self.conn.close()
                print("The sqlite connection is closed")

    def insert_sukien(self, list_sukien):
        try:
            sql_insert_query = """INSERT INTO SUKIEN VALUES (?, ?, ? ,? , ?, ?, ?)"""
            data = list_sukien
            self.cur.execute(sql_insert_query, data)
            self.conn.commit()
            return True
        except sqlite3.Error as error:
            print("Failed to update sqlite table", error)
            return False
        finally:
            if self.conn:
                # self.conn.close()
                print("The sqlite connection is closed")

    def insert_csvc(self, list_csvc):
        try:
            sql_insert_query = """INSERT INTO CSVC VALUES (? , ?, ?, ?)"""
            data = tuple(list_csvc)
            self.cur.execute(sql_insert_query, data)
            self.conn.commit()
            return True
        except sqlite3.Error as error:
            print("Failed to update sqlite table", error)
            return False
        finally:
            if self.conn:
                # self.conn.close()
                print("The sqlite connection is closed")

    def insert_ctcsvc(self, list_ctcsvc):
        try:
            sql_insert_query = """INSERT INTO CTCSVC VALUES (?, ?, ?)"""
            data = tuple(list_ctcsvc)
            self.cur.execute(sql_insert_query, data)
            self.conn.commit()
            return True
        except sqlite3.Error as error:
            print("Failed to update sqlite table", error)
            return False
        finally:
            if self.conn:
                # self.conn.close()
                print("The sqlite connection is closed")

    def xoacosovatchat(self, MACSVC):
        try:
            sql_update_query = """DELETE FROM CSVC  WHERE MACSVC = ?"""
            self.cur.execute(sql_update_query, (MACSVC,))
            self.conn.commit()
            print("Record DELETE successfully")
            # self.cur.close()
            return True

        except sqlite3.Error as error:
            print("Failed to DELETE sqlite table", error)
            return False
        finally:
            if self.conn:
                
                print("The sqlite connection is closed")


    def xoasukien(self, MASK):
        try:
            sql_update_query = """DELETE FROM SUKIEN  WHERE MASK = ?"""
            self.cur.execute(sql_update_query, (MASK,))
            self.conn.commit()
            print("Record DELETE successfully")
            # self.cur.close()
            return True

        except sqlite3.Error as error:
            print("Failed to DELETE sqlite table", error)
            return False
        finally:
            if self.conn:
                
                print("The sqlite connection is closed")
db = MY_DB()

# db.xoacosovatchat("CSVC6")
# result = db.select_all_user()

# # db.updateSqliteTable("001", "Lê Quang Vũ", "Nam", "vu.lq204624@sis.hust.edu.vn", "Công An", "Quản Lý", "2002-03-22", "Láng - Đống Đa", "0366493337")

# # db.update_user()

# result = db.ThongTinNguoiDung("quangvu2", "vu123")
# print(result)

# result = db.select_all_HoKhau(None, None, None)
# result = db.select_all_NhanKhau(None, None, "KS2", None, None, None)
# result = db.TongTien("SK2")
# # result = db.select_all_HoKhau_NhanKhau_maHK("NK1")
# # print(result.fetchall())

# db.insert_sukien(('NK2', 'Lê Quang Vũ', '23444444', 'SK3', 'đám cưới', '2000-01-01 00:00:00', '2000-01-01 00:00:00'))
# for num_row, row_data in enumerate(result):
#     print(row_data)


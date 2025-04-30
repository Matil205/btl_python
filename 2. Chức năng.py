# Phan 1: File
import os
import csv
from datetime import datetime

TEN_FILE_NHAN_VIEN = "NHANVIEN.TXT"
NAM_HIEN_TAI = 2025
TY_LE_TANG_LUONG = 0.10 # 10%

def doc_du_lieu_nhan_vien(ten_file):
    """Đọc dữ liệu nhân viên từ file TXT và trả về một danh sách."""
    danh_sach_nhan_vien = []
    if not os.path.exists(ten_file):
        print(f"File '{ten_file}' không tồn tại.")
        return danh_sach_nhan_vien
    with open(ten_file, 'r', encoding='utf-8') as file_txt:
        for line in file_txt:
            thong_tin = line.strip().split(',')
            if len(thong_tin) == 5:
                danh_sach_nhan_vien.append(thong_tin)
    return danh_sach_nhan_vien

def hien_thi_thong_tin(nhan_vien):
    """Hiển thị thông tin của một nhân viên."""
    print(f"Họ tên: {nhan_vien[0]}")
    print(f"Ngày sinh: {nhan_vien[1]}")
    print(f"Ngày vào công ty: {nhan_vien[2]}")
    print(f"Đơn vị làm việc: {nhan_vien[3]}")
    print(f"Mức lương: {nhan_vien[4]}")
    print("-" * 20)

def tim_kiem_nhan_vien(danh_sach):
    """Tìm kiếm và hiển thị thông tin nhân viên theo tên."""
    ten_tim_kiem = input("Nhập tên nhân viên cần tìm: ")
    ket_qua_tim_kiem = [nv for nv in danh_sach if ten_tim_kiem.lower() in nv[0].lower()]
    if ket_qua_tim_kiem:
        print(f"Tìm thấy {len(ket_qua_tim_kiem)} nhân viên có tên '{ten_tim_kiem}':")
        for nv in ket_qua_tim_kiem:
            hien_thi_thong_tin(nv)
    else:
        print(f"Không tìm thấy nhân viên nào có tên '{ten_tim_kiem}'.")

def xoa_nhan_vien(danh_sach, ten_file):
    """Xóa nhân viên khỏi danh sách theo tên."""
    ten_xoa = input("Nhập tên nhân viên cần xóa: ")
    danh_sach_moi = [nv for nv in danh_sach if ten_xoa.lower() not in nv[0].lower()]
    if len(danh_sach_moi) < len(danh_sach):
        ghi_lai_du_lieu(danh_sach_moi, ten_file)
        print(f"Đã xóa các nhân viên có tên chứa '{ten_xoa}' khỏi danh sách.")
    else:
        print(f"Không tìm thấy nhân viên nào có tên chứa '{ten_xoa}' trong danh sách.")

def ghi_lai_du_lieu(danh_sach, ten_file):
    """Ghi lại danh sách nhân viên vào file."""
    with open(ten_file, 'w', encoding='utf-8') as file_txt:
        for nv in danh_sach:
            file_txt.write(','.join(nv) + '\n')

# Phần 4: Các chức năng nâng cao
def loc_theo_danh_muc(danh_sach):
    """Lọc danh sách nhân viên theo một danh mục (ví dụ: đơn vị làm việc)."""
    danh_muc = input("Chọn danh mục để lọc (họ tên, ngày sinh, ngày vào công ty, đơn vị làm việc, mức lương): ").lower()
    gia_tri_loc = input(f"Nhập giá trị cần lọc cho danh mục '{danh_muc}': ").lower()
    chi_so_cot = -1
    if danh_muc == "họ tên":
        chi_so_cot = 0
    elif danh_muc == "ngày sinh":
        chi_so_cot = 1
    elif danh_muc == "ngày vào công ty":
        chi_so_cot = 2
    elif danh_muc == "đơn vị làm việc":
        chi_so_cot = 3
    elif danh_muc == "mức lương":
        chi_so_cot = 4

    if chi_so_cot != -1:
        ket_qua_loc = [nv for nv in danh_sach if gia_tri_loc in nv[chi_so_cot].lower()]
        if ket_qua_loc:
            print(f"\nDanh sách nhân viên theo bộ lọc '{danh_muc}' = '{gia_tri_loc}':")
            for nv in ket_qua_loc:
                hien_thi_thong_tin(nv)
        else:
            print(f"Không có nhân viên nào phù hợp với bộ lọc '{danh_muc}' = '{gia_tri_loc}'.")
    else:
        print("Danh mục không hợp lệ.")

def sap_xep_thong_tin(danh_sach):
    """Sắp xếp danh sách nhân viên theo một danh mục."""
    danh_muc = input("Chọn danh mục để sắp xếp (họ tên, ngày sinh, ngày vào công ty, đơn vị làm việc, mức lương): ").lower()
    thu_tu = input("Chọn thứ tự (asc/desc): ").lower()
    chi_so_cot = -1
    if danh_muc == "họ tên":
        chi_so_cot = 0
    elif danh_muc == "ngày sinh":
        chi_so_cot = 1
    elif danh_muc == "ngày vào công ty":
        chi_so_cot = 2
    elif danh_muc == "đơn vị làm việc":
        chi_so_cot = 3
    elif danh_muc == "mức lương":
        chi_so_cot = 4

    if chi_so_cot != -1:
        try:
            if danh_muc == "mức lương":
                danh_sach.sort(key=lambda nv: float(nv[chi_so_cot]), reverse=(thu_tu == 'desc'))
            else:
                danh_sach.sort(key=lambda nv: nv[chi_so_cot], reverse=(thu_tu == 'desc'))
            print(f"\nĐã sắp xếp danh sách theo '{danh_muc}' ({thu_tu}):")
            for nv in danh_sach:
                hien_thi_thong_tin(nv)
        except ValueError:
            print("Lỗi: Không thể sắp xếp theo danh mục đã chọn.")
    else:
        print("Danh mục không hợp lệ.")

def thong_ke_luong(danh_sach):
    """Tính tổng lương và trung bình lương của cả công ty và từng đơn vị."""
    tong_luong_cong_ty = 0
    so_luong_nhan_vien = len(danh_sach)
    luong_theo_don_vi = {}

    for nv in danh_sach:
        try:
            luong = float(nv[4])
            tong_luong_cong_ty += luong
            don_vi = nv[3]
            if don_vi not in luong_theo_don_vi:
                luong_theo_don_vi[don_vi] = {"tong": 0, "so_luong": 0}
            luong_theo_don_vi[don_vi]["tong"] += luong
            luong_theo_don_vi[don_vi]["so_luong"] += 1
        except ValueError:
            print(f"Lỗi: Mức lương không hợp lệ cho nhân viên '{nv[0]}'.")

    print("\n--- THỐNG KÊ LƯƠNG ---")
    if so_luong_nhan_vien > 0:
        trung_binh_luong_cong_ty = tong_luong_cong_ty / so_luong_nhan_vien
        print(f"Tổng lương của cả công ty: {tong_luong_cong_ty:,.2f}")
        print(f"Trung bình lương của cả công ty: {trung_binh_luong_cong_ty:,.2f}")
    else:
        print("Không có dữ liệu nhân viên.")

    print("\nThống kê lương theo đơn vị:")
    for don_vi, thong_ke in luong_theo_don_vi.items():
        trung_binh_luong_don_vi = thong_ke["tong"] / thong_ke["so_luong"]
        print(f"- Đơn vị '{don_vi}':")
        print(f"  + Tổng lương: {thong_ke['tong']:,.2f}")
        print(f"  + Trung bình lương: {trung_binh_luong_don_vi:,.2f}")

def du_doan_luong(danh_sach):
    """Dự đoán lương trong những năm tiếp theo cho từng người."""
    nam_hien_tai = NAM_HIEN_TAI
    ty_le_tang = TY_LE_TANG_LUONG

    print("\n--- DỰ ĐOÁN LƯƠNG ---")
    for nv in danh_sach:
        try:
            ten = nv[0]
            luong_hien_tai = float(nv[4])
            print(f"Dự đoán lương cho nhân viên: {ten}")
            for nam_du_kien in range(nam_hien_tai + 1, nam_hien_tai + 6): # Dự đoán cho 5 năm tiếp theo
                luong_du_kien = luong_hien_tai * (1 + ty_le_tang)**(nam_du_kien - nam_hien_tai)
                print(f"- Năm {nam_du_kien}: {luong_du_kien:,.2f}")
            print("-" * 20)
        except ValueError:
            print(f"Lỗi: Mức lương không hợp lệ cho nhân viên '{nv[0]}'.")

def hien_thi_menu():
    """Hiển thị menu các chức năng."""
    print("\n--- DANH MỤC QUẢN LÝ NHÂN VIÊN ---")
    print("1. Tìm kiếm thông tin nhân viên")
    print("2. Xóa nhân viên")
    print("3. Lọc theo danh mục")
    print("4. Sắp xếp thông tin")
    print("5. Thống kê lương")
    print("6. Dự đoán lương")
    print("0. Thoát")

def xu_ly_lua_chon(lua_chon, danh_sach):
    """Xử lý lựa chọn của người dùng."""
    if lua_chon == '1':
        tim_kiem_nhan_vien(danh_sach)
    elif lua_chon == '2':
        danh_sach_moi = xoa_nhan_vien(danh_sach, TEN_FILE_NHAN_VIEN)
        if danh_sach_moi is not None:
            return danh_sach_moi
    elif lua_chon == '3':
        loc_theo_danh_muc(danh_sach)
    elif lua_chon == '4':
        sap_xep_thong_tin(danh_sach)
    elif lua_chon == '5':
        thong_ke_luong(danh_sach)
    elif lua_chon == '6':
        du_doan_luong(danh_sach)
    elif lua_chon == '0':
        print("Cảm ơn bạn đã sử dụng chương trình!")
        return None
    else:
        print("Lựa chọn không hợp lệ. Vui lòng thử lại.")
    return danh_sach

if __name__ == "__main__":
    danh_sach_nv = doc_du_lieu_nhan_vien(TEN_FILE_NHAN_VIEN)
    while True:
        hien_thi_menu()
        lua_chon = input("Nhập lựa chọn của bạn: ")
        danh_sach_nv_moi = xu_ly_lua_chon(lua_chon, danh_sach_nv)
        if danh_sach_nv_moi is None:
            break
        danh_sach_nv = danh_sach_nv_moi
# nhap_thong_tin_nhan_vien_chi_tiet_luu_thong_tin

def nhap_thong_tin_nhan_vien():
    """Nhập thông tin chi tiết của 30 nhân viên và lưu vào file NHANVIEN.TXT."""
    danh_sach_nhan_vien = []
    for i in range(30):
        print(f"Nhập thông tin cho nhân viên thứ {i+1}:")
        while True:
            ho_ten = input("Họ tên (không quá 25 ký tự): ")
            if len(ho_ten) <= 25:
                break
            else:
                print("Họ tên quá dài, vui lòng nhập lại.")
        ngay_sinh = input("Ngày sinh (YYYY-MM-DD): ")
        ngay_vao_cong_ty = input("Ngày vào công ty (YYYY-MM-DD): ")
        don_vi_lam_viec = input("Đơn vị làm việc: ")
        while True:
            try:
                muc_luong = float(input("Mức lương: "))
                if muc_luong >= 0:
                    break
                else:
                    print("Mức lương phải là một số không âm, vui lòng nhập lại.")
            except ValueError:
                print("Mức lương không hợp lệ, vui lòng nhập số.")

        danh_sach_nhan_vien.append(f"{ho_ten},{ngay_sinh},{ngay_vao_cong_ty},{don_vi_lam_viec},{muc_luong}\n")

    luu_vao_txt(danh_sach_nhan_vien, "NHANVIEN.TXT")
    print("Đã nhập và lưu thông tin chi tiết của 30 nhân viên vào file NHANVIEN.TXT")

def luu_vao_txt(du_lieu, ten_file):
    """Lưu danh sách dữ liệu vào file TXT."""
    with open(ten_file, 'w', encoding='utf-8') as file_txt:
        file_txt.writelines(du_lieu)

if __name__ == "__main__":
    nhap_thong_tin_nhan_vien()


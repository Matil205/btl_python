def kiem_tra_dinh_dang_ngay(ngay):
    try:
        if len(ngay) != 10 or ngay[4] != "-" or ngay[7] != "-":
            return False
        nam, thang, ngay_thang = map(int, ngay.split("-"))
        if not (1 <= thang <= 12 and 1 <= ngay_thang <= 31 and 1900 <= nam <= 2025):
            return False
        return True
    except ValueError:
        return False
def nhap_thong_tin_nhan_vien():
    danh_sach_nhan_vien = []
    print("Nhập thông tin nhân viên (nhập họ tên để trống để dừng nhập):")
    while True:
        ho_ten = input("Họ tên (không quá 25 ký tự): ").strip()
        if ho_ten == "":
            break
        if any(nhan_vien["Họ tên"] == ho_ten for nhan_vien in danh_sach_nhan_vien):
            print("Họ tên đã tồn tại, vui lòng nhập lại hoặc để trống để dừng.")
            continue
        while len(ho_ten) > 25:
            print("Họ tên quá dài, vui lòng nhập lại.")
            ho_ten = input("Họ tên (không quá 25 ký tự): ").strip()
            if ho_ten == "":
                break
        if ho_ten == "":
            break

        while True:
            ngay_sinh = input("Ngày sinh (YYYY-MM-DD): ").strip()
            if kiem_tra_dinh_dang_ngay(ngay_sinh):
                break
            print("Ngày sinh không đúng định dạng YYYY-MM-DD hoặc không hợp lệ, vui lòng nhập lại.")

        while True:
            ngay_vao_cong_ty = input("Ngày vào công ty (YYYY-MM-DD): ").strip()
            if kiem_tra_dinh_dang_ngay(ngay_vao_cong_ty):
                break
            print("Ngày vào công ty không đúng định dạng YYYY-MM-DD hoặc không hợp lệ, vui lòng nhập lại.")

        don_vi_lam_viec = input("Đơn vị làm việc: ").strip()

        while True:
            try:
                muc_luong = float(input("Mức lương: "))
                if muc_luong >= 0:
                    break
                else:
                    print("Mức lương phải là một số không âm, vui lòng nhập lại.")
            except ValueError:
                print("Mức lương không hợp lệ, vui lòng nhập số.")

        nhan_vien = {
            "Họ tên": ho_ten,
            "Ngày sinh": ngay_sinh,
            "Ngày vào công ty": ngay_vao_cong_ty,
            "Đơn vị làm việc": don_vi_lam_viec,
            "Mức lương": muc_luong
        }
        danh_sach_nhan_vien.append(nhan_vien)

    if danh_sach_nhan_vien:
        print(f"Đã lưu thông tin của {len(danh_sach_nhan_vien)} nhân viên vào file NHANVIEN.TXT")
    else:
        print("Không có nhân viên nào được nhập.")
if __name__ == "__main__":
    nhap_thong_tin_nhan_vien()

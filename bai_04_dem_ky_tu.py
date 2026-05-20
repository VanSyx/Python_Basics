# Bài 4: Liệt kê số lần xuất hiện của mỗi ký tự.

import sys  # Import thư viện sys để cấu hình cách nhập và xuất dữ liệu.
sys.stdin.reconfigure(encoding="utf-8")  # Cấu hình dữ liệu nhập theo bảng mã UTF-8.
sys.stdout.reconfigure(encoding="utf-8")  # Cấu hình dữ liệu xuất theo bảng mã UTF-8.

chuoi = input("Nhập chuỗi: ")  # Nhập chuỗi bất kỳ từ bàn phím.
da_dem = ""  # Tạo chuỗi rỗng để lưu các ký tự đã được đếm.

for ky_tu in chuoi:  # Duyệt từng ký tự trong chuỗi.
    if ky_tu not in da_dem:  # Chỉ xử lý nếu ký tự này chưa được đếm.
        so_lan = chuoi.count(ky_tu)  # Đếm số lần xuất hiện của ký tự trong chuỗi.
        print("Ký tự", repr(ky_tu), "xuất hiện", so_lan, "lần")  # In ký tự và số lần xuất hiện.
        da_dem = da_dem + ky_tu  # Thêm ký tự vào danh sách đã đếm.

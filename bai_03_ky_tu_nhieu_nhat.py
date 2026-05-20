# Bài 3: Tìm ký tự xuất hiện nhiều nhất trong chuỗi.

import sys  # Import thư viện sys để cấu hình cách nhập và xuất dữ liệu.
sys.stdin.reconfigure(encoding="utf-8")  # Cấu hình dữ liệu nhập theo bảng mã UTF-8.
sys.stdout.reconfigure(encoding="utf-8")  # Cấu hình dữ liệu xuất theo bảng mã UTF-8.

chuoi = input("Nhập chuỗi: ")  # Nhập chuỗi từ bàn phím.
ky_tu_nhieu_nhat = ""  # Tạo biến để lưu ký tự xuất hiện nhiều nhất.
so_lan_nhieu_nhat = 0  # Tạo biến để lưu số lần xuất hiện nhiều nhất.

for ky_tu in chuoi:  # Duyệt từng ký tự trong chuỗi.
    so_lan = chuoi.count(ky_tu)  # Đếm số lần ký tự hiện tại xuất hiện trong chuỗi.
    if so_lan > so_lan_nhieu_nhat:  # Kiểm tra ký tự hiện tại có xuất hiện nhiều hơn kết quả cũ không.
        ky_tu_nhieu_nhat = ky_tu  # Cập nhật ký tự xuất hiện nhiều nhất.
        so_lan_nhieu_nhat = so_lan  # Cập nhật số lần xuất hiện nhiều nhất.

print("Ký tự xuất hiện nhiều nhất:", ky_tu_nhieu_nhat)  # In ký tự xuất hiện nhiều nhất.
print("Số lần xuất hiện:", so_lan_nhieu_nhat)  # In số lần xuất hiện của ký tự đó.

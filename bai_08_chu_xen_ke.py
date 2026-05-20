# Bài 8: Đổi chữ xen kẽ một chữ hoa và một chữ thường.

import sys  # Import thư viện sys để cấu hình cách nhập và xuất dữ liệu.
sys.stdin.reconfigure(encoding="utf-8")  # Cấu hình dữ liệu nhập theo bảng mã UTF-8.
sys.stdout.reconfigure(encoding="utf-8")  # Cấu hình dữ liệu xuất theo bảng mã UTF-8.

chuoi = input("Nhập chuỗi: ")  # Nhập chuỗi từ bàn phím.
ket_qua = ""  # Tạo chuỗi rỗng để lưu kết quả.

for i in range(len(chuoi)):  # Duyệt từng vị trí trong chuỗi bằng chỉ số.
    if i % 2 == 0:  # Kiểm tra vị trí hiện tại là vị trí chẵn.
        ket_qua = ket_qua + chuoi[i].upper()  # Đổi ký tự ở vị trí chẵn thành chữ hoa.
    else:  # Trường hợp vị trí hiện tại là vị trí lẻ.
        ket_qua = ket_qua + chuoi[i].lower()  # Đổi ký tự ở vị trí lẻ thành chữ thường.

print("Chuỗi sau khi đổi xen kẽ:", ket_qua)  # In kết quả ra màn hình.

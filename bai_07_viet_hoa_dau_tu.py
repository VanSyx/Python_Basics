# Bài 7: Chuyển ký tự đầu tiên của mỗi từ thành chữ in hoa.

import sys  # Import thư viện sys để cấu hình cách nhập và xuất dữ liệu.
sys.stdin.reconfigure(encoding="utf-8")  # Cấu hình dữ liệu nhập theo bảng mã UTF-8.
sys.stdout.reconfigure(encoding="utf-8")  # Cấu hình dữ liệu xuất theo bảng mã UTF-8.

chuoi = input("Nhập chuỗi: ")  # Nhập chuỗi từ bàn phím.
ds_tu = chuoi.split()  # Tách chuỗi thành danh sách các từ.
ds_tu_moi = []  # Tạo danh sách rỗng để lưu các từ sau khi xử lý.

for tu in ds_tu:  # Duyệt từng từ trong danh sách.
    tu_moi = tu[0].upper() + tu[1:]  # Viết hoa ký tự đầu tiên và giữ nguyên phần còn lại.
    ds_tu_moi.append(tu_moi)  # Thêm từ mới vào danh sách kết quả.

ket_qua = " ".join(ds_tu_moi)  # Ghép các từ đã xử lý thành một chuỗi.
print("Chuỗi sau khi viết hoa đầu từ:", ket_qua)  # In kết quả ra màn hình.

# Bài 2: Đảo ngược thứ tự các từ trong chuỗi.

import sys  # Import thư viện sys để cấu hình cách nhập và xuất dữ liệu.
sys.stdin.reconfigure(encoding="utf-8")  # Cấu hình dữ liệu nhập theo bảng mã UTF-8.
sys.stdout.reconfigure(encoding="utf-8")  # Cấu hình dữ liệu xuất theo bảng mã UTF-8.

chuoi = input("Nhập chuỗi: ")  # Nhập chuỗi từ bàn phím.
ds_tu = chuoi.split()  # Tách chuỗi thành danh sách các từ.
ds_tu_dao_nguoc = ds_tu[::-1]  # Đảo ngược thứ tự các từ trong danh sách.
ket_qua = " ".join(ds_tu_dao_nguoc)  # Ghép danh sách từ đã đảo thành chuỗi mới.
print("Chuỗi sau khi đảo ngược:", ket_qua)  # In chuỗi kết quả ra màn hình.

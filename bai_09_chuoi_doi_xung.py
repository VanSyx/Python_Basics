# Bài 9: Kiểm tra chuỗi có đối xứng hay không.

import sys  # Import thư viện sys để cấu hình cách nhập và xuất dữ liệu.
sys.stdin.reconfigure(encoding="utf-8")  # Cấu hình dữ liệu nhập theo bảng mã UTF-8.
sys.stdout.reconfigure(encoding="utf-8")  # Cấu hình dữ liệu xuất theo bảng mã UTF-8.

chuoi = input("Nhập chuỗi: ")  # Nhập chuỗi từ bàn phím.
chuoi_dao_nguoc = chuoi[::-1]  # Tạo chuỗi đảo ngược từ chuỗi ban đầu.

if chuoi == chuoi_dao_nguoc:  # So sánh chuỗi ban đầu với chuỗi đảo ngược.
    print("Chuỗi đối xứng.")  # Thông báo nếu hai chuỗi giống nhau.
else:  # Trường hợp hai chuỗi không giống nhau.
    print("Chuỗi không đối xứng.")  # Thông báo chuỗi không đối xứng.

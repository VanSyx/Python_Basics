# Bài 1: Chuẩn hóa các từ trong họ tên.

import sys  # Import thư viện sys để cấu hình cách nhập và xuất dữ liệu.
sys.stdin.reconfigure(encoding="utf-8")  # Cấu hình dữ liệu nhập theo bảng mã UTF-8.
sys.stdout.reconfigure(encoding="utf-8")  # Cấu hình dữ liệu xuất theo bảng mã UTF-8.

chuoi = input("Nhập họ tên cần chuẩn hóa: ")  # Nhập chuỗi họ tên từ bàn phím.
ds_tu = chuoi.split()  # Tách chuỗi thành danh sách các từ, tự bỏ khoảng trắng thừa.
ds_tu_moi = []  # Tạo danh sách rỗng để lưu các từ sau khi chuẩn hóa.

for tu in ds_tu:  # Duyệt lần lượt từng từ trong danh sách vừa tách.
    tu_moi = tu[0].upper() + tu[1:].lower()  # Viết hoa chữ đầu và viết thường các chữ còn lại.
    ds_tu_moi.append(tu_moi)  # Thêm từ đã chuẩn hóa vào danh sách mới.

ket_qua = " ".join(ds_tu_moi)  # Ghép các từ trong danh sách thành một chuỗi hoàn chỉnh.
print("Chuỗi sau khi chuẩn hóa:", ket_qua)  # In kết quả ra màn hình.

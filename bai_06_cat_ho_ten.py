# Bài 6: Cắt chuỗi họ tên thành họ lót và tên.

import sys  # Import thư viện sys để cấu hình cách nhập và xuất dữ liệu.
sys.stdin.reconfigure(encoding="utf-8")  # Cấu hình dữ liệu nhập theo bảng mã UTF-8.
sys.stdout.reconfigure(encoding="utf-8")  # Cấu hình dữ liệu xuất theo bảng mã UTF-8.

def cat_ho_ten(ho_ten):  # Định nghĩa hàm nhận vào một chuỗi họ tên.
    ds_tu = ho_ten.split()  # Tách họ tên thành danh sách các từ.
    ten = ds_tu[-1]  # Lấy từ cuối cùng trong danh sách làm tên.
    ho_lot = " ".join(ds_tu[:-1])  # Ghép các từ còn lại thành chuỗi họ lót.
    return ho_lot, ten  # Trả về hai giá trị là họ lót và tên.


ho_ten = input("Nhập họ tên đầy đủ: ")  # Nhập họ tên từ bàn phím.
ho_lot, ten = cat_ho_ten(ho_ten)  # Gọi hàm để tách họ lót và tên.
print("Họ lót:", ho_lot)  # In phần họ lót ra màn hình.
print("Tên:", ten)  # In phần tên ra màn hình.

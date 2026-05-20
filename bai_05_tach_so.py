# Bài 5: Kiểm tra chuỗi có ký tự số hay không và tách các số ra mảng riêng.

import sys  # Import thư viện sys để cấu hình cách nhập và xuất dữ liệu.
sys.stdin.reconfigure(encoding="utf-8")  # Cấu hình dữ liệu nhập theo bảng mã UTF-8.
sys.stdout.reconfigure(encoding="utf-8")  # Cấu hình dữ liệu xuất theo bảng mã UTF-8.

def tach_so(chuoi):  # Định nghĩa hàm nhận vào một chuỗi cần kiểm tra.
    ds_so = []  # Tạo danh sách rỗng để lưu các ký tự số.
    for ky_tu in chuoi:  # Duyệt từng ký tự trong chuỗi.
        if ky_tu.isdigit():  # Kiểm tra ký tự hiện tại có phải là chữ số không.
            ds_so.append(ky_tu)  # Thêm ký tự số vào danh sách.
    return ds_so  # Trả về danh sách các ký tự số tìm được.


chuoi = input("Nhập chuỗi: ")  # Nhập chuỗi từ bàn phím.
ds_so = tach_so(chuoi)  # Gọi hàm để tách các ký tự số trong chuỗi.

if len(ds_so) > 0:  # Kiểm tra danh sách số có phần tử hay không.
    print("Chuỗi có ký tự số.")  # Thông báo chuỗi có ký tự số.
    print("Mảng các số:", ds_so)  # In danh sách các ký tự số đã tách.
else:  # Trường hợp danh sách số rỗng.
    print("Chuỗi không có ký tự số.")  # Thông báo chuỗi không có ký tự số.

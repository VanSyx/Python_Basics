# Bài 10: Đọc một số có 3 chữ số thành chữ tiếng Việt.

import sys  # Import thư viện sys để cấu hình cách nhập và xuất dữ liệu.
sys.stdin.reconfigure(encoding="utf-8")  # Cấu hình dữ liệu nhập theo bảng mã UTF-8.
sys.stdout.reconfigure(encoding="utf-8")  # Cấu hình dữ liệu xuất theo bảng mã UTF-8.

so = int(input("Nhập số có 3 chữ số: "))  # Nhập số từ bàn phím và đổi sang kiểu số nguyên.
hang_tram = so // 100  # Lấy chữ số hàng trăm bằng phép chia lấy phần nguyên.
hang_chuc = (so // 10) % 10  # Lấy chữ số hàng chục.
hang_don_vi = so % 10  # Lấy chữ số hàng đơn vị.
chu_so = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]  # Tạo danh sách cách đọc các chữ số.
ket_qua = chu_so[hang_tram] + " trăm"  # Bắt đầu kết quả bằng phần hàng trăm.

if hang_chuc == 0 and hang_don_vi == 0:  # Kiểm tra số tròn trăm.
    ket_qua = ket_qua  # Giữ nguyên kết quả vì không cần đọc hàng chục và hàng đơn vị.
elif hang_chuc == 0:  # Kiểm tra trường hợp không có hàng chục nhưng có hàng đơn vị.
    ket_qua = ket_qua + " lẻ " + chu_so[hang_don_vi]  # Thêm cách đọc hàng đơn vị sau chữ "lẻ".
elif hang_chuc == 1:  # Kiểm tra trường hợp hàng chục bằng 1.
    ket_qua = ket_qua + " mười"  # Thêm chữ "mười" vào kết quả.
    if hang_don_vi != 0:  # Kiểm tra hàng đơn vị có khác 0 không.
        ket_qua = ket_qua + " " + chu_so[hang_don_vi]  # Thêm cách đọc hàng đơn vị.
else:  # Trường hợp hàng chục từ 2 đến 9.
    ket_qua = ket_qua + " " + chu_so[hang_chuc] + " mươi"  # Thêm cách đọc hàng chục.
    if hang_don_vi == 1:  # Kiểm tra hàng đơn vị bằng 1.
        ket_qua = ket_qua + " mốt"  # Đọc 1 sau hàng chục là "mốt".
    elif hang_don_vi == 5:  # Kiểm tra hàng đơn vị bằng 5.
        ket_qua = ket_qua + " lăm"  # Đọc 5 sau hàng chục là "lăm".
    elif hang_don_vi != 0:  # Kiểm tra hàng đơn vị khác 0.
        ket_qua = ket_qua + " " + chu_so[hang_don_vi]  # Thêm cách đọc hàng đơn vị bình thường.

print("Cách đọc:", ket_qua)  # In cách đọc số ra màn hình.

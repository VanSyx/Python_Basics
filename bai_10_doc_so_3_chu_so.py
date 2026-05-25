import sys

sys.stdin.reconfigure(encoding="utf-8")
sys.stdout.reconfigure(encoding="utf-8")


def doc_hang_chuc(hang_chuc, hang_don_vi, chu_so):
    if hang_chuc == 0 and hang_don_vi == 0:
        return ""

    if hang_chuc == 0:
        return "lẻ " + chu_so[hang_don_vi]

    if hang_chuc == 1:
        if hang_don_vi == 0:
            return "mười"
        return "mười " + chu_so[hang_don_vi]

    ket_qua = chu_so[hang_chuc] + " mươi"

    if hang_don_vi == 1:
        ket_qua = ket_qua + " mốt"
    elif hang_don_vi == 5:
        ket_qua = ket_qua + " lăm"
    elif hang_don_vi != 0:
        ket_qua = ket_qua + " " + chu_so[hang_don_vi]

    return ket_qua


def doc_so_3_chu_so(so):
    chu_so = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]

    hang_tram = so // 100
    hang_chuc = (so // 10) % 10
    hang_don_vi = so % 10

    ket_qua = chu_so[hang_tram] + " trăm"
    phan_chuc = doc_hang_chuc(hang_chuc, hang_don_vi, chu_so)

    if phan_chuc != "":
        ket_qua = ket_qua + " " + phan_chuc

    return ket_qua


def main():
    so = int(input("Nhập số có 3 chữ số: "))

    if so < 100 or so > 999:
        print("Vui lòng nhập số có đúng 3 chữ số.")
    else:
        print("Cách đọc:", doc_so_3_chu_so(so))


if __name__ == "__main__":
    main()

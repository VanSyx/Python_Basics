import sys

sys.stdin.reconfigure(encoding="utf-8")
sys.stdout.reconfigure(encoding="utf-8")


def viet_hoa_tu(tu):
    return tu[0].upper() + tu[1:]


def viet_hoa_dau_tu(chuoi):
    danh_sach_tu = chuoi.split()
    ket_qua = []

    for tu in danh_sach_tu:
        ket_qua.append(viet_hoa_tu(tu))

    return " ".join(ket_qua)


def main():
    chuoi = input("Nhập chuỗi: ")
    print("Kết quả:", viet_hoa_dau_tu(chuoi))


if __name__ == "__main__":
    main()

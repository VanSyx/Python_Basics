import sys

sys.stdin.reconfigure(encoding="utf-8")
sys.stdout.reconfigure(encoding="utf-8")


def chuan_hoa_tu(tu):
    return tu[0].upper() + tu[1:].lower()


def chuan_hoa_ho_ten(ho_ten):
    danh_sach_tu = ho_ten.split()
    ket_qua = []

    for tu in danh_sach_tu:
        ket_qua.append(chuan_hoa_tu(tu))

    return " ".join(ket_qua)


def main():
    ho_ten = input("Nhập họ tên cần chuẩn hóa: ")
    print("Kết quả:", chuan_hoa_ho_ten(ho_ten))


if __name__ == "__main__":
    main()

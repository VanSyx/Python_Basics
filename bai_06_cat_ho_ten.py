import sys

sys.stdin.reconfigure(encoding="utf-8")
sys.stdout.reconfigure(encoding="utf-8")


def cat_ho_ten(ho_ten):
    danh_sach_tu = ho_ten.split()

    if len(danh_sach_tu) == 0:
        return "", ""

    ten = danh_sach_tu[-1]
    ho_lot = " ".join(danh_sach_tu[:-1])
    return ho_lot, ten


def main():
    ho_ten = input("Nhập họ tên đầy đủ: ")
    ho_lot, ten = cat_ho_ten(ho_ten)

    print("Họ lót:", ho_lot)
    print("Tên:", ten)


if __name__ == "__main__":
    main()

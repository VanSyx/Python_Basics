import sys

sys.stdin.reconfigure(encoding="utf-8")
sys.stdout.reconfigure(encoding="utf-8")


def dao_nguoc_cac_tu(chuoi):
    danh_sach_tu = chuoi.split()
    danh_sach_tu_dao = danh_sach_tu[::-1]
    return " ".join(danh_sach_tu_dao)


def main():
    chuoi = input("Nhập chuỗi: ")
    print("Kết quả:", dao_nguoc_cac_tu(chuoi))


if __name__ == "__main__":
    main()

import sys

sys.stdin.reconfigure(encoding="utf-8")
sys.stdout.reconfigure(encoding="utf-8")


def tach_so(chuoi):
    danh_sach_so = []

    for ky_tu in chuoi:
        if ky_tu.isdigit():
            danh_sach_so.append(ky_tu)

    return danh_sach_so


def co_ky_tu_so(chuoi):
    return len(tach_so(chuoi)) > 0


def main():
    chuoi = input("Nhập chuỗi: ")
    danh_sach_so = tach_so(chuoi)

    if co_ky_tu_so(chuoi):
        print("Chuỗi có ký tự số.")
        print("Mảng các số:", danh_sach_so)
    else:
        print("Chuỗi không có ký tự số.")


if __name__ == "__main__":
    main()

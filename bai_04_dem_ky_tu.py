import sys

sys.stdin.reconfigure(encoding="utf-8")
sys.stdout.reconfigure(encoding="utf-8")


def dem_so_lan_ky_tu(chuoi):
    ket_qua = {}

    for ky_tu in chuoi:
        if ky_tu in ket_qua:
            ket_qua[ky_tu] = ket_qua[ky_tu] + 1
        else:
            ket_qua[ky_tu] = 1

    return ket_qua


def in_ket_qua(ket_qua):
    for ky_tu in ket_qua:
        print("Ký tự", repr(ky_tu), "xuất hiện", ket_qua[ky_tu], "lần")


def main():
    chuoi = input("Nhập chuỗi: ")
    ket_qua = dem_so_lan_ky_tu(chuoi)
    in_ket_qua(ket_qua)


if __name__ == "__main__":
    main()

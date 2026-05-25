import sys

sys.stdin.reconfigure(encoding="utf-8")
sys.stdout.reconfigure(encoding="utf-8")


def doi_chu_xen_ke(chuoi):
    ket_qua = ""

    for i in range(len(chuoi)):
        if i % 2 == 0:
            ket_qua = ket_qua + chuoi[i].upper()
        else:
            ket_qua = ket_qua + chuoi[i].lower()

    return ket_qua


def main():
    chuoi = input("Nhập chuỗi: ")
    print("Kết quả:", doi_chu_xen_ke(chuoi))


if __name__ == "__main__":
    main()

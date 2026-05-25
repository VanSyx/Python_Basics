import sys

sys.stdin.reconfigure(encoding="utf-8")
sys.stdout.reconfigure(encoding="utf-8")


def tim_ky_tu_nhieu_nhat(chuoi):
    ky_tu_nhieu_nhat = ""
    so_lan_nhieu_nhat = 0

    for ky_tu in chuoi:
        so_lan = chuoi.count(ky_tu)
        if so_lan > so_lan_nhieu_nhat:
            ky_tu_nhieu_nhat = ky_tu
            so_lan_nhieu_nhat = so_lan

    return ky_tu_nhieu_nhat, so_lan_nhieu_nhat


def main():
    chuoi = input("Nhập chuỗi: ")

    if chuoi == "":
        print("Chuỗi rỗng, không có ký tự để tìm.")
    else:
        ky_tu, so_lan = tim_ky_tu_nhieu_nhat(chuoi)
        print("Ký tự xuất hiện nhiều nhất:", repr(ky_tu))
        print("Số lần xuất hiện:", so_lan)


if __name__ == "__main__":
    main()

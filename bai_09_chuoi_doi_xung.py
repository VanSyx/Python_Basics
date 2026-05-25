import sys

sys.stdin.reconfigure(encoding="utf-8")
sys.stdout.reconfigure(encoding="utf-8")


def la_chuoi_doi_xung(chuoi):
    chuoi_dao_nguoc = chuoi[::-1]
    return chuoi == chuoi_dao_nguoc


def main():
    chuoi = input("Nhập chuỗi: ")

    if la_chuoi_doi_xung(chuoi):
        print("Chuỗi đối xứng.")
    else:
        print("Chuỗi không đối xứng.")


if __name__ == "__main__":
    main()

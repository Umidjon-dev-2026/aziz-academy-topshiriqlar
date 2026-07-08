books = []

while True:
    print("\n=== Kutubxona ===")
    print("1. Kitob qo'shish")
    print("2. Kitoblarni ko'rish")
    print("3. Kitobni o'chirish")
    print("4. Chiqish")

    tanlov = input("Tanlang: ")

    if tanlov == "1":
        nom = input("Kitob nomi: ")
        books.append(nom)
        print("Kitob qo'shildi.")

    elif tanlov == "2":
        if not books:
            print("Kutubxona bo'sh.")
        else:
            for i, book in enumerate(books, 1):
                print(f"{i}. {book}")

    elif tanlov == "3":
        if not books:
            print("Kutubxona bo'sh.")
        else:
            for i, book in enumerate(books, 1):
                print(f"{i}. {book}")
            n = int(input("Raqamni kiriting: "))
            if 1 <= n <= len(books):
                books.pop(n - 1)
                print("Kitob o'chirildi.")

    elif tanlov == "4":
        print("Dastur tugadi.")
        break

    else:
        print("Noto'g'ri tanlov!")
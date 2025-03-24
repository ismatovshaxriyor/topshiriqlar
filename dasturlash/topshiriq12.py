class UY_KUTUBXONASI:
    def __init__(self, name, author, year, page):
        self.name = name
        self.author = author
        self.year = year
        self.page = page

    def searching_by_author(self, author):
        if self.author.lower() == author.lower():
            print(f"{author}ning kitobi topildi: {self.name}")
            return True

    def searching_by_year(self, year):
        if self.year == year:
            print(f"{year}-yilda da chiqqan kitob: {self.name}")
            return True

kitob1 = UY_KUTUBXONASI("Sapiens: A Brief History of Humankind", "Yuval Noah Harari", 2011, 498)
kitob2 = UY_KUTUBXONASI("The Catcher in the Rye", "J.D. Salinger", 1951, 277)
kitob3 = UY_KUTUBXONASI("1984", "George Orwell", 1949, 328)

kitoblar = [kitob1, kitob2, kitob3]

while True:
    print("""1. Kitoblar haqida ma'lumot
2. Muallif bo'yicha qidirish
3. Yili bo'yicha qidirish
4. Yangi kitob qo'shish
5. Kitobni o'chirish
6. Chiqish(istalgan belgi)
""")

    choice = input("Bo'limni tanlang: ")
    print("")

    if choice == "1":
        for kitob in kitoblar:
            print(f"Kitob nomi: {kitob.name}")
            print(f"Muallifi: {kitob.author.title()}")
            print(f"Yili: {kitob.year}")
            print(f"Beti: {kitob.page}\n")

    elif choice == "2":
        count = 0
        author = input("Muallif nomini kiriting: ")
        for kitob in kitoblar:
            if kitob.searching_by_author(author) == True:
                count += 1
        if count == 0:
            print("Kitob topilmadi\n")
        print("")

    elif choice == "3":
        count = 0
        year = int(input("Yilni kiriting: "))
        for kitob in kitoblar:
            if kitob.searching_by_year(year) == True:
                count += 1
        if count == 0:
            print("Kitob topilmadi\n")
        print("")

    elif choice == "4":
        name = input("Yangi kitob nomini kiriting: ")
        author = input("Yangi kitob muallifini kiriting: ")
        year = int(input("Yangi kitob yilini kiriting: "))
        page = int(input("Yangi kitob betlar sonini kiriting: "))

        new_book = UY_KUTUBXONASI(name, author, year, page)
        kitoblar.append(new_book)
        print("\nYangi kitob qo'shildi\n")

    elif choice == "5":
        count = 0
        name = input("O'chirilayotgan kitob nomini kiriting: ")
        for kitob in kitoblar:
            if kitob.name == name:
                print(f"{name} o'chirildi\n")
                kitoblar.remove(kitob)
                count += 1
        if count == 0:
            print("Kitob topilmadi\n")
    else:
        print("Dastur yakunlandi!")
        break

students = ["SEMA NUR", "AHMET YASAR" ]



# Ogrenci Ekleme 
def add_stu():
    name = input("Eklemek istediginiz ogrencinin adini giriniz : ").upper()
    surname = input("Eklemek istediginiz ogrencinin soyadini giriniz : ").upper()
    stu =  name + " " + surname

    if stu not in students:
        students.append(stu)
        print("Ogrenci Eklendi.")
    else:
        print(stu , ", zaten listede bulunmaktadir.")         


# Ogrenci Silme
def del_stu():
    print(students)
    name = input("Silmek istediginiz ogrencinin adini giriniz : ").upper()
    surname = input("Silmek istediginiz ogrencinin soyadini giriniz : ").upper()
    stu =  name + " " + surname
    if stu in students:
        students.remove(stu)
        print("Ogrenci Silindi.")
    else:
        print(stu , ", listede bulunmamaktadir.")  

# Birden Fazla Ogrenci Ekleme
def add_multiple_stu():
    num = input("Eklenecek Ogrenci Sayisini Giriniz : ")
    i=0
    while i < int(num):
        i+=1
        name = input("Eklemek istediginiz ogrencinin adini giriniz : ").upper()
        surname = input("Eklemek istediginiz ogrencinin soyadini giriniz : ").upper()
        stu =  name + " " + surname
        if stu not in students:
            students.append(stu)
            print("Ogrenci Eklendi.")
        else:
            print(stu , ", zaten listede bulunmaktadir.")


# Birden Fazla Ogrenci Silme
def del_multiple_stu():
    num = input("Silinecek Ogrenci Sayisini Giriniz : ")
    print(students)
    for i in range(int(num)):
        name = input("Silmek istediginiz ogrencinin adini giriniz : ").upper()
        surname = input("Silmek istediginiz ogrencinin soyadini giriniz : ").upper()
        stu =  name + " " + surname
        if stu in students:
            students.remove(stu)
            print("Ogrenci Silindi.")
        else:
            print(stu , ", listede bulunmamaktadir.")


# Ogrenci Numarasi Ogrenme
def stu_num():
    name = input("Ogrencinin adini giriniz : ").upper()
    surname = input("Ogrencinin soyadini giriniz : ").upper()
    stu =  name + " " + surname
    if stu in students:
        stuNum = students.index(stu)
        print(stu , " adli pgrencinin numarasi : " , stuNum)
    else:
        print("Ogrenciye dair bilgi bulunamadi")


# Ogrenci Listesi
def stu_list():
    for i in students:
        print(i)

# Islem Secimi
while True:
    print("YAPILABILECEK ISLEMLER")
    print(" 1-Ogrenci Ekle\n 2-Ogrenci Sil\n 3-Coklu Ogrenci Ekle\n 4-Coklu Ogrenci Sil\n 5-Ogrenci Numarasi Ogrenme\n 6-Ogrenci Listesi\n 0-Programi Sonlandir")    
    select = int(input("Islemi Seciniz : "))
    if select == 1:
        add_stu()
    elif select == 2:
        del_stu()
    elif select == 3:
        add_multiple_stu()
    elif select == 4:
        del_multiple_stu()
    elif select == 5:
        stu_num()
    elif select == 6:
        stu_list()
    else:
        print("Program Sonlandi...")
        break

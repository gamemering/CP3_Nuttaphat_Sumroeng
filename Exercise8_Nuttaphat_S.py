usernameInput = input("Username :")
passwordInput = input("Password :")
if usernameInput  == "admin" and passwordInput == "1234":
    print("Login Success\n-----------------------------")
    print("    ร้าน G shop Bekery ยินดีให้บริการ    \n")
    print("             รายการสินค้า             \n")
    print("1.ขนมปังใส้ฮอตดอก   กล่องละ 50 บาท")
    print("2.เค้กกล้วยหอม      กล่องละ 30 บาท")
    print("3.ขนมปังสังขยา      กล่องละ 20 บาท")
    print("4.พายไก่           กล่องละ 40 บาท\n")
    list = int(input("ทานอะไรดีครับ :"))
    print("-----------------------------")
    if list == 1 :
        print("\nขนมปังใส้ฮอตดอก")
        amount = int(input("จำนวน(กล่อง) :"))
        result = amount * 50
        print("รวม =",result,"บาท")
        print("\nขอบคุณที่มาอุดหนุนครับ\n-----------------------------")
    elif list == 2 :
        print("\nเค้กกล้วยหอม")
        amount = int(input("จำนวน(กล่อง) :"))
        result = amount * 30
        print("รวม =", result, "บาท")
        print("\nขอบคุณที่มาอุดหนุนครับ\n-----------------------------")
    elif list == 3 :
        print("\nขนมปังสังขยา")
        amount = int(input("จำนวน(กล่อง) :"))
        result = amount * 20
        print("รวม =", result, "บาท")
        print("\nขอบคุณที่มาอุดหนุนครับ\n-----------------------------")
    elif list == 4 :
        print("\nพายไก่")
        amount = int(input("จำนวน(กล่อง) :"))
        result = amount * 40
        print("รวม =", result, "บาท")
        print("\nขอบคุณที่มาอุดหนุนครับ\n-----------------------------")
else :
    print("Wrong username or password\n-----------------------------")

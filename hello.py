print("안녕하세요 코드 txt입니다")
print("받으신 코드로 로그인해주세요")
a = int(input("1번은 로그인 2번은 추가: "))
if a == 1:
    app = input("받으신 코드는? ")
    with open("id.txt", 'r', encoding="UTF-8") as File:
        for i in File:
            if i == app:
                print(f"'{app}'에 초대되셨습니다.")
                exit()
        print("초대되지 않은 코드입니다")
elif a == 2:
    app = input("추가하실 코드는? ")
    with open('id.txt', 'a', encoding="UTF-8") as File:
        File.write("\n")
        File.write(app)
else:
    print("숫자를 다시 입력해주세요")        
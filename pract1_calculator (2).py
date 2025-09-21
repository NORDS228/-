def calculator():
    try:
        print("Что вы хотите сделать с числами? \n"
                           "1 -  Арифметические действия, 2 - Сравнение, 3 -  Логические, 4 -  Побитовые операции, 5 - Принадлежность, 6 -  Тождественность ")
        action = int(input("Введите номер необходимой операции: "))
        if action == 1:
            print("---")
            print("1 - сложение, 2 - вычитание, 3 - умножение, 4 - деление, \n"
                                          "5 - остаток от деления, 6 - целочисленное деление A на B, 7 - остаток от деления A на B, 8 - возведение A в степень B ")
            arithmetic_action = int(input("Введите номер необходимой операции: "))
            print("---")
            if arithmetic_action in range (1,8):
                a = float(input("Введите число A: "))
                b = float(input("Введите число B: "))
                if arithmetic_action == 1:
                    print(a+b)
                elif arithmetic_action == 2:
                    print(a-b)
                elif arithmetic_action == 3:
                    print(a*b)
                elif arithmetic_action == 4:
                    print(a/b)
                elif arithmetic_action == 5:
                    print(a%b)
                elif arithmetic_action == 6:
                    print(a//b)
                elif arithmetic_action == 7:
                    print(a**b)
                elif arithmetic_action == 8:
                    print(a^b)
            else:
                print("Ошибка выбора опции")
        elif action == 2: #сравнение
            print("---")
            print("1 - A равно B, 2 - A не равно B, 3 - A больше B, 4 - A меньше B, 5 - A Больше или равно B, 6 - A Меньше или равно B ")
            eval_action = int(input("Введите номер необходимой операции: "))
            print("---")
            if eval_action in range (1,7):
                a = float(input("Введите число A: "))
                b = float(input("Введите число B: "))
                if eval_action == 1:
                    print(a == b)
                elif eval_action == 2:
                    print(a != b)
                elif eval_action == 3:
                    print(a > b)
                elif eval_action == 4:
                    print(a < b)
                elif eval_action == 5:
                    print (a >= b)
                elif eval_action == 6:
                    print (a <= b)
            else:
                print("Ошибка выбора опции")
        elif action == 3: #Логические
            print("---")
            print("Выберите логическую операцию: 1 - Логическое 'И' (А and B); 2 - Логическое 'ИЛИ'(A or B), 3 - Логическое 'НЕ' (not A, not B) ")
            logical_action = int(input("Введите номер необходимой операции: "))
            print("---")
            if logical_action in range (1,4):
                a = float(input("Введите число A: "))
                b = float(input("Введите число B: "))
                if logical_action == 1:
                    print(a and b)
                elif logical_action == 2:
                    print(a or b)
                elif logical_action == 3:
                    print("Не А - ", not a,"Не B - ", not b)
            else:
                print("Ошибка выбора опции")
        elif action == 4: #Побитовые операции
            print("---")
            print("Выберите побитовую операцию: 1 - & Побитовое И (A&B); 2- | Побитовое ИЛИ (A|B); 3 - ^ Побитовое ИСКЛЮЧАЮЩЕЕ ИЛИ (A^B) \n"
                                      "4 - ~ Побитовое НЕ, 5 - << Побитовый сдвиг A влево на B, 6 - >> Побитовый сдвиг A вправо на B. ")
            binary_action = int(input("Введите номер необходимой операции: "))
            print("---")
            if binary_action in range (1,7):
                a = int(input("Введите значение A: "))
                b = int(input("Введите значение B: "))
                if binary_action == 1:
                    print (a & b)
                elif binary_action == 2:
                    print (a | b)
                elif binary_action == 3:
                    print (a ^ b)
                elif binary_action == 4:
                    print("Побитовое не a - ", ~a)
                    print("Побитовое не b - ",~ b)
                elif binary_action == 5:
                    print(a<<b)
                elif binary_action == 6:
                    print(a>>b)
            else:
                print("Ошибка выбора опции")
        elif action == 5: #Принадлежность
            print("---")
            print("Выберите операцию принадлежности: 1 - A принадлежит B, 2 - A НЕ принадлежит B, 3 - B принадлежит A, 4 - B НЕ принадлежит A ")
            affilative_action = int(input("Введите номер необходимой операции: "))
            print("---")
            if affilative_action in range (1,5):
                a = input("Введите число A: ")
                b = input("Введите число B: ")
                if affilative_action == 1:
                    print(a in b)
                elif affilative_action == 2:
                    print(a not in b)
                elif affilative_action == 3:
                    print(b in a)
                elif affilative_action == 4:
                    print(a not in b)
            else:
                print("Ошибка выбора опции")
        elif action == 6: #Тождественность
            print("---")
            print("Выберите опцию: 1 - A тождественно B, 2 - A не тождественно B ")
            identity_action = int(input("Введите номер необходимой операции: "))
            print("---")
            if identity_action in range(1,3):
                a = float(input("Введите число A: "))
                b = float(input("Введите число B: "))
                if identity_action == 1:
                    print(a is b)
                elif identity_action == 2:
                    print(a is not b)
            else:
                print("Ошибка выбора опции")
    except ZeroDivisionError:
        print("Ошибка, на ноль делить нельзя!")
    except ValueError:
        print("Ошибка значения, введите число!")
    const_dec = 1
    while const_dec !=0:
        decision = input("Желаете попробовать ещё раз? (Y/N)").lower()
        if decision == "y":
            calculator()
        elif decision == "n":
            const_dec = 0
            print("Пока!")
calculator() 
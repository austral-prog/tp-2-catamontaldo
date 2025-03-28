def change():
    expense = 23.75
    money = 100
    print("Ingresar gasto:")
    print(expense)
    print("Dinero recibido:")
    print(money)
    print("\nVuelto")
    print("\nPesos:")
    x = money - expense
    y = int(x)
    print(y)
    print("Centavos:")
    print(int((x - y)*100))
change()

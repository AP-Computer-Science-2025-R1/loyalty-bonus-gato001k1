wf=int(input("what is the weather forecast for tomorrow?: "))
rain=input("will it rain tomorrow? (y/n) : ")
if wf > 20 :
        print("Wear a cozy hoodie")
elif wf < 20 and wf >10:
        print("wear your hoodie")
        print("wear your jacket")
elif wf > 5 and wf < 10:
        print("Wear long sleeves")
        print("Wear your jacket")
        print("Wear your hoodie")
        print("Remember to wear your gloves")
        print("Wear winter pants")

else:
        print("it is very cold outside")
        print("Wear your jacket")
        print("Wear Gloves")
        print("Wear puffy socks")
        print("Wear A heavy winter jacket")
        print("Wear a Hoodie below the jacket")
        print("Wear winter pants")
        print("Bring something hot to drink")
if rain == "y":
        print("i recommend for you to wear your rain jacket")

currency = {"USD" : 81, "EUR" : 84, "INR" : 1, "Pound" : 97, "Chinese yuan" : 11, "Brazillian Real" : 15}
def convert(c1, a, c2):
    return "The currency in {} after converting into {} is {}".format(c1, c2, a * currency[c1] / currency[c2])

print("---------------------------------")
print("|   currency converter    |")
print("---------------------------------")
for i in currency.keys():
    print(i)

c1 = input("Enter the currency: ")
a = int(input("Amount: "))
c2 = input("Enter The Currency you want to convert to: ")

print(convert(c1,a,c2))
print("--Vise-Versa--".center(130," "))
print(convert(c2,a,c1))

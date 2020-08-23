number = int(input("เอากี่แถว : "))
for x in range(number):
    print(((number-x-1)*" ")+((2*x+1)*("*")))

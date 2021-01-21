import sys

a = input("Please enter any Number: ")
a = int(a)

i=2
i = int(i)

if a == 1 :
    print("thats not a prime number!")

elif a > 1:
    while i < a-1:
        i=i+1
        if a % i == 0:
            print("Thats not a prime number!")
            exit()

    print("thats a prime number")







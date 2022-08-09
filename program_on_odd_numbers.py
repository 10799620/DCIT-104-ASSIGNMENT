#Alex Teye Teye Ametepey 
#10977620
#A simple program on how to find the sum of all odd numbers less than a given number###

num = float(input("enter a number: "))
i = 0
sums = 0

while i < num:
	if i%2 == 1:
		sums += i
	i += 1

print("The sum of all odd numbers less than ",num, " is: ", sums)
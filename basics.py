# basics.py
x = input("Input a command: ")
print("You entered {}.".format(x))
if x == 'add':
		print("Add")
		a = 1
		b = 2
		print("a = {}".format(a))
		c = a + b 
		print("{} + {} = {}".format(a, b, c))
elif x == "s": #colon block
	print("subtract")
	a = 1
	b = 2
	c = a - b
	print("{} - {} = {}".format(a, b, c))
else:
	print("{} is not an active command.".format(x))

print("Done")

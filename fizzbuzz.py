# def generate(upto):
#     return "1"

def generate(upto):
	output = ""

	for number in range(1, upto +1):
		if number % 3 == 0 and number % 5 == 0:
			output += "FizzBuzz"
	
		elif (number % 3 == 0):
			output += "Fizz"
		
		elif (number % 5 == 0):
			output += "Buzz"
		
		else: 
			output += str(number)
		
		output += ", " # Adds a comma and space after each number

	return(output)


print(generate(100))
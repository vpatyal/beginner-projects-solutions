import sys


def calculate_fibonacci_number(n):
	# initialize the fibonacci sequence with first 2 numbers
	fibonacci_seq = [0, 1]

	# calculate fibonacci number at x+2 location in the fibonacci sequence
	for x in range(n):
		fibonacci_number_at_xplus2 = fibonacci_seq[x] + fibonacci_seq[x + 1]
		fibonacci_seq.append(fibonacci_number_at_xplus2)

	print("Fibonacci number at nth sequence is: {}".format(fibonacci_seq[n]))
	print("Fibonacci sequence :" + str(fibonacci_seq[0:n+1]))


def main():
	try:
		n = int(input("Enter a number n to get fibonnaci number at that sequence: "))
	except (ValueError):
		print("Not a valid number, program terminating!")
		sys.exit(99)

	calculate_fibonacci_number(n)


if __name__ == '__main__':
	main()

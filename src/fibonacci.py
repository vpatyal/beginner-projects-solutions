import sys


def calculate_fibonacci_number(n):
	# initialize the fibonacci sequence with first 2 numbers
	fibonacci_seq = [0, 1]
	for x in range(n - 2):
		xplus2_number = fibonacci_seq[x] + fibonacci_seq[x + 1]
		# print("{}, {}, {}, {}".format(x, xplus2_number, fibonacci_seq[x], fibonacci_seq[x - 1]))
		fibonacci_seq.append(xplus2_number)

	print("Fibonacci number at {0}th sequence is: {1}".format(n, fibonacci_seq[n - 1]))
	print("Fibonacci sequence :" + str(fibonacci_seq[0:n]))


def main():
	try:
		n = int(input("Enter a number to get fibonnaci number at that sequence: "))
	except (ValueError):
		print("Not a valid number, program terminating!")
		sys.exit(99)

	calculate_fibonacci_number(n)


if __name__ == '__main__':
	main()

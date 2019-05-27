import sys


def check_pythagorean_triple(a, b, c):
	x = a ** 2
	y = b ** 2
	z = c ** 2

	if (x + y) == z or (x + z) == y or (y + z) == x:
		return True
	else:
		return False


def get_user_input():
	print("\nEnter 3 numbers")
	try:
		a = int(input("First number : "))
		b = int(input("Second number : "))
		c = int(input("Third number : "))
	except (ValueError):
		print("Not a valid number, program terminating!")
		sys.exit(99)
	else:
		return a, b, c


def main():
	while True:
		a, b, c = get_user_input()
		is_pythagorean_triple = check_pythagorean_triple(a, b, c)

		if is_pythagorean_triple:
			print("{0}, {1}, {2} are pythagorean triple".format(a, b, c))
		else:
			print("{0}, {1}, {2} are not pythagorean triple".format(a, b, c))

		try_again = str(input("\n\nDo you want to try again (Y/N)? ")).upper()
		if try_again == "Y":
			pass
		else:
			break


if __name__ == '__main__':
	main()

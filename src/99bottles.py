def write_lyrics(bottles):
	if 99 >= bottles > 2:
		print("\n{0} bottles of beer on the wall, {1} bottles of beer.".format(bottles, bottles))
		print("Take one down and pass it around, {0} bottles of beer on the wall.".format(bottles - 1))
	elif bottles == 2:
		print("\n{0} bottles of beer on the wall, {1} bottles of beer.".format(bottles, bottles))
		print("Take one down and pass it around, {0} bottle of beer on the wall.".format(bottles - 1))
	elif bottles == 1:
		print("\n{0} bottle of beer on the wall, {1} bottle of beer.".format(bottles, bottles))
		print("Take one down and pass it around, no more bottles of beer on the wall.".format(bottles - 1))
	elif bottles == 0:
		buyagain = 99
		print("\nNo more bottles of beer on the wall, no more bottles of beer.")
		print("Go to the store and buy some more, {0} bottles of beer on the wall".format(buyagain))
	else:
		print("!!! Invalid input {0} !!!".format(bottles))


def main():
	beerbottles = 99

	while beerbottles >= 0:
		write_lyrics(beerbottles)
		beerbottles = beerbottles - 1


if __name__ == '__main__':
	main()

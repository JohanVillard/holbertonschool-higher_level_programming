def uppercase(str):
	up_str = ""
	for char in str:
		if "a" <= char <= "z":
			up_str += chr(ord(char) - 32)
		else:
			up_str += char

	print("{}".format(up_str))

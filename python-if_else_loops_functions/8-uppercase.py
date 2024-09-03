def uppercase(str):
    upper_str = ""
    for char in str:
        if 97 <= ord(char) <= 122:
            upper_str += chr(ord(char) - 32)
        else:
            upper_str += char

    print("{}".format(upper_str))

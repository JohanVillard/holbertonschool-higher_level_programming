def uppercase(str):
    upper_str = ""
    for idx in range(len(str)):
        if ord(str[idx]) >= 97 and ord(str[idx]) <= 122:
            upper_str += chr(ord(str[idx]) - 32)
        else:
            upper_str += chr(ord(str[idx]))

    print("{}".format(upper_str))

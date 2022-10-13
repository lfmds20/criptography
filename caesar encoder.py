import string 

flag = input("Message: ")

mytable = flag.maketrans("DEFGHIJKLMNOPQRSTUVWXYZABCdefghijklmnopqrstuvwxyzabc", "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")

print(flag.translate(mytable))
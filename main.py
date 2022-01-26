a = "nitin"

def reverse_string(a):
    temp=""
    for i in a:
        temp=i+temp
    if (temp==a):
        print("This text is a palindrome")
    else:
        print("This text is not a palindrome")
    return temp

print(reverse_string(a))

def main():
    num = int(input("Enter a number: "))
    if is_palindrome(num):
        print(f"{num} is a palindrome.")
    else:
        print(f"{num} is not a palindrome.")

def is_palindrome(num):
    number_str = str(num)
    reversed_str = number_str[::-1]
    return number_str == reversed_str
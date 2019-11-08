def isPalindrome(x: int) -> bool:
        strX = str(x)
        for i,letter in enumerate(reversed(strX)):
            if(letter != strX[i]):
                return False 
        return True

def main():
    print("Testing 123")
    print(isPalindrome(123))
    print("Testing -123")
    print(isPalindrome(-123))
    print("Testing 123321")
    print(isPalindrome(123321))

main()
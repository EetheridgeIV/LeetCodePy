def reverse(x):
    xs = str(x)
    answer = ""
    for letter in reversed(xs):
        if(letter == '-'):
            answer = letter + answer
        else:
            answer = answer + letter
    if(int(answer) > pow(2,31) - 1):
        return 0
    elif(int(answer) < -1*pow(2,31)):
        return 0
    else:
        return int(answer)

def main():
    print("Testing 123")
    print(reverse(123))

main()


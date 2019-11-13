def romanToInt(s: str) -> int:
        symbolTable = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        
        result = 0 
        
        for index,symbol in enumerate(s):
            if (symbol == "I" and (index + 1) < len(s)):
                if(s[index+1] == "V"):
                    result = -1*symbolTable[symbol] + result 
                elif(s[index+1] == "X"):
                    result = -1*symbolTable[symbol] + result 
                else:
                    result = result + symbolTable[symbol] 
            elif (symbol == "X" and (index + 1) < len(s)):
                if(s[index+1] == "L"):
                            result = -1*symbolTable[symbol] + result 
                elif(s[index+1] == "C"):
                    result = -1*symbolTable[symbol] + result 
                else:
                    result = result + symbolTable[symbol] 
            elif (symbol == "C" and (index + 1) < len(s)):
                if(s[index+1] == "D"):
                            result = -1*symbolTable[symbol] + result
                elif(s[index+1] == "M"):
                    result = -1*symbolTable[symbol] + result
                else:
                    result = result + symbolTable[symbol] 
            else:
                result = result + symbolTable[symbol]
        return result

def main():
    print("Testing IV")
    print(romanToInt("IV"))
    print("Testing MCMXCIV")
    print(romanToInt("MCMXCIV"))

main()
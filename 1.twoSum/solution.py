def twosum(nums, target):
    complements = {}
    for index, number in enumerate(nums):
        complement = target - number

        if complement in complements:
            return [complements[complement], index]
        else:
            complements[number] = index

def main():
    print(twosum([2, 7, 11, 15], 9))

main()

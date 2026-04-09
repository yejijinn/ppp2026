def average(nums):
    average = sum(nums)/len(nums)
    print(average)
    return(average)

def main():
    nums = (input("숫자를 입력해주세요.(띄어쓰기로 입력해주세요. (ex)1 2 3 4 5 )= "))
    long = nums.split()

    numbers = []
    for i in long:
        numbers.append(int(i))
    average(numbers)
    print(numbers)

if __name__ == '__main__':
    main()
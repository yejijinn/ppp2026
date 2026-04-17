def text2list(text):
    text.split() 
    num_list = []
    for num_text in text.split(): 
        num_list.append(int(num_text))
    #print(num_list)
    return num_list

def count_list(nums):
    return len(nums)

def average_list(nums):
    return sum(nums) / len(nums)

def max_list(nums):
    return max(nums)

def min_list(nums):
    return min(nums)

def middle_list(nums):
    return sorted(nums) [len(nums)//2]

def read_text(filename):
    with open(filename) as f:   #f=open(filenamme)
        text=f.readline()
    #print(f"!{text}")
    return text

def main ():
    input_text = read_text("lec/lec07/hw10/numbers_hw_1.txt")
    #input_text = "5,10,3,4,7"
    nums = text2list(input_text)
    print ("주어진 리스트는 = ",nums)
    print (f"총 숫자의 개수는 = {count_list(nums)}")
    print (f"주어진 숫자의 평균은 = {average_list(nums)}")
    print (f"숫자의 최대값은 = {max_list(nums)}")
    print (f"숫자의 최소값은= {min_list(nums)}")
    print (f"숫자의 중앙값은= {middle_list(nums)}")

if __name__=="__main__":
    main()
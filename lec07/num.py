def text2list(text):
    text.split() 
    num_list = []
    for num_text in text.split(): 
        num_list.append(int(num_text))
    print(num_list)

    num_list = [int(x) for x in text.split()] #지능형 리스트 -> 위에 4줄과 똑같음
    print(num_list)
    return num_list

def average_list(nums):
    return sum(nums) / len(nums)

def read_text(filename):
    with open(filename) as f:   #f=open(filenamme)
        text=f.readline()
    print(f"!{text}")
    return text

def main ():
    input_text = read_text("lec/lec07/numbers_1.txt")
    #input_text = "5,10,3,4,7"
    nums = text2list(input_text)
    print ("주어진 리스트는 ",nums)
    print (average_list(nums))

if __name__=="__main__":
    main()
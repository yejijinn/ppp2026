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

def read_num_list(filename):
    num_list=[]
    with open(filename) as f:   #f=open(filenamme)
        lines=f.readlines() #readlines s 붙임   
        for line in lines :
            #num_list.append(int(line.strip()))
            num_list.extend([int(x) for x in line.split()])
    return num_list

def main ():
    nums = read_num_list("lec/lec08/numbers_1.txt") #input_text = "5,10,3,4,7"
    print ("주어진 리스트는 ",nums)
    print (average_list(nums))

if __name__=="__main__":
    main()
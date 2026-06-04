import random

def gugudan_correct():
    a= random.randint(2,9)
    b= random.randint(2,9)
    ans = input (f"{a} x {b} =>>>?")
    return int(ans) == a*b

def main():
    # while True:
    count = 0
    score = 0
    for i in range (10):
        if gugudan_correct():
            score+=10
            count+=1
    print(f"정답을 맞힌 개수는 {count}개, {score}점 입니다.")

if __name__=="__main__":
    main()
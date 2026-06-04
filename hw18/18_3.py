import random
# words = {"사과":"ㅅㄱ","수박":"ㅅㅂ","복숭아":"ㅂㅅㅇ","딸기":"ㄸㄱ","포도":"ㅍㄷ","체리":"ㅊㄹ"}
# key = 사과 / value = ㅅㄱ
words = {"ㅅㄱ":"사과","ㅅㅂ":"수박","ㅂㅅㅇ":"복숭아","ㄸㄱ":"딸기","ㅍㄷ":"포도","ㅊㄹ":"체리"}
# key = ㅅㄱ / value = 사과


def correct(quiz):
    answer = input(f"과일중에 {quiz}에 맞는 과일을 적어주세요 = ")
    
    if answer == words[quiz]:
        print ("정답입니다!")
    
    else:
        print("오답입니다!")

    return answer
        

def main():
    # words = {"사과":"ㅅㄱ","수박":"ㅅㅂ","복숭아":"ㅂㅅㅇ","딸기":"ㄸㄱ","포도":"ㅍㄷ","체리":"ㅊㄹ"}
    # print("=========", list(words.values()))
    quiz = random.choice(list(words.keys())) 
    answer = correct(quiz)

if __name__=="__main__":
    main()
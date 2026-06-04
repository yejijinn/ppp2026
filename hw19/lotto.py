import random

def random_number(rotate):
    #n =random.randint(1,45)

    for n in range(int(rotate)):
        number = random.sample(range(1,46),6)

    print(f"로또번호 입니다. = {number}")


def main():
    rotate = input(f"반복을 원하시는 횟수를 알려주세요. = ")
    random_number(rotate)
if __name__=="__main__":
    main()
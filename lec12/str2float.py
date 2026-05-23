def str2float(text: str, default_value: float = -999): #:은 str만 받겠다는 뜻 / 값을 전달받지 않으면 999사용
    try: #안 부분 실횅 -> 오류 -> except부분 실행
        return float(text)
    except ValueError:
        return default_value


def main():
    # input_str = "123"
    retsult = str2float("apple")
    print(retsult)

if __name__=="__main__":
    main()
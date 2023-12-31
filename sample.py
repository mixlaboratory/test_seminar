import os
import random
from math import gcd

#ヌメロン用
num=[0,1,2,3,4,5,6,7,8,9]
ans=random.sample(num,3)
answer=[]
count=0

#文字列を反転する
def reverse_string(input_str):
    return input_str[::-1]
    
#文字列を大文字にする
def capitalize_string(input_str):
    return input_str.capitalize()

#数字を計算して結果を返す
def shiki(x, y, z):
    intx = int(x)
    inty = int(y)
    intz = int(z)

    w = intx * inty
    w = w - intz
    return w

#フィボナッチ数列の計算
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib = [0, 1]
        for i in range(2, n):
            fib.append(fib[i-1] + fib[i-2])
        return fib

#分数の計算（山口幹太）    
class Fraction:
    def __init__(self, array):
        self.array = array
        self.numerator = array[0]
        self.denominator = array[1]
    #分数の足し算
    def plus(self, other):
        result_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        result_denominator = self.denominator * other.denominator
        return Fraction([result_numerator, result_denominator])
    #分数の約分
    def reduction(self):
        common_divisor = gcd(self.numerator, self.denominator)
        self.numerator //= common_divisor
        self.denominator //= common_divisor
        return self
    #分数の表示
    def display(self):
        print(f"{self.numerator}/{self.denominator}")



#メイン関数
if __name__ == "__main__":
    text = input("Enter a string: ")
	
    reversed_text = reverse_string(text)
    capitalized_text = capitalize_string(text)

    print("Reversed:", reversed_text)
    print("Capitalized:", capitalized_text)
    
    print("hoge")
    print("Ooi")
    
    #高梨美雪(好きな数字(整数)を3つ入力し、結果をprintする)
    a = input("put number1: ")
    b = input("put number2: ")
    c = input("put number3: ")
    k = shiki(a,b,c)
    print("結果：", k)

    #丸本啓太ヌメロン
    print("3桁の数字を当てるヌメロン\n")
    print("値と桁があってるとEAT 値だけ合っているとBITE\n")
    print("チャンスは3回")
    while True:
        while True:
            print("ヌメロン"+str(count)+"回目の挑戦")
            a=input("3桁の異なる数字を入力>>\n")

            for i in range(3):
                answer.append(int(a[i]))
            
            if a[0]==a[1]==a[2]:
                print("異なる数字を入力してね\n")
                answer.clear()
            elif a[0]==a[1] or a[0]==a[2] or a[1]==a[2]:
                print("異なる数字を入力してね\n")
                answer.clear()
            else:
                break

        EAT=0
        BITE=0

        for i in range(3):
            if answer[i]==ans[i]:
                EAT+=1
            elif answer[i] in ans:
                BITE+=1
            else:
                pass
        print(str(answer)+" 判定:"+str(EAT)+"EAT,"+str(BITE)+"BITE\n")
        answer.clear()
        
        if EAT==3:
            print("正解！")
            break
        elif count==3:
            print("失敗")
            break
        else:
            count+=1

    #荒木沙紀フィボナッチ数列
    n = 10  # 長さの指定
    print(fibonacci(n))  

    #朝田青葉プリント
    print("朝田青葉")

    #山口幹太（分数の足し算（約分付き））
    #分数1（fraction1）
    numerator1 = int(input("分数 1 の分子を入力してください: "))
    denominator1 = int(input("分数 1 (ゼロ以外) の分母を入力してください: "))
    fraction1 = Fraction([numerator1, denominator1])
    #分数2（fraction2）
    numerator2 = int(input("分数 2 の分子を入力してください: "))
    denominator2 = int(input("分数 2 (ゼロ以外) の分母を入力してください: "))
    fraction2 = Fraction([numerator2, denominator2])
    #結果（result）
    result = fraction1.plus(fraction2).reduction().display()

    #相原惟人（足し算）


    # ユーザーに数値を入力してもらう
    num1 = float(input("最初の数を入力してください: "))
    num2 = float(input("次の数を入力してください: "))

   # 足し算を行う
    result = num1 + num2

   # 結果を表示する 
   print("結果: {} + {} = {}".format(num1, num2, result))



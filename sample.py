import os

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
    
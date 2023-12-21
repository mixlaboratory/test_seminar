import os

#文字列を削除する
def reverse_string(input_str):
    return input_str[::-1]
    
#文字列を大文字にする
def capitalize_string(input_str):
    return input_str.capitalize()

#メイン関数
if __name__ == "__main__":
    text = input("Enter a string: ")
	
    reversed_text = reverse_string(text)
    capitalized_text = capitalize_string(text)

    print("Reversed:", reversed_text)
    print("Capitalized:", capitalized_text)
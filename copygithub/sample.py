import os

#文字列を反転する
def reverse_string(input_str):
    return input_str[::-1]
    
#文字列を大文字にする
def capitalize_string(input_str):
    return input_str.capitalize()

# 名前を出力する関数
def output_name(name):
    print("Genimai:", name)

# ディレクトリを作成し、画像データを格納する関数
def create_directory_and_store_data():
    directory_path = "my_data"
    os.makedirs(directory_path, exist_ok=True)

    # 画像データを作成または取得してディレクトリに格納する処理
    image_data = ""
    image_file_path = os.path.join(directory_path, ".txt")

    with open(image_file_path, "w") as file:
        file.write(image_data)

#メイン関数
if __name__ == "__main__":
    text = input("Enter a string: ")
	
    reversed_text = reverse_string(text)
    capitalized_text = capitalize_string(text)

    

    print("Reversed:", reversed_text)
    print("Capitalized:", capitalized_text)

    # 新しい関数を呼び出し、ディレクトリを作成し画像データを格納する
    create_directory_and_store_data()
    
    print("hoge")
    print("Ooi")
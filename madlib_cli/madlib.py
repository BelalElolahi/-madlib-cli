


def read_template(path) : 
   with open(path,'r') as f : 
      content = f.read()
   return content  

def parse_template(contents) :
    parsed_contents = "" 
    parsed_words = []
    in_brackets = False 
    temp_word_string = ""

    num_brackets = contents.count('{') + contents.count('}')
    if (num_brackets > 0 and num_brackets % 2 == 0):
       
            for char in contents:
                if char == '{':
                    parsed_contents += char
                    in_brackets = True
                elif char == '}':
                    parsed_contents += char
                    in_brackets = False
                    parsed_words.append(temp_word_string)
                    temp_word_string = ""
                elif in_brackets:
                    temp_word_string += char
                else:
                    parsed_contents += char
    else:
        raise Exception("Incorrect template format")
    
    return (parsed_contents, tuple(parsed_words))

def merge(parsed_contents, responses):
    return parsed_contents.format(*responses)

def write_file_contents(path, content):
    with open(path, 'wb') as f:
        f.write(content)

def wellcom_message():
    print ( """
**************************************
**    Welcome to the MadLib cli!   **
**               ^_^               **
**************************************
""")  
    print("follow the instrcutions\n")

def  get_response (words) :
    responses =[]
    for word in  words :
        response = input('enter ' +str(word) +':')
        responses.append(response)
    return responses  
        

def creat_madlib():
    
    file = read_template("assets/dark_and_stormy_night_template.txt")
    parsed_string, contents = parse_template(file)

    
    wellcom_message()

    user_words = []


    user_words = get_response(contents)

    completed_madlib = merge(parsed_string, user_words)

    print("Thanks!  See your completed Madlib :\n")
    print(completed_madlib + "\n")

    write_file_contents("assets/missing.txt", completed_madlib.encode())


if __name__ == "__main__":
    creat_madlib()
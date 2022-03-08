import re

def read_template(file_path:str)->str:

 try:
    
    with open (file_path) as file:
        content=file.read()
    return content.strip()
 except FileNotFoundError:
     raise(FileNotFoundError)

def parse_template(word:str)->str:

 part=re.findall(r'{(.*?)}',word)

 stripped=re.sub('{.*?}','{}',word)

 return stripped,tuple(part)

def merge(string:str,word_to_add:tuple)->str :
   
    updatedText=string.format(*word_to_add)

    with open('assets/GameAnswer.txt','w') as output:
        output.write(updatedText)
    return updatedText

input_list=[]
def gameStart():
   
    print("""
     Welcome To MADLIB Game 
    """)

    all_contant=read_template('assets/Game.txt')
    text_body,list_of_words=parse_template(all_contant)

    for i in list_of_words:
         user_input=input(f'Enter a {i} ')
         input_list.append(user_input)

    return merge(text_body,tuple(input_list))
    
if __name__=="__main__":
  print(gameStart())
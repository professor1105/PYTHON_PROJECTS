import random
import string
coding=input("1 for coding and any number for decoding ")
coding=True if (coding=="1")  else False
st=input("Enter messages: ")
words=st.split()
def generate_letters():
    letters=string.ascii_lowercase
    word="".join(random.choice(letters)for i in range(3))
    return word
if (coding):
    newwords=[]
    for word in words:
        if(len(word)>=3):
           
            r=generate_letters()
            stnew=r + word[1:] + word[0] + r
            newwords.append(stnew)
        else:
            newwords.append(word[::-1])
    print(" ".join(newwords))
else:
    newwords=[]
    for word in words:
        if(len(word)>3):
            stnew=word[3:-3]
            stnew=stnew[-1]+stnew[:-1]
            newwords.append(stnew)
        else:
            newwords.append(word[::-1])
    print(" ".join(newwords))      
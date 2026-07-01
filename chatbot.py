import datetime
import time
name=input("Enter your name for personalized experience:")
present_time = datetime.datetime.now().hour
if 5<=present_time < 12:
    print("\t"," ","Good Morning",name)
elif 12<=present_time < 17:
    print("\t"," ","Good Afternoon",name)
elif 17<=present_time < 20:
    print("\t"," ","Good Evening",name)
else:
    print("\t"," ","Good Night",name) 
time.sleep(1)
print("\t")

print("\t","\t","welcome To")

print("\t","===RULE BASED CHATBOT===","\n")
time.sleep(2)
print("Here are some instructions:")
print("1.To see current memory of bot type (view)")
print("2.It can only answer the questions which is stored in the memory of bot")
print("3.currently don't do maths","\n")
print(" <<You can Type (modify) to train this chatbot by adding your own question and answers>>","\n")
time.sleep(2)
d1={"hello": "hlo! what's up?",
    "see you later": "ttyl! l8r",
       "oh my god": "omg! no way",
     "by the way": "btw! just so u know",
       "who are you": "an AI! ur digital helper",
     "what you can also do for me": "I am a rule based chatbot only so I can only give answer to the question which are set in my code",
}
file=open("op.txt","r")
for line in file:
    line=line.strip()
    key, value=line.split(":",1)
    d1[key]=value
file.close()


def op(parameter):
    parameter=parameter.lower()
    for el in d1:
        if(el in parameter):
            return d1[el]
      
    else:    
        return"I don't know it yet "

while True:
    inpt=input("Enter your Question:")
    inpt=inpt.lower()
    
    print("Bot is thinking...")
    time.sleep(1)
    if(inpt=="view"):
        print(d1)
        continue
    if(inpt=="modify"):
    
        print("NOW U CAN ADD YOUR DATA IN MEMORY OF BOT","\n")
        key=input("enter urs question:")
        value=input("enter ur answer:")
        d1[key]=value
        
        print("Data u provided is added successfully")

        file=open("op.txt","a")
        file.write(f"{key}:{value}\n")
        file.close()
        continue

    
    elif(inpt=="bye"):
        print("Bye Take care!!!!",name)
        break
    
    result=op(inpt)
    print("Bot Reply=",result)   
Questions=[["The International Literacy Day is observed on?" ,'Sep 8','Nov 28','May 2','Sep 22',4],
            ["What is the capital of India?" ,"Delhi", "Mumbai", "Kolkata", "Chennai",1],
            ["Which planet is known as the Red Planet?","Jupiter", "Venus", "Mars", "Saturn",3], 
            ["Who painted the Mona Lisa?" ,"Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet",3],
            ["which language is used to create facebook?","python" , "french", "javascript", "php",4],
            ["which city  is capital of india ?","pune","delhi","mumbai","aurangabad","nagpur",2],
            ["who is current prime minister of india ?","fadanvis","nehru","modi","gandhi","baneerjee",3],
            ["who was brother of lord rama?","pandvas","laxman","arjun","duryodhan",2]
            ["who is owner of jaguar ?","ratan tata","ambani","adani","musk",1],
            ["what is the capital of bihar?" ,'patna','vhubaneswar','kolkata','kerla',1]]
levels = [1000, 10000, 20000, 40000, 80000, 160000, 320000,10000000,35000000,70000000]
money = 0
for i in range(0,len(Questions)):
    print(f"{levels[i]} ruppe ke liye prosna ye app ke computer screen me")
    Question=Questions[i]
    print(f"{Question[0]}")
    print(f'a.{Question[1]}               b.{Question[2]}')
    print(f'c.{Question[3]}               d.{Question[4]}')
    print("NOTE:- 1 se 4 ke under jabab dena hay or koi bhi jabab diya to disqualify ho jaoge app")
    x=int(input("Apka Uttar: "))
    if (x== 0):
        money = levels[i-1]
        break
    if (x==Question[-1]):
        print(f"Sehi jabab app jit jate ho {levels[i]} Rupees")
        if(1==3):
         money=10000
        elif(i== 6):
         money=320000
        elif(i== 10):
         money=10000000
        elif(i== 12):
         money=35000000
        elif(i== 14):
         money=70000000
        print(f"7 CRORE!!! congratulations")
    else:
        print("WORNG ANSWER!!")
        break
print(f"take home money is {money}")
print("better luck next time... Numashkar bhen o aur bhai o")
print("Yehi khatam hota hay ye show Kun Banega CROREOATI")    
              
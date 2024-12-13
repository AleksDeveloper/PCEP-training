email = "alejandro@gmail.com"
concat = ""
for i in email:
    if(i != "@"):
        print(i)
        concat += i
    else:
        print(concat)
        break

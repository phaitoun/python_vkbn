table = ['study math online','learn English online','learn Thai online',
         'study science online','read test preparation o-net','do housework',
         'learn to draw','learn to sing']
study = input("subject : ")
table.remove(study)
print("There is still", (len(table)) ,"things to do")
for i in range(len(table)):
    print((str(i+1))+ '.'+ table[i])


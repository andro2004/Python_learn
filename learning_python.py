#print function:
##print("Your learning path:\n\tPython basics\n\tData eng\n\tAI")

#date = "30/9/2004"
#print(date.replace("/","-"))
#print(date )

#word = "Andro"
#print(word[0:2]*3)
#print(word[-5:-3])
#print(word[2:])
#print(word[0:5:2])

word  = "986-Maria, (D@t@ Engineer );; 27y  "
word = word.strip()
word = word.replace("@","a").replace(";","").replace("(","").replace(")","")
word = word[4:]
word = word.replace(","," ")
word = word.split()
print(f"""Name: {word[0]}
Role: {word[1]+" "+word[2]}
Age: {word[3].replace("y","")}""")
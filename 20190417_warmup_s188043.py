goingbad = open("morningfileread.txt")
word = ""
trailingwords = ""
bigstring = ""
trailingwordscounter = 0
answer = []
charcounter = 0

test = goingbad.readlines()
test2= (2,"stuff")
for line in test:
    bigstring += line
while charcounter < len(bigstring):
    char = bigstring[charcounter]
    word+=char
    if char == '\'':
        charcounter+=2
        continue
    if char == ' ':
        if word == "like":
            charcounter+=1
            j= 0
            while j <=3:
                trailingwords += bigstring[charcounter]
                if (bigstring[charcounter] == " "):
                    j+=1
            trailingwordscounter+=1
            answer.append((trailingwordscounter,(word + trailingwords)))
        else:
            word = ""
    charcounter +=1

print (answer)
if name=="main";

text = open("INPUT.txt", "r")
text = text.read().replace(" ","")

print(text)
N = int(text[0])

text1 = text[1:N]+text[N+1]
print(text1)

file = open("OUTPUT.TXT", "w")
file.write(text1)

file.close()
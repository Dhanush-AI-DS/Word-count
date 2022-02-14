## DEVELOPED BY: S.Dhanush
## REFERENCE NUMBER: 21004324
num_words =0
file1 = open("text.txt", "r")
print(file1.read())

with open('text.txt','r') as file1:
    for i in file1:
        word =i.split()
        num_words += len(word)
print("Number of words={}".format(num_words))
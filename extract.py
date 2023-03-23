import csv
import bleach

str = "I am a highly intelligent question answering bot. If you ask me a question that is rooted in truth, I will give you the answer. If you ask me a question that is nonsense, trickery, or has no clear answer, I will respond with 'Sorry I dont know , Ill pass you to an agent'. \n"

with open("data.csv") as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        striped0 = bleach.clean(row[0])
        striped1 = bleach.clean(row[1])
        str = str + f"\nQ: {striped0}\nA: {striped1}"
str = str + f"\nQ: [INPUT]\nA: "
print(str)

import pandas

car = pandas.read_csv("nato_phonetic_alphabet.csv")
lar = {row.letter:row.code for (index,row) in car.iterrows()}

fafef = input().upper()

c = [lar[i] for i in fafef]
print(c)
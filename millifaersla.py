fees = []
person = ["Monnei", "Fjee", "Dolladollabilljoll"]
for i in range(3):
    fee = int(input())
    fees.append(fee)
    
print(person[fees.index(min(fees))])


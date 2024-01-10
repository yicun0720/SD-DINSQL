import json
import random

with open("dev.json", "r") as file:
    data = json.load(file)

result = []

wrong_nlq = []

with open('wrong_nlq.txt') as f:
    for line in f:
        wrong_nlq.append(line.strip())

i = 0
for row in data:
    if wrong_nlq.count(row['question']) != 0:
        i += 1
        result.append(row)

random.shuffle(result)
with open("wrong.json", "w") as file:
    json.dump(result, file)
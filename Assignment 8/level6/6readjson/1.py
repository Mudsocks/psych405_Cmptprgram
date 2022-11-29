import pandas as pd #shorten name for ease of reference

#load the imported data as a variable (df)
df = pd.read_json('data.json')
sum = 0
valid_ans = []
for i in enumerate(df.values[3]):
    print(i[1])
    if i[1] == 1:
        valid_ans.append(i[0])
    #sum += i[1]

print(valid_ans)

for i in enumerate(valid_ans):
    print(i[0])
    print(df.values[2][i[0]])
    sum += df.values[2][i[0]]

mean = sum / len(df.values)

print(mean)
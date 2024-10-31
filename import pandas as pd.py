import pandas as pd

data ={
    'Ism':['Asliddin','Abbos','Komron','Sardor','Kozim','Farhod','Laziz','Azam','Qosim','Akmal'],
    'Yoshi':[18,19,23,17,21,19,20,34,12,25],
    'Shahar':['Qashqadaryo','Andijon','Fargona','Qashqadaryo','Samarqand','Qashqadaryo','Fargona','Namangan','Andijon','Qashqadaryo']
 }
df = pd.DataFrame(data)

print(df)

young_people = df[df['Yoshi'] < 20]
print("20 yoshdan kichik talabalar:\n", young_people)

df['Yoshi'] += 1
print("Yangilangan DataFrame:\n", df)

shahar_t = df[df['Shahar'] == 'Qashqadaryo']
print("Qashqadaryolik talabalar:\n",shahar_t)
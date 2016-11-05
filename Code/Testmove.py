import json


def bubble_sort(data):
    for i in range(0,len(data)):
        for j in range(i+1,len(data)):
            if data[i]['Time']<data[j]['Time']:
                data[i],data[j]=data[j],data[i]


f=open('data_file.txt','r')
score_data=json.load(f)
f.close()

bubble_sort(score_data)
print('[RANKING]')
for score in score_data:
    print("Time:%4.1f"%(score['Time']))
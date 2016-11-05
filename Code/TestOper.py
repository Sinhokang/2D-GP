import json


f=open('data_file.txt','r')
score_data=json.load(f)
f.close()

score_data.append({"Time:":33.3})
print(score_data)

f=open('data_file.txt','w')
json.dump(score_data,f)
f.close()
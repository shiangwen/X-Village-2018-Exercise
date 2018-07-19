'''
要求1: 把用 "requests 模組" 得到的 JSON 資料寫到 檔案1裡 (檔名為: music_show.json)

要求2: 把所有表演的資料裡面的 

title(活動名稱)、startDate(活動起始日期)、endDate(活動結束日期) 

寫到檔案2裡面 (檔名為: music_show.txt)
且每一行格式為 title : startDate ~ endDate
'''
import json
import requests

url = 'https://cloud.culture.tw/frontsite/trans/SearchShowAction.do?method=doFindTypeJ&category=5'
response = requests.get(url)
response.encoding = 'utf-8' 


f = open('music_show.json', 'w')
f.write(response.text) 
f.close()

g = open('music_show.json', 'r')
data=json.load(g)
print(type(data))
print(data[1]['title'])

with open('music_show.txt','w')as h:

    #data是list
    #write只能寫str
    #h.write(str(data[0]))
    for i in range (len(data)):
        h.write(str(data[i]['title'])+str(':')+str(data[i]['startDate'])+'~'+str(data[i]['endDate'])+'\n')
    #data[0]['title']['startDate']+data[0]['title']['endDate'] 看清楚目錄
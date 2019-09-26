# import browserhistory as bh
# import pandas as pd
# # d = bh.get_browserhistory()
# # bh.write_browserhistory_csv()
# # print(d['chrome'][0][2])
# name=['url','search','datetime']
# data = pd.read_csv('chrome_history.csv',names=name)
# print(data.head())

# from firebase import firebase
# fbconn = firebase.FirebaseApplication('https://hackathon-db1.firebaseio.com/',None)
# while True:
#     temp = input("Enter Your name: ")
#     data_to_upload = {
#         'name':temp
#     }
#     result = fbconn.post('/User/',data_to_upload)
#     print(result)

from firebase import firebase

config = {
  "apiKey": "AIzaSyDWvV7pCfkVCs__kTAm3Cgu7HRTDKJnSVg",
  "authDomain": "hackathon-db1.firebaseapp.com",
  "databaseURL": "https://hackathon-db1.firebaseio.com",
  "storageBucket": "hackathon-db1.appspot.com",
  "serviceAccount": "hackathon-db2-cb5b619d453f.json"
}

firebase = firebase(config)

print("test")

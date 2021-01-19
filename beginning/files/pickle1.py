import pickle

file = open('pickle1.pkl', 'wb')

obj = {'snowflake': 6, 'triangle': 3,
       'ultraSuperUberSensitivePasswordFromSecLists': 'dolphin'}

pickle.dump(obj, file)

import pandas as pd
import psycopg2 


# X = pd.read_csv('/Users/yunselee/Desktop/project/data/Features.csv')
# y = pd.read_csv('/Users/yunselee/Desktop/project/data/Targets.csv')#
# X = X[['OverallQual','GrLivArea','GarageCars']]
# data = pd.concat([X,y],axis = 1)
# data.to_csv('/Users/yunselee/Desktop/project/data/FeaturesTarget.csv',index=False)





conn = psycopg2.connect(
host="ec2-100-24-169-249.compute-1.amazonaws.com",
port='5432',
database="d8babgb8sm5aaj",
user="mmbtcqanwwdyuq",
password="71c9c6ae2951ac89098a3bdd2349b913b68ddb431a89092ec832a00e9aa04661")

#커서 생성
cur =conn.cursor()

#테이블이 이미 존재하는 경우 삭제
cur.execute("DROP TABLE IF EXISTS Price_pred_data")

cur.execute('''create table Price_pred_data(
    OverallQual INT,
    GrLivArea INT,
    GarageCars INT,
    SalePrice INT
)
''')

with open('/Users/yunselee/Desktop/project/data/FeaturesTarget.csv','r') as f:
    next(f)
    cur.copy_from(f,'Price_pred_data',sep=',',null='NA') # 포스트그레는 null로 인식해줘야 됨.

conn.commit()









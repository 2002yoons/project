import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore') 

train = pd.read_csv('/Users/yunselee/Desktop/project/data/train.csv')
#Id 특성 제거
train_id = train['Id']
del train['Id']

#이상치 제거
train1 = train.copy()
train1 = train1.drop(train1[(train1['GarageArea']>1200) & (train1['SalePrice']<300000)].index)
train1 = train1.drop(train1[(train1['GrLivArea']>4000) & (train1['SalePrice']<300000)].index)
train1 = train1.drop(train1[(train1['TotalBsmtSF']>5000)].index)

# 피쳐와 타겟 분리
X = train1.drop('SalePrice', axis=1)
y = train1['SalePrice'].to_frame()

df= train1

#결측치 처리

df['PoolQC'] = df['PoolQC'].fillna('None')
df['MiscFeature'] = df['MiscFeature'].fillna('None')
df['Alley'] = df['Alley'].fillna('None')
df['Fence'] = df['Fence'].fillna('None')
df['FireplaceQu'] = df['FireplaceQu'].fillna('None')
df['LotFrontage'] = df.groupby('Neighborhood')['LotFrontage'].transform(lambda i: i.fillna(i.median()))
#garage가 포함된 특성 살펴보기
garage_cols = [col for col in df if col.startswith('Garage')]
df[garage_cols]
# 숫자형 특성 0으로 대체:
for i in df[garage_cols].select_dtypes(exclude='object').columns:
    df[i] = df[i].fillna(0)
# 카테고리형 특성 None으로 대체:
for i in df[garage_cols].select_dtypes(include='object').columns:
    df[i] = df[i].fillna('None')
#bsmt가 포함된 특성 살펴보기
bsmt_cols = [col for col in df if col.startswith('Bsmt')]
# 숫자형 특성 0으로 대체:
for i in df[bsmt_cols].select_dtypes(exclude='object').columns:
    df[i] = df[i].fillna(0)
# 카테고리형 특성 None으로 대체:
for i in df[bsmt_cols].select_dtypes(include='object').columns:
    df[i] = df[i].fillna('None')
#mas가 포함된 특성 살펴보기
mas_cols = [col for col in df if col.startswith('Mas')]
# 숫자형 특성 0으로 대체:
for i in df[mas_cols].select_dtypes(exclude='object').columns:
    df[i] = df[i].fillna(0)
# 카테고리형 특성 None으로 대체:
for i in df[mas_cols].select_dtypes(include='object').columns:
    df[i] = df[i].fillna('None')
df['MSZoning'] = df.groupby('Neighborhood')['MSZoning'].transform(lambda i: i.fillna(i.value_counts().index[0]))
df = df.fillna(df.mode().iloc[0])

#데이터 타입 변환
df['MSSubClass'] = df['MSSubClass'].astype(str)
df['MoSold'] = df['MoSold'].astype(str)           
df['YrSold'] = df['YrSold'].astype(str)  
#특성 공학
df['Total_House_SF'] = df['TotalBsmtSF'] + df['FirstFlrSF'] + df['SecondFlrSF']
df['Total_Home_Quality'] = (df['OverallQual'] + df['OverallCond'])/2
df['Total_Bathrooms'] = (df['FullBath'] + (0.5 * df['HalfBath']) + df['BsmtFullBath'] + (0.5 * df['BsmtHalfBath']))

# 특성 정규화

# numeric_cols = df.select_dtypes(exclude='object').columns
# skew_limit = 0.5
# skew_vals = df[numeric_cols].skew()
# skew_cols = (skew_vals
#              .sort_values(ascending=False)
#              .to_frame()
#              .rename(columns={0:'Skew'})
#              .query('abs(Skew) > {0}'.format(skew_limit)))
# for col in skew_cols.index:
#     df[col] = boxcox1p(df[col], boxcox_normmax(df[col] + 1))

# 타겟 정규화
# y["SalePrice"] = np.log1p(y["SalePrice"])    

#카테고리컬 데이터 원핫 인코딩 적용
categ_cols = df.dtypes[df.dtypes == np.object]        
categ_cols = categ_cols.index.tolist()                
df_enc = pd.get_dummies(df, columns=categ_cols, drop_first=True)   

X=df_enc

X.to_csv('/Users/yunselee/Desktop/project/data/Features.csv',index=False)
y.to_csv('/Users/yunselee/Desktop/project/data/Targets.csv',index=False)

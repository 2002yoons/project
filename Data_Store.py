import psycopg2 


#포스트그레 연결
conn = psycopg2.connect(
host="localhost",
port='5432',
database="postgres",
user="postgres",
password="0928")

#커서 생성
cur =conn.cursor()

#테이블이 이미 존재하는 경우 삭제
cur.execute("DROP TABLE IF EXISTS prices_train")

#테이블 생성
cur.execute('''create table prices_train(
    Id INT PRIMARY KEY NOT NULL, 
    MSSubClass INT,
    MSZoning VARCHAR(32),
    LotFrontage FLOAT,
    LotArea INT,
    Street VARCHAR(32),
    Alley VARCHAR(32),
    LotShape VARCHAR(32),
    LandContour VARCHAR(32),
    Utilities VARCHAR(32),
    LotConfig VARCHAR(32),
    LandSlope VARCHAR(32),
    Neighborhood VARCHAR(32),
    Condition1 VARCHAR(32),
    Condition2 VARCHAR(32),
    BldgType VARCHAR(32),
    HouseStyle VARCHAR(32),
    OverallQual INT,
    OverallCond INT,
    YearBuilt INT,
    YearRemodAdd INT,
    RoofStyle VARCHAR(32),
    RoofMatl VARCHAR(32),
    Exterior1st VARCHAR(32),
    Exterior2nd VARCHAR(32),
    MasVnrType VARCHAR(32),
    MasVnrArea FLOAT,
    ExterQual VARCHAR(32),
    ExterCond VARCHAR(32),
    Foundation VARCHAR(32),
    BsmtQual VARCHAR(32),
    BsmtCond VARCHAR(32),
    BsmtExposure VARCHAR(32),
    BsmtFinType1 VARCHAR(32),
    BsmtFinSF1 INT,
    BsmtFinType2 VARCHAR(32),
    BsmtFinSF2 INT,
    BsmtUnfSF INT,
    TotalBsmtSF INT,
    Heating VARCHAR(32),
    HeatingQC VARCHAR(32), 
    CentralAir VARCHAR(32),
    Electrical VARCHAR(32),
    FirstFlrSF INT,
    SecondFlrSF INT,
    LowQualFinSF INT,
    GrLivArea INT,
    BsmtFullBath INT,
    BsmtHalfBath INT,
    FullBath INT,
    HalfBath INT,
    BedroomAbvGr INT,
    KitchenAbvGr INT,
    KitchenQual VARCHAR(32),
    TotRmsAbvGrd INT,
    Functional VARCHAR(32),
    Fireplaces INT,
    FireplaceQu VARCHAR(32),
    GarageType VARCHAR(32),
    GarageYrBlt FLOAT,
    GarageFinish VARCHAR(32),
    GarageCars INT,
    GarageArea INT,
    GarageQual VARCHAR(32),
    GarageCond VARCHAR(32),
    PavedDrive VARCHAR(32),
    WoodDeckSF INT,
    OpenPorchSF INT,
    EnclosedPorch INT,
    SsnPorch INT,
    ScreenPorch INT,
    PoolArea INT,
    PoolQC VARCHAR(32),
    Fence VARCHAR(32), 
    MiscFeature VARCHAR(32),
    MiscVal INT,
    MoSold INT,
    YrSold INT,
    SaleType VARCHAR(32),
    SaleCondition VARCHAR(32),
    SalePrice INT
)
''')

with open('/Users/yunselee/Desktop/project/data/train.csv','r') as f:
    next(f)
    cur.copy_from(f,'prices_train',sep=',',null='NA') # 포스트그레는 null로 인식해줘야 됨.

conn.commit()


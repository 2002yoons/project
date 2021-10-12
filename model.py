import pandas as pd
import numpy as np
import pickle
import warnings
warnings.filterwarnings('ignore') 
from scipy.special import boxcox1p
from scipy.stats import boxcox_normmax
from sklearn.linear_model import Lasso, LassoCV
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error


X = pd.read_csv('/Users/yunselee/Desktop/project/data/Features.csv')
y = pd.read_csv('/Users/yunselee/Desktop/project/data/Targets.csv')

#
X = X[['OverallQual','GrLivArea','GarageCars']]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=12345)

def rmse(ytrue, ypredicted):
    return np.sqrt(mean_squared_error(ytrue, ypredicted))


model = Lasso(max_iter = 100000, normalize = True)

lassocv = LassoCV(alphas = None, cv = 10, max_iter = 100000, normalize = True)
lassocv.fit(X_train, y_train)

model.set_params(alpha=lassocv.alpha_)
model.fit(X_train, y_train)

print('The Lasso:')
print("Alpha =", lassocv.alpha_)
print("RMSE =", rmse(y_test, model.predict(X_test)))


pickle.dump(model,open('/Users/yunselee/Desktop/project/flask_app/model.pkl','wb')) 
from sklearn import linear_model
from sklearn import datasets
import numpy as np


diabetes = datasets.load_diabetes()
diabetes_X_train = diabetes.data[:-20]
diabetes_X_test  = diabetes.data[-20:]
diabetes_y_train = diabetes.target[:-20]
diabetes_y_test  = diabetes.target[-20:]

regr = linear_model.LinearRegression()
regr.fit(diabetes_X_train, diabetes_y_train)

print (regr.coef_)

np.mean((regr.predict(diabetes_X_test) - diabetes_y_test) ** 2)

regr.score(diabetes_X_test, diabetes_y_test)

#import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
#We do not want to see warnings
warnings.filterwarnings("ignore")

data = pd.read_csv("./uber.csv")

df = data.copy()

df.head()

df.info()

df["pickup_datetime"] = pd.to_datetime(df["pickup_datetime"])

df.info()

df.describe()

df.isnull().sum()

df.corr()

df.dropna(inplace=True)

plt.boxplot(df['fare_amount'])

q_low = df["fare_amount"].quantile(0.01)
q_hi  = df["fare_amount"].quantile(0.99)

df = df[(df["fare_amount"] < q_hi) & (df["fare_amount"] > q_low)]

df.isnull().sum()

from sklearn.model_selection import train_test_split

x = df.drop("fare_amount", axis = 1)

y = df['fare_amount']

x['pickup_datetime'] = pd.to_numeric(pd.to_datetime(x['pickup_datetime']))
x = x.loc[:, x.columns.str.contains('^Unnamed')]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 1)

from sklearn.linear_model import LinearRegression

lrmodel = LinearRegression()
lrmodel.fit(x_train, y_train)

predict = lrmodel.predict(x_test)

from sklearn.metrics import mean_squared_error,r2_score
lrmodelrmse = np.sqrt(mean_squared_error(predict, y_test))
print("R2 score is",r2_score(predict, y_test))
print("RMSE error for the model is ", lrmodelrmse)

from sklearn.ensemble import RandomForestRegressor
rfrmodel = RandomForestRegressor(n_estimators = 100, random_state = 101)

rfrmodel.fit(x_train, y_train)
rfrmodel_pred = rfrmodel.predict(x_test)

rfrmodel_rmse = np.sqrt(mean_squared_error(rfrmodel_pred, y_test))
print("R2 score is",r2_score(rfrmodel_pred, y_test))
print("RMSE value for Random Forest is:",rfrmodel_rmse)

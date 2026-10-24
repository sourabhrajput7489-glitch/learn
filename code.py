import pandas as pd
import matplotlib as plt
from sklearn.linear_model import LinearRegression

df=pd.DataFrame(
    {
        "x":[1,2,3,4,5,6,7,8,9,10],
        "y":[12,22,33,44,55,66,77,88,99,102]
    }
)
df
x=df["x"].values.reshape(-1,1)
model=LinearRegression()
model.fit(x,y)
model.coef_
model.intercept_
model.predict([[3000]])
---------------------------------------------------------------

df=pd.read_csv("data/HouseData.csv")
x=df["Area"]
y=df["Price"]
x=x.values.reshape(-1,1)
model=LinearRegression()
model.fit(x,y)
model.coef_
model.intercept_
model.predict([[3000]])
----------------------------------------------------------------
x_train=x[:1700]
y_train=y[:1700]
x_test=x[1700:]
y_test=y[1700:]
y_pred=model.predict(x_test)
import matplotlib.pyplot as plt
plt.plot(x_test, y_test, "o")
plt.plot(x_test,y_pred,"o")
plt.show()
model.score(x_test,y_test)
---------------------------------------------------------------------
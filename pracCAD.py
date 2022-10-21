import pandas as pd
import matplotlib.pyplot as plt
my_data=pd.read_csv("diabetes")

print(my_data.shape)
print(my_data.head(9))

cor1=my_data.corr()
print(cor1)

df_1=pd.DataFrame(cor1)
df_1.to_csv("diabetes")

import pandas as pd
from matplotlib import pyplot as plt
plt.rcParams["figure.figsize"]=[7.00,3.50]
plt.rcParams["figure.autolayout"]=True
columns=["Pregnancies","Glucose","BloodPressure","SkinThickness","Insulin","BMI","DiabetesPedigreeFunction","Age","Outcome"]
df=pd.read_csv("diabetes",usecols=columns)
print("Contents in csvfile:\n",df)
plt.plot(df.Pregnancies,df.Glucose,df.BloodPressure,df.SkinThickness,df.Insulin,df.BMI,df.DiabetesPedigreeFunction,df.Age,df.Outcome)
plt.show()

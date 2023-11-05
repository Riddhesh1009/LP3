import pandas as pd
import seaborn as sns

df=pd.read_csv("diabetes.csv")
df

x=df.drop('Outcome',axis=1)

y=df['Outcome']

sns.countplot(x=y)

from sklearn.preprocessing import MinMaxScaler
scaler=MinMaxScaler()
x_scaled=scaler.fit_transform(x)

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x_scaled,y,random_state=0,test_size=0.25)

from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier(n_neighbors=5)
knn.fit(x_train,y_train)

y_pred=knn.predict(x_test)

from sklearn.metrics import confusion_matrix,recall_score,precision_score,accuracy_score,f1_score
print("Confusion Matrix")
print(confusion_matrix(y_test, y_pred))
print("Accuracy Score:", accuracy_score(y_test, y_pred))
print("RecallScore:", recall_score(y_test, y_pred))
print("F1 Score:", f1_score(y_test, y_pred))
print("Precision Score:",precision_score(y_test, y_pred))
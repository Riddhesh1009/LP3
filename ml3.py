import pandas as pd
import seaborn as sns

df=pd.read_csv("Churn_Modelling.csv")
df.shape

df.head()

x=df[['CreditScore','Age','Tenure','Balance','NumOfProducts','HasCrCard','IsActiveMember','EstimatedSalary']]
y=df["Exited"]

x

sns.countplot(x=y)

y.value_counts()

from sklearn.preprocessing import StandardScaler

scaler=StandardScaler()

x_scaled=scaler.fit_transform(x)
x_scaled

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test =train_test_split(x_scaled,y,random_state=0,test_size=0.25)

from sklearn.neural_network import MLPClassifier

ann=MLPClassifier(hidden_layer_sizes=(100,100,1000),random_state=0,max_iter=100,activation="relu")

ann.fit(x_train,y_train)

y_pred=ann.predict(x_test)

y_pred

from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score, accuracy_score
print("Confusion Matrix")
print(confusion_matrix(y_test, y_pred))
print("Accuracy Score:", accuracy_score(y_test, y_pred))
print("RecallScore:", recall_score(y_test, y_pred))
print("F1 Score:", f1_score(y_test, y_pred))
print("Precision Score:",precision_score(y_test, y_pred))
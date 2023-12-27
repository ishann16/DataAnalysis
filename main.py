import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("student_record.csv")
print(df.head())
df.describe()
df.info()
df.isnull().sum()

#removing a column
df = df.drop("Unnamed: 0", axis = 1)
print(df.head())

plt.figure(figsize= (4,5))
ax = sns.countplot(data = df, x="Gender")
ax.bar_label(ax.containers[0])
plt.show()

gb = df.groupby("ParentEduc").agg({"MathScore":'mean', "ReadingScore":'mean', "WritingScore":'mean'})
print(gb)

sns.heatmap(gb, annot=True)
plt.title("Relation between parents education of children")
plt.show()
#from above analysis we can conclude that parents education have impacted score's of their children

print(df["EthnicGroup"].unique())

#distribution of ethnic groups
groupA = df.loc[(df["EthnicGroup"] == "group A")].count()
groupB = df.loc[(df["EthnicGroup"] == "group B")].count()
groupC = df.loc[(df["EthnicGroup"] == "group C")].count()
groupD = df.loc[(df["EthnicGroup"] == "group D")].count()
groupE = df.loc[(df["EthnicGroup"] == "group E")].count()

#creating a pie chart
l = ["group A", "group B", "group C", "group D", "group E"]
mlist = [groupA["EthnicGroup"], groupB["EthnicGroup"], groupC["EthnicGroup"], groupD["EthnicGroup"], groupE["EthnicGroup"]]
plt.pie(mlist, labels = l, autopct = "%1.2f%%")
plt.title("Distribution of ethnic groups")
plt.show()

#creating a bar-graph
ax = sns.countplot(data=df, x="EthnicGroup")
ax.bar_label(ax.containers[0])

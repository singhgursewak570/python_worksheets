
# Worksheet 6 Pandas
import pandas as pd

print(pd.__version__)

df=pd.DataFrame({"Name":["Alice","Bob","Charlie"],
                 "Age":[25,30,35],
                 "City":["New York","Los Angeles","Chicago"]})
print(df)

s1=pd.Series([100,200,300,400,500])
s2=pd.Series([10,20,30,40,50])
print(s1[1],s1[3])
print(s1+s2)

print(df[["Name","City"]])
df["Salary"]=[50000,60000,70000]
print(df)
print(df["Age"].mean(),df["Salary"].sum())

print(df[df["Age"]>28])
print(df.set_index("Name"))
print(df.reset_index())

df2=pd.DataFrame({"Name":["John","Jane","Emily"],
                  "Department":["Sales","Marketing","HR"],
                  "Salary":[50000,60000,55000]})
print(df2[df2["Salary"]>55000][["Name","Department"]])

print(df2.groupby("Department")["Salary"].mean())
print(df2.groupby("Department")["Salary"].agg(["min","max"]))

df1=pd.DataFrame({"Name":["John","Jane","Emily"],
                  "Department":["Sales","Marketing","HR"]})
df3=pd.DataFrame({"Name":["John","Jane","Emily"],
                  "Experience":[5,7,3]})
m=pd.merge(df1,df3,on="Name")
print(m.sort_values("Experience",ascending=False))

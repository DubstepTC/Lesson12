import pandas as pd

data = pd.read_csv("adult.data.csv")
data.head()

# print(data["sex"].value_counts())
#
# print(data[data['sex'] == "Female"]["age"].mean())

# a = data['native-country'].value_counts(normalize=TrueS)
# print(a[4])

# age1 = data[data['salary'] == '>50K']['age']
# age2 = data[data['salary'] == '<=50K']['age']
# print("Средний возраст : {0} (>50K) , {1} (<=50K); среднеквадратичные отклонения - {2} (>50K), {3} (<=50K)".format(
#     round(age1.mean()), round(age2.mean()),
#     round(age1.std(), 1), round(age2.std(), 1)))

sp1 = data[data['salary'] == '>50K'] and data['education'].unique()
sp2 = ["Bachelors", "Prof-school", "Assoc-acdm", "Assoc-voc", "Masters", "Doctorate"]
if (sp1 != sp2):
    print("Утверждение неверно")
else :
    print("Утверждение верно")
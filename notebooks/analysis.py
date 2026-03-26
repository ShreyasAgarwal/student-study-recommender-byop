
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("../data/student_scores.csv")

print(data.describe())

plt.scatter(data['physics'], data['maths'])
plt.xlabel("Physics Score")
plt.ylabel("Maths Score")
plt.title("Physics vs Maths Performance")
plt.show()

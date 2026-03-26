import pandas as pd
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

os.makedirs("../model", exist_ok=True)

data = pd.read_csv("../data/student_scores.csv")

# determine weakest subject automatically
def weakest(row):
    scores = {
        "physics": row["physics"],
        "chemistry": row["chemistry"],
        "maths": row["maths"]
    }
    return min(scores, key=scores.get)

data["recommended_subject"] = data.apply(weakest, axis=1)

X = data[['physics','chemistry','maths']]
y = data['recommended_subject']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

pred = model.predict(X_test)
print("Model accuracy:", accuracy_score(y_test, pred))

joblib.dump(model,"../model/study_model.pkl")
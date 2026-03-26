# Smart Study Recommender

## Project Description

The **Smart Study Recommender** is a simple machine learning application developed for the **Fundamentals of AI and ML course**. The purpose of this project is to assist students in identifying which subject they should concentrate on based on their academic performance.

Students often struggle to decide which subject requires more attention during exam preparation. This system analyzes scores in **Physics, Chemistry, and Mathematics** and recommends the subject where improvement is most needed.

The project demonstrates how basic machine learning techniques can be applied to solve a practical educational problem.

---

## How the System Works

1. A dataset containing student scores is used for training the model.
2. The system determines the **weakest subject** for each student based on their marks.
3. A **Decision Tree classification model** is trained using this dataset.
4. When a user enters their scores, the model predicts the subject that should receive more focus.

---

## Technologies Used

The project was implemented using the following tools:

* **Python**
* **Pandas** for data processing
* **Scikit-learn** for building the machine learning model
* **Matplotlib** for basic data visualization
* **Joblib** for saving the trained model
* **Streamlit** for creating a simple web interface
* **GitHub** for version control

---

## Project Structure

```id="r1kdrs"
smart-study-recommender
│
├── data
│   └── student_scores.csv
│
├── src
│   └── recommender.py
│
├── notebooks
│   └── analysis.py
│
├── model
│   └── study_model.pkl
│
├── app.py
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository:

```id="4o2ilv"
git clone https://github.com/yourusername/smart-study-recommender.git
```

Move into the project folder:

```id="vt19zh"
cd smart-study-recommender
```

Install the required libraries:

```id="o3q4cw"
pip install -r requirements.txt
```

---

## Training the Model

Before running the application, the machine learning model needs to be trained.

```id="b3vhq7"
cd src
python recommender.py
```

This script will:

* load the dataset
* train the decision tree model
* evaluate the model accuracy
* store the trained model inside the `model` folder

---

## Running the Application

Once the model is trained, start the web interface using Streamlit.

```id="fkl3wy"
streamlit run app.py
```

The application will open in your browser where you can input your subject scores.

---

## Example Prediction

Example input:

```id="a5xqhh"
Physics: 40
Chemistry: 75
Maths: 50
```

Example output:

```id="wq7xaq"
Recommended subject to focus on: Physics
```

---

## Possible Improvements

Some future enhancements for this project include:

* using a larger and more realistic dataset
* recommending specific **topics** rather than only subjects
* improving prediction accuracy with more advanced models
* deploying the application online

---

## Learning Outcomes

While developing this project, the following concepts were explored:

* data preprocessing using Python
* supervised learning techniques
* decision tree classification
* model training and evaluation
* building a simple AI-based application

---

## Author

**Shreyas Agarwal**
CSE (AI & ML) – First Year
Course: Fundamentals of AI and ML

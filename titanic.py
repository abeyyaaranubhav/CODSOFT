# ---------------------------------------------
# Step 1 — Import Libraries
# ---------------------------------------------
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# ---------------------------------------------
# Step 2 — Load Dataset
# ---------------------------------------------
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

print("Dataset Loaded Successfully!")
print(df.head())

# ---------------------------------------------
# Step 3 — Check Data Summary
# ---------------------------------------------
print(df.info())
print(df.describe())
print(df.isnull().sum())

# ---------------------------------------------
# Step 4 — Data Cleaning
# ---------------------------------------------
# Drop irrelevant columns
df = df.drop(['Name', 'Ticket', 'Cabin'], axis=1)

# Fill missing values
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

# Label Encoding for categorical variables
le = LabelEncoder()
df['Sex'] = le.fit_transform(df['Sex'])
df['Embarked'] = le.fit_transform(df['Embarked'])

# ---------------------------------------------
# Step 5 — Split Features and Target
# ---------------------------------------------
X = df.drop('Survived', axis=1)
y = df['Survived']

# ---------------------------------------------
# Step 6 — Train-Test Split
# ---------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ---------------------------------------------
# Step 7 — Train Model (Logistic Regression)
# ---------------------------------------------
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# ---------------------------------------------
# Step 8 — Make Predictions
# ---------------------------------------------
y_pred = model.predict(X_test)

# ---------------------------------------------
# Step 9 — Evaluate Model
# ---------------------------------------------
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# ---------------------------------------------
# DONE!
# ---------------------------------------------

# CODSOFT
## Python Projects Repository
This repository contains three Python projects that demonstrate different aspects of programming, data analysis, and machine learning:<br>
## Titanic Survival Prediction
A machine learning project that predicts passenger survival on the Titanic using features such as age, gender, class, and fare.<br>
Implements data preprocessing, exploratory data analysis (EDA), and model building using algorithms like Logistic Regression, Random Forest, or others.<br>
Demonstrates skills in handling real-world datasets and building predictive models.<br>
### Project Overview
The Titanic Survival Prediction project is a classic machine learning project aimed at predicting whether a passenger survived the Titanic disaster based on features such as age, gender, class, fare, and family relationships. This project helps you understand data preprocessing, feature engineering, and building predictive models using Python and scikit-learn.
### Dataset
The dataset used in this project contains information about passengers aboard the Titanic. Key features include:
### Feature	Description
PassengerId	Unique identifier for each passenger
Pclass	Ticket class (1 = 1st, 2 = 2nd, 3 = 3rd)
Name	Name of the passenger
Sex	Gender of the passenger
Age	Age in years
SibSp	Number of siblings/spouses aboard
Parch	Number of parents/children aboard
Ticket	Ticket number
Fare	Passenger fare
Cabin	Cabin number
Embarked	Port of embarkation (C = Cherbourg, Q = Queenstown, S = Southampton)
Survived	Survival (0 = No, 1 = Yes) — target variable
### Project Goals
Predict whether a passenger survived or not based on available features.
Explore feature engineering techniques to handle missing data and categorical variables.
Build a machine learning model and evaluate its performance.
### Steps / Workflow
#### 1. Data Loading
Load the dataset (titanic.csv) using pandas.
#### 2. Data Cleaning
Handle missing values (e.g., missing age or embarked information).
Convert categorical variables (Sex, Embarked) into numerical form.
#### 3. Feature Selection
Select features relevant to predicting survival, e.g.:
Pclass, Sex, Age, SibSp, Parch, Fare, Embarked
#### 4. Model Building
Split the dataset into training and testing sets.
Use Logistic Regression (or other classifiers) to predict survival.
Train the model on the training set.
#### 5. Model Evaluation
Evaluate the model using metrics like accuracy, confusion matrix, and classification report.
#### 6. Predictions
Predict survival for new or test data.
### Technologies Used
Python 3.x<br>
pandas<br>
scikit-learn<br>
numpy<br>
### Project Highlights
Classic beginner-friendly ML project.<br>
Demonstrates data preprocessing, feature engineering, and model evaluation.<br>
Can be extended with advanced techniques like Random Forest, XGBoost, or Hyperparameter Tuning for better accuracy.<br>
### Future Improvements
Handle missing data more intelligently (impute based on other features).<br>
Add feature interactions (e.g., family size = SibSp + Parch).<br>
Try different machine learning models (RandomForest, Gradient Boosting, SVM).<br>
Visualize feature importance and survival rates using matplotlib or seaborn.<br>
## Iris Flower Classification
A classic machine learning project for classifying Iris flower species based on sepal and petal measurements.<br>
Covers data preprocessing, visualization, and training models such as Decision Tree, K-Nearest Neighbors, or Support Vector Machines.<br>
Provides insights into supervised learning, feature importance, and model evaluation techniques.<br>
### Project Overview<br>

The Iris dataset contains 150 samples, each with four features:<br>
1. Sepal Length<br>
2. Sepal Width<br>
3. Petal Length<br>
4. Petal Width<br>
#### Using these measurements, the model predicts one of three species:<br>
(i) Iris setosa<br>
(ii) Iris versicolor<br>
(iii) Iris virginica<br>
This project uses Logistic Regression from scikit-learn to build a multi-class classification model.<br>

### Features of the Project<br>
- Loads the Iris dataset from scikit-learn<br>
- Splits data into training and testing sets<br>
- Standardizes feature values for better model performance<br>
- Trains a Logistic Regression classifier<br>
- Generates predictions<br>
- Displays detailed model evaluation<br>
- Plots a confusion matrix for easy visualization<br>

### Technologies Used<br>
- Python<br>
- Scikit-learn<br>
- NumPy<br>
- Matplotlib<br>
### Project Structure<br>
├── iris_classifier.py          # Main ML model code<br>
├── README.md                   # Project documentation<br>
├── .gitignore                  # Clean repo configuration<br>
└── LICENSE           # MIT license<br>
### How to Run the Project<br>
#### Install required libraries:<br>
pip install scikit-learn matplotlib numpy<br>
#### Run the script:
python iris_classifier.py<br>
The script will train the model, print the classification report, and show a confusion matrix plot.<br>
### Model Evaluation<br>
#### The model is evaluated using:
*Accuracy<br>
*Precision<br>
*Recall<br>
*F1-score<br>

#### Confusion Matrix<br>
Logistic Regression performs extremely well on the Iris dataset, achieving high accuracy and very few misclassifications.<br>

#### Confusion Matrix Visualization<br>

<img width="1111" height="927" alt="Screenshot 2025-12-06 154520" src="https://github.com/user-attachments/assets/604b92fc-2729-45ae-9a4a-3fd356f6fb49" />

## Inventory Management System
A GUI-based Python application for managing inventory in a small business or store.<br>
Features include adding, updating, and deleting products, tracking stock levels, and generating reports.<br>
Built using tkinter for the interface and MySQL for data storage, demonstrating practical application development skills.<br>
### Features
- Add items with name, quantity, and price<br>
- Update item details<br>
- Delete items from inventory<br>
- View full inventory list<br>
- Search for specific items<br>
### How to Run
#### Save the code to a file, for example:<br>
inventory.py<br>
### Run it in your terminal:
python inventory.py<br>
### Example Usage
- Copy
- Edit
  1. Add Item<br>
  2. Update Item<br>
  3. Delete Item<br>
  4. View Inventory<br>
  5. Search Item<br>
  6. Exit<br>
- Enter your choice: 1<br>
- Enter product name: Pen<br>
- Enter quantity: 20<br>
- Enter price: 5<br>
- Item added successfully!<br>

Requirements
- Python 3.x
### Conclusion
These projects collectively showcase proficiency in Python programming, data handling, machine learning, GUI development, and database integration. They are ideal for beginners and intermediates looking to strengthen their practical coding and ML experience.

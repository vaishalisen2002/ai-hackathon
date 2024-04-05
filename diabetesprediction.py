# -*- coding: utf-8 -*-
"""DiabetesPrediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zg9lGiPiNuAZhLTEgG_41mqhc4j7n0xA

Importing the Dependencies
"""

import numpy as np # arrray operation
import pandas as pd # DAta frame
from sklearn.preprocessing import StandardScaler # To standerized the dataset
from sklearn.model_selection import train_test_split # to split dataset into test and trainnig
from sklearn import svm # model Support vector machine-->supervised->classification
from sklearn.metrics import accuracy_score  # to calculate the accuracy  of model

"""DAta collection and Analysis
PIMA Diabetes Dataset
"""

#loading the dataset to a Dataframe
diabetes_dataset = pd.read_csv("C:\\Users\\91993\\Downloads\\diabetes (1).csv")
# Print the first 5 rows of the DataFrame
print(diabetes_dataset.head())

# Get the number of rows and columns
num_rows, num_cols = diabetes_dataset.shape

# Print the number of rows and columns
print(f"Number of rows: {num_rows}")
print(f"Number of columns: {num_cols}")

# Getting the statistical measures of the data
diabetes_dataset.describe()

diabetes_dataset['Outcome'].value_counts()

"""Label 0-->Non diabetic
Label 1-->Diabetic
"""

diabetes_dataset.groupby('Outcome').mean()

# separating the data and label
x = diabetes_dataset.drop(columns='Outcome', axis=1)
y = diabetes_dataset['Outcome']

# only data
print(x)

# only label
print(y)

"""Standardization of DAta"""

scaler = StandardScaler()

scaler.fit(x)

standardized_data = scaler.transform(x)

print(standardized_data)

X = standardized_data
Y = diabetes_dataset['Outcome']

print(X)
print(Y)

"""Split the data into train and Test"""

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y,random_state=2)  #20% test data

print(X.shape,X_train.shape ,X_test.shape)

"""Training the model"""

classifier = svm.SVC(kernel='linear')

# training the SVM classifier
classifier.fit(X_train,Y_train)

"""Model Evaluation
Accuracy Score
"""

# accuracy score from the training data
X_train_prediction = classifier.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction,Y_train)

print('Accuracy score of the training data: ',training_data_accuracy)

# accuracy score of test data
X_test_prediction = classifier.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction,Y_test)
print("Accuracy of the test data :", test_data_accuracy)


"""Making a Predictive System"""


def predict_diabetes():
  # Get user input
  glucose = float(input("Enter Glucose Level: "))
  pregnancies = float(input("Enter no . of pregnancies: "))
  skin_thickness = float(input("Enter Skin Thickness: "))
  insulin = float(input("Enter Insulin: "))
  bmi = float(input("Enter BMI: "))
  dpf = float(input("Enter Diabetes Pedigree Function: "))
  age = float(input("Enter Age: "))
  blood_pressure = float(input("Enter Blood Pressure: "))

  # Convert input data to numpy array
  input_data = np.array([[glucose, pregnancies, skin_thickness, insulin, bmi, dpf, age,blood_pressure]])

  # Standardize the input data
  scaler = StandardScaler()
  scaler.fit(X_train)
  std_data = scaler.transform(input_data)

  # Make a prediction
  prediction = classifier.predict(std_data)

  if prediction[0] != 0:
    print("The person is diabetic")
  else:
    print("The person is not diabetic")

# Call the function to predict diabetes
predict_diabetes()

#UI

import tkinter as tk
from tkinter import messagebox
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

def predict_diabetes():
    try:
        # Get user input
        glucose = float(glucose_entry.get())
        pregnancies = float(pregnancies_entry.get())
        skin_thickness = float(skin_thickness_entry.get())
        insulin = float(insulin_entry.get())
        bmi = float(bmi_entry.get())
        dpf = float(dpf_entry.get())
        age = float(age_entry.get())
        blood_pressure = float(blood_pressure_entry.get())

        # Convert input data to numpy array
        input_data = np.array([[glucose, pregnancies, skin_thickness, insulin, bmi, dpf, age, blood_pressure]])

        # Standardize the input data
        scaler = StandardScaler()
        scaler.fit(X_train)
        std_data = scaler.transform(input_data)

        # Make a prediction
        prediction = classifier.predict(std_data)

        if prediction[0] != 0:
            messagebox.showinfo("Prediction", "The person is diabetic")
        else:
            messagebox.showinfo("Prediction", "The person is not diabetic")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values")

# Load your trained model
classifier = SVC(kernel='linear')
# Load your training data (X_train, y_train) here

# Create main window
root = tk.Tk()
root.title("Diabetes Prediction")

# Create labels and entry fields for user input
tk.Label(root, text="Glucose Level:").grid(row=0, column=0, padx=5, pady=5)
glucose_entry = tk.Entry(root)
glucose_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="No. of Pregnancies:").grid(row=1, column=0, padx=5, pady=5)
pregnancies_entry = tk.Entry(root)
pregnancies_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Skin Thickness:").grid(row=2, column=0, padx=5, pady=5)
skin_thickness_entry = tk.Entry(root)
skin_thickness_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(root, text="Insulin:").grid(row=3, column=0, padx=5, pady=5)
insulin_entry = tk.Entry(root)
insulin_entry.grid(row=3, column=1, padx=5, pady=5)

tk.Label(root, text="BMI:").grid(row=4, column=0, padx=5, pady=5)
bmi_entry = tk.Entry(root)
bmi_entry.grid(row=4, column=1, padx=5, pady=5)

tk.Label(root, text="Diabetes Pedigree Function:").grid(row=5, column=0, padx=5, pady=5)
dpf_entry = tk.Entry(root)
dpf_entry.grid(row=5, column=1, padx=5, pady=5)

tk.Label(root, text="Age:").grid(row=6, column=0, padx=5, pady=5)
age_entry = tk.Entry(root)
age_entry.grid(row=6, column=1, padx=5, pady=5)

tk.Label(root, text="Blood Pressure:").grid(row=7, column=0, padx=5, pady=5)
blood_pressure_entry = tk.Entry(root)
blood_pressure_entry.grid(row=7, column=1, padx=5, pady=5)

# Create predict button
predict_button = tk.Button(root, text="Predict", command=predict_diabetes)
predict_button.grid(row=8, column=0, columnspan=2, padx=5, pady=10)

# Run the main event loop
root.mainloop()


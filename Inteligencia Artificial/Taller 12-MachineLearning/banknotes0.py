import csv
import random

from sklearn import svm
from sklearn.linear_model import Perceptron
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier

# model = Perceptron()
model = svm.SVC()
# model = KNeighborsClassifier(n_neighbors=3)
# model = GaussianNB()

# Read data in from file
with open("banknotes.csv") as f:
    reader = csv.reader(f)
    next(reader)

    data = []
    for row in reader:
        data.append({
            "evidence": [float(cell) for cell in row[:4]],
            "label": "Authentic" if row[4] == "0" else "Counterfeit"
        })

# Separate data into training and testing groups
holdout = int(0.80 * len(data))
random.shuffle(data)
testing = data[:holdout]
training = data[holdout:]

# Train model on training set
X_training = [row["evidence"] for row in training]
y_training = [row["label"] for row in training]
model.fit(X_training, y_training)

# Make predictions on the testing set
X_testing = [row["evidence"] for row in testing]
y_testing = [row["label"] for row in testing]
predictions = model.predict(X_testing)

# Compute how well we performed
correct = 0
incorrect = 0
total = 0
authOk = 0
conterOk  = 0
authErr = 0
conterErr = 0

for actual, predicted in zip(y_testing, predictions):
    total += 1
    if actual == predicted:
        correct += 1
        if actual == "Authentic":
            authOk += 1
        else:
            conterOk += 1
    else:
        incorrect += 1
        if actual == "Authentic":
            authErr += 1
        else:
            conterErr += 1

# Print results
print(f"Results for model {type(model).__name__}")
print(f"Correct: {correct}")
print(f"Incorrect: {incorrect}")
print(f"Authentic Correct Predicted: {authOk}")
print(f"Authentic Incorrect Predicted: {authErr}")
print(f"Counterfeit Correct Predicted: {conterOk}")
print(f"Counterfeit Incorrect Predicted: {conterErr}")
print(f"Accuracy: {100 * correct / total:.2f}%")

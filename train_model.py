import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle

# 1. Generate Synthetic Data
# Let's assume a relationship: More study hours -> Higher chance of passing
# We'll generate 100 samples
np.random.seed(42)

# Study hours: Random values between 0 and 12 hours
study_hours = np.random.uniform(0, 12, 100)

# Pass probability: Sigmoid-like relationship
# Pass if 1.5 * hours - 8 + noise > 0
# This means roughly around 5.3 hours is the 50/50 cutoff without noise
# Adding some noise to make it realistic
logits = 1.5 * study_hours - 8 + np.random.normal(0, 2, 100)
pass_fail = (logits > 0).astype(int) # 1 for Pass, 0 for Fail

# Create DataFrame
df = pd.DataFrame({'Study_Hours': study_hours, 'Pass_Fail': pass_fail})

print("First 5 rows of data:")
print(df.head())

# 2. Split Data
X = df[['Study_Hours']]
y = df['Pass_Fail']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Train Model
model = LogisticRegression()
model.fit(X_train, y_train)

# 4. Evaluate
accuracy = model.score(X_test, y_test)
print(f"Model Accuracy on Test Set: {accuracy * 100:.2f}%")

# Test a few predictions
test_hours = np.array([[1], [5], [10]])
predictions = model.predict(test_hours)
probabilities = model.predict_proba(test_hours)

print("\nSample Predictions:")
for i, hours in enumerate(test_hours):
    status = "Pass" if predictions[i] == 1 else "Fail"
    prob = probabilities[i][1] * 100
    print(f"Study Hours: {hours[0]} -> Prediction: {status} ({prob:.2f}% probability)")

# 5. Save Model
with open('student_model.pkl', 'wb') as f:
    pickle.dump(model, f)
print("\nModel saved to 'student_model.pkl'")

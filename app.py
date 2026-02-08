from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import os

app = Flask(__name__)

# Load the model
model_path = 'student_model.pkl'
model = None

if os.path.exists(model_path):
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
else:
    print("Model not found. Please run train_model.py first.")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if not model:
        return jsonify({'error': 'Model not loaded. Please contact administrator.'}), 500

    try:
        data = request.json
        hours = float(data.get('hours'))
        
        # Predict
        prediction = model.predict(np.array([[hours]]))[0]
        probability = model.predict_proba(np.array([[hours]]))[0][1]
        
        result = "Pass" if prediction == 1 else "Fail"
        prob_percent = round(probability * 100, 2)
        
        return jsonify({
            'result': result,
            'probability': prob_percent
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)

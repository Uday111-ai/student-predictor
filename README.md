# Student Pass Predictor

**[🔴 Live Demo](https://student-predictor-zzpg.onrender.com)**

A machine learning web application that predicts the probability of a student passing or failing based on their study hours.

## 🚀 Features

- **Machine Learning Model**: Uses Logistic Regression trained on synthetic data to predict outcomes.
- **Web Interface**: A clean and responsive user interface built with Flask, HTML, CSS, and JavaScript.
- **Real-time Predictions**: Get instant pass/fail predictions and probability scores.
- **Data Persistence**: The trained model is saved and loaded using Python's `pickle` module.

## 🛠️ Technologies Used

- **Python**: Core programming language.
- **Flask**: Web framework for the backend.
- **Scikit-learn**: For building and training the Logistic Regression model.
- **Pandas & NumPy**: For data manipulation and numerical operations.
- **Frontend**: HTML5, CSS3, JavaScript.

## 📦 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/student-pass-predictor.git
   cd student-pass-predictor
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## 🏃‍♂️ Usage

1. **Train the Model:**
   Before running the application, generate the trained model file (`student_model.pkl`):
   ```bash
   python train_model.py
   ```
   You should see a message confirming the model has been saved.

2. **Run the Application:**
   Start the Flask development server:
   ```bash
   python app.py
   ```

3. **Access the App:**
   Open your web browser and go to:
   `http://127.0.0.1:5000`

4. **Make a Prediction:**
   - Enter the number of study hours in the input field.
   - Click the "Predict" button.
   - View the result (Pass/Fail) and the probability score.

## 📂 Project Structure

```
student_analysis/
├── static/
│   ├── style.css        # CSS for styling
│   └── script.js        # JavaScript for frontend logic
├── templates/
│   └── index.html       # Main HTML template
├── app.py               # Flask application entry point
├── train_model.py       # Script to train and save the ML model
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

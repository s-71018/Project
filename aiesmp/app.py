from flask import Flask, request, render_template
import pickle
import pandas as pd

app = Flask(__name__)

# Load the trained model
with open('health_model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_consultation', methods=['POST'])
def get_consultation():
    # Retrieve form data
    fever = request.form.get('Fever')
    cough = request.form.get('Cough')
    fatigue = request.form.get('Fatigue')
    difficulty_breathing = request.form.get('Difficulty Breathing')
    age = request.form.get('Age')
    gender = request.form.get('Gender')
    blood_pressure = request.form.get('Blood Pressure')
    cholesterol = request.form.get('Cholesterol Level')


    # Prepare data for prediction
    input_data = pd.DataFrame([{
        'Fever': fever,
        'Cough': cough,
        'Fatigue': fatigue,
        'Difficulty Breathing': difficulty_breathing,
        'Age': int(age),
        'Gender': gender,
        'Blood Pressure': blood_pressure,
        'Cholesterol Level': cholesterol
    }])

    # Ensure the columns match what the model was trained on
    expected_columns = ['Fever', 'Cough', 'Fatigue', 'Difficulty Breathing', 'Age', 'Gender', 'Blood Pressure', 'Cholesterol Level']
    for column in expected_columns:
        if column not in input_data.columns:
            input_data[column] = None  # Add missing columns with default values

    # Make prediction
    try:    
        prediction = model.predict(input_data)    
        result = f"Predicted Disease: {prediction[0]}"
    except Exception as e:
        result = f"Error: {str(e)}"

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)

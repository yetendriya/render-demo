from flask import Flask, request, jsonify, render_template
import joblib  # Update to joblib
import numpy as np

# Load the trained model and scaler using joblib
model_path = 'DecisionTree_Model.pkl'  # Make sure the file name matches
scaler_path = 'Scaler.pkl'     # Make sure the file name matches

# Use joblib to load the files
model = joblib.load(model_path)
scaler = joblib.load(scaler_path)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract data from the form and convert to float
        float_features = [float(x) for x in request.form.values()]
        # Scale the features using the loaded scaler
        scaled_features = scaler.transform([float_features])
        
        # Make prediction using the loaded model
        prediction = model.predict(scaled_features)
        output = 'Leak Detected' if prediction[0] == 1 else 'No Leak Detected'

        return render_template('index.html', prediction_text='Prediction: {}'.format(output))
    except Exception as e:
        return render_template('index.html', prediction_text='Error: {}'.format(str(e)))

if __name__ == "__main__":
    app.run(debug=True)

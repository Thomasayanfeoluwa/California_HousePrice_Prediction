import pickle
import numpy as np
from flask import Flask, request, render_template

app = Flask(__name__)

# Load the trained model and scaler
try:
    regresion = pickle.load(open('models/regresion.pkl', 'rb'))
    scaler = pickle.load(open('models/scaler.pkl', 'rb'))  # Load the scaler
except FileNotFoundError:
    print("Error: Model or scaler file not found. Ensure 'regresion.pkl' and 'scaler.pkl' are in the 'models' directory.")
    exit(1)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'POST':
        try:
            # Get and validate input features
            MedInc = float(request.form.get('MedInc'))
            HouseAge = float(request.form.get('HouseAge'))
            AveRooms = float(request.form.get('AveRooms'))
            AveBedrms = float(request.form.get('AveBedrms'))
            Population = float(request.form.get('Population'))
            AveOccup = float(request.form.get('AveOccup'))
            Latitude = float(request.form.get('Latitude'))
            Longitude = float(request.form.get('Longitude'))

            # Log the input data
            print(f"Input Data: {MedInc}, {HouseAge}, {AveRooms}, {AveBedrms}, {Population}, {AveOccup}, {Latitude}, {Longitude}")

            # Prepare and scale the input data
            input_data = np.array([[MedInc, HouseAge, AveRooms, AveBedrms, Population, AveOccup, Latitude, Longitude]])
            input_data_scaled = scaler.transform(input_data)  # Apply scaling
            result = regresion.predict(input_data_scaled)

            # Log the prediction result
            print(f"Prediction Result: {result[0]}")

            # Format the result (assuming prediction is in $100,000s, common for California Housing dataset)
            return render_template('home.html', results=result[0] * 100000)  # Scale to dollars

        except (TypeError, ValueError) as e:
            print(f"Error processing input: {e}")
            return render_template('home.html', results="Error: Invalid input data. Please enter valid numbers.")
        except Exception as e:
            print(f"Unexpected error: {e}")
            return render_template('home.html', results="Error: An unexpected error occurred.")
    else:
        return render_template('home.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004, debug=True)
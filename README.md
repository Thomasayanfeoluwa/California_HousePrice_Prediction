California Housing Price Prediction Web Application
Welcome to the California Housing Price Prediction project!
This application is a lightweight Flask web service that predicts house prices in California based on user-input features.
It leverages a trained Ridge Regression model with pre-applied feature scaling to deliver reliable predictions.

Project Structure
bash
Copy
Edit
├── models/
│   ├── regresion.pkl   # Trained Ridge Regression model
│   └── scaler.pkl      # Trained Scaler (e.g., StandardScaler)
├── templates/
│   ├── index.html      # Input form page
│   └── home.html       # Results display page
├── application.py              # Main Flask application
├── README.md           # Project documentation
How It Works
The user fills out a form with features such as Median Income, House Age, Average Rooms, etc.

Input features are scaled using a pre-trained Scaler to match the model’s training conditions.

The Ridge Regression model makes a prediction based on the scaled inputs.

The predicted house price is displayed on the results page.

Features
Robust Error Handling: Validates inputs and handles invalid data gracefully.

Scalable Design: Separation of model and scaler allows easy retraining or model upgrading.

Simple Deployment: Can be deployed locally or hosted on cloud platforms (e.g., AWS, Azure, Render).

Getting Started
Prerequisites
Python 3.8 or above

Install required libraries:

bash
Copy
Edit
pip install flask numpy scikit-learn
Running the Application
Ensure that the trained model (regresion.pkl) and scaler (scaler.pkl) are placed inside the models/ directory.

Run the Flask app:

bash
Copy
Edit
python app.py
Open your web browser and navigate to:

arduino
Copy
Edit
http://localhost:5004/
Notes
The prediction output is multiplied by 100,000 to convert it into actual dollar values, following the common scale used in the California Housing Dataset.

If the model or scaler files are missing, the application will terminate and prompt you with a clear error message.

Debug mode is enabled (debug=True) for development purposes. Disable it in production.

Future Improvements
Implement API endpoints for programmatic access (e.g., /api/predict).

Add data validation on the frontend (HTML form).

Containerize the application with Docker for better portability.

Extend to other regression models (e.g., Lasso, ElasticNet) for performance comparison.

Author
Idowu Thomas
AI & Machine Learning Engineer | Data Scientist | Software Developer
https://www.linkedin.com/in/idowu-thomas-adegoke?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3B9ms4RFleRMem%2FSjXcOTGnA%3D%3D



Setup Guide and Deployment Instructions
1. Local Setup (Development Environment)
Step 1: Clone the Repository (or Download the Code)
bash
Copy
Edit
git clone https://github.com/your-username/your-repository.git
cd your-repository
(If you do not use GitHub yet, simply download the project folder and navigate into it.)

Step 2: Set Up a Virtual Environment (Highly Recommended)
bash
Copy
Edit
python -m venv venv
Activate the environment:

Windows:

bash
Copy
Edit
venv\Scripts\activate
Mac/Linux:

bash
Copy
Edit
source venv/bin/activate
Step 3: Install Project Dependencies
bash
Copy
Edit
pip install -r requirements.txt
Step 4: Run the Application Locally
bash
Copy
Edit
python app.py
Access the app at:

arduino
Copy
Edit
http://localhost:5004/
2. Deployment Guide (Production Environment)
There are several ways to deploy this Flask app.
Here is a general deployment strategy for Render.com (free hosting platform).

Deploy to Render.com (Recommended for Beginners)
Step 1: Prepare Required Files
Make sure you have:

requirements.txt (already created)

app.py (your Flask app)

models/ folder with regresion.pkl and scaler.pkl

templates/ folder with index.html and home.html

A render.yaml file (optional but cleaner deployment)

Example render.yaml:

yaml
Copy
Edit
services:
  - type: web
    name: california-housing-predictor
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: python app.py
    envVars:
      - key: FLASK_ENV
        value: production
Step 2: Push Your Project to GitHub
Create a GitHub repository.

Push your local project to GitHub.

bash
Copy
Edit
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/your-username/your-repository.git
git push -u origin main
Step 3: Deploy on Render
Go to https://render.com/

Create an account (free).

Click "New Web Service" ➔ Connect to your GitHub repo.

Set the Build Command to:

nginx
Copy
Edit
pip install -r requirements.txt
Set the Start Command to:

nginx
Copy
Edit
python app.py
Choose Python 3.8+ as your environment.

Click Deploy.

Render will build your app and assign a live URL (e.g., https://your-app-name.onrender.com).

3. Important Production Notes
Turn off Debug Mode: Set debug=False in app.py before deploying to production.

Set a specific port: Render automatically sets a PORT environment variable. Modify app.py to:

python
Copy
Edit
import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
Secure your model files: Avoid exposing .pkl files directly if you add an API endpoint.

Monitor Logs: Always check the build logs and application logs for any errors during deployment.

Congratulations! 🎉
You now have a professional-grade California Housing Price Prediction application that can be run locally and deployed publicly.


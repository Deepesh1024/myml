from flask import Flask, request, render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)
app = application

## Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        try:
            # Retrieve form data
            gender = request.form.get('gender')
            race_ethnicity = request.form.get('ethnicity')
            parental_level_of_education = request.form.get('parental_level_of_education')
            lunch = request.form.get('lunch')
            test_preparation_course = request.form.get('test_preparation_course')

            # Ensure the form data is properly converted to float
            reading_score = float(request.form.get('reading_score'))
            writing_score = float(request.form.get('writing_score'))

            # Create CustomData object
            data = CustomData(
                gender=gender,
                race_ethnicity=race_ethnicity,
                parental_level_of_education=parental_level_of_education,
                lunch=lunch,
                test_preparation_course=test_preparation_course,
                reading_score=reading_score,
                writing_score=writing_score
            )

            # Get DataFrame for prediction
            pred_df = data.get_data_as_data_frame()
            print(pred_df)
            print("Before Prediction")

            # Perform prediction
            predict_pipeline = PredictPipeline()
            print("Mid Prediction")
            results = predict_pipeline.predict(pred_df)
            print("After Prediction")

            # Render results on the home page
            return render_template('home.html', results=results[0])
        
        except Exception as e:
            print(f"Error occurred: {e}")  # Log the error
            return render_template('home.html', error=str(e))  # Display error to the user

if __name__ == '__main__':
    app.run(port=5001, debug=True)  # Run the app in debug mode

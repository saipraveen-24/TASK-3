from flask import Flask, render_template, request
import pickle
import numpy as np

# Initialize the Flask app
app = Flask(__name__)

# Load the trained model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input values from the form
        features = [float(x) for x in request.form.values()]
        final_input = [np.array(features)]

        # Predict using the model
        prediction = model.predict(final_input)[0]
        result = 'Diabetic' if prediction == 1 else 'Not Diabetic'

        # Send the result back to the same template
        return render_template('index.html', result=result)
    except Exception as e:
        return render_template('index.html', result=f"Error: {e}")

if __name__ == "__main__":
    app.run(debug=True)

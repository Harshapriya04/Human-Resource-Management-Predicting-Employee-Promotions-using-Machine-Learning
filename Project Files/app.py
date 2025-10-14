from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load your trained ML model
model = joblib.load('model.joblib')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # Collect form data
        department = request.form['department']
        education = request.form['education']
        no_of_trainings = request.form['no_of_trainings']
        age = request.form['age']
        previous_year_rating = request.form['previous_year_rating']
        length_of_service = request.form['length_of_service']
        KPIs = request.form['KPIs']
        awards_won = request.form['awards_won']
        avg_training_score = request.form['avg_training_score']

        # Convert categorical values
        if education == '1':
            education = 1
        elif education == '2':
            education = 2
        else:
            education = 3

        KPIs = 1 if KPIs == '1' else 0
        awards_won = 1 if awards_won == '1' else 0

        # Prepare input for prediction
        total = [[department, education, int(no_of_trainings), int(age),
                  float(previous_year_rating), float(length_of_service),
                  KPIs, awards_won, float(avg_training_score)]]

        # Predict using model
        prediction = model.predict(total)

        # Prepare result message
        if prediction[0] == 1:
            text = "Congratulations! The employee is eligible for promotion."
        else:
            text = "Sorry, the employee is not eligible for promotion."

        # Render result page with message
        return render_template('submit.html', text=text)
    
    # Render the prediction form page for GET requests
    return render_template('predict.html')

if __name__ == "__main__":
    app.run(debug=True)
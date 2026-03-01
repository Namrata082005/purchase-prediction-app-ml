# 🧾 Purchase Prediction – ML Deployment with Flask

_Predicting whether a customer will make a purchase based on age and estimated salary using a pre-trained ML model deployed as a web app.\_

---

## 📌 Table of Contents

- <a href="#overview">Overview</a>

- <a href="#business-problem">Project Goal</a>

- <a href="#dataset">Dataset</a>

- <a href="#tools--technologies">Tools \& Technologies</a>

- <a href="#project-structure">Project Structure</a>

- <a href="#data-cleaning--preparation">Data Preparation</a>

- <a href="#exploratory-data-analysis-eda">Model Training \& Analysis</a>

- <a href="#research-questions--key-findings">Key Features \& Insights</a>

- <a href="#dashboard">Web Interface</a>

- <a href="#how-to-run-this-project">How to Run This Project</a>

- <a href="#final-recommendations">Future Improvements</a>

- <a href="#author--contact">Author \& Contact</a>

---

<h2><a class="anchor" id="overview"></a>Overview</h2>

This project is a simple web application that predicts whether a customer will make a purchase using a pre-trained machine learning model. Users can input their age and estimated salary to get a prediction along with probability scores. The app is built with Flask for the backend and HTML/CSS with Bootstrap for the frontend, serving as a beginner's demonstration of ML model deployment.

---

<h2><a class="anchor" id="business-problem"></a>Project Goal</h2>

Predicting customer purchase behavior helps businesses target marketing efforts effectively. This project aims to:

- Deploy a basic ML model as an interactive web app

- Handle user inputs and provide real-time predictions with probabilities

- Demonstrate end-to-end ML workflow from model loading to user interface

- Focus on simplicity for educational purposes as a second ML project

---

<h2><a class="anchor" id="dataset"></a>Dataset</h2>

- Assumed training data: CSV or similar with columns like `Age`, `EstimatedSalary`, and target `Purchased` (binary)

- Pre-trained model and scaler saved as pickle files (`purchase\_knn.pkl` and `scaler.pkl`)

- No raw data included; model assumes classification on historical customer data (e.g., Social Network Ads dataset)

---

<h2><a class="anchor" id="tools--technologies"></a>Tools \& Technologies</h2>

- Python (Flask for web framework, Scikit-learn for ML model)

- HTML/CSS (with Bootstrap 5 for styling)

- Pickle (for model serialization)

- GitHub

---

<h2><a class="anchor" id="project-structure"></a>Project Structure</h2>

purchase-prediction/

│

├── README.md

├── .gitignore

├── app.py # Main Flask application script

├── purchase\_knn.pkl # Pre-trained ML model

├── scaler.pkl # Feature scaler

│

├── templates/ # Folder for HTML templates

│ └── home.html # UI template for the web form

---

<h2><a class="anchor" id="data-cleaning--preparation"></a>Data Preparation</h2>

- User inputs: Age (float), Estimated Salary (float)

- Scaling inputs using loaded scaler to match training data

- Prediction uses scaled features for KNN classification

---

<h2><a class="anchor" id="exploratory-data-analysis-eda"></a>Model Training \& Analysis</h2>

\*\*Assumptions from Training:\*\*

- Model: K-Nearest Neighbors (KNN) classifier from Scikit-learn

- Features: Age, Estimated Salary

- No explicit EDA in this deployment; assume prior analysis showed:

&nbsp; - Positive correlation between salary/age and purchase likelihood

&nbsp; - Decision boundaries based on clusters in feature space

\*\*Potential Issues:\*\*

- No input validation (e.g., negative age/salary)

- Probabilities derived from KNN's predict\_proba

---

<h2><a class="anchor" id="research-questions--key-findings"></a>Key Features \& Insights</h2>

1\. \*\*Input Features\*\*: Age and Estimated Salary for binary classification

2\. \*\*Prediction Logic\*\*: Real-time scaling, inference, and probability calculation

3\. \*\*User Experience\*\*: Simple form with prediction text and progress bars for probabilities

4\. \*\*Insights\*\*: Higher salary and certain age groups increase purchase probability

5\. \*\*Limitations\*\*: Binary output; no multi-class or advanced features

---

<h2><a class="anchor" id="dashboard"></a>Web Interface</h2>

\- Flask-based web app shows:

&nbsp; - Inputs for age and estimated salary

&nbsp; - Prediction result (Will Purchase or Will Not Purchase)

&nbsp; - Progress bars for probability scores (No Purchase vs. Purchase)

&nbsp; - Stylish design with gradient background and Bootstrap components

---

<h2><a class="anchor" id="how-to-run-this-project"></a>How to Run This Project</h2>

1\. Clone the repository:

git clone https://github.com/yourusername/purchase-prediction.git

Install dependencies:

Bashpip install flask scikit-learn

Run the app:

Bashpython app.py

Open in browser:

Visit http://localhost:5000

Enter details and predict!

---

<h2><a class="anchor" id="final-recommendations"></a>Future Improvements</h2>

1\. Add more features (e.g., gender, location)

2\. Implement input validation and error messages

3\. Deploy to cloud (e.g., Heroku)

4\. Include training notebook for full reproducibility

5\. Enhance with JavaScript for dynamic UI

---

<h2><a class="anchor" id="author--contact"></a>Author \& Contact</h2>

Name: Namrata Pokharkar

📧 Email: namratapokharkar20@gmail.com

🔗 LinkedIn: www.linkedin.com/in/namrata-pokharkar-862a55288


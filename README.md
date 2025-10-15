# Human-Resource-Management-Predicting-Employee-Promotions-using-Machine-Learning
**Project Overview**
This project develops a data-driven system to predict the likelihood of an employee being promoted within an organization. It addresses the critical challenge of subjectivity and bias in traditional Human Resource (HR) promotion processes, which can lead to missed talent and high attrition.

By leveraging machine learning, this application provides HR managers with an objective, real-time score of an employee's promotion readiness, shifting talent management from a reactive checklist to a proactive, strategic tool for growth and retention.

**Key Features**
Objective Prediction: Utilizes the Random Forest Classifier to generate a quantifiable probability score based on objective data (KPIs, tenure, training scores).
Bias Mitigation: Employs the SMOTE technique during training to handle the class imbalance (low promotion rate), ensuring the model is fair and robust.
Three-Tier Architecture: Structured into Data, Application (Flask), and Presentation tiers for scalability and maintainability.
Real-Time Scoring: Deployed as a lightweight Flask web application for instant prediction after user input.

**Technical Stack**
Prediction Model
  Technology: Random Forest Classifier (Scikit-learn)
  Role: Selected for superior accuracy, stability, and reliable prediction.
Data Handling
  Technology: pandas, numpy, imblearn (SMOTE)
  Role: Used for cleaning, pre-processing, and crucial imbalance handling of the data.
Web Framework
  Technology: Flask
  Role: Acts as the lightweight server for hosting the prediction API.
Model Persistence
  echnology: joblib
  Role: Used to serialize and load the trained model (model.joblib) for deployment.
Front-End
  echnology: HTML/CSS
  Role: Provides the user interface for inputting employee features and displaying results.



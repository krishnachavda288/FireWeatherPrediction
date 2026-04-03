# 🔥 Fire Weather Index (FWI) Prediction System

## 📌 Project Overview

This project is a **machine learning web application** that predicts the **Fire Weather Index (FWI)** using environmental and meteorological parameters.
I built this project **primarily as a learning exercise** to understand and apply different **regression techniques** and to deploy a trained ML model using **Flask**.
The application allows users to input weather-related features and get a real-time FWI prediction through a web interface.
## 🎯 Learning Objectives

The main goal of this project was to **learn and compare regression models**, including:

* Linear Regression
* Ridge Regression
* Lasso Regression
* Elastic Net Regression
* Multiple Linear Regression

Through this project, I explored:

* Feature scaling using `StandardScaler`
* Model training and evaluation
* Regularization techniques (L1, L2)
* Model serialization using `pickle`
* Deploying an ML model as a web application
* 
## 🧠 Machine Learning Details

**Input Features:**
* Temperature (°C)
* Relative Humidity (RH)
* Wind Speed (Ws)
* Rainfall (mm)
* FFMC (Fine Fuel Moisture Code)
* DMC (Duff Moisture Code)
* ISI (Initial Spread Index)
* Fire Class
* Region

**Target Variable:**
* Fire Weather Index (FWI)

**Final Model Used:**
* Ridge Regression (selected after experimentation with multiple regression techniques)

## 🌐 Web Application

The ML model is integrated into a **Flask web application** where users can:

* Understand input parameters via a description section
* Enter feature values using a clean UI
* Get real-time FWI predictions

## 🚀 Live Demo

👉 **Live Application:**

https://fire-weather-index-predit.onrender.com/


## 🛠 Tech Stack

* **Programming Language:** Python
* **Machine Learning:** Scikit-learn
* **Web Framework:** Flask
* **Model Serving:** Gunicorn
* **Deployment:** Render
* **Frontend:** HTML, CSS


## 📁 Project Structure

├── application.py
├── requirements.txt
├── ridge_model.pkl
├── scaler.pkl
├── templates/
│   ├── index.html
│   └── home.html
└── README.md


## 📈 What I Learned

* How regularization (Ridge, Lasso, Elastic Net) impacts regression models
* How to scale features correctly before prediction
* How to deploy ML models using Flask
* How to move from a notebook-based model to a production-style web app
* Basics of cloud deployment and debugging

This project was built for **learning and hands-on practice** in machine learning regression techniques and ML deployment.

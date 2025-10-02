# Parkinson's Disease Prediction and Tele-Consultancy

This project is a web-based application designed for the early detection of Parkinson's disease using voice frequency analysis. It leverages a machine learning model to predict the likelihood of the disease and includes a feature for users to schedule tele-consultancy appointments with medical professionals.

### About Parkinson's Disease

Parkinson's disease is a progressive neurodegenerative disorder that primarily affects the nervous system, leading to a variety of motor symptoms. These symptoms, which include tremors, stiffness, and difficulty with balance and coordination, worsen over time. As the disease advances, it can lead to significant disability and complications that severely impact a person's quality of life.

While there is currently no cure for Parkinson's, **early detection is crucial**. An early diagnosis allows for timely medical intervention, including therapies and medications that can help manage symptoms, slow the progression of the disease, and significantly improve the patient's long-term outlook and independence. This project aims to provide an accessible tool for early screening, encouraging individuals to seek professional medical advice sooner.

### Key Features

*   **Parkinson's Disease Prediction:** Utilizes voice frequency data to predict the presence of Parkinson's disease.
*   **Machine Learning Model:** Employs a Support Vector Machine (SVM) algorithm for accurate classification.
*   **Tele-consultancy Scheduling:** Allows users to book appointments with doctors directly through the platform.
*   **Web Interface:** Built with Django to provide a user-friendly and interactive experience.

### Tech Stack

*   **Backend:** Python, Django
*   **Machine Learning:** Scikit-learn (SKLearn), NumPy, Pandas
*   **Development Environment:** Google Colab

### How It Works

The core of this project is the prediction model. A Support Vector Machine (SVM) classifier is trained on a dataset containing various voice metrics from both healthy individuals and patients with Parkinson's disease. The model learns to distinguish between the two groups based on these vocal features. The Django application provides an interface for users to submit their voice data, which is then processed by the trained model to generate a prediction. The integrated appointment system allows users to seamlessly connect with healthcare providers for further consultation.

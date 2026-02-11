## Experimental Analysis

The Jupyter notebook included in this repository documents the data
preprocessing, feature extraction, model training, and evaluation
process for phishing URL detection.

Phishing attacks are increasing rapidly, and many users cannot easily differentiate between genuine and fake websites. Traditional blacklist-based methods fail against new phishing URLs. This project uses machine learning, which can detect phishing URLs based on patterns instead of relying only on known blacklists.

⚙️ How the System Works

The user enters a website URL.

The URL is cleaned and normalized.

Features are extracted from the URL using TF-IDF.

A trained machine learning model analyzes the features.

The system predicts whether the URL is SAFE or PHISHING.

The result is displayed instantly on the web interface.

✨ Key Features

Machine learning–based phishing detection

Real-time URL analysis

Clean and user-friendly web interface

AI chatbot for phishing awareness

Fast prediction with lightweight backend

Educational and real-world applicable project

🧰 Technologies Used

Programming Language: Python

Web Framework: Flask

Machine Learning: scikit-learn

Frontend: HTML, CSS, Tailwind CSS, JavaScript

Model Storage: Pickle (.pkl)

📂 Project Structure (Simplified)
cyber-phishing-url-detector/
│
├── app8.py                 # Main Flask backend
├── test_model.py           # Model testing script
├── templates/              # HTML templates
├── static/                 # Static files (CSS, JS)
├── .gitignore              # Ignored large files
└── README.md               # Project documentation

🖥️ How to Set Up Environment

To run this project, Python 3.8 or above must be installed on your system.

After downloading or cloning the repository:

Open the project folder in VS Code or any editor

Open a terminal inside the project directory

Install required Python libraries (Flask, scikit-learn, etc.)

The machine learning model files are not included in the repository due to GitHub size limits.

▶️ How to Run the Project

Make sure Python is installed.

Place trained model and vectorizer .pkl files in the project directory.

Run the Flask application file.

Open the local server URL shown in the terminal.

Enter a website URL to check if it is safe or phishing.

⚠️ Important Note (Read This)

Model files and datasets are not included in this repository.

Due to GitHub file size limitations:

.pkl (trained models)

.csv (datasets)

.ipynb (notebooks)

result images

are excluded.

You must add your own trained model and vectorizer files before running the application.

🧪 Limitations

Accuracy depends on training data quality

Cannot guarantee 100% phishing detection

Advanced phishing techniques may bypass detection

🚀 Future Enhancements

Improve accuracy using deep learning

Browser extension integration

Cloud deployment

Larger and updated phishing datasets

🎓 Educational Value

This project is useful for:

Machine Learning students

Cybersecurity beginners

Academic mini / major projects

Understanding real-world ML applications

📜 Disclaimer

This project is developed for educational purposes only.
Users should always follow safe browsing practices.

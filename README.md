# SATURN - Sentiment Analysis for User Review on Network

**SATURN** is a sentiment analysis project designed to analyze user reviews on a network, providing an accurate sentiment (positive, negative, or neutral) based on the text input. The tool leverages natural language processing (NLP) with Python's Flask framework and NLTK for text processing.

## Objectives
- **Analyze User Reviews**: Automatically analyze user reviews to determine the overall sentiment (Positive, Negative, or Neutral).
- **Provide Real-time Sentiment Analysis**: Users can input text to get immediate sentiment feedback.
- **Flask-based Web Application**: The project is built using Flask, making it easy to run as a web app.
- **Use of NLTK**: Natural Language Toolkit (NLTK) is used for processing and analyzing textual data.

## Project Overview
The SATURN project consists of:
1. **app.py**: The main Python script running the Flask app and sentiment analysis logic.
2. **templates/index.html**: The HTML template for the user interface.
3. **requirements.txt**: Contains the required Python packages for the project.
4. **README.md**: This file with detailed instructions for setup and usage.

## Installation Guide

To get started with the project, follow these steps:

### Step 1: Clone the repository
To download the project to your local machine, clone the repository using the following command:

```bash
git clone https://github.com/kishanss04/sentiment-analysis.git
```
### Step 2: Folder Structure
Once you’ve cloned the repository, you’ll see the following folder structure:

```bash
sentiment-analysis/
├── app.py                 # Main application script
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
└── templates/
    └── index.html         # HTML template for the web interface
``` 
### Step 3: Install Prerequisites
To run this project, you'll need to install the required Python packages. Open Command Prompt (Windows) or Terminal (Mac/Linux) and run the following commands:

```bash
pip install Flask
pip install nltk
```
### Step 4: Run the Application
Once the dependencies are installed, navigate to the project directory where the app.py file is located:

```bash
cd sentiment-analysis
```

Now, run the Flask application using the following command:

```bash
python app.py
```
This will start the web application. You can now access the sentiment analysis tool in your browser by visiting http://127.0.0.1:5000/

## Troubleshooting
If you encounter any issues while running the project, feel free to leave a comment on the GitHub repository, or you can contact me directly at:

Email: kishanss1804@gmail.com
GitHub: kishanss04

## License
This project is licensed under the MIT License.


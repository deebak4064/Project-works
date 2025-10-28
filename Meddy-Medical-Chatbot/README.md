# Meddy: End-to-End Medical Chatbot

A smart, user-friendly health chatbot powered by NLP and machine learning, served on a modern web interface.


## 🌐 Features

- Modern web chat interface (Bootstrap styled, mobile-friendly)
- Natural language symptom checking and interactive conversation
- Predicts possible medical conditions and gives basic precautions
- Machine learning powered backend using PyTorch


## 📁 Project Structure


Meddy-Medical-Chatbot/
│
├── app.py                     # Main Flask backend (AJAX chat route)
├── README.md                  # You are here
├── requirements.txt
├── LICENSE
├── nnet.py, nltk_utils.py     # Model & tokenization code
├── intents.json, intents_short.json
├── Meddy.ipynb                # Data exploration notebook
├── models/ and data/          # Model and CSV files (ensure in correct location)
└── templates/
    └── index.html             # Modern chat UI template




## 🚀 How to Run

1. **Install dependencies**  
   ```
   pip install -r requirements.txt
   ```

2. **Ensure your trained models and data files are in the proper places**  
   (see comments in `app.py` & file structure above)

3. **Start the Flask server:**  
   ```
   python app.py
   ```

4. **Open in your browser:**  
   [http://localhost:5000/](http://localhost:5000/)

***

## 💡 API (For developers)

- **POST `/chat`**  
  Send:  
  ```json
  {"sentence": "I have a headache and sore throat"}
  ```
  Receive:  
  ```json
  {"response": "Hmm, I'm 88.23% sure this is headache."}
  ```

***

## ✨ Credits

Created by DEEBAK KUMAR.  
Inspired by open source and the AI healthcare community.

***

Feel free to personalize more with screenshots, FAQ, or contribution guidelines! Let me know if you want those sections, too.
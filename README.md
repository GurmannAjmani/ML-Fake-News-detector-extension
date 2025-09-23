# News Detector

A machine learning-based fake news detection system. This project provides a backend API for classifying news headlines or articles as "True" or "Fake" using a trained Random Forest model, and a browser extension frontend for easy access.

## Project Structure

```
news-detector/
│
├── requirements.txt             
├── tester.py                       
│
├── backend/
│   ├── main.py                    
│   ├── test_preprocessor.py        
│   ├── label_encoder.joblib       
│   ├── random_forest_model.joblib 
│   ├── tokenizer.json            
│   ├── requirements.txt            
│   └── __pycache__/              
│
└── extension/
    ├── manifest.json              
    ├── popup.html                 
    ├── popup.js                 
    └── popup.css                  
```

## Features

- **Backend**: Fast API for news classification using a pre-trained model.
- **Frontend**: Browser extension for quick news verification.
- **Preprocessing**: Consistent text preprocessing for both training and inference.

## Setup & Reproduction

### 1. Backend

#### Prerequisites

- Python 3.8+
- (Recommended) Create a virtual environment:
  ```
  python -m venv venv
  source venv/bin/activate  # On Windows: venv\Scripts\activate
  ```

#### Install dependencies

```
cd backend
pip install -r requirements.txt
```

#### Run the backend server

```
python main.py
```

The API should now be running.

#### Test the backend

You can use `tester.py` 

### 2. Browser Extension

#### Load the extension

1. Open your browser (Chrome/Edge/Brave).
2. Go to `chrome://extensions/` and enable "Developer mode".
3. Click "Load unpacked" and select the `extension/` folder.
4. The "News Detector" extension should now appear in your browser.

#### Usage

- Click the extension icon.
- Enter or select news text.
- The extension will send the text to the backend API and display the prediction.

### 3. Notes

- Ensure the backend server is running before using the extension.
- The extension and backend communicate via HTTP; you may need to adjust CORS settings in the backend for local testing.
- The trained model and tokenizer are included for immediate use.

## Requirements

- See `backend/requirements.txt` for backend dependencies.
- The extension runs in any Chromium-based browser.
.


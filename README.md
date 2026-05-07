# News Detector

A machine learning-based **fake news detection system**.  
This project provides:  
- A **backend API** (FastAPI) for classifying news headlines or articles as **"True"** or **"Fake"** using a trained Random Forest model.  
- A **browser extension frontend** for quick and fun access.  

Live API: [https://ml-fake-news-detector-extension.onrender.com](https://ml-fake-news-detector-extension.onrender.com) 

---

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


---

##  Features

- **Backend**: FastAPI serving a pre-trained Random Forest model.  
- **Frontend**: Browser extension (dark mode UI) for fast verification.  
- **Preprocessing**: Consistent text preprocessing (tokenization, stopword removal, padding).  

---

##  Setup & Reproduction

### 1. Backend


The backend is already deployed on Render: https://ml-fake-news-detector-extension.onrender.com/predict

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


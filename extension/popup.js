const PROD_URL = "https://ml-fake-news-detector-extension.onrender.com/predict";
const DEV_URL  = "http://127.0.0.1:8000/predict";

// Restore checkbox state across popup opens
const devModeCheckbox = document.getElementById("devMode");
chrome.storage.local.get("devMode", (data) => {
  devModeCheckbox.checked = !!data.devMode;
});
devModeCheckbox.addEventListener("change", () => {
  chrome.storage.local.set({ devMode: devModeCheckbox.checked });
});

document.getElementById("checkBtn").addEventListener("click", async () => {
  const inputText = document.getElementById("newsInput").value;
  const resultElem = document.getElementById("result");
  const isDevMode = devModeCheckbox.checked;
  const API_URL = isDevMode ? DEV_URL : PROD_URL;

  if (!inputText.trim()) {
    resultElem.textContent = "Please enter some text.";
    return;
  }

  resultElem.textContent = "Checking...";

  try {
    const response = await fetch(API_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text: inputText })
    });

    const data = await response.json();
    if (data.result) {
      resultElem.textContent = "Prediction: " + data.result;
    } else {
      resultElem.textContent = "Error: " + (data.error || "Unknown");
    }

  } catch (err) {
    resultElem.textContent = isDevMode
      ? "Error: Could not connect to local backend (localhost:8000)."
      : "Error: Could not connect to backend.";
  }
});

const API_URL = "https://ml-fake-news-detector-extension.onrender.com/predict";

document.getElementById("checkBtn").addEventListener("click", async () => {
  const inputText = document.getElementById("newsInput").value;
  const resultElem = document.getElementById("result");

  if (!inputText.trim()) {
    resultElem.textContent = "Please enter some text!";
    resultElem.classList.add("fade");
    return;
  }

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
    resultElem.classList.add("fade");
    setTimeout(() => resultElem.classList.remove("fade"), 500);

  } catch (err) {
    resultElem.textContent = "Error: Could not connect to backend.";
    resultElem.classList.add("fade");
    setTimeout(() => resultElem.classList.remove("fade"), 500);
  }
});

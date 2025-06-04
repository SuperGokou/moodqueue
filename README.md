# 📊 Mood of the Queue

## 👤 Author

**Ming Xia**  
Data Scientist | AI Enthusiast | Streamlit Developer  


This is a lightweight internal tool built with **Streamlit** to help support agents **log and visualize the emotional tone** of the ticket queue throughout the day. Users can select a mood, add an optional note, and view real-time mood statistics — all stored in **Google Sheets**.

---

## 🔧 Features

### ✅ Log a Mood
- Emoji-based mood input: 😊 😠 😕 🎉
- Optional note input (e.g., “lots of Rx delays today”)
- Automatically stores the mood, note, and timestamp to a Google Sheet

### 📈 Visualize the Mood
- Select a specific date to view mood distribution
- See a **bar chart** of mood counts for that day
- Optionally view the raw data in table format

---

## 🚀 How to Run Locally

### 1. Clone the Repo

    git clone <your-repo-url>
    cd moodqueue


### 2. Install Requirements

    pip install -r requirements.txt

### 3. Launch the App

    streamlit run app.py

## ✨ Bonus Features (Optional / Stretch Goals)

These are optional enhancements beyond the core requirements that could improve the app’s usability and insightfulness:

- [X] Auto-refresh the chart
- [X] Group by day or allow filtering
- [X] Add subtle UI polish or interaction niceties

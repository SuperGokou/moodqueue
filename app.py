import streamlit as st
import pandas as pd
from datetime import datetime
from streamlit_gsheets import GSheetsConnection
from streamlit_autorefresh import st_autorefresh



# -------- Auto-refresh every 3 seconds ----------#

st_autorefresh(interval=3000, key="datarefresh") 


# ------------------ Constants ------------------ #
mood_map = {
    "😊": "Happy",
    "😠": "Angry",
    "😕": "Confused",
    "🎉": "Excited"
}

captions = [
            "***Happy***",
            "***Angry***",
            "***Confused***",
            "***Excited***"
]

emoji_list = ["😊", "😠", "😕", "🎉"]

conn = st.connection("gsheets", type=GSheetsConnection)
existing_entries = conn.read(worksheet='MoodQueue', ttl='60s')

# ----------------- UI Elements -----------------#
with st.sidebar:
    st.header('📊 Mood of the Queue')
    st.markdown("***")
        
    mood = st.radio(':rainbow[**How\'s your day going?**]', emoji_list, captions = captions, horizontal=True)

    mood = mood_map[mood]

    st.markdown("****")
            
    note = st.text_area("**Add a short note (Optional)**", height=200)

    col1, col2, col3 = st.columns([1,1,1]) 
    with col2: 
        submit_button = st.button('Submit', use_container_width=True)

# ------------------ UI Elements --------------------#

# --- Google Sheets Connection and Data Handling --- #

    if submit_button:
        
        timestamp = datetime.now()
        new_entry = {
            'Time': [timestamp.strftime('%m-%d-%Y')],
            'Mood': [mood],
            'Note': [note]
        }
        
        existing_entries = pd.concat([existing_entries, pd.DataFrame(new_entry)], ignore_index=True)
        conn.update(worksheet="MoodQueue", data=existing_entries)
        st.success(f"Entry saved successfully! Timestamp: {timestamp}")  
# --- Google Sheets Connection and Data Handling --- #

# ----------------- Visualize the Mood ------------------#
st.header('Visualize the Mood')

date_list = existing_entries['Time'].to_list()
date_sort_list = sorted(list(set(date_list)), reverse=True)

selected_option = st.radio('**How would you like View the form?**', ['Bar Chart', 'Excel'], horizontal=True)
todaydate = (datetime.now().strftime('%m-%d-%Y'))

if selected_option == 'Bar Chart':
    
    data_select = st.selectbox('**Select the Date:**', date_sort_list)
    selected_date = existing_entries[existing_entries['Time'] == data_select]
    
    if selected_date.empty:
        st.info("No mood entries for today yet.")
    else:
        day = 'Today' if todaydate == data_select else data_select
        st.title(f"Mood Counts for {day}")
        mood_counts = selected_date['Mood'].value_counts().reset_index()
        mood_counts.columns = ['Mood', 'Count']
        st.bar_chart(mood_counts.set_index('Mood'))

else:
    st.dataframe(existing_entries)
# ----------------- Visualize the Mood ------------------#

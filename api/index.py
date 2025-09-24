from fastapi import FastAPI
from datetime import datetime
import pytz

app = FastAPI()

# Timetable dictionary
timetable = {
    "Monday": [
        {"time": "09:00 - 09:45", "subject": "BETCH1/BATCH2 DBMS/OS (12)"},
        {"time": "09:45 - 10:30", "subject": "BETCH1/BATCH2 DBMS/OS (12)"},
        {"time": "10:30 - 11:20", "subject": "R-09"},
        {"time": "11:20 - 12:10", "subject": "DBMS-09"},
        {"time": "12:10 - 01:00", "subject": "LUNCH"},
        {"time": "01:00 - 01:50", "subject": "SUP-17"},
        {"time": "01:50 - 02:40", "subject": "DS-114"},
        {"time": "02:40 - 03:30", "subject": "OS-114"},
    ],
    "Tuesday": [
        {"time": "09:00 - 09:45", "subject": "BETCH1/BATCH2 MICRO PROJECT (12)"},
        {"time": "09:45 - 10:30", "subject": "BETCH1/BATCH2 MICRO PROJECT (12)"},
        {"time": "10:30 - 11:20", "subject": "R-09"},
        {"time": "11:20 - 12:10", "subject": "DBMS-09"},
        {"time": "12:10 - 01:00", "subject": "LUNCH"},
        {"time": "01:00 - 01:50", "subject": "SUP-17"},
        {"time": "01:50 - 02:40", "subject": "OS-114"},
        {"time": "02:40 - 03:30", "subject": "DS-114"},
    ],
    "Wednesday": [
        {"time": "09:00 - 09:45", "subject": "BETCH1/BATCH2 MICRO PROJECT (12)"},
        {"time": "09:45 - 10:30", "subject": "BETCH1/BATCH2 MICRO PROJECT (12)"},
        {"time": "10:30 - 11:20", "subject": "R-09"},
        {"time": "11:20 - 12:10", "subject": "DBMS-09"},
        {"time": "12:10 - 01:00", "subject": "LUNCH"},
        {"time": "01:00 - 01:50", "subject": "SUP-11"},
        {"time": "01:50 - 02:40", "subject": "DS-114"},
        {"time": "02:40 - 03:30", "subject": "OS-114"},
    ],
    "Thursday": [
        {"time": "09:00 - 09:45", "subject": "OS-09"},
        {"time": "09:45 - 10:30", "subject": "DBMS-09"},
        {"time": "10:30 - 11:20", "subject": "R-120"},
        {"time": "11:20 - 12:10", "subject": "R-120"},
        {"time": "12:10 - 01:00", "subject": "LUNCH"},
        {"time": "01:00 - 01:50", "subject": "08/SUP"},
        {"time": "01:50 - 02:40", "subject": "LAB-15 LAB"},
        {"time": "02:40 - 03:30", "subject": "DS-114"},
    ],
    "Friday": [
        {"time": "09:00 - 09:45", "subject": "BETCH2/BATCH1 DBMS/OS (12)"},
        {"time": "09:45 - 10:30", "subject": "BETCH2/BATCH1 DBMS/OS (12)"},
        {"time": "10:30 - 11:20", "subject": "DBMS-09"},
        {"time": "11:20 - 12:10", "subject": "DS-09"},
        {"time": "12:10 - 01:00", "subject": "LUNCH"},
        {"time": "01:00 - 01:50", "subject": "MENTOR-LIB-08"},
        {"time": "01:50 - 02:40", "subject": "PROJECT-08"},
        {"time": "02:40 - 03:30", "subject": "OS-09"},
    ]
}

@app.get("/attendance/today")
def get_today_attendance():
    # Get IST date
    ist = pytz.timezone("Asia/Kolkata")
    today = datetime.now(ist).strftime("%A")

    response = {"day": today}
    if today in timetable:
        for i, lec in enumerate(timetable[today], start=1):
            response[f"lec{i}"] = lec
    else:
        response["message"] = "No classes today"

    return response

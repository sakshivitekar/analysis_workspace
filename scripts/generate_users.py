import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import os

# Ensure folder exists
os.makedirs("data/raw", exist_ok=True)

# ---------------- USERS ----------------
num_users = 1000

users = pd.DataFrame({
    "user_id": range(1, num_users + 1),
    "role": np.random.choice(["student", "recruiter"], num_users),
    "college_id": np.random.randint(1, 20, num_users),
    "signup_date": [
        datetime.now() - timedelta(days=random.randint(0, 60))
        for _ in range(num_users)
    ]
})

users.to_csv("data/raw/users.csv", index=False)

# ---------------- EVENTS ----------------
num_events = 2000

events = pd.DataFrame({
    "event_id": range(1, num_events + 1),
    "user_id": np.random.randint(1, num_users + 1, num_events),
    "event_name": np.random.choice(["login", "post", "apply", "comment"], num_events),
    "timestamp": [
        datetime.now() - timedelta(days=random.randint(0, 60))
        for _ in range(num_events)
    ]
})

events.to_csv("data/raw/events.csv", index=False)

print("Users and Events datasets created successfully!")

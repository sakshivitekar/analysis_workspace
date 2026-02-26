import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import os 

# Ensure folder exists
os.makedirs("data/raw", exist_ok=True)

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

print("users.csv created successfully!")
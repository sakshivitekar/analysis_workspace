import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Basic setup
num_posts = 500
num_comments = 2000
num_jobs = 200
num_applications = 800
num_users = 1000

roles = ["student", "alumni", "admin"]
colleges = [101, 102, 103, 104, 105]

# ---------------- POSTS ----------------
posts = pd.DataFrame({
    "post_id": range(1, num_posts + 1),
    "user_id": np.random.randint(1, num_users + 1, num_posts),
    "content": [f"Post content {i}" for i in range(1, num_posts + 1)],
    "created_at": [
        datetime.now() - timedelta(days=random.randint(0, 180))
        for _ in range(num_posts)
    ],
    "role": np.random.choice(roles, num_posts),
    "college_id": np.random.choice(colleges, num_posts)
})

# ---------------- COMMENTS ----------------
comments = pd.DataFrame({
    "comment_id": range(1, num_comments + 1),
    "post_id": np.random.randint(1, num_posts + 1, num_comments),
    "user_id": np.random.randint(1, num_users + 1, num_comments),
    "comment_text": [f"Comment text {i}" for i in range(1, num_comments + 1)],
    "created_at": [
        datetime.now() - timedelta(days=random.randint(0, 180))
        for _ in range(num_comments)
    ]
})

# ---------------- JOBS ----------------
jobs = pd.DataFrame({
    "job_id": range(1, num_jobs + 1),
    "title": [f"Job Title {i}" for i in range(1, num_jobs + 1)],
    "company": np.random.choice(["TCS", "Infosys", "Wipro", "Google", "Microsoft"], num_jobs),
    "location": np.random.choice(["Mumbai", "Pune", "Bangalore", "Delhi"], num_jobs),
    "created_at": [
        datetime.now() - timedelta(days=random.randint(0, 180))
        for _ in range(num_jobs)
    ],
    "college_id": np.random.choice(colleges, num_jobs)
})

# ---------------- APPLICATIONS ----------------
applications = pd.DataFrame({
    "application_id": range(1, num_applications + 1),
    "job_id": np.random.randint(1, num_jobs + 1, num_applications),
    "user_id": np.random.randint(1, num_users + 1, num_applications),
    "status": np.random.choice(["applied", "shortlisted", "rejected", "selected"], num_applications),
    "applied_at": [
        datetime.now() - timedelta(days=random.randint(0, 180))
        for _ in range(num_applications)
    ],
    "role": np.random.choice(roles, num_applications),
    "college_id": np.random.choice(colleges, num_applications)
})

# Save files
posts.to_csv("data/raw/posts.csv", index=False)
comments.to_csv("data/raw/comments.csv", index=False)
jobs.to_csv("data/raw/jobs.csv", index=False)
applications.to_csv("data/raw/applications.csv", index=False)

print("Dummy content datasets generated successfully!")
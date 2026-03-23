import pandas as pd
import os

base_path = "../data/raw"

users = pd.read_csv(os.path.join(base_path, "users.csv"))
events = pd.read_csv(os.path.join(base_path, "events.csv"))
posts = pd.read_csv(os.path.join(base_path, "posts.csv"))
comments = pd.read_csv(os.path.join(base_path, "comments.csv"))
jobs = pd.read_csv(os.path.join(base_path, "jobs.csv"))
applications = pd.read_csv(os.path.join(base_path, "applications.csv"))

print("All datasets loaded successfully!\n")

print("1. User count by role")
print(users["role"].value_counts(), "\n")

print("2. Event count by type")
print(events["event_type"].value_counts(), "\n")

print("3. Total posts")
print(len(posts), "\n")

print("4. Comments per post (top 5)")
comments_per_post = comments.groupby("post_id").size().sort_values(ascending=False).head()
print(comments_per_post, "\n")

print("5. Applications by status")
print(applications["status"].value_counts(), "\n")

if "company" in jobs.columns:
    print("6. Jobs by company")
    print(jobs["company"].value_counts(), "\n")

print("Reusable pandas queries executed successfully!")
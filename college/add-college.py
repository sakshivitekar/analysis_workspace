import pandas as pd

users = pd.read_csv("data/raw/users.csv")

colleges = ["ABC College", "XYZ College", "PQR Institute"]

# auto fill college column
users["college"] = [colleges[i % 3] for i in range(len(users))]

# save back
users.to_csv("data/raw/users.csv", index=False)

print("College column filled successfully ✅")
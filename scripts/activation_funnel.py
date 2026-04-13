import pandas as pd

# ----------------------------
# 1. Load data
# ----------------------------
users = pd.read_csv("data/raw/users.csv")
posts = pd.read_csv("data/raw/posts.csv")
applications = pd.read_csv("data/raw/applications.csv")

# ----------------------------
# 2. Clean column names
# ----------------------------
users.columns = users.columns.str.strip()
posts.columns = posts.columns.str.strip()
applications.columns = applications.columns.str.strip()

# ----------------------------
# 3. Merge college into posts & applications
# ----------------------------
posts = posts.merge(users[['user_id', 'college']], on='user_id', how='left')
applications = applications.merge(users[['user_id', 'college']], on='user_id', how='left')

# ----------------------------
# 4. Overall Funnel
# ----------------------------
signup_users = users['user_id'].nunique()
post_users = posts['user_id'].nunique()
apply_users = applications['user_id'].nunique()

funnel = pd.DataFrame({
    'Step': ['Signed Up', 'Post Created', 'Applied'],
    'Users': [signup_users, post_users, apply_users]
})

funnel['Conversion %'] = (funnel['Users'] / signup_users) * 100

# Save overall funnel
funnel.to_csv("outputs/activation_funnel.csv", index=False)

# ----------------------------
# 5. College-wise Funnel (Advanced)
# ----------------------------
funnel_list = []

for college in users['college'].dropna().unique():

    signup = users[users['college'] == college]['user_id'].nunique()
    post = posts[posts['college'] == college]['user_id'].nunique()
    apply = applications[applications['college'] == college]['user_id'].nunique()

    funnel_list.append([college, signup, post, apply])

college_funnel = pd.DataFrame(funnel_list, columns=['College', 'Signup', 'Post', 'Apply'])

# Save college funnel
college_funnel.to_csv("outputs/college_funnel.csv", index=False)

# ----------------------------
# 6. Print outputs
# ----------------------------
print("\n📊 Overall Funnel:\n")
print(funnel)

print("\n🎓 College-wise Funnel:\n")
print(college_funnel)
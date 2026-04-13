import pandas as pd 
import matplotlib.pyplot as plt

users = pd.read_csv("data/raw/users.csv")
events = pd.read_csv("data/raw/events.csv")


users["signup_date"] = pd.to_datetime(users["signup_date"])
signups_per_day = users.groupby(users["signup_date"].dt.date).size()

plt.figure(figure=(10,5))
plt.plot(sighups_per_day.index,signups_per-day.values)
plt.titile("Signups per day")
plt.xlable("Data")
plt.ylable("Number of signups")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("outputs/signups_per_day.png")
plt.close()



events["timestamp"] = pd.to_datetime(events["timestamp"])
events_per_day = events.groupby(events["tiimestamp"].dt.date).size()


plt.figure(figure=(10,5))
plt.plot(events_per_day.index,events_per_day.values)
plt.title("Events per day")
plt.xlabel("Date")
plt.ylabel("Number of events")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("outputs/events_per_day.png")
plt.close()






top_event_types = events["event_type"].value_counts().head(10)

plt.figure(figure=(8,5))
plt.bar(top_event_types.index,top_event_types.values)
plt.title("Top Event Types")
plt.xlabel(" Event Types")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("outputs/events_per_day.png")
plt.close()

print("visualization completed")

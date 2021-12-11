import pandas as pd
counts = df[df["Incident Zip"] == 10023]["Complaint Type"].value_counts().head(10)
import pandas as pd
df = pd.read_csv("311_Service_Requests_2020.csv")  # read_csv()

parking_zip = df[df["Incident Zip"] == 10023]["Complaint Type"].value_counts()["Illegal Parking"] # count vs Value_count
total_zip = df[df["Incident Zip"] == 10023]["Complaint Type"].count() 
fraction_zip = parking_zip / total_zip
fraction_zip

parking_NY = df["Complaint Type"].value_counts()["Illegal Parking"]
total_NY = df["Complaint Type"].count()
fraction_NY = parking_NY / total_NY

higher_parking_proportion = fraction_zip > fraction_NY
higher_parking_proportion
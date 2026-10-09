import pandas as pd

data={"Name":["Pratik","Parshv","Shubham","Samrudhi","Vaishnavi","Prathmesh"],
      "Rollno":[23,44,45,81,91,103],
      "Age":[20,20,20,19,21,20],
      "Marks":[84,89,79,96,92,90]}
s=pd.DataFrame(data)
print(s)

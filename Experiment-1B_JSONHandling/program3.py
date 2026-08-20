import pandas as pd
from io import StringIO

json_data = """
[
    {
        "Roll_No": 101,
        "Name": "hema",
        "Marks": 89
    },
    {
        "Roll_No": 102,
        "Name": "lahari",
        "Marks": 92
    },
    {
        "Roll_No": 103,
        "Name": "ramya",
        "Marks": 88
    }
]
"""

df = pd.read_json(StringIO(json_data))

print("Parsed JSON Data")
print(df)
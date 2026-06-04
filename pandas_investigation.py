# pandas_investigation.py

import pandas as pd

url = "https://api.acodingtutor.com/sales"

df = pd.read_json(url)
# create a pivot table using pandas
pt = pd.pivot_table(df, values="Quantity", index="Product", columns="Colour", aggfunc="sum")
pt.fillna(0, inplace=True)
pt["Total"] = pt.sum(axis=1)

totals_row = pt.sum(axis=0).to_frame().T
totals_row.index = ["Total"]
pt_with_totals = pd.concat([pt, totals_row])

print (pt_with_totals)






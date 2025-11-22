import pandas as pd
import dataframe_image as dfi

# Create a sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, ""],
        'City': ['New York', 'London', 'Paris']}

df = pd.DataFrame(data)

# Export the DataFrame as a PNG image
dfi.export(df, 'table_from_dataframe.png')
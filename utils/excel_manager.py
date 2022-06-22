
# Import pandas
import pandas as pd

# Load the xlsx file
excel_data = pd.read_excel('data/input.xlsx')
# Read the values of the file in the dataframe
data = pd.DataFrame(excel_data, columns=['Time', 'Volume'])
# Print the content
# print("The content of the file is:\n", data)

depth = data.shape[0]

for value in range(depth):
    print(data.loc[value]['Volume'])
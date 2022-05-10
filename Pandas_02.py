import pandas as pd

from Pandas_00_TableData import fStaticTable_Favourte_Colour_and_Animal

def fConvert_To_Dict():
    rTestTable = fStaticTable_Favourte_Colour_and_Animal()
    result = {}
    for a in range(len(rTestTable)):
        result.update({"Key" + str(a+1): rTestTable[a]})
    return result

data = fConvert_To_Dict()
df = pd.DataFrame(data)
#print(df)

ageSumByColour = df.groupby(["Key3"]).Key2.sum()
print(ageSumByColour)

ageAverageByAnimal = df.groupby(["Key4"]).Key2.mean()
print(ageAverageByAnimal)
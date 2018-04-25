import pandas as pd

df1 = pd.read_excel('C:\\Users\\ichha\\testdata1.xlsx')
df2 = pd.read_excel('C:\\Users\\ichha\\testdata2.xlsx')

df1.head()

difference = df2[df1!=df2]
print difference
print "dddd"

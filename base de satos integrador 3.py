#import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_excel('/Users/jcc/Desktop/LICENCIATURA UVM/TERCER CUATRIMESTRE/Data1.xlsx')
corr_matrix = df.corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.show()

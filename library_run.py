import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def csv (namefile):
      df = pd.read_csv(namefile)
      return df

def scatterplot(df,x, y, z, txt):
      sns.scatterplot(data=df, x= x, y= y, hue=z)
      plt.title(txt)
      plt.show()
      
def boxplot(df,x, y, z, txt):
      # Melakukan analisis berdasarkan waktu pengiriman dari cabang asal ke cabang tujuan
      sns.boxplot(data=df, x=x, y=y, hue=z)

      # Menambahkan judul yang sesuai
      plt.title(txt)
      plt.show()
      
def groupdata (df,x,y,z):
      grouped_data = df.groupby([x, y])[z].mean()
      return grouped_data
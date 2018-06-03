#Necessary imports
import pandas as pd

# Reading data locally
df = pd.read_csv('/Users/Venkatesh Suvarna/PycharmProjects/DataMining_Assignment3/winequality-red.csv',sep=';')

#Normalization
def normalize(df):
    df["quality"] = (df["quality"] - df["quality"].min()) / (df["quality"].max() - df["quality"].min())
    print (df["quality"])


#Binning:
def binning(col, cut_points, labels=None):
  #Define min and max values:
  minval = col.min()
  maxval = col.max()

  #create list by adding min and max to cut_points
  break_points = [minval] + cut_points + [maxval]

  #if no labels provided, use default labels 0 ... (n-1)
  if not labels:
    labels = range(len(cut_points)+1)

  #Binning using cut function of pandas
  colBin = pd.cut(col,bins=break_points,labels=labels,include_lowest=True)
  return colBin


column = "quality"


choice = (int)(input('Press 1 to normalize Quality column. \n Press 2 to bin the Quality column.'))
if choice==1:
    print(normalize(df))
elif choice==2:
    # Binning age:
    cut_points = [4, 5, 6]
    labels = ["low", "medium", "high", "very high"]
    df["quality"] = binning(df["quality"], cut_points, labels)
    print(pd.value_counts(df["quality"], sort=False))
else:
    print("Invalid input")







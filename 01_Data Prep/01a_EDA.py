# Import packages
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import LabelBinarizer

import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("/Users/sujitharajan/Documents/GitHub/IS460/data/Clean_Dataset.csv")
df.head()
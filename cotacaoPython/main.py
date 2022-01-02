from IPython.core.display import display
from pandas_datareader import data as web
import pandas as pd
import matplotlib.pyplot as plt

#cotacao unica
cotacao_bovespa = web.DataReader("^BVSP", source="yahoo", start= "28/12/2021", end="31/12/2021")
display(cotacao_bovespa)
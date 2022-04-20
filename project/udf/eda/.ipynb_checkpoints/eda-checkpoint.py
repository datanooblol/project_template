import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from udf.utils.utils import *


def viz_na(inputs, title="data", x=16, y=8):
    # data_name = get_df_name(data)
    plt.figure(figsize=(x,y))
    g = sns.heatmap(inputs.isna(), cbar=False)
    plt.title(f"{title} N/A viz")
    return g
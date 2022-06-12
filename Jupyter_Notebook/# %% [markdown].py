# %% [markdown]
# # Jupyter notebook in VSCode
# This is much better than other jupyter notebook

# %%
print("python ka chilla with baba aammar")

# %% [markdown]
# - **Variables is a great option, you can see each varible in a different window**

# %%
ms = "my name is muhammad sohail"
ms

# %%
import numpy as np
x = np.array([1,2,3,4,5])
x

# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
 
data = pd.read_csv("iris.csv")

# %%
import pandas as pd
import matplotlib.pyplot as plt
phool = pd.read_csv("iris.csv")
 
plt.plot(phool.Id, phool["SepalLengthCm"], "r--")
plt.show

# %%
import seaborn as sns
sns.set_theme(style="ticks", palette="pastel")

# Load the example tips dataset
tips = sns.load_dataset("tips")

# Draw a nested boxplot to show bills by day and time
sns.boxplot(x="day", y="total_bill",
            hue="smoker", palette=["m", "g"],
            data=tips)
sns.despine(offset=10, trim=True)



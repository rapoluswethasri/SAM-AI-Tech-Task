

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    'Restaurant': ['A', 'B', 'C', 'D', 'E'],
    'Ratings': [4.5, 4.0, 3.8, 4.7, 4.2],
    'Votes': [250, 180, 120, 300, 210],
    'Cost': [500, 350, 200, 650, 450]
}

df = pd.DataFrame(data)

sns.set_style("whitegrid")

plt.figure(figsize=(12,7))

graph = sns.barplot(
    x='Restaurant',
    y='Ratings',
    data=df,
    palette='viridis'
)

plt.title(
    "Restaurant Ratings Dashboard",
    fontsize=20,
    fontweight='bold'
)

plt.xlabel(
    "Restaurant Names",
    fontsize=14
)

plt.ylabel(
    "Ratings",
    fontsize=14
)

for i in graph.containers:
    graph.bar_label(i)

plt.show()

plt.figure(figsize=(8,8))

colors = ['gold', 'lightblue', 'lightgreen', 'orange', 'pink']

plt.pie(
    df['Votes'],
    labels=df['Restaurant'],
    autopct='%1.1f%%',
    colors=colors,
    startangle=140,
    shadow=True
)

plt.title(
    "Restaurant Votes Distribution",
    fontsize=18,
    fontweight='bold'
)

plt.show()

plt.figure(figsize=(10,6))

sns.scatterplot(
    x='Ratings',
    y='Votes',
    size='Cost',
    hue='Restaurant',
    data=df,
    sizes=(100, 500)
)

plt.title(
    "Ratings vs Votes Analysis",
    fontsize=18,
    fontweight='bold'
)

plt.xlabel("Ratings", fontsize=14)
plt.ylabel("Votes", fontsize=14)

plt.show()


plt.figure(figsize=(10,6))

plt.plot(
    df['Restaurant'],
    df['Cost'],
    marker='o',
    linewidth=3
)

plt.title(
    "Restaurant Cost Analysis",
    fontsize=18,
    fontweight='bold'
)

plt.xlabel("Restaurant", fontsize=14)
plt.ylabel("Cost", fontsize=14)

plt.grid(True)

plt.show()


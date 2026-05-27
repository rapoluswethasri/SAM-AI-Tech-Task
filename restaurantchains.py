import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    'Restaurant_Chain': ['KFC', 'Dominos', 'Pizza Hut', 'KFC', 'Dominos', 'Burger King'],
    'Branch': ['Hyderabad', 'Chennai', 'Bangalore', 'Mumbai', 'Delhi', 'Pune'],
    'Ratings': [4.5, 4.2, 4.0, 4.6, 4.1, 3.9],
    'Votes': [500, 450, 300, 550, 400, 280]
}

df = pd.DataFrame(data)

print(df)

chain_count = df['Restaurant_Chain'].value_counts()

print(chain_count)

average_ratings = df.groupby('Restaurant_Chain')['Ratings'].mean()

print(average_ratings)

total_votes = df.groupby('Restaurant_Chain')['Votes'].sum()

print(total_votes)

plt.figure(figsize=(10,6))

sns.barplot(
    x='Restaurant_Chain',
    y='Ratings',
    data=df,
    palette='Set2'
)

plt.title(
    "Restaurant Chain Ratings Analysis",
    fontsize=18,
    fontweight='bold'
)

plt.xlabel("Restaurant Chain")
plt.ylabel("Ratings")

plt.show()

plt.figure(figsize=(10,6))

sns.barplot(
    x=total_votes.index,
    y=total_votes.values,
    palette='viridis'
)

plt.title(
    "Restaurant Chain Popularity",
    fontsize=18,
    fontweight='bold'
)

plt.xlabel("Restaurant Chain")
plt.ylabel("Total Votes")

plt.show()
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    'Restaurant Name': ['KFC', 'Dominos', 'Pizza Hut', 'Burger King', 'Subway'],
    'Votes': [1200, 950, 700, 400, 250],
    'Aggregate rating': [4.2, 4.0, 3.8, 3.5, 3.9]
}

df = pd.DataFrame(data)

df.head()

highest_votes = df.loc[df['Votes'].idxmax()]

print("Restaurant With Highest Votes:\n")
print(highest_votes)

lowest_votes = df.loc[df['Votes'].idxmin()]

print("Restaurant With Lowest Votes:\n")
print(lowest_votes)

correlation = df['Votes'].corr(df['Aggregate rating'])

print("Correlation Between Votes and Ratings:")
print(correlation)

plt.figure(figsize=(8,5))

sns.scatterplot(x=df['Votes'],
                y=df['Aggregate rating'])

plt.title('Votes vs Ratings')
plt.xlabel('Votes')
plt.ylabel('Aggregate Rating')

plt.show()

plt.figure(figsize=(8,5))

colors = ['red', 'blue', 'green', 'orange', 'purple']

sns.barplot(x='Restaurant Name',
            y='Votes',
            data=df,
            palette=colors)

plt.title('Restaurant Votes Analysis')
plt.xlabel('Restaurant Name')
plt.ylabel('Votes')

plt.show()

plt.figure(figsize=(4,3))

sns.heatmap(df[['Votes', 'Aggregate rating']].corr(),
            annot=True,
            cmap='Spectral')

plt.title('Correlation Heatmap')

plt.show()

print("""
Insights:

1. KFC received the highest number of votes.
2. Subway received the lowest number of votes.
3. Restaurants with higher ratings generally received more votes.
4. Positive correlation exists between votes and ratings.
""")
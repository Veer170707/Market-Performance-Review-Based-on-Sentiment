import pandas as pd
import matplotlib.pyplot as plt
fear_greed_df = pd.read_csv("fear_greed_index.csv")
historical_data_df = pd.read_csv("historical_data.csv")
historical_data_df['parsed_data'] = pd.to_datetime(
    historical_data_df['Timestamp IST'],
    format = '%d-%m-%Y %H:%M',
    errors='coerce'
)

historical_data_df['date'] = historical_data_df['parsed_data'].dt.strftime('%Y-%m-%d')
merged_data = pd.merge(historical_data_df,fear_greed_df[['date','value','classification']],on = 'date',how = 'left')
merged_data = merged_data.dropna(subset = ['classification'])

df = pd.read_csv('merged.csv')
df.columns  = df.columns.str.lower()
clean_df = df[["value", "closed pnl"]].dropna()
plt.figure(figsize = (8,5))
plt.scatter(
    clean_df["value"],
    clean_df["closed pnl"],
    s=5
)
plt.xlabel("Sentiment Value")
plt.ylabel("Closed PnL")
plt.title("Sentiment and Closed  PnL Relation")


direction_counts = (
    df.groupby(["classification", "direction"])
    .size()
    .unstack(fill_value=0)
)

direction_counts.plot(
    kind = "bar",
    figsize=(10,6)
)

plt.xlabel("Market Sentiment")
plt.ylabel("Number of Trades")
plt.title("Trader Direction by Market Sentiment")


plt.xticks(rotation=15)


plt.show()




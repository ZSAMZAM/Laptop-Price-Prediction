import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Load dataset
df = pd.read_csv("laptop_price.csv", encoding="latin1")

# One-hot encode
df_encoded = pd.get_dummies(df, drop_first=True)

# Features and target
X = df_encoded.drop("Price_euros", axis=1)
y = df_encoded["Price_euros"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Save the model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

# Also save X columns for later use in Streamlit
with open("X_columns.pkl", "wb") as f:
    pickle.dump(X.columns.tolist(), f)

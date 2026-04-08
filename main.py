from src.load_data import load_data
from src.preprocessing import preprocess_data
from src.train import train_model, save_model

print("STARTING CLUSTERING MODEL")

df = load_data('data/mall_customers.csv')  # change this name

X = preprocess_data(df)

model = train_model(X)

save_model(model)

print("Clustering pipeline executed successfully!")
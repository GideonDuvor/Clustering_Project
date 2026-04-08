from sklearn.cluster import KMeans
import pickle

def train_model(X):
    try:
        model = KMeans(n_clusters=3, random_state=42)
        model.fit(X)

        print("Clustering model trained successfully")
        return model

    except Exception as e:
        print(f"Training error: {e}")


def save_model(model, filename='models/model.pkl'):
    with open(filename, 'wb') as file:
        pickle.dump(model, file)
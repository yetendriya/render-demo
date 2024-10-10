import pickle

model_path = 'best_model(2).pkl'  # Adjust the path if necessary
try:
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    print("Model loaded successfully.")
except Exception as e:
    print("Error loading model:", e)

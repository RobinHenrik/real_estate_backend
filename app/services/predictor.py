import pandas as pd
from app.models.model_loader import load_model

model_path = "models/regression_forest_14_12_24.pkl"
model = load_model(model_path)

if model is None:
    raise RuntimeError('Could not load model')

dataset_path = "data/listings_data.csv"
data_df = pd.read_csv(dataset_path)
data_df = data_df.drop(columns=['hoone materjal'])
data_df = data_df[~data_df["linnaosa"].str.contains(r"\btuba\b|-", na=False)]
data_df['omandivorm'] = data_df['omandivorm'].fillna('korteriomand')
data_df = data_df.drop(columns=['hind', 'id'], errors='ignore')
categorical_columns = ["maakond", "linn", "linnaosa", "seisukord", "energiamärgis", "omandivorm"]
df = pd.get_dummies(data_df, columns=categorical_columns, drop_first=True)
feature_columns = df.columns.tolist()
print(feature_columns)

def preprocess_input(input_data: dict) -> pd.DataFrame:
    input_df = pd.DataFrame([input_data])

    input_encoded = pd.get_dummies(input_df)
    input_encoded = input_encoded.reindex(columns=feature_columns, fill_value=0)
    return input_encoded

def make_prediction(input_data: dict) -> float:
    processed_input = preprocess_input(input_data)
    prediction = model.predict(processed_input)
    return round(prediction[0], 2)
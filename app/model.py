import numpy as np
import re
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import FunctionTransformer

# Besin değerlerini normalize eder
def scaling(dataframe):
    scaler = StandardScaler()
    prep_data = scaler.fit_transform(dataframe.iloc[:, 6:15].to_numpy())
    return prep_data, scaler

# K-en yakın komşu modeli kurar
def nn_predictor(prep_data):
    neigh = NearestNeighbors(metric='cosine', algorithm='brute')
    neigh.fit(prep_data)
    return neigh

# Sklearn pipeline oluşturur (scaling + KNN)
def build_pipeline(neigh, scaler, params):
    transformer = FunctionTransformer(neigh.kneighbors, kw_args=params)
    pipeline = Pipeline([('std_scaler', scaler), ('NN', transformer)])
    return pipeline

# Malzemeye göre veriyi filtreler
def extract_data(dataframe, ingredients):
    extracted_data = dataframe.copy()
    extracted_data = extract_ingredient_filtered_data(extracted_data, ingredients)
    return extracted_data

# Malzeme içeren tarifleri regex ile filtreler
def extract_ingredient_filtered_data(dataframe, ingredients):
    extracted_data = dataframe.copy()
    regex_string = ''.join(map(lambda x: f'(?=.*{x})', ingredients))
    extracted_data = extracted_data[
        extracted_data['RecipeIngredientParts'].str.contains(regex_string, regex=True, flags=re.IGNORECASE)
    ]
    return extracted_data

# Kullanıcının girişine göre pipeline'ı uygular ve komşuları döner
def apply_pipeline(pipeline, _input, extracted_data):
    _input = np.array(_input).reshape(1, -1)
    return extracted_data.iloc[pipeline.transform(_input)[0]]

# Ana öneri fonksiyonu
def recommend(dataframe, _input, ingredients=[], params={'n_neighbors': 5, 'return_distance': False}):
    extracted_data = extract_data(dataframe, ingredients)
    if extracted_data.shape[0] >= params['n_neighbors']:
        prep_data, scaler = scaling(extracted_data)
        neigh = nn_predictor(prep_data)
        pipeline = build_pipeline(neigh, scaler, params)
        return apply_pipeline(pipeline, _input, extracted_data)
    else:
        return None

# "..." içindeki stringleri ayıklar
def extract_quoted_strings(s):
    strings = re.findall(r'"([^"]*)"', s)
    return strings

# Önerilen tarifleri temizlenmiş liste olarak verir
def output_recommended_recipes(dataframe):
    if dataframe is not None:
        output = dataframe.copy()
        output = output.to_dict("records")
        for recipe in output:
            recipe['RecipeIngredientParts'] = extract_quoted_strings(recipe['RecipeIngredientParts'])
            recipe['RecipeInstructions'] = extract_quoted_strings(recipe['RecipeInstructions'])
    else:
        output = None
    return output

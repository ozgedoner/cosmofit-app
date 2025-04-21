from fastapi import FastAPI
from pydantic import BaseModel, conlist
from typing import List, Optional
import pandas as pd
import os
from model import recommend, output_recommended_recipes


# Veri setini oku
dataset_path = os.path.join(os.path.dirname(__file__), "dataset.csv")
dataset = pd.read_csv(dataset_path, compression='gzip')

app = FastAPI()

class Params(BaseModel):
    n_neighbors: int = 5
    return_distance: bool = False

class PredictionIn(BaseModel):
    nutrition: conlist(float, min_items=9, max_items=9)
    ingredients: List[str] = []
    params: Optional[Params] = Params()

class Recipe(BaseModel):
    Name: str
    CookTime: str
    PrepTime: str
    TotalTime: str
    RecipeIngredientParts: List[str]
    Calories: float
    FatContent: float
    SaturatedFatContent: float
    CholesterolContent: float
    SodiumContent: float
    CarbohydrateContent: float
    FiberContent: float
    SugarContent: float
    ProteinContent: float
    RecipeInstructions: List[str]

class PredictionOut(BaseModel):
    output: Optional[List[Recipe]] = None

@app.get("/")
def home():
    return {"health_check": "OK"}

@app.post("/generate", response_model=PredictionOut)
def generate(prediction_input: PredictionIn):
    recommendation_dataframe = recommend(
        dataset,
        prediction_input.nutrition,
        prediction_input.ingredients,
        prediction_input.params.dict()
    )
    output = output_recommended_recipes(recommendation_dataframe)
    return {"output": output}

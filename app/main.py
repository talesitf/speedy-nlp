from fastapi import FastAPI, Query
import os
import uvicorn
import pandas as pd

from scripts import load_models, index_finder

app = FastAPI()

df = pd.read_csv("data/recipes_data_small.csv")
df = df[['title','ingredients','directions']]


vec, X = load_models()

@app.get("/hello")
def read_hello():
    return {"message": "hello world"}

@app.get("/query")
def query_route(query: str = Query(..., description="Search query")):

    indexes, results = index_finder(query, vec, X)
    results = [f"title: {recipe['title']}, 'content': Ingredients: {recipe['ingredients']} Directions: {recipe['directions']}, relevance: {result}" for recipe, result in zip(indexes, results)]
    # TODO: write your code here, keeping the return format
    return {"results": results, "message": "OK"}

def run():
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

if __name__ == "__main__":
    run()
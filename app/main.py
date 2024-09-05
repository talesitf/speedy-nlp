from fastapi import FastAPI, Query
import sys
import uvicorn
import pandas as pd

sys.path.insert(0, 'scripts')

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

    results, indexes = index_finder(query, vec, X)
    recipes = df.iloc[results]
    titles = recipes['title'].values
    ingredients = recipes['ingredients'].values
    directions = recipes['directions'].values

    results = []
    for i in range(len(titles)):
        results.append({"title": titles[i], "content": {"ingredients": ingredients[i], "directions": directions[i]}, "score": indexes[i]})
    # TODO: write your code here, keeping the return format
    return {"results": results, "message": "OK"}

def run():
    uvicorn.run("main:app", host="0.0.0.0", port=2323, reload=True)

if __name__ == "__main__":
    run()
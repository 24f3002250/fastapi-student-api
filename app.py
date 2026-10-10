from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

df = pd.read_csv("q-fastapi.csv")

@app.get("/api")
def get_students(classes: list[str] = Query(default=[], alias="class")):
    data = df
    if classes:
        data = df[df["class"].isin(classes)]
    return {"students": data.to_dict(orient="records")}

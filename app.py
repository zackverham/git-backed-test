from fastapi import FastAPI
import tensorflow as tf 

app = FastAPI()

@app.get("/")
def index():
    return {"hello": "world"}

@app.get("/compute")
def compute():
    return {"Tensorflow computation":  str(tf.reduce_sum(tf.random.normal([1000, 1000])))}
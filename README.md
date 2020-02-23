# Irises Modelling with Flask API
This repo is to train a model for predicting types of irises (Setosa, Versicolour, and Virginica) and create a FLASK app to return a prediction from POST request on a local machine.

## Prerequisites

- Install [Docker](https://www.docker.com/)


## Usage

1. Clone this repo
2. cd to this repo
3. Run the service
```
docker build -t flask_api_model . && docker run -p 5000:5000 -d flask_api_model
```
4. Send POST request to Flask app to obtain prediction result (This example sends a post request with a JSON containing a 2x4 matrix of `[[1.0,1.0,1.0,1.0],[3.0,3.0,3.0,3.0]]` and `["versicolor","virginica"]` will be returned)
```
curl --header "Content-Type: application/json" --request POST --data '{"X":[[1.0,1.0,1.0,1.0],[3.0,3.0,3.0,3.0]]}' -s http://localhost:5000/api
```
5. Run below to stop the container
```
docker stop flask_api_model
```

## Reference
- https://medium.com/sfu-big-data/machine-learning-deployment-a-storm-in-a-teacup-10541ec3b0d6
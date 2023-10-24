
# Project Name

## Description

This project has been done in partnership with Servier as an "entrance challenge" in their recruitment methods. Molecule descriptions were provided by Servier in order to build models to predict drug properties. These datasets will be used for this project :
- dataset_single.csv
- dataset_multi.csv

These datasets can be found in src/data

## Features

Have been implemented :
- Building machine learning models such as RandomForest, MLP and LSTM for the binary classification problem (Model1, Model2) 
- Predicting class from input data
- Flask API for model deployment
- Using docker containers to deploy the Flask API

## Getting Started

### Prerequisites

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/BenScherrer/servier_drug_prop_classification.git
   ```

2. Navigate to the project directory:
   ```bash
   cd servier_drug_prop_classification
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Usage as a Package

Not implemented yet.

### Usage via Flask API

Use the Flask API to run trainings and predicts:

1. Start the Flask API:

   ```bash
   # In src folder
   flask --app main run
   ```

2. Access the API via a web browser or a tool like Postman.

3. To perform training:

   ```
   http://127.0.0.1:5000/train?data_path=[path_to_data]&method=[LSTM/MLP/RandomForest]
   ``` 

4. Predicting:
   ```
   http://127.0.0.1:5000/predict?model_path=[path_to_model]&method=[LSTM/MLP/RandomForest]&instance=[smile]
   ```

5. Evaluate a model:

WIP

6. Misc

Vizualisation is key. Next steps for this project would be to implement visualisation tools through the Flask API that allows the user to :
   - Visualize models that have already been create
   - Handle the training datasets
   - Select models to load and perform model evaluations or prediction


## Docker

1. Build the Docker image:

   ```bash
   docker build . -t servier
   ```

2. Run the Docker container:

   ```bash
   # In project folder
   docker run -d -p 5000:5000 -v ./src/data:/app/src/data:Z -v ./src/models:/app/src/models:Z servier:latest
   ```
   This will create volumes for the data and the models that will be created while using the application. In order to perform training, it is necessary to copy the data in the ./src/data folder.

3. Training, predicting...:

   Training or predicting will be the same as in the "Usage via Flask API" section. Except the IP address will be 0.0.0.0:5000

   For instance :

   ```
   http://0.0.0.0:5000/train?data_path=[path_to_data]&method=[LSTM/MLP/RandomForest]
   ```

   Note that the path_to_data will be different for the docker container. It should point to the data volume : "/app/src/data/dataset_single.csv"

   TODO : There seems to be an issue with training models like MLP or RandomForest using the dockerize version of the code. It might be because of the preprocessing part which is different than for LSTM training. To train these models, please use a locally hosted Flask API instead.

## Contact

BenScherrer on GitHub

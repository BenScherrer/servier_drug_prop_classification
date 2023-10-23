
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

## Docker

Explain how to use Docker to run the project in a containerized environment.

1. Build the Docker image:

   ```bash
   docker build . -t servier
   ```

2. Run the Docker container:

   ```bash
   docker run -d -p 5000:5000 - v ./src/data:/app/src/data -v ./src/models:/app/src/models servier:latest
   ```


## Contact

BenScherrer on GitHub

## Acknowledgments

Mention any libraries, tools, or resources that you used and want to acknowledge.
sklearn
tensorflow/keras

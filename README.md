# Census Income Prediction API

This project trains a machine learning model to predict whether a person’s income is `>50K` or `<=50K` using census data. It includes data processing, model training, unit tests, slice-based model evaluation, and a REST API built with FastAPI.

## Project Overview

This project:
- loads and cleans census income data
- processes categorical and numerical features
- trains a classification model
- evaluates model performance
- saves the trained model and encoder
- exposes predictions through a FastAPI application
- includes unit tests
- reports model performance on slices of the data

## GitHub Repository

[Deploying-a-Scalable-ML-Pipeline-with-FastAPI](https://github.com/656nm/Deploying-a-Scalable-ML-Pipeline-with-FastAPI)

## Environment Setup

You can use either conda or pip.

### Option 1: Conda

```bash
conda env create -f environment.yml
conda activate <your_env_name>
    
## Repositories

Github: https://github.com/656nm/Deploying-a-Scalable-ML-Pipeline-with-FastAPI

# Data

The dataset used for this project is stored in: data/census.csv


# Model

Run: python train_model.py

Which will:
- load the census dataset
- split the data into train/test sets
- process the features
- train the model
- save the trained model and encoder in the model/ directory
- generate slice-based metrics in slice_output.txt

# Slice-Based Model Performance

Detailed model performance on data slices is saved in: slice_output.txt

# Start the FastAPI app with:

run uvicorn main:app --reload

# The API will run at:

http://127.0.0.1:8000

# API Endpoints

GET /
(which Returns a welcome message.)

Example response: in json
{"message":"Welcome to the census income prediction API"}

# POST /data/

Returns an income prediction based on census feature inputs.

## Model Card

The model card for this project is included in `model_card_template.md`.


## Project Files

Main files included in this project:

- `train_model.py`
- `main.py`
- `local_api.py`
- `test_ml.py`
- `slice_output.txt`
- `model/model.pkl`
- `model/encoder.pkl`


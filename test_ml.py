import pytest
import numpy as np
from sklearn.ensemble import RandomForestClassifier

# TODO: add necessary import
from ml.model import train_model, compute_model_metrics, inference

# TODO: implement the first test. Change the function name and input as needed
def test_train_model_returns_model():
    """
    Test that train_model returns a trained RandomForestClassifier.
    """
    X_train = np.array([
        [25, 40],
        [30, 50],
        [35, 60],
        [40, 70]
    ])
    y_train = np.array([0, 0, 1, 1])

    model = train_model(X_train, y_train)

    assert isinstance(model, RandomForestClassifier)

# TODO: implement the second test. Change the function name and input as needed
def test_compute_model_metrics():
    """
    Test precision, recall, and F1 on a small known example.
    """
    y = np.array([1, 0, 1, 1])
    preds = np.array([1, 0, 0, 1])

    precision, recall, fbeta = compute_model_metrics(y, preds)

    assert precision == pytest.approx(1.0)
    assert recall == pytest.approx(2 / 3)
    assert fbeta == pytest.approx(0.8)

# TODO: implement the third test. Change the function name and input as needed
def test_inference_returns_correct_number_of_predictions():
    """
    Test that inference returns one prediction per input row.
    """
    X_train = np.array([
        [25, 40],
        [30, 50],
        [35, 60],
        [40, 70]
    ])
    y_train = np.array([0, 0, 1, 1])

    model = train_model(X_train, y_train)

    X_test = np.array([
        [28, 45],
        [38, 65]
    ])

    preds = inference(model, X_test)

    assert len(preds) == len(X_test)

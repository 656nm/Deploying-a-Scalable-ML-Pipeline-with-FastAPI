# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details

This model is a supervised machine learning classification model trained to predict whether a person’s income is greater than 50K per year or less than or equal to 50K per year. The model used is a Random Forest classifier.

The model was trained on the UCI Census Income dataset used in this project. The implementation includes data preprocessing for categorical and numerical features, model training, and inference through a FastAPI application.

## Intended Use

This model is intended for educational purposes as part of the Udacity machine learning deployment project. It is designed to demonstrate how to train, evaluate, and deploy a machine learning model through an API. It should not be used to make real hiring, compensation, lending, legal, or other high-stakes decisions about individuals.

## Training Data

The training data comes from the census dataset included in this project in `data/census.csv`. The dataset contains demographic and employment-related features such as age, workclass, education, marital status, occupation, race, sex, hours per week, and native country. The target variable is whether income is `>50K` or `<=50K`.

## Evaluation Data

The evaluation data is a held-out test split from the same census dataset. The data was split into training and testing subsets before model training so that model performance could be evaluated on unseen examples.

## Metrics

The model was evaluated using classification metrics including precision, recall, and F1 score.

Example overall model performance:
- Precision: 0.7419
- Recall: 0.6384
- F1: 0.6863

In addition to overall metrics, slice-based performance was generated for categorical features and saved in `slice_output.txt`.

## Ethical Considerations

This dataset includes sensitive demographic and personal attributes such as sex, race, and marital status. Predictions from this model may reflect historical bias present in the training data. Because of this, the model may produce unfair outcomes for some groups. The model should be used only for learning and demonstration, not for real-world decision-making involving people.

## Caveats and Recommendations

This model is limited by the quality and age of the dataset and by the fact that it was trained for a classroom project rather than production use. Performance may vary across demographic groups, and slice-based metrics should be reviewed carefully. Before any real-world use, the model would require deeper fairness analysis, better validation, monitoring, and documentation.

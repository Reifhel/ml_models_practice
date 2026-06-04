# Instructions

###### _Project Structure, Rules, and Requirements_

The goal of the challenge is to build a classification model using a decision tree that can predict with high accuracy whether a transaction is fraudulent or not. The model should be evaluated based on metrics that consider both the ability to detect fraud (sensitivity) and the ability to avoid false positives (specificity). Banco SeguraMais seeks a balance between these metrics to ensure the security of its customers without compromising the user experience. Write an analysis of the results obtained at the end of the file, including your interpretations of the results; the result does not necessarily have to be positive when applying the decision tree model.

### Dataset:

The provided dataset contains information about bank transactions carried out by Banco SeguraMais customers. Each row in the dataset represents a transaction, and the columns contain relevant information about the transaction and its status (fraud or non-fraud). Below is a description of the variables in the dataset:

- `Customer: `Unique identifier of the customer who performed the transaction
- `Transaction Type:` The type of transaction performed (e.g., Withdrawal, PIX, Debit, Credit)
- `Transaction Amount:` The monetary value of the transaction
- `Pre-Transaction Balance:` The customer’s balance before the transaction
- `Post-Transaction Balance:` The customer’s balance after the transaction
- `Transaction Time: `The time at which the transaction was performed
- `Class:` The target variable, indicating whether the transaction was fraudulent (1) or legitimate (0)

## Tasks

Use this checklist to help organize your delivery

- [ ] Explore the dataset and understand the meaning of each variable.
- [ ] Prepare the data, including handling missing values and transforming categorical variables, if necessary.
- [ ] Divide the data into training and test sets.
- [ ] Build and train a decision tree model for classifying transactions.
- [ ] Evaluate the model's performance using sensitivity and specificity.
- [ ] Interpret the results, highlighting potential improvements or limitations of the model.
- [ ] Write a critical analysis at the end of the document, presenting your interpretations of the decision tree models performance.

## Note

The dataset is compressed in the resources section; you must extract it first.

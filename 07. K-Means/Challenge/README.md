# Instructions

###### _Project Structure, Rules, and Requirements_

Use the K-Means algorithm to cluster the samples in the Iris dataset, optimizing the models hyperparameters with the help of the Optuna library.

### Dataset:

The Iris dataset contains 150 flower samples, divided into three species (Setosa, Versicolor, and Virginica), each described by four numerical attributes:

- Sepal length
- Seplal width
- Petal length
- Petal width

Target:

- 0: setosa
- 1: versicolor
- 2: virginica

# Base Code

You can import the dataset directly from scikit-learn using the following code:

```python
from sklearn.datasets import load_iris
iris = load_iris()
X = iris.data         # Flower attributes
y = iris.target       # Actual classes (used only for evaluation)
```

# Tasks

Use this checklist to help organize your delivery

- [ ] Import the Iris dataset as instructed.
- [ ] Perform an exploratory analysis of the data, examining the distribution of the attributes.
- [ ] Implement the K-Means algorithm to cluster the samples.
- [ ] Use Optuna to optimize the K-Means hyperparameters.
- [ ] Evaluate the quality of the clusters using the classes for evaluation purposes.

## Note

The dataset is compressed in the resources section; you must extract it first.

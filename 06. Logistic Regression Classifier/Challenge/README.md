# Instructions

###### _Project Structure, Rules, and Requirements_

The goal is to train a logistic regression model to correctly classify the observations as pulsars or non-pulsars, using only the provided attributes. The data file is available in pulsar.csv.

### Dataset:

The dataset consists of 17,898 observations, each representing statistical measurements of signals obtained by radio telescopes. Below are the eight available attributes:

- `Mean of the integrated profile`: The mean of the integrated signal profile, which represents the average signal intensity over time.
- `Standard deviation of the integrated profile`: The standard deviation of the integrated profile, indicating the variation in intensity around the mean.
- `Excess kurtosis of the integrated profile`: The excess kurtosis of the integrated profile, which measures the “tail” of the signal distribution relative to a normal distribution.
- `Skewness of the integrated profile`: Skewness of the integrated profile, representing the degree of distortion of the signal distribution around the mean.
- `Mean of the DM-SNR curve`: Mean of the DM-SNR curve (measure of the signal-to-noise ratio as a function of variance), which quantifies the average signal intensity adjusted for different variances.
- `Standard deviation of the DM-SNR curve`: Standard deviation of the DM-SNR curve, indicating the variability of the signal-to-noise ratio across different variances.
- `Excess kurtosis of the DM-SNR curve`: Excess kurtosis of the DM-SNR curve, assessing the presence of extreme peaks in the signal-to-noise ratio distribution.
- `Skewness of the DM-SNR curve`: Skewness of the DM-SNR curve, showing the tilt of the signal-to-noise ratio distribution relative to the mean.
- `target_class `: Binary target class indicating the object type:
  - 1: True pulsars (highly magnetized neutron stars)
  - 0: Non-pulsars (noise or other astrophysical sources)

## Tasks

Use this checklist to help organize your delivery

- [ ] Load and explore the dataset.
- [ ] Analyze and understand the available attributes.
- [ ] Prepare the data for modeling (cleaning, handling missing values, normalizing, if necessary).
- [ ] Train a logistic regression model using the provided features.
- [ ] Evaluate the model's performance in classifying pulsars and non-pulsars.

## Note

The dataset is compressed in the resources section; you must extract it first.

# Instructions

###### _Project Structure, Rules, and Requirements_

Apply the PCA algorithm to reduce the dimensionality of the data, while retaining as much information as possible. After the reduction, facilitate the visualization and analysis of the transformed data. Calculate the reconstruction error of the dataset based on the selected principal components.

## Dataset

Use the housing.csv dataset, which contains data on homes, including price, area, number of bedrooms, bathrooms, and floors, as well as features such as access to the main street, presence of a guest room, basement, water heating, air conditioning, parking spaces, location in a desirable area, and furnishing status (furnished, semi-furnished, unfurnished).

### Dataset Columns

- `price`: Price of the house.
- `area`: Floor area of the house (in square feet).
- `bedrooms`: Number of bedrooms.
- `bathrooms`: Number of bathrooms.
- `stories`: Number of stories (floors).
- `mainroad`: Access to the main road (yes = has access, no = does not have access).
- `guestroom`: Has a guest room (yes = yes, no = no).
- `basement`: Has a basement (yes = yes, no = no).
- `hotwaterheating`: Has hot water heating (yes = yes, no = no).
- `airconditioning`: Has air conditioning (yes = yes, no = no).
- `parking`: Number of parking spaces.
- `prefarea`: Located in a preferred area (yes = yes, no = no).
- `furnishingstatus`: Furnishing status of the home:
- `furnished`: Fully furnished home, ready to move in, including essential furniture such as beds, sofas, cabinets, appliances, etc.
- `semi-furnished`: Partially furnished home, with some basic furniture or items, but not fully equipped.
- `unfurnished`: Unfurnished home, delivered empty, with no furniture or appliances.

# Tasks

Use this checklist to help organize your delivery

- [ ] Load the housing.csv dataset and analyze its columns and data types.
- [ ] Preprocess the data as needed for PCA (e.g., coding categorical variables, normalization).
- [ ] Apply the PCA algorithm to the dataset to reduce its dimensionality.
- [ ] Visualize the transformed data in a lower-dimensional space.
- [ ] Calculate and report the reconstruction error of the dataset after applying PCA.
- [ ] Interpret the results, highlighting the key factors identified by the PCA.

## Note

The dataset is compressed in the resources section; you must extract it first.

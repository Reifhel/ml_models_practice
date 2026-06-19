# Instructions

###### _Project Structure, Rules, and Requirements_

Your challenge is to apply hierarchical clustering algorithms.

## Context

Taxonomic classification is a central task in biology, used to understand the relationships between organisms based on shared traits. Hierarchical clustering is an interpretable method that simulates the formation of evolutionary relationships among species, similar to a phylogenetic tree.

In this challenge, at least 10 distinct clusters were generated among the species. For educational purposes, we recommend using 10 as the minimum number of clusters during the analysis.

We emphasize that the data are synthetic and do not represent the behavior or information of real species.

## Dataset

The dataset contains 600 records, each representing a fictional species. The attributes were generated through simulation but are based on principles inspired by real biology.

Numeric and Boolean attributes:

| Name               | Type   | Description                                                |
| ------------------ | ------ | ---------------------------------------------------------- |
| species_id         | string | Unique species identifier (e.g., SP001)                    |
| body_mass_kg       | float  | Average body mass of the species (in kg)                   |
| num_legs           | int    | Number of limbs (e.g., 0, 2, 4, 6)                         |
| has_wings          | bool   | Does it have wings? (1 = yes, 0 = no)                      |
| tail_length_cm     | float  | Average tail length (in centimeters)                       |
| eye_count          | int    | Number of eyes (e.g., 0, 2, 4)                             |
| nocturnal          | bool   | Active at night? (1 = yes, 0 = no)                         |
| avg_lifespan_years | float  | Average life expectancy of the species (in years)          |
| has_venom          | bool   | Does this species have venom or a toxin? (1 = yes, 0 = no) |

Categorical attributes:

| Name            | Type   | Description                                              |
| --------------- | ------ | -------------------------------------------------------- |
| diet_type       | string | Diet type of the species: herbivore, carnivore, omnivore |
| skin_type       | string | Type of body covering: fur, scales, feathers, skin       |
| social_behavior | string | Social behavior: solitary, pair-living, group-living     |

# Tasks

Use this checklist to help organize your delivery

- [ ] Load and explore the dataset of 600 fictional species, analyzing the available attributes.
- [ ] Apply hierarchical clustering algorithms to group the species based on the provided characteristics.
- [ ] Generate and interpret dendrograms to visualize the clusters that have formed.
- [ ] Set a cutoff point in the dendrograms to obtain at least 10 distinct clusters.
- [ ] Identify and describe the resulting taxonomic groups, highlighting relevant patterns.
- [ ] Conduct a detailed analysis of the results, discussing possible simulated evolutionary relationships among the clusters.

## Note

The dataset is compressed in the resources section; you must extract it first.

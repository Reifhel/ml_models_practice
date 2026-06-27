# Instructions

###### _Project Structure, Rules, and Requirements_

Use the Apriori algorithm to analyze the provided dataset, which contains 10,000 game purchase records. Each row in the file represents a game purchase by a customer, with the following columns:

- Customer ID: unique identifier for the customer
- Game ID: unique identifier for the game
- Game Name: commercial name of the game

## Objective

The objective is to identify association rules among purchased games, evaluating the most relevant rules based on support, confidence, and lift metrics. Use the results to gain insights that can be applied to recommendations, bundles, or promotions.

## Suggested Questions to Ask During EDA

During exploratory data analysis (EDA), consider investigating the number of unique games, the best-selling games, and the percentage of each games occurrence relative to the customer base.

# Tasks

Use this checklist to help organize your delivery

- [ ] Load and explore the game_sales.csv dataset, analyzing its key characteristics.
- [ ] Conduct an exploratory analysis of the data, answering questions such as: the number of unique games, the best-selling games, and the percentage of each game's occurrence.
- [ ] Prepare the data for the Apriori algorithm by structuring it as needed.
- [ ] Apply the Apriori algorithm to identify association rules among purchased games.
- [ ] Evaluate the generated rules using the metrics of support, confidence, and lift.
- [ ] Present the key insights derived from the association rules, highlighting potential opportunities for recommendations, bundles, or promotions.

# Note

The dataset is compressed in the resources section; you must extract it first.

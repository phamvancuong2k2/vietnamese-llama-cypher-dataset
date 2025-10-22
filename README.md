# Vietnamese Llama Cypher Dataset

## Project Overview
The Vietnamese Llama Cypher Dataset is designed for fine-tuning language models using Neo4j graph databases. This dataset captures relationships and entities in a structured format, enabling efficient querying and manipulation for various NLP tasks.

## Neo4j Schema Description
The dataset is structured in a graph format that represents entities as nodes and relationships as edges. The key components of the schema include:

- **Nodes**: Represent distinct entities such as users, products, and transactions.
- **Properties**: Each node can have various properties that describe its attributes.

## Relationship Types
The dataset includes several types of relationships that capture how entities are connected:

- **FRIENDS_WITH**: Represents a friendship between two users.
- **PURCHASED**: Captures the purchase relationship between a user and a product.
- **REVIEWED**: Indicates a review relationship where a user reviews a product.

## Query Examples
Here are some examples of Cypher queries that can be executed using this dataset:

1. **Find all friends of a user**:
   ```cypher
   MATCH (u:User {name: 'John'})-[:FRIENDS_WITH]->(friends)
   RETURN friends
   ```

2. **List all products purchased by a user**:
   ```cypher
   MATCH (u:User {name: 'John'})-[:PURCHASED]->(p:Product)
   RETURN p
   ```

3. **Get all reviews of a specific product**:
   ```cypher
   MATCH (p:Product {name: 'Product A'})<-[:REVIEWED]-(u:User)
   RETURN u, p
   ```

## Usage Instructions
To use the Vietnamese Llama Cypher Dataset for fine-tuning:

1. **Set up Neo4j**: Install and configure a Neo4j database.
2. **Load the Dataset**: Import the dataset into your Neo4j instance.
3. **Run Queries**: Utilize the provided Cypher queries to explore and fine-tune your models.
4. **Fine-tuning**: Use the data extracted from the graph for training your language models.

For further assistance, please refer to the official Neo4j documentation or reach out to the community.

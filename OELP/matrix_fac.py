import numpy as np
from sklearn.decomposition import NMF

# Sample movie-feature matrix (replace this with your actual data)
movie_feature_matrix = np.array([
    [1, 0, 1, 0, 1],  # Movie 1: Action, Comedy, Drama
    [0, 1, 1, 0, 0],  # Movie 2: Comedy, Romance
    [1, 0, 0, 1, 1],  # Movie 3: Action, Sci-Fi, Drama
    [0, 0, 1, 1, 0],  # Movie 4: Drama, Romance
    [1, 0, 1, 0, 1],  # Movie 5: Comedy
])

# Number of latent features (adjust based on your preference)
n_features = 2

# Perform NMF for matrix factorization
model = NMF(n_components=n_features, init='random', random_state=42)
movie_factors = model.fit_transform(movie_feature_matrix)
feature_weights = model.components_

# Print the original matrix
print("Original Matrix:")
print(movie_feature_matrix)

# Print the decomposed matrices
print("\nMovie Factors:")
print(np.round(movie_factors, 2))

print("\nFeature Weights:")
print(np.round(feature_weights, 2))
# Reconstruct the original matrix
reconstructed_matrix = np.dot(movie_factors, feature_weights)

# Print the reconstructed matrix
print("\nReconstructed Matrix:")
print(np.round(reconstructed_matrix, 2))

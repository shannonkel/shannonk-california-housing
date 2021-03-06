import pickle
from sklearn.neighbors import KNeighborsRegressor


# Create a local instance of the sklearn class
knn_model = KNeighborsRegressor(n_neighbors=8)
# Fit your instance to the training dataset
knn_model.fit(X_train_scaled, y_train)
# Make predictions on the testing dataset
y_preds = knn_model.predict(X_test_scaled)
# root mean squared error represents the average error (in $) of our model
knn_rmse = int(np.sqrt(metrics.mean_squared_error(y_test, y_preds)))
# R-squared is the proportion of the variance in the DV that's explained by the model
knn_r2=round(metrics.r2_score(y_test, y_preds),2)
print(knn_rmse, knn_r2)

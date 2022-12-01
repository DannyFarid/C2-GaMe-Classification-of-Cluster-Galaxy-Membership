"""
This module gives examples of how to use the C2GaMe module.
"""
import C2GaMe
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

# gain access to RF model class
RF = C2GaMe.RF()

# gain access to the classifier object itself
RF_clf: RandomForestClassifier = RF.classifier

example_data = pd.DataFrame({
    'd2d': np.arange(10),
    'v': np.arange(10),
    'mratio': np.arange(10),
    'ssfr': np.arange(10)
})

# use the RF object to make deterministic predictions
RF.predict_det(example_data)

# use the RF object to make probabilistic predictions
RF.predict_proba(example_data)

# gain access to the KNN model class
KNN = C2GaMe.KNN()


# gain access to the classifier object itself
KNN_clf: KNeighborsClassifier = KNN.classifier

# use the RF object to make deterministic predictions
KNN.predict_det(example_data)

# use the RF object to make probabilistic predictions
KNN.predict_proba(example_data)

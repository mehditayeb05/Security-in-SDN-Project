import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Charger les données de trafic réseau
data = pd.read_csv('network_traffic.csv')

# Prétraiter les données
X = data.drop('label', axis=1)  # Supposons que 'label' est la colonne de classe (légitime ou attaque)
y = data['label']

# Diviser les données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# Entraîner un modèle de détection d'anomalies
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Prédictions et évaluation
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

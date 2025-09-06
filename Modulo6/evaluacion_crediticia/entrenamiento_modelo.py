# archivo: entrenamiento_modelo.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, roc_auc_score
import joblib

# Simulación de datos
np.random.seed(42)
n = 1000
data = pd.DataFrame({
    'edad': np.random.randint(18, 70, size=n),
    'ingresos': np.random.normal(50000, 15000, size=n),
    'historial_crediticio': np.random.choice(['bueno', 'regular', 'malo'], size=n),
    'deuda': np.random.normal(10000, 5000, size=n),
    'empleado': np.random.choice(['si', 'no'], size=n),
    'compra': np.random.choice([0, 1], size=n)
})

# Guardar dataset
data.to_csv("datos_crediticios.csv", index=False)

# Preprocesamiento
features = ['edad', 'ingresos', 'historial_crediticio', 'deuda', 'empleado']
target = 'compra'

numeric_features = ['edad', 'ingresos', 'deuda']
categorical_features = ['historial_crediticio', 'empleado']

numeric_transformer = Pipeline([
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler())
])

categorical_transformer = Pipeline([
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('encoder', OneHotEncoder(handle_unknown='ignore'))
])

preprocessor = ColumnTransformer([
    ('num', numeric_transformer, numeric_features),
    ('cat', categorical_transformer, categorical_features)
])

# División de datos
X = data[features]
y = data[target]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Pipeline de modelo
clf_pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier(random_state=42))
])

# Validación cruzada
param_grid = {
    'classifier__n_estimators': [50, 100],
    'classifier__max_depth': [5, 10]
}

grid_search = GridSearchCV(clf_pipeline, param_grid, cv=5, scoring='accuracy')
grid_search.fit(X_train, y_train)

# Evaluación
best_model = grid_search.best_estimator_
y_pred = best_model.predict(X_test)
y_proba = best_model.predict_proba(X_test)[:, 1]

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred))
print("Recall:", recall_score(y_test, y_pred))
print("AUC-ROC:", roc_auc_score(y_test, y_proba))

# Guardar modelo
joblib.dump(best_model, "modelo_crediticio.pkl")

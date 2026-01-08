import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier

# Caricamento e Scaling
data = load_breast_cancer()
X, y = data.data, data.target
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Definizione Modelli
modelli = {
    'SVM (RBF)': SVC(kernel='rbf', C=1.0, gamma=0.01),
    'KNN (K=61)': KNeighborsClassifier(n_neighbors=61)
}

# Calcolo Cross-Validation
risultati = {}
for nome, modello in modelli.items():
    punteggi = cross_val_score(modello, X_scaled, y, cv=10) # 10 esperimenti
    risultati[nome] = punteggi

# 2. Generazione Grafico 📊
plt.figure(figsize=(8, 6))
plt.boxplot(risultati.values(), tick_labels=risultati.keys())
plt.title('Confronto Accuratezza: SVM vs KNN (10-Fold CV)')
plt.ylabel('Accuratezza')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
plt.savefig('confronto_svm_knn.png')

# Stampa medie
for nome, punteggi in risultati.items():
    print(f"{nome} - Accuratezza Media: {punteggi.mean():.4f} (+/- {punteggi.std():.4f})")
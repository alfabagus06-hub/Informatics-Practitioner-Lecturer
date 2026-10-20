import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

rng = np.random.default_rng(23)
n = 600
study_hours = rng.uniform(0, 6, n)
attendance = rng.uniform(45, 100, n)
assignment_rate = rng.uniform(30, 100, n)
# Label sintetis untuk latihan; bukan definisi risiko akademik yang nyata.
risk_score = (6 - study_hours)*5 + (100-attendance)*0.35 + (100-assignment_rate)*0.2 + rng.normal(0, 8, n)
y = (risk_score > 48).astype(int)
X = np.column_stack([study_hours, attendance, assignment_rate])
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)
model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000))
model.fit(X_train, y_train)
pred = model.predict(X_test)
print("Akurasi:", round(accuracy_score(y_test, pred), 3))
print("\nClassification report:")
print(classification_report(y_test, pred, target_names=["Risiko lebih rendah", "Perlu dukungan (simulasi)"]))
print("Confusion matrix:")
print(confusion_matrix(y_test, pred))
print("\nFitur: jam belajar, kehadiran, persentase tugas selesai.")
print("Peringatan: data dan label sintetis; hasil tidak boleh digunakan untuk keputusan nyata.")

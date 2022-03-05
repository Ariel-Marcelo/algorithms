from subprocess import HIGH_PRIORITY_CLASS
from sklearn import tree

Sunny = 1
Overcast = 2
Rain = 3

High = 1
Normal = 2

Weak = 1
Strong = 2

caracteristicas = [
  [Sunny, High, Weak],
  [Sunny, High, Strong],
  [Overcast, High, Weak],
  [Rain, High, Weak],
  [Rain, Normal, Weak],
  [Rain, Normal, Strong],
  [Overcast, Normal, Strong],
  [Sunny, High, Weak],
  [Sunny, Normal, Weak],
  [Rain, Normal, Weak],
  [Sunny, Normal, Strong],
  [Overcast, High, Strong],
  [Overcast, Normal, Weak],
  [Rain, High, Strong]
]

jugar = [
  "No",
  "No",
  "Si",
  "Si",
  "Si",
  "No",
  "Si",
  "No",
  "Si",
  "Si",
  "Si",
  "Si",
  "Si",
  "No"
]

parametros = ["outlook", "Humidity", "Wind"] 

arbol = tree.DecisionTreeClassifier()
arbol = arbol.fit(caracteristicas, jugar)
tree.plot_tree(arbol)
prediccion = arbol.predict([[Rain, High, Weak]])
print("D15, Rain, High, Weak", prediccion)
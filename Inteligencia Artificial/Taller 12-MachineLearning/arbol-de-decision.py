from sklearn import tree

caracteristicas = [
  [0, 250, 36], 
  [10, 150, 34], 
  [2, 90, 10], 
  [6, 78, 8], 
  [4, 20, 1],
  [1, 170, 70],
  [8, 160, 41],
  [10, 180, 38],
  [6, 200, 45]
]

genero = [
  "H",
  "M",
  "H",
  "M",
  "M",
  "H",
  "M",
  "H",
  "H"
]

parametros = ["Longitud", "Peso", "Edad"]


arbol = tree.DecisionTreeClassifier()
arbol = arbol.fit(caracteristicas, genero)
tree.plot_tree(arbol)

prediccion = arbol.predict([[10, 180, 38]])

print ("Comic: 8, 290, 38", prediccion)


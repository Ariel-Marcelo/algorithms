from pomegranate import *

# Rain node has no parents
terremoto = Node(DiscreteDistribution({
    "yes": 0.002,
    "no": 0.998
}), name="terremoto")

robo = Node(DiscreteDistribution({
    "yes": 0.001,
    "no": 0.999
}), name="robo")

# Track maintenance node is conditional on rain
alarma = Node(ConditionalProbabilityTable([
    ["yes", "yes", "yes", 0.95],
    ["yes", "no", "yes", 0.94],
    ["no", "yes", "yes",0.29],
    ["no", "no", "yes",0.001],
    ["yes", "yes", "no", 0.05],
    ["yes", "no", "no", 0.06],
    ["no", "yes", "no",0.71],
    ["no", "no", "no",0.999]
], [robo.distribution, terremoto.distribution]), name="alarma")

# Train node is conditional on rain and maintenance
johnLlama = Node(ConditionalProbabilityTable([
    ["yes", "yes", 0.90],
    ["yes", "no", 0.10],
    ["no", "yes", 0.05],
    ["no", "no", 0.95],    
], [alarma.distribution]), name="johnLlama")

# Appointment node is conditional on train
mariaLlama = Node(ConditionalProbabilityTable([
    ["yes", "yes", 0.70],
    ["yes", "no", 0.30],
    ["no", "yes", 0.01],
    ["no", "no", 0.99],
], [alarma.distribution]), name="mariaLlama")

# Create a Bayesian Network and add states
model = BayesianNetwork()
model.add_states(robo, terremoto, alarma, johnLlama, mariaLlama)

# Add edges connecting nodes
model.add_edge(robo, alarma)
model.add_edge(terremoto, alarma)
model.add_edge(alarma, johnLlama)
model.add_edge(alarma, mariaLlama)

# Finalize model
model.bake()
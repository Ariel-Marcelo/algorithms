from pomegranate import *

# Rain node has no parents
rain = Node(DiscreteDistribution({
    "yes": 0.2,
    "no": 0.7
}), name="rain")

splinkers = Node(DiscreteDistribution({
    "yes": 0.6,
    "no": 0.4
}), name="splinkers")

# Train node is conditional on rain and maintenance
neighbor = Node(ConditionalProbabilityTable([
    ["yes", "yes", 0.3],
    ["yes", "no", 0.4],
    ["no", "yes", 0.7],
    ["no", "no", 0.6],    
], [rain.distribution]), name="neighbor")

# Track maintenance node is conditional on rain
grass = Node(ConditionalProbabilityTable([
    ["yes", "yes", "yes", 0.9],
    ["yes", "no", "yes", 0.7],
    ["no", "yes", "yes",0.8],
    ["no", "no", "yes",0.2],
    ["yes", "yes", "no", 0.1],
    ["yes", "no", "no", 0.3],
    ["no", "yes", "no",0.2],
    ["no", "no", "no",0.8]
], [rain.distribution, splinkers.distribution]), name="grass")



# Appointment node is conditional on train
dog = Node(ConditionalProbabilityTable([
    ["yes", "yes", "yes", 0.90],
    ["yes", "no", "yes", 0.40],
    ["no", "yes", "yes", 0.5],
    ["no", "no", "yes", 0.3],
    ["yes", "yes", "no", 0.1],
    ["yes", "no", "no", 0.6],
    ["no", "yes", "no", 0.5],
    ["no", "no", "no", 0.7]
], [neighbor.distribution, grass.distribution]), name="dog")

# Create a Bayesian Network and add states
model = BayesianNetwork()
model.add_states(rain, splinkers, neighbor, grass, dog)

# Add edges connecting nodes
model.add_edge(rain, neighbor)
model.add_edge(rain, grass)
model.add_edge(splinkers, grass)
model.add_edge(grass, dog)
model.add_edge(neighbor, dog)


# Finalize model
model.bake()

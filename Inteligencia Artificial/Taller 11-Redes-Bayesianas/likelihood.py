from model import model

# Calculate probability for a given observation
probability = model.probability([["yes", "-", "-", "-", "yes"]])

print(probability)

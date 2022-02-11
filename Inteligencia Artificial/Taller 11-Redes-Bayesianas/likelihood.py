from model import model

# Calculate probability for a given observation
probability = model.probability([["yes", "no", "no", "yes", "yes"]])

print(probability)

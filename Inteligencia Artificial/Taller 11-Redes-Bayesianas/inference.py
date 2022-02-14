from model import model

# Calculate predictions
predictions = model.predict_proba({
    "dog": "no",
    "grass": "yes"
})

# Print predictions for each node
for node, prediction in zip(model.states, predictions):
    if isinstance(prediction, str):
        print(f"{node.name}: {prediction}")
    elif node.name == "splinkers":
        print(f"{node.name}")
        for value, probability in prediction.parameters[0].items():
            print(f"    {value}: {probability:.4f}")

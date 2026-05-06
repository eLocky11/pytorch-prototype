import torch
import torch.nn as nn

# Data
# x - input
# y - output = 3x + 2

x_train = torch.tensor([
    [1,0],
    [2,0],
    [3,0],
    [4,0],
    [5,0],
    [6,0],
    [7,0],
    [8,0],
    [9,0],
    [10,0],
])

y_train = 3 * x_train + 2

# Model
model = nn.Linear(1, 1)

# Error function
loss_fn = nn.MSELoss()

# Optimization
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

# Learning
epochs = 1000

for epoch in range(epochs):
    y_pred = model(x_train)
    loss = loss_fn(y_pred, y_train)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if epoch % 100 == 0:
        print(f"Epoch {epoch}, Loss: {loss.item():.6f}")

# Checking the model
test_x = torch.tensor([[10.0]])
prediction = model(test_x)

print()
print("Checking:")
print(f"x = 10")
print(f"The model predicted y = {prediction.item():.2f}")
print(f"Right answer y = {3 * 10 + 2}")

# What parameters did the model learn
weight = model.weight.item()
bias = model.bias.item()

print()
print("The learned formula:")
print(f"y = {weight:.2f}x + {bias:.2f}")
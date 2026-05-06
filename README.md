# PyTorch Formula Prototype

## Project Description

This is a small educational **PyTorch** prototype created to learn the basic neural network training workflow.

The goal of the project is to train a simple model to learn the relationship between an input value `x` and an output value `y` using the formula:

```text
y = 3x + 2
```

This project is not intended for real-world use. Its purpose is to demonstrate the minimum working machine learning pipeline:

1. preparing data;
2. creating a model;
3. calculating loss;
4. running backpropagation;
5. updating model parameters;
6. testing the trained model.

---

## Current Status

At the current stage, the project contains one main script:

```text
train.py
```

This script includes:

- training data;
- an `nn.Linear` model;
- the `MSELoss` loss function;
- the `SGD` optimizer;
- the training loop;
- model prediction testing;
- output of the learned formula.

---

## Technologies Used

- Python
- PyTorch
- Git

---

## What This Prototype Teaches

This project helps understand the basic PyTorch components.

### Tensor

Data is stored as tensors:

```python
x_train = torch.tensor([[1.0], [2.0], [3.0]])
```

### Model

The model is created with:

```python
model = nn.Linear(1, 1)
```

It tries to learn a relationship in the form:

```text
y = wx + b
```

Where:

- `w` is the weight;
- `b` is the bias;
- both parameters are adjusted automatically during training.

### Loss Function

The error is calculated using:

```python
loss_fn = nn.MSELoss()
```

It measures how far the model predictions are from the correct answers.

### Optimizer

The model parameters are updated using:

```python
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
```

### Training Loop

The core PyTorch training loop:

```python
y_pred = model(x_train)
loss = loss_fn(y_pred, y_train)

optimizer.zero_grad()
loss.backward()
optimizer.step()
```

---

## How to Run the Project

1. Make sure Python is installed.
2. Make sure PyTorch is installed.
3. Open the project folder in a terminal.
4. Run:

```bash
python train.py
```

After running the script, the program should print the training progress, the model prediction, and the approximate formula learned by the model.

---

## Expected Result

After training, the model should learn an approximation of:

```text
y = 3x + 2
```

For example, for:

```text
x = 10
```

The correct answer is:

```text
y = 32
```

The model should predict a value close to `32`.

---

## Current Project Structure

```text
pytorch-formula-prototype/
│
├── train.py
├── README.md
└── .gitignore
```

---

## Recommended `.gitignore`

```gitignore
# Python
__pycache__/
*.pyc
*.pyo
*.pyd

# Virtual environment
.venv/
venv/
env/

# IDE
.vscode/
.idea/

# PyTorch / model files
*.pt
*.pth
*.onnx

# System files
.DS_Store
Thumbs.db
```

---

# Future Improvement Plan

## Stage 1. Improve the Current Script

### 1. Add More Test Values

Currently, the model is tested with one value. More test values can be added:

```text
x = 10
x = 15
x = 25
x = -5
```

This will make it easier to check how well the model generalizes.

---

### 2. Improve Training Output

The script can print more useful training information:

- epoch number;
- current loss;
- model weight;
- model bias;
- final learned formula.

Example output:

```text
Epoch 100 | Loss: 0.00231 | y = 2.98x + 2.11
```

---

### 3. Add Configurable Parameters

Move training parameters into variables:

```python
epochs = 1000
learning_rate = 0.01
```

This will make experiments easier.

---

## Stage 2. Split the Project into Multiple Files

After the first working version, the project can be split into separate files:

```text
pytorch-formula-prototype/
│
├── train.py
├── model.py
├── data.py
├── predict.py
├── config.py
├── README.md
└── .gitignore
```

### `model.py`

Contains the model definition.

### `data.py`

Contains training data preparation.

### `train.py`

Runs the training process.

### `predict.py`

Runs predictions using the trained model.

### `config.py`

Stores project settings:

- number of epochs;
- learning rate;
- training data size;
- path for saving the model.

---

## Stage 3. Save and Load the Model

Add model saving:

```python
torch.save(model.state_dict(), "model.pt")
```

And model loading:

```python
model.load_state_dict(torch.load("model.pt"))
```

This will make it possible to reuse the trained model without training it again every time.

---

## Stage 4. Add a Separate Prediction Mode

Create a separate file:

```text
predict.py
```

Then run:

```bash
python predict.py
```

Example interaction:

```text
Enter x: 10
Model prediction: 31.98
```

---

## Stage 5. Add Training Visualization

Add charts using `matplotlib`:

- loss curve;
- comparison between correct values and model predictions.

This will help visualize how the model learns.

---

## Stage 6. Move to a Nonlinear Formula

After the linear formula, try a more complex relationship:

```text
y = x² + 2x + 1
```

For this task, a single `nn.Linear(1, 1)` model will not be enough.

A small neural network can be used instead:

```python
model = nn.Sequential(
    nn.Linear(1, 16),
    nn.ReLU(),
    nn.Linear(16, 16),
    nn.ReLU(),
    nn.Linear(16, 1)
)
```

This helps explain why hidden layers and activation functions are useful.

---

## Stage 7. Move to Classification

The next educational project can be point classification.

Example task:

```text
If x + y > 0 → class 1
Otherwise → class 0
```

This will introduce:

- binary classification;
- `BCEWithLogitsLoss`;
- accuracy;
- the difference between regression and classification.

---

## Stage 8. Move to Image Recognition

After basic regression and classification, the project can move to the MNIST dataset.

Goal:

```text
Recognize handwritten digits from 0 to 9
```

New topics:

- `torchvision`;
- `DataLoader`;
- batches;
- `CrossEntropyLoss`;
- simple neural networks for images.

---

# Learning Roadmap

## Minimal Roadmap

1. Linear regression: `y = 3x + 2`.
2. Nonlinear regression: `y = x² + 2x + 1`.
3. Binary point classification.
4. MNIST classification.
5. Saving and loading a model.
6. Using a trained model in a separate prediction script.

---

## More Practical Roadmap

1. Simple formula learning.
2. Tabular data.
3. Basic object classification.
4. Mini recommendation system.
5. Image data.
6. Small custom dataset.
7. Simple inference script.
8. Model export.

---

# Future Mini-Project Ideas

## 1. Temperature Prediction

The model receives the hour of the day and predicts the temperature.

Goal: understand nonlinear relationships.

---

## 2. Game Object Classification

The model receives object features:

- weight;
- price;
- rarity;
- type;
- level.

Then it predicts the item category.

This can be useful for future game development projects.

---

## 3. Mini Game Recommendation System

The model receives user and game features and predicts whether the user will like the game.

Example features:

- likes strategy games;
- likes RPGs;
- prefers short games;
- the game is turn-based;
- the game is free;
- the game is difficult.

---

## 4. Simple Game Balance Model

The model predicts whether an item is too strong based on its stats.

Example features:

- damage;
- attack speed;
- rarity;
- cost;
- player level.

---

## 5. Simple Image Recognition

Possible tasks:

- circle / square / triangle classification;
- tile type recognition;
- simple game icon classification.

---

# Project Goal

The main goal of this project is not to build a complex neural network, but to understand the fundamental PyTorch workflow:

```text
data → model → prediction → loss → backward → optimizer → improved model
```

After understanding this cycle, it will be easier to move on to more complex tasks:

- classification;
- image recognition;
- game-related data;
- recommendation systems;
- custom datasets.

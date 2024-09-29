import torch
import onnx
from transformers import GPT2Model

# Load a pretrained model
model = GPT2Model.from_pretrained('gpt2')

# Dummy input for conversion
dummy_input = torch.randint(0, 1000, (1, 20))  # Example input size

# Export the model to ONNX format
torch.onnx.export(model, dummy_input, "gpt2.onnx", opset_version=11)

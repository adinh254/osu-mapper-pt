import torch
x = torch.rand(5, 3)
print(x)

print("CUDA is Enabled." if torch.cuda.is_available() else "CUDA is Disabled.")

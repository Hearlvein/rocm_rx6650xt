import time
import torch

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using: {device}")
if device.type == "cuda":
    print(torch.cuda.get_device_name(0))
    print(f"VRAM: {torch.cuda.get_device_properties(0).total_memory / 1e9:.1f} GB")

# Put some real load on the GPU: repeated large matrix multiplications
n = 4096
a = torch.randn(n, n, device=device)
b = torch.randn(n, n, device=device)

for _ in range(3):  # warm-up
    a @ b
if device.type == "cuda":
    torch.cuda.synchronize()

start = time.time()
for _ in range(50):
    a @ b
if device.type == "cuda":
    torch.cuda.synchronize()  # GPU runs async, so wait before stopping the clock
elapsed = time.time() - start

print(f"50 matmuls of {n}x{n}: {elapsed:.2f}s ({50 * 2 * n**3 / elapsed / 1e12:.2f} TFLOPS)")
# ROCm on the AMD Radeon RX 6650 XT

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A minimal [uv](https://docs.astral.sh/uv/) project that gets **PyTorch running on the AMD Radeon RX 6650 XT (`gfx1032`)** with ROCm 7.14.0, using a single command.

| Component   | Version                                    |
| ----------- | ------------------------------------------ |
| GPU         | AMD Radeon RX 6650 XT (`gfx1032`, RDNA 2)  |
| Python      | 3.13                                       |
| ROCm        | 7.14.0                                     |
| PyTorch     | 2.12.0+rocm7.14.0                          |
| torchvision | 0.27.0+rocm7.14.0                          |
| torchaudio  | 2.11.0+rocm7.14.0                          |
| Triton      | 3.7.1+rocm7.14.0                           |

## Why this repo exists

The RX 6650 XT (`gfx1032`) is easy to get wrong with ROCm and PyTorch. This project pins a working, tested set of gfx1032 wheels (PyTorch, torchvision, and the ROCm SDK) so that `uv sync` gives you a working GPU environment without manual wheel hunting.

## Quick start

Requirements: Linux, [uv](https://docs.astral.sh/uv/getting-started/installation/), and the `amdgpu` kernel driver loaded.

```bash
git clone https://github.com/Hearlvein/rocm_rx6650xt.git
cd rocm_rx6650xt
uv sync
uv run gpu.py
```

`uv sync` creates the virtual environment and installs everything, including the gfx1032 builds of PyTorch and the ROCm SDK (about 50 packages).

## Verify it works

`gpu.py` checks that PyTorch sees the GPU and runs a quick matmul benchmark.

Expected output:

```text
Using: cuda
AMD Radeon RX 6650 XT
VRAM: 8.6 GB
50 matmuls of 4096x4096: 1.01s (6.80 TFLOPS)
```

> **Note:** PyTorch reports `cuda` because ROCm builds reuse the `torch.cuda` API through HIP. This is expected on AMD GPUs.

The benchmark figure was measured on my machine. Yours will vary with clocks, cooling, and drivers.

## Using it in your own project

```python
import torch

device = torch.device("cuda")  # this is your Radeon GPU
x = torch.randn(4096, 4096, device=device)
y = x @ x
```

To reuse these wheels in another uv project, copy the relevant index and source settings from [`pyproject.toml`](pyproject.toml).

## Tested environment

- GPU: AMD Radeon RX 6650 XT (8 GB)
- OS: CachyOS (Arch-based, rolling release)
- Kernel: 7.2.9-1-cachyos (uses the in-kernel `amdgpu` driver)
- Python: 3.13.16 (CPython, managed by uv)

Other recent Linux distributions with the `amdgpu` driver should work, but only the setup above has been tested.

## Troubleshooting

- **`Using: cpu`**: PyTorch can't see the GPU. Check that `/dev/kfd` exists and that your user is in the `render` and `video` groups:
```bash
  groups
  sudo usermod -aG render,video $USER   # then log out and back in
```
- **Out of memory**: the card has 8 GB of VRAM, so reduce batch sizes or use mixed precision.
- **Wrong Python version**: the project pins Python 3.13 via `.python-version`, and uv will fetch it automatically.

## Contributing

Issues and pull requests are welcome, especially test reports from other RDNA 2 cards (RX 6600 / 6600 XT and similar).

## License

[MIT](LICENSE)

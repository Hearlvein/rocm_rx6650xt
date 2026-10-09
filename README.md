❯ uv sync
Using CPython 3.13.16
Creating virtual environment at: /home/james/dev/.venv
Resolved 65 packages in 2.30s
      Built rocm-rx6650xt @ file:///home/james/dev/rocm_rx6650xt                                                                           Prepared 1 package in 4ms
Installed 51 packages in 701ms
 + amd-torch-device-gfx1032==2.12.0+rocm7.14.0
 + amd-torchvision-device-gfx1032==0.27.0+rocm7.14.0
 + asttokens==3.0.2
 + comm==0.2.3
 + debugpy==1.8.22
 + executing==2.2.1
 + filelock==3.29.1
 + fsspec==2026.4.0
 + ipykernel==7.4.0
 + ipython==9.17.1
 + ipython-pygments-lexers==1.1.1
 + jedi==0.20.0
 + jinja2==3.1.6
 + jupyter-client==8.10.0
 + jupyter-core==5.9.1
 + markupsafe==3.0.3
 + matplotlib-inline==0.2.2
 + mpmath==1.3.0
 + nest-asyncio2==1.7.4
 + networkx==3.6.1
 + numpy==2.4.4
 + packaging==26.3
 + parso==0.8.7
 + pexpect==4.9.0
 + pillow==12.2.0
 + platformdirs==4.12.4
 + prompt-toolkit==3.0.53
 + psutil==7.2.2
 + ptyprocess==0.7.0
 + pure-eval==0.2.4
 + pygments==2.21.0
 + python-dateutil==2.9.0.post0
 + pyzmq==27.2.0
 + rocm==7.14.0
 + rocm-bootstrap==0.1.0
 + rocm-rx6650xt==1.0.0 (from file:///home/james/dev/rocm_rx6650xt)
 + rocm-sdk-core==7.14.0
 + rocm-sdk-device-gfx1032==7.14.0
 + rocm-sdk-libraries==7.14.0
 + setuptools==81.0.0
 + six==1.17.0
 + stack-data==0.6.3
 + sympy==1.14.0
 + torch==2.12.0+rocm7.14.0
 + torchaudio==2.11.0+rocm7.14.0
 + torchvision==0.27.0+rocm7.14.0
 + tornado==6.5.10
 + traitlets==5.16.1
 + triton==3.7.1+git0263a6a6.rocm7.14.0
 + typing-extensions==4.15.0
 + wcwidth==0.9.2
 
❯ uv run gpu.py
Using: cuda
AMD Radeon RX 6650 XT
VRAM: 8.6 GB
50 matmuls of 4096x4096: 1.01s (6.80 TFLOPS)

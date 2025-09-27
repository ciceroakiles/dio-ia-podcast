FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04

RUN apt update && apt install -y python3 python3-pip python-is-python3 git

RUN pip install --upgrade pip
RUN pip install git+https://github.com/huggingface/parler-tts.git
RUN pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
RUN pip install transformers accelerate huggingface_hub
RUN pip install pydub ffmpeg

WORKDIR /workspace
COPY main.py /workspace
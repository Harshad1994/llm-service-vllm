# Introduction

FastAPI Service built to offer different LLM models as a service.
The models use paged attention for fast inference speeds.

# Getting Started

1. Clone the repository
2. Install requisite packages from requirements.txt
3. Run the main.py with arguments

# Run the service

Simply run main.py with following arguments

To RUN Llama-2-13b-hf
```
python main.py --model meta-llama/Llama-2-13b-hf --tensor-parallel-size 4 --download-dir /datadisk/harshad/download_dir --gpu-memory-utilization 0.6

```

To RUN Llama-2-70b-hf   using awq quantization
```
python main.py --model TheBloke/Llama-2-70B-chat-AWQ --tensor-parallel-size 4 --download-dir /datadisk/llms/model_dir --gpu-memory-utilization 0.6 --quantization awq
```

arguments
```
--model ---> Model name from huggingface
--tensor-parallel-size  ----> No of gpu devices to utilize
--download_dir  ----> path of directory to store models
--gpu-memory-utilization ---->  How much percent of total gpu memory to utilize
--quantization  ---> AWQ, GPT-Q etc

```
# Contribute
TODO: Describe how to contribute to the service

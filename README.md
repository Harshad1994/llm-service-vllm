# llm_service_vLLM
FastAPI Service built to offer different LLM models as a service. The serivce is built on vllm repo. 


# How to run
simply run following script with arguments.

python main.py --model meta-llama/Llama-2-13b-hf --tensor-parallel-size 4 --download-dir /datadisk/harshad/download_dir --gpu-memory-utilization 0.6

--model ---> Model name from huggingface
--tensor-parallel-size  ----> No of gpu devices to utilize
--download_dir  ----> path of directory to store models
--gpu-memory-utilization ---->  How much percent of total gpu memory to utilize
--quantization  ---> AWQ, GPT-Q etc



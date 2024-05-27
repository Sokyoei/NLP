# Llama3

下载 `llama3` 源码

```shell
git clone https://github.com/meta-llama/llama3
cd llama3
```

<!-- 下载模型文件（需要进入 llama3 官网申请）

在 [huggingface] 申请

```shell
bash ./download.sh
``` -->

下载 [Llama-Chinese] llama3 中文大模型

```shell
git clone https://www.modelscope.cn/FlagAlpha/Llama3-Chinese-8B-Instruct.git
cd Llama3-Chinese-8B-Instruct
git lsf pull
```

conda 创建环境并安装依赖

```shell
conda create -n llama python=3.10
conda activate llama
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
pip install transformers
```

使用 [ollama] 部署

[huggingface]: https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct
[ollama]: https://ollama.com/
[Llama-Chinese]: https://github.com/LlamaFamily/Llama-Chinese

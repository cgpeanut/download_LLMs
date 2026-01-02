---
quantized_by: ubergarm
pipeline_tag: text-generation
base_model: mistralai/Devstral-Small-2-24B-Instruct-2512
license: apache-2.0
base_model_relation: quantized
tags:
- ik_llama.cpp
- imatrix
- mistral3
- mistral-common
---

## imatrix Quantization of mistralai/Devstral-Small-2-24B-Instruct-2512
*NOTE* `ik_llama.cpp` can also run your existing GGUFs from bartowski, unsloth, mradermacher, etc if you want to try it out before downloading my quants.

Some of ik's new quants are supported with [Nexesenex/croco.cpp](https://github.com/Nexesenex/croco.cpp) fork of KoboldCPP with Windows builds for CUDA 12.9. Also check for [Windows builds by Thireus here.](https://github.com/Thireus/ik_llama.cpp/releases) which have been CUDA 12.8.

These quants provide best in class perplexity for the given memory footprint.

## Big Thanks
Shout out to Wendell and the **Level1Techs** crew, the community [Forums](https://forum.level1techs.com/t/deepseek-deep-dive-r1-at-home/225826), [YouTube Channel](https://www.youtube.com/@Level1Techs)!  **BIG thanks** for providing **BIG hardware** expertise and access to run these experiments and make these great quants available to the community!!!

Also thanks to all the folks in the quanting and inferencing community on [BeaverAI Club Discord](https://huggingface.co/BeaverAI) and on [r/LocalLLaMA](https://www.reddit.com/r/LocalLLaMA/) for tips and tricks helping each other run, test, and benchmark all the fun new models! Thanks to huggingface for hosting all these big quants!

Finally, I *really* appreciate the support from [aifoundry.org](https://aifoundry.org) so check out their open source RISC-V based solutions!

## Quant Collection

## IQ4_KSS 12.069 GiB (4.398 BPW)

<details>

<summary>👈 Secret Recipe</summary>

```bash
#!/usr/bin/env bash

custom="
## Attention
## Keep qkv the same to allow --merge-qkv
blk\..*\.attn_q.*\.weight=iq6_k
blk\..*\.attn_k.*\.weight=iq6_k
blk\..*\.attn_v.*\.weight=iq6_k
blk\..*\.attn_output.*\.weight=iq6_k

## Dense Layers
blk\..*\.ffn_down\.weight=iq4_ks
blk\..*\.ffn_(gate|up)\.weight=iq4_kss

## Non-Repeating layers
token_embd\.weight=iq4_k
output\.weight=iq6_k
"""

custom=$(
  echo "$custom" | grep -v '^#' | \
  sed -Ez 's:\n+:,:g;s:,$::;s:^,::'
)

./build/bin/llama-quantize \
    --custom-q "$custom" \
    --imatrix /mnt/raid/models/ubergarm/Devstral-Small-2-24B-Instruct-2512-GGUF/imatrix-Devstral-Small-2-24B-Instruct-2512-BF16.dat \
    /mnt/raid/models/ubergarm/Devstral-Small-2-24B-Instruct-2512-GGUF/Devstral-Small-2-24B-Instruct-2512-BF16.gguf \
    /mnt/raid/models/ubergarm/Devstral-Small-2-24B-Instruct-2512-GGUF/Devstral-Small-2-24B-Instruct-2512-IQ4_KSS.gguf \
    IQ4_KSS \
    24
```

</details>

## Quick Start
For examples check out quickstart on my
[ubergarm/GLM-4.7-GGUF](https://huggingface.co/ubergarm/GLM-4.7-GGUF#quick-start)
repo. Keep in mind this is a *dense* model and *not* and MoE so will
benefit from full GPU offload. Check out ik's latest `-sm graph`
"tensor parallel" feature as well and use `-t 1` when full GPU offload.

Finally, I feel like there are some tool calling / MCP / agentic use issues. When testing with my local `pydantic-ai` framework the server throws issues like `Common part does not match fully`. You might need to check into newer PRs on mainline or possibly something like this from bartowski [bartowski/llama.cpp](https://github.com/ggml-org/llama.cpp/compare/master...bartowski1182:llama.cpp:master) so YMMV. Good luck!

## References
* [ik_llama.cpp](https://github.com/ikawrakow/ik_llama.cpp)
* [Getting Started Guide (already out of date lol)](https://github.com/ikawrakow/ik_llama.cpp/discussions/258)
* [ubergarm-imatrix-calibration-corpus-v02.txt](https://gist.github.com/ubergarm/edfeb3ff9c6ec8b49e88cdf627b0711a?permalink_comment_id=5682584#gistcomment-5682584)
* [llama.cpp PR17889](https://github.com/ggml-org/llama.cpp/pull/17889)

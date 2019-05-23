import tensorflow에서 벗어나기
################################
:date: 2019-03-15 20:25
:category: blog,
:tags: ai
:slug: tensorflow
:excerpt: 


Sutton 교수님께서 70년간 AI 연구자들이 반복한 실수와 그로부터 우리가 배워야 하는 것에 대한 글 `<The Bitter Lesson> <http://www.incompleteideas.net/IncIdeas/BitterLesson.html>`__ 을 공유했다. 글을 관통하는 메세지는 체스, 바둑 같은 역사적 사례에서 볼 수 있듯이 인공지능의 혁신은 언제나 computation에 있었다는 것. General하고 scalable한 알고리즘만이 생존하고 세상을 바꾼다는 것.

GPU 1개로 논문을 구현할 수 있었던 1, 2년 전과 달리 지금은 DGX 하나로도 SOTA를 찍기 어려워졌다. 돈이 없으면 논문 하나도 제대로 구현 못 하는데, DGX가 있더라도 full로 쓰는 법을 모르면 빛 좋은 개살구일 뿐이다. 하지만 딥러닝의 기초, 퍼셉트론, LSTM 정도의 튜토리얼이 수도 없이 재생산되고 +0.3% SOTA 같은 쓸데없는 정보들이 공유되는 환경에서 optimization이나 low-level 엔지니어링에 대한 필요성을 느끼거나 정보를 얻기란 굉장히 어렵다.

나를 예를 들면, 적당히 모델을 학습시킬 때 GPU-utilization이 90% 이상을 찍고 있지 않다면 어딘가에 bottleneck이 있고, 그걸 프로파일러로 찾을 수 있다는 것, 그래프를 cpu에 먼저 넣고 컴파일해서 gpu에 넣으면 OOM을 피할 수 있다거나, `tf.Defun <https://github.com/tensorflow/tensorflow/blob/32edfdd8e4d24db2a3789c85227f1887e4faca95/tensorflow/python/framework/function.py#L45>`__ 같은 걸 언제 왜 써야 하는지, `fp16 <https://docs.nvidia.com/deeplearning/sdk/mixed-precision-training/>`__ 과 `sparsity <https://openai.com/blog/block-sparse-gpu-kernels/>`__ 가 왜 중요한지, `Adam <https://arxiv.org/abs/1412.6980>`__ 과 `adafactor <https://arxiv.org/abs/1804.04235>`__ 가 어떻게 다른지, tf.cast 같은 함수가 얼마나 비효율적인지, `tf.custom_gradient <https://www.tensorflow.org/api_docs/python/tf/custom_gradient>`__ 와 `custom op <https://www.tensorflow.org/guide/extend/op>`__ 으로 어떻게 그런 비효율을 없앨 수 있는지 따위를 알아야 한다는 걸 몰랐다.

만약 세상의 "진짜" 문제를 “직접” 풀고 싶지만 논문을 읽고 구현하는데 매너리즘에 빠져다면, import tensorflow에서 벗어나 compute에 대해 고민해보는게 도움이 될 것 같다. `Tensor Core <https://www.nvidia.com/en-us/data-center/tensorcore/>`__ 와 같은 하드웨어에 대한 이해부터 MPI, `NCCL <https://docs.nvidia.com/deeplearning/sdk/nccl-developer-guide/docs/index.html>`__, `fp16 <https://docs.nvidia.com/deeplearning/sdk/mixed-precision-training/>`__ 과 `sparsity <https://openai.com/blog/block-sparse-gpu-kernels/>`__ 와 `TensorFlow XLA <https://www.tensorflow.org/xla>`__, `Mesh TensorFlow <https://github.com/tensorflow/mesh/>`__, `Horovod <https://github.com/horovod/horovod>`__ 등으로 Data/Model parallelization를 하는 것, Adafactor, `Blocksparse <https://openai.com/blog/block-sparse-gpu-kernels/>`__, `Gradient recompute <https://github.com/openai/gradient-checkpointing>`__, `nvprof <http://docs.nvidia.com/cuda/profiler-users-guide/index.html>`__ 따위로 memory optimization과 Compute/Network/Pipeline bandwidth에서 bottleneck을 없애는 것. 그리고 `Transformer-xl <https://arxiv.org/abs/1901.02860>`__, `BigGAN <https://arxiv.org/abs/1809.11096>`__, `GPT-2 <https://openai.com/blog/better-language-models/>`__ 와 같은 논문들 뒤에 보이지 않는 엔지니어링을 생각하고, 찾아보고, 구현하는 것.

`GPT-2 <https://openai.com/blog/better-language-models/>`__ 가 보여주었듯이 scalable한 모델을 만들고 다룰 수 있느냐 없느냐에 따라 풀 수 있는 문제의 범위와 그 결과가 크게 바뀐다. 세상이 바뀌듯 우리도 변해야 한다.

- The Bitter Lesson: http://www.incompleteideas.net/IncIdeas/BitterLesson.html
- Mesh TensorFlow: https://www.youtube.com/watch?v=HgGyWS40g-g
- Horovod: https://github.com/horovod/horovod
- TF custom op: https://www.tensorflow.org/guide/extend/op
- TF performance: https://www.tensorflow.org/guide/performance/overview
- Tensorpack: https://github.com/tensorpack/benchmarks/tree/master/DCGAN
- Tensor cores: https://stackoverflow.com/questions/47335027
- Parallel and Distributed Deep Learning: https://www.youtube.com/watch?v=xtxxLWZznBI
- Blocksparse: https://openai.com/blog/block-sparse-gpu-kernels/
- Gradient checkpoint: https://github.com/openai/gradient-checkpointing

원글: `Facebook <https://www.facebook.com/carpedm20/posts/2102786876467493>`__

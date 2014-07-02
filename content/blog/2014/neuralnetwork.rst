Neural Network
##############
:date: 2014-06-29 23:04
:category: machine learning,
:tags: machine learning
:excerpt: 

Neural network란 무엇인가?
~~~~~~~~~~~~~~~~~~~~~~~~~~

신경망 네트워크(Neural network)를 설명하기 전에 인공 뉴런(artificial neuron)의 대표적인 두가지, Perceptron 과 Sigmoid neuron에 대해서 설명하고자 한다.

Perceptron은 x1, x2 ... 와 같은 몇개의 binary input을 받으며 하나의 binary output을 만들어 낸다. Perceptron 아이디어를 만들어낸 Frank Rosenblatt는 w1, w2 ... 와 같이 각 input의 중요도를 나타내는 정수, 즉 weight 를 만들어 냈다. 즉, neuron의 output은 weight와 input의 곱의 합으로 결정이 되며, 그 값이 threshold 값 보다 크면 output이 1이 되고, 작다면 그 반대인 0이 된다.

이러한 Perceptron은 여러개의 layer를 형성하면서 좀더 인간의 neural network와 닮아가게 된다. 

.. _page: http://moliware.com/

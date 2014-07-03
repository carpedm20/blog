[번역] Neural Network를 이용한 손글씨 인지
##########################################
:date: 2014-07-03 10:24
:category: Machine Learning,
:tags: machine learning, neural network, perceptron, sigmoid neuron
:slug: neural-net-translation

http://neuralnetworksanddeeplearning.com/ 에 올라온 챕터을 이해하고 기록하고자 번역 작업을 시작한다. 번역의 속도를 높이기 위해 **수많은** 의역이 포함되어 있다. 

CHAPTER 1 Using neural nets to recognize handwritten digits
-----------------------------------------------------------

인간의 사각계는 이 세계의 불가사의 중 하나다. 잠시 아래의 손글씨들을 잠시 읽어보자.

.. image:: http://neuralnetworksanddeeplearning.com/images/digits.png
   :width: 160 px
   :align: center

대부분의 사람들은 그다지 큰 노력없이 504192 라고 읽을 수 있을 것이다. 하지만 이러한 과정은 생각만큼 쉽지는 않다. 인간 좌뇌 우뇌에서는, V1으로 알려진 일차 시각 피질(primary visual cortex)이 있으며, 이러한 V1은 1억 4천만개의 뉴런과 뉴런 사이에 형성된 100억개의 연결들이 존재한다. 하지만 모든 시각 피질(V2, V3, V4 그리고 V5)의 연결들은 더욱 복잡한 이미지 처리를 하게 된다. 즉, 우리의 머릿속에는 수억년간 진화해온 슈퍼컴퓨터가 있으며, 시각적 세계를 이해하는데 매우 적합하게 진화해 왔다. 다시 손글씨 숫자들 이야기로 돌아가면, 숫자륵 읽는 것은 쉽지 않은 과정이다. 하지만, 우리 인간은 두 눈이 보여주는 것들을 꽤나 자연스럽게 이해해 왔다. 이러한 과정은 무의식 중에 일어나기 때문에 우리는 시각계의 문제를 해결하는 것이 얼마나 어려운지를 알아채지 못하곤 한다.

시각적 패턴 인지의 어려움은 위의 예시처럼 손으로 쓴 숫자들을 읽는 컴퓨터 프로그램을 만들려고 할 때 명백해 진다. 우리가 쉽게 생각했던 것이 급격하게 어려워 보일것이다. 우리가 모양을 인지하는 과정을 간략하게 보면, "9는 위쪽에 곡선이 있고 오른쪽 아래에는 수직선이 있다", 일 것이고 알고리즘으로 설명하기에는 쉽지가 않아 보인다. 당신이 그런 규칙들을 정확하게 만들다 보면, 수많은 경고와 에러의 늪, 그리고 예외적인 케이스 문제에 쉽게 빠져 버리고 말 것이다. 절망적이군..

Neural Network는 이러한 문제를 다른 방식으로 접근한다. 핵심은 training example이라 불리는 많은 양의 손글씨 숫자들을 가지고:

.. image:: http://neuralnetworksanddeeplearning.com/images/mnist_100_digits.png
   :width: 440px
   :align: center


숫자를 인지하는 방법을 배우는 시스템을 만드는 것이다. 즉, neural network는 주어진 예시들을 이용해 손글씨 숫자 인지를 위한 규칙을 자동적으로 만들어 낸다. 또한, training example의 수를 늘림으로써 network는 손글씨에 대해 더욱 많이 배우면서 정확도를 높일 수 있다. 그래서 위에 제시된 100개의 예시 외에 수천 수만개의 training example을 사용하면 더욱 좋은 손글씨 인지 시스템을 만들 수 있게 될 것이다.

이 챕터에서는 neural network를 사용해 손글씨 숫자를 인지하는 컴퓨터 프로그램을 만들게 된다. 프로그램은 74 줄 밖에 안되며, 특별한 neural network 라이브러리를 전혀 사용하지 않는다. 하지만 이 짧은 프로그램은 사람의 중재없이  96프로의 정확도를 보여준다. 그리고 이후의 챕터에서는 정확도를 99프로로 높이게 된다. 실제로 뛰어난 상업 neural network는 은행에서 수표를 읽거나 우체국에서 주소를 읽는데 사용이 된다.

우리가 손글씨 인지에 집중하는 이유는 neural network의 전반적인 이해에 도움이 되는 훌륭한 문제이기 때문이다. 문제로써 가장 좋은 이유는 바로 우리의 도전의식을 북돋기 때문이다. 그리고 deep learning과 같이 더욱 발전된 기술들을 이해하는데 도움이 된다. 이 책의 후반부에는, 컴퓨터 비전, 음성 인식, 자연어 처리 등의 다양한 분야에서 이러한 아이디어가 어떻게 적용되는지를 공부하게 될 것이다.

만약 이 챕터의 목적이 단순히 손글씨 숫자를 인지하는 프로그램을 짜는것이라면, 이 챕터는 훨씬 짧았을 것이다! 하지만 perceptron과 sigmoid neuron과 같은 인공 뉴런과 neural network의 일반적인 러닝 알고리즘인 stochastic gradient descent와 같이 neural network의 핵심이 되는 아이디어들을 공부하게 될 것이다. 따라서 나는 왜 아이디어들이 그렇게 정의가 되었는지를 설명하고 여러분들이 neural network에 대한 직관을 형성하는데 집중할 것이다. 그렇기 때문에 단순한 매커니즘을 설명할 때 보다 더 많은 설명을 추가하게 되었지만 (역자는 고통 받는다...), 여러분들의 깊은 이해를 위해서는 꼭 필요한 것들이다. 이 챕터를 다 읽고 나면, deep learning은 무엇이고 왜 중요한지를 이해하기 위한 준비가 될 것이다.


Perceptrons
-----------


Neural Network란 무엇인가? 먼저 시작하기 전에, 나는 인공 뉴런(artificial neuron)의 한 종류인 Perceptron에 대해서 설명하고자 한다. Perceptron은 `Warren McCulloch`_ 와 `Walter Pitts`_ 의 초기 `작업 <http://scholar.google.ca/scholar?cluster=4035975255085082870>`_ 에 영감을 받아 1950, 60년대에 과학자 `Frank Rosenblatt`_ 에 의해  `개발 <http://books.google.ca/books/about/Principles_of_neurodynamics.html?id=7FhRAAAAMAAJ>`_ 되었다. 하지만 최근에는 perceptron 보다는 다른 인공 뉴런 모델을 주로 사용한다. 이 책에서 뿐만 아니라 오늘날 사용되는 대부분의neural network는 sigmoid neuron을 주로 사용한다. 우리는 조만간 sigmoid neuron에 대해 자세히 다룰것이지만, sigmoid neuron이 왜 정의가 되었는지 이해하기 전에 perceptron에 대해서 먼저 이해해 보도록 하자.

그렇다면 perceptron은 어떻게 작동하는 것일까? 하나의 perceptron은 여러개의 binary input인 x1, x2 ...를 받으며, 하나의 binary output을 만들어 낸다:

.. image:: http://neuralnetworksanddeeplearning.com/images/tikz0.png
   :align: center

위의 예시에서는 x1, x2, x3를 input으로 받는다. 일반적인 경우, 이보다 더 많거나 적은 input들을 받을 수 있다. Rosenblatt은 output을 계산하는 하나의 공식을 제시했다. 그는 w1, w2.. 와 같이 각 input의 상대적 중요도를 나타내는  weight를 소개했다. 뉴런의 output인 0 또는 1은 각 weight와 input들의 곱의 합이 정해진 threshold 값 보다 크거나 작은지에 따라 결정된다. wieght와 같은 다른 parameter처럼  threshold는 실수값을 가진다. 이를 수식으로 설명하면:

.. raw:: html

   <a class="displaced_anchor" name="eqtn1"></a>\begin{eqnarray}
   \mbox{output} & = & \left\{ \begin{array}{ll}
         0 & \mbox{if } \sum_j w_j x_j \leq \mbox{ threshold} \\
         1 & \mbox{if } \sum_j w_j x_j > \mbox{ threshold}
         \end{array} \right.
   \tag{1}\end{eqnarray}

이것이 perceptron이 작동하는 방법의 전부다!

Perceptron은 기본적은 수학 모델이다. Perceptron은 input의 중요도에 의해 결정되는 하나의 장치라고 생각할 수 있다. 이제 예를 하나 들어보자. 사실 현실적인 예는 아니지만, 여러분들이 perceptron을 이해하는데에는 도움을 줄 것이며, 추후에 좀 더 사실적인 예도 제시할 것이다. 먼저 주말이 오고 있고, 당신의 도시에 치즈 축제가 열린다고 가정해 보자. 당신은 치즈를 좋아하며, 축제에 갈것인지 안갈건지를 결정하려고 한다. 당신은 세가지 요소를 고려해 결정을 내리게 된다:

   1. 날씨가 좋은가?
   2. 당신의 남자친구 혹은 여자친구가 당신과 같이가려고 하는가?
   3. 축제가 대중 교통 근처에 있는가? (당신은 차를 가지고 있지 않다)

우리는 이 세가지 요소들을 x1, x2, x3 라고 표현할 것이다. 예를들어, x1 = 1은 날씨가 좋다는 뜻이며, w1 = 0은 나쁘다는 뜻이다. 비슷하게, x2 = 1이면 당신의 연인이 가고싶어 한다는 뜻이고, x2 = 0 이면 가기 싫어한다는 것이다. x3의 경우에도 마찬가지이다.

이제, 당신은 틀림없이 치즈를 좋아하고, 당신의 연인이 축제가 가기 싫어하더라도, 대중 교통 근처에 없더라도 기꺼이 축제에 가고싶다고 생각해보자. 하지만 아마 당신은 나쁜 날씨를 혐오하며, 날씨가 나쁜 경우 당신이 축제에 갈 방법이 없다고 생각해보자. 그러면 여러분은 perceptron을 사용해서 이러한 의사 결정 모델을 만들 수 있다. 한가지 방법은 w1 =6, w2 = 2, w3 = 2로 parameter를 설정하는 것이다. 다른 값들보다 더 큰 값을 가진 w1 이 날씨가 연인의 결정과 대중교통의 가까움 보다 훨씬 더 중요하다는 것을 나타낸다. 마지막으로, threshold 를 5로 정했다고 생각해 보자. 이러한 perceptron은 날씨가 좋다면 output은 항상 1이 되며, 날씨가 나쁘다면 항상 0이 된다. 즉, 연인의 결정과 대중교통의 가까움은 output에 전혀 영향을 끼지지 않는다는 것을 의미한다.

wieght와 threshold를 바꿔가면서, 우리는 다른 의사 결정 모델을 만들 수 있다. 예를들어, threshold 를 3으로 정했다고 가정해보자. 그렇다면 perceptron은 날씨가 좋을땐 언제든지 혹은 교통 수단과 연인의 의사 조건이 맞았을 때 축제에 참가할 수 있게 될 것이다. 이런 방법으로 전혀 다른 의사 결정 모델을 만들 수 있다. threshold 를 줄이는 것은 당신이 축제에 더욱 가고싶다는 의미를 나타낸다.

하지만 perceptron은 인간의 의사결정 모델과는 전혀 닮지 않았다! 하지만 위의 예시가 의미하는 바는 perceptron이 결정들을 만들기 위해서 어떻게 다른 요소들을 계산하는지를 보여준다. 또한, 복잡한 perceptron 네트워크를 구축한다면 미묘한 결정을 내릴 수 있게 될 것이다.

.. image:: http://neuralnetworksanddeeplearning.com/images/tikz1.png
   :align: center

위에 보이는 네트워크에서는, 첫번째 열의 perceptron들이 input에 중요도를 계산해 3개의 간단한 결정을 내린다. 여기서 첫번째 열의 perceptron들을 첫번째 층(layer) perceptron 이라 부르겠다. 그렇다면 두번째 층에 있는 perceptron들은 무엇을 하는가? 각각의 perceptron 은 첫번째 층에서 만들어진 의사 결정들을 토대로 새로운 결정을 만들어 낸다. 이러한 방법으로 두번째 층의 perceptron은 첫번째 층보다 더욱 복잡하고 추상적인 레벨의 결정을 내릴 수 있다.마찬가지로 세번째 층의 perceptron 은 더더욱 복잡한 결정을 내릴 것이다. 이러한 방식으로, 다층 레이어의 perceptron 네트워크는 세련된 의사 결정을 내릴 수 있는 것이다.

그런데, 나는 perceptron을 하나의 output 만 만들어 내는 모델이라고 정의를 내렸다. 하지만 위의 네트워크는 여러개의 output 들을 만들어 내는 것 처럼 보인다. 사실, 그것들은 여전히 하나의 output 이다. 여러개의 output 화살표들은 단지 다른 perceptron에서의 output을 input으로 사용되는 것을 나타낼 때 유용할 뿐이다.

.. raw:: html

   <p>이제 perceptron 을 좀더 간단한 방법으로 정리해보자. $\sum_j w_j x_j > \mbox{threshold}$ 은 다소 다루기 어려운 식이며, 우리는 이것을 두개의 식으로 나눠 간단하게 할 수 있다. 가장 첫번째 변화는 $\sum_j w_j x_j$ 를 $w \cdot x \equiv \sum_j w_j x_j$ 처럼 하나의 점곱(dot product = scalar product)으로 바꾸는 것이다. 여기서 w 와 x 는 각각 weight 와 input 의 벡터가 된다. 두번째 변화는 threshold 항을 식의 반대쪽으로 옮기고, $b \equiv-\mbox{threshold}$ 로 나타낼 수 있다. 여기서 b는 bias의 약자이다.</p>

.. raw:: html

   <a class="displaced_anchor" name="eqtn2"></a>\begin{eqnarray}
   \mbox{output} = \left\{ 
      \begin{array}{ll} 
         0 & \mbox{if } w\cdot x + b \leq 0 \\
         1 & \mbox{if } w\cdot x + b > 0
      \end{array}
   \right.
   \tag{2}\end{eqnarray}

여기서 bias는 perceptron이 얼마나 쉽게 1의 output을 만드는지에 대한 척도라고 생각하면 된다. 큰 bias를 가진 perceptron은 쉽게 1이라는 output를 만들 수 있고, 매우 큰 음수의 bias의 경우에는 1의 output을 만들기 어려울 것이다. bias는 perceptron을 설명할 때 큰 비중을 차지하진 않지만 더욱 간단한 식을 만들 수 있게 해준다. 그렇기 때문에 앞으로는 threshold가 아닌 bias를 이용할 것이다.

나는 앞서 perceptron을 input의 중요도를 바탕으로 결정을 내리는 방법이라고 설명했다. 이러한 perceptron은 AND, OR, NAND와 같은 기본적인 논리 계산에도 사용될 수 있다. 예를 들어, 각각의 weight가 -2인 두 input을 가진 perceptron을 생각해 보자. 그리고 여기서 bias는 3이다.

.. image:: http://neuralnetworksanddeeplearning.com/images/tikz2.png
   :align: center


.. raw:: html

   <p>그러면 input이 00 일때 $(-2)*1+(-2)*1+3 = -1$ 의 결과가 양수이기 때문에 1의 output을 만든다. 01과 10의 input에 경우에도 output은 1이 된다. 하지만 11의 input에 대해서는 0의 output을 출력한다. 이는 $(-2)*1+(-2)*1+3 = -1$ 가 음수이기 때문이다. 그래서 우리는 perceptron을 이용해서 NAND 게이트를 만들었다!</p>

NAND 게이트 예제는 perceptron을 간단한 논리 계산에 사용될 수 있음을 보여준다. 사실, 그 어따한 논리 계산도 perceptron으로 표현될 수 있다. 왜나하면 NAND 게이트로 어떠한 계산도 할 수 있기 때문이다.

.. image:: http://neuralnetworksanddeeplearning.com/images/tikz3.png
   :align: center

위와 같은 NAND 게이트를 perceptron으로 표현하기 위해선, 각 weight 가 -2이고 bias가 3인 perceptron을 사용하면 된다. 아래 그림은 완성된 network를 보여준다.

.. image:: http://neuralnetworksanddeeplearning.com/images/tikz4.png
   :align: center



( .. 진행중 .. )

.. _Frank Rosenblatt: http://en.wikipedia.org/wiki/Frank_Rosenblatt
.. _Warren McCulloch: http://en.wikipedia.org/wiki/Warren_McCulloch
.. _Walter Pitts: http://en.wikipedia.org/wiki/Walter_Pitts


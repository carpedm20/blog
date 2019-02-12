딥러닝 논문 구현에 대한 생각
############################
:date: 2018-10-26 23:04
:category: blog,
:tags: ai
:slug: paper-implementation
:excerpt: 


.. raw:: html

   <div class="pure-g">
      <iframe class="align-center" src="//www.slideshare.net/slideshow/embed_code/key/at2f2YgI8ftkdv" width="595" height="373" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe>
   </div>
   <br/>

저는 TensorFlow가 공개된 2015년 11월부터 지금까지 여러 편의 논문을 구현하고 오픈 소스들을 읽으면서 많은 것을 배울 수 있었습니다. 다양한 분야의 연구자들이 어떤 고민을 하고 있는지, 특정 분야에서만 사용되는 노하우가 어떤 것이 있는지를 알 수 있었고, 몇 날 며칠을 같은 코드를 디버깅하면서 생긴 요령도 지금 하는 연구에 큰 도움이 되고 있습니다.

하지만 논문 구현 자체는 문장과 수식을 코드로 번역하는 과정으로, 익숙해지면 생각 없이 기계적으로 할 수 있는 단순 반복 작업이 될 수 있습니다. 연구자들을 성장하게 만든 "실패의 과정"은 생략하고 정답만 재현하는 것이기 때문에, 많이 빨리 구현하는 것보단 논문에선 보이지 않는 저자의 의도를 파악하고 정답을 끌어낸 수많은 실패를 상상해 보는 것이 더 중요한 것 같습니다. 그리고 비슷한 논문을 계속 구현하면 새로 배우는 것이 점점 없어지기 때문에 다른 분야에서 더 복잡한 논문을 구현하는 것도 중요합니다.

하지만 저는 숫자와 속도에 너무 집착했었고 비판적 사고 없이 뇌를 비우고 구현하며 시간만 때운 경우가 많았습니다. 저와 비슷한 실수를 하시는 분이 없으면 좋겠고, 계속해서 구현을 즐기고 이야기할 수 있는 분들이 많아졌으면 좋겠습니다.

마지막으로 OpenAI의 `Greg Brockman <https://twitter.com/gdb>`_ 과 `Ilya Sutskever <https://twitter.com/ilyasut>`_ 가 구현에 관해 쓴 `글 <https://www.quora.com/What-are-the-best-ways-to-pick-up-Deep-Learning-skills-as-an-engineer/answer/Greg-Brockman>`_ 도 읽어보면 좋을 것 같습니다.

원글: `Facebook <https://www.facebook.com/groups/TensorFlowKR/permalink/638778569796538/>`_

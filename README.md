# parametric-bezier-fitting

Aproximação de uma curva de Bézier paramétrica de grau arbitrário (n) a um conjunto de
pontos aleatórios. Coloque um slide-button (variável p) para controlar o número de pontos
(que será igual a p+1, p>3) a serem aproximados pela curva de Bézier, e outro slide-button
para controlar o grau da curva. Os pontos a serem aproximados devem ter suas coordenadas
geradas por um gerador de números aleatórios. Com relação aos parâmetros
correspondentes aos pontos gerados, teremos dois casos para compararmos:
(a). Parametrização uniforme: O valor de parâmetro da curva de Bézier correspondente ao i-
ésimo ponto a ser aproximado é dado por i/p (parametrização uniforme), sendo que o
primeiro ponto terá valor 0 e o último ponto (p+1-ésimo) terá valor de parâmetro 1.
(b). Parametrização pelo comprimento dos segmentos: Após a geração aleatória dos pontos,
calculam-se as distâncias entre os pontos consecutivos, colocando-se numa lista. Em seguida,
somam-se as distâncias para formar o total. E então cria-se uma lista com as distâncias
normalizadas por esse total (vão ficar entre 0 e 1). Encontre pelo MMQ as coordenadas dos
pontos de controle (um MMQ para as abscissas e um MMQ para as ordenadas), desenhe a
curva e exiba o erro residual total para cada tipo de parametrização, sendo este a soma dos
erros nas abscissas e nas ordenadas (e =||A x - b|| para cada dimensão, onde x é a solução aproximada encontrada). Projeto em trio.

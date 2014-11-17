Współczynnik korelacji liniowej
============

Teoria
------
Współczynnik korelacji liniowej Pearsona to znormalizowana wielkość określająca zależność między dwiema zmiennymi losowymi. Obliczany jest jako iloraz kowariancji oraz iloczynu odchyleń standardowych. Podstawowe informacje można znaleźć w [Wikipedii](http://pl.wikipedia.org/wiki/Wsp%C3%B3%C5%82czynnik_korelacji_Pearsona).

Estymator współczynnika Pearsona dla ograniczonych, równolicznych serii danych może zostać wyrażony równaniem[link](http://www.sciweavers.org/tex2img.php?eq=r%3D%5Cfrac%7B%5Csum_%7Bi%3D1%7D%5E%7Bn%7D+%28x_i+-+%5Coverline%7Bx%7D%29%28y_i+-+%5Coverline%7By%7D%29%7D+%7B%5Csqrt%7B%5Csum_%7Bi%3D1%7D%5E%7Bn%7D+%28x_i+-+%5Coverline%7Bx%7D%29%5E2%7D+%5Csqrt%7B%5Csum_%7Bi%3D1%7D%5E%7Bn%7D+%28y_i+-+%5Coverline%7By%7D%29%5E2%7D%7D)


Często stosowane jest jednak przybliżenie określone wzorem  [link](http://latex.codecogs.com/gif.view?%5Ctilde%7Br%7D%3D%5Cfrac%7B%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%20x_i%20y_i%20-%20%5Cfrac%7B%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%20x_i%20%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%20y_i%7D%7Bn%7D%7D%20%7B%20%5Csqrt%7B%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%20x_i%5E2%20-%20%5Cfrac%7B%28%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%20x_i%29%5E2%7D%7Bn%7D%7D%20%5Csqrt%7B%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%20y_i%5E2%20-%20%5Cfrac%7B%28%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%20y_i%29%5E2%7D%7Bn%7D%7D%20%7D)

Zadania
-------

1. Napisz w pythonie funkcję pearson, która obliczy współczynnik korelacji dla znanych ćwiczenia 1. zbiorów preferencji muzycznych. Użyj wzoru przybliżającego współczynnik korelacji. (Dlaczego jest on lepszy do obliczeń?)
 Czy gusta Ani i Boni są podobne? Jak ma się to do odległości manhattan między ich preferencjami?

2. Napisz funkcję  pearsonNumpy, która wykorzysta bibliotekę numpy do obliczenia współczynnika korelacji. Jak bardzo różnią się uzyskane wartości? (wykorzystaj funkcję corrcoef).

Zadanie dla chętnych
---------------------
3*. Zapoznaj się z konsolą pythona w ArcGIS. Następnie wczytaj do katalogu warstwy z Bazy Danych Ogólnogeograficznych (zubożone). 
Znajdź współczynnik korelacji między zaludnieniem polskich powiatów a ich powierzchnią. (lub dowolnej innej zależności)
 



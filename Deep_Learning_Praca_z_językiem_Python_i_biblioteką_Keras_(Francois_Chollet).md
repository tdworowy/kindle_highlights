#### Deep Learning. Praca z językiem Python i biblioteką Keras (Francois Chollet)
      Cały ten proces oparto na głównej idei: znaczenie jest pochodną zależności między parami różnych rzeczy (między słowami języka, pikselami obrazu itd.), a zależności te można opisać przy użyciu funkcji odległości

      Bardziej adekwatna nazwa tej techniki uczenia maszynowego mogłaby mieć formę: warstwowe uczenie reprezentacji, hierarchiczne uczenie reprezentacji, a nawet modele głęboko różniczkowalne lub łańcuchy przekształceń geometrycznych (ta nazwa podkreślałaby to, że najważniejszym elementem uczenia maszynowego jest ciągła przestrzeń przekształceń geometrycznych).

      Powinieneś znać trzy typy sieci: sieci gęstych połączeń, sieci konwolucyjne i sieci rekurencyjne.

      Jedynym prawdziwym niebezpieczeństwem związanym ze współczesną sztuczną inteligencją jest błędne zinterpretowanie możliwości modeli i ich przecenianie. Jedną z fundamentalnych cech ludzkiego umysłu jest tendencja do rzutowania intencji, wiary i wiedzy na otaczające rzeczy. Jeżeli na kamieniu narysujemy uśmiechniętą twarz, to będziemy mieli wrażenie, że ten kamień jest szczęśliwy. W odniesieniu do uczenia głębokiego oznacza to np., że jeżeli uda nam się wytrenować działający poprawnie model generujący podpisy rysunków, to może nam się wydać, że model „rozumie” to, co znajduje się na rysunku. W takim przypadku zostaniemy niemile zaskoczeni przez absurdalne opisy generowane przez model w odniesieniu do obrazów spoza treningowego zbioru danych (patrz rysunek 9.1).

      9.2.3. Wnioski Musisz pamiętać o tym, że tak naprawdę współczesne sieci neuronowe mogą tylko przypisywać punktom przestrzeni X punkty przestrzeni Y poprzez przekształcenia geometryczne o charakterze ciągłym.


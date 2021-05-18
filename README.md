# ConnectFour (Cztery w rzędzie)
*Cztery w rzędzie* ([*Connect Four*](https://en.wikipedia.org/wiki/Connect_Four)) planszowa gra logiczna dla dwóch osób, w której wykorzystuje się planszę o wymiarach 7 x 6 pól. Pierwszy gracz wrzuca swój żeton do wybranej przez niego kolumny. Żeton zajmuje najniższą pozycję. Gracze wrzucają swoje żetony na przemian, aż jeden z nich ułoży cztery żetony w poziomie, pionie lub ukosie. Wygrywa ten gracz, który zrobi to jako pierwszy. Jeżeli natomiast plansza się zapełni, a nie utworzy się żadna czwórka, jest remis. [Wikipedia](https://pl.wikipedia.org/wiki/Czw%C3%B3rki)
Program implementuje zarówno klasyczną wersję gry jak i odmianę [*PopOut*](https://en.wikipedia.org/wiki/Connect_Four#PopOut) z możliwością usuwania żetonów ze spodu planszy.

## Technologie
- Python 3.8.2
- PySide2 5.15.2
- Qt 5.15.2

## Przegląd aplikacji
Okno wyświetla siatkę 7 kolumn x 6 wierszy, przycisk nad i pod każdą kolumną, informacje o stanie rozgrywki (np. *"Player 1 turn!"*), przycisk do rozpoczynania i resetowania gry oraz rozwijalną listę wybory reguł gry. Początkowo pola siatki są puste. Gracze na zmianę wrzucają monety do wybranych przez siebie kolumn. Pola, w których jest żeton gracza 1 są czerwone, pola z żetonami gracza 2 są żółte. Gracze wybierają kolumnę, do której wrzucą żeton klikając przycisk nad nią lub (w przypadku *PopOut*) pod nią, by usunąć swój żeton ze spodu planszy. Wygrywa gracz, który pierwszy ustawi cztery monety w linii (poziomo, pionowo lub po skosie). Gdy gra się skończy, wyświetlane jest okienko z napisem *"Player 1 won!"*, *"Player 2 won!"* lub *"Game drawn!"*. Możliwe jest zresetowanie planszy bez zamykania głównego okna.

## Przegląd kodu
Za logikę gry odpowiadają klasy modelujące rozgrywkę: klasa `ConnectFourBase` jest klasą bazową dla implementacji kompletnych reguł w klasach `ConnectFourClassic` i `ConnectFourPopOut`:
```python
class  ConnectFourBase
class  ConnectFourClassic(ConnectFourBase)
class  ConnectFourPopOut(ConnectFourBase)
```
Rozgrywka toczy się w oknie głównym `MainWindow`, które wyświetla np. planszę i przyciski do gry. Do wyświetlania ważnych komunikatów w trakcie rozgrywki używane jest okienko dialogowe `GameStateDialog`:
```python
class  MainWindow(QMainWindow)
class  GameStateDialog(QDialog)
```
Do obsługi błednego ruchu użytkownika w trakcie gry używana jest klasa wyjątku `WrongMoveException`:
```python
class  WrongMoveException(Exception)
```

## Podsumowanie
Projekt udało się w pełni zrealizować. Wytyczne dla projektu zostały wypełnione i rozwiązanie jest w pełni kompletne. Testy zawarte w pliku `connectfour_test.py` potwierdzają działanie logiki programu.  

## Istotne fragmenty kodu
1. Wyrażenia lambda: https://github.com/sweakpl/connect-four/blob/c48716e2000b34ad9ae50820b29df5f9f5f49089/mainwindow.py#L143-L146
2. Wyrażenia listowe:
3. Klasy:
4. Wyjątki:
5. Moduły:
6. Dekoratory:

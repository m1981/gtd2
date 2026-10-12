# GTD-App — Przypadki użycia

Krótkie opisy (use case briefs) według Cockburna, w terminach ze słownika (slownik.md). Wymagania pochodne każdego przypadku pokazuje generowana macierz slad.md. Identyfikatory UC są niezmienne i nie oznaczają kolejności.

### UC-01 Przechwycić Element

*Poziom:* cel użytkownika (morze) · *Zakres:* G-AKT-01 GTD-App · *Aktor główny:* G-AKT-02 Użytkownik · *Aktor wspierający:* G-AKT-06 Serwer poczty (tylko kanał e-mail)

Użytkownik \[G-AKT-02\] przekazuje GTD-App \[G-AKT-01\] treść dowolnym Kanałem przechwycenia \[G-OPR-03\]. GTD-App wykonuje Przechwycenie \[G-OPR-02\]: tworzy jeden nowy Element \[G-ELM-01\] w Stanie W Inboxie \[G-ELM-03\], nie wymagając Projektu \[G-PRJ-01\], Etykiety \[G-ETK-01\] ani żadnej daty \[G-ATR-04…08\]. Przypadek kończy się, gdy Element jest trwale zapisany i widoczny w Inboxie \[G-ELM-14\]. Użytkownik nie decyduje tu o dalszym losie Elementu; należy to do Doprecyzowania \[G-OPR-04\] w UC-02.

- *Warianty kanału \[G-OPR-03\]:* pole tekstowe, widżet, dyktowanie, udostępnienie z innej aplikacji, adres e-mail \[G-AKT-06\].
- *Do rozstrzygnięcia:* „trwale zapisany” oznacza zapis lokalny na urządzeniu, nie synchronizację (definicja przy CAP-03).

### UC-02 Opróżnić Inbox

*Poziom:* cel użytkownika (morze) · *Zakres:* G-AKT-01 GTD-App · *Aktor główny:* G-AKT-02 Użytkownik · *Aktor wspierający:* G-AKT-05 Kalendarz zewnętrzny (tylko gdy wynikiem jest Zaplanowane i integracja jest włączona) · *Zawiera:* UC-03 Doprecyzować Element (ryba) · *Wywoływany też z:* Przeglądu tygodniowego \[G-OPR-13\]

Użytkownik \[G-AKT-02\] przegląda po kolei Elementy \[G-ELM-01\] w Stanie W Inboxie \[G-ELM-03\] i dla każdego wykonuje Doprecyzowanie \[G-OPR-04\] (UC-03). Każde Doprecyzowanie kończy się dokładnie jednym wynikiem, który zmienia Stan Elementu \[G-ELM-02\] na inny niż W Inboxie; Element nigdy nie wraca do Inboxu. Przypadek kończy się sukcesem, gdy Inbox jest Pusty \[G-ELM-15\]. Użytkownik może przerwać w dowolnym momencie: Elementy już doprecyzowane zachowują nowy Stan, pozostałe zostają W Inboxie.

Możliwe wyniki Doprecyzowania opisuje UC-03.

- *Gwarancja minimalna:* żaden Element nie zostaje utracony; każdy ma po przerwaniu albo nowy Stan, albo nadal W Inboxie.
- *Kolejność:* GTD-App prezentuje Elementy od najstarszego (według chwili Przechwycenia \[G-OPR-02\]). Elementy przechwycone w trakcie (UC-01) dołączają na koniec bieżącego opróżniania.

### UC-03 Doprecyzować Element

*Poziom:* podfunkcja (ryba) · *Zakres:* G-AKT-01 GTD-App · *Aktor główny:* G-AKT-02 Użytkownik · *Zawierany przez:* UC-02, Przegląd tygodniowy \[G-OPR-13\] · *Warunek wstępny:* Element w Stanie W Inboxie \[G-ELM-03\]

Użytkownik \[G-AKT-02\] rozpatruje jeden Element \[G-ELM-01\] w Stanie W Inboxie i wykonuje Doprecyzowanie \[G-OPR-04\]: rozstrzyga, czy Element wymaga działania, i wybiera dokładnie jeden wynik z tabeli poniżej. GTD-App pokazuje jako pierwszą, wyróżnioną opcję „Zrób teraz” \[G-OPR-05\] (D-33). Dla wyników wymagających danych GTD-App prosi tylko o minimum: Datę wykonania \[G-ATR-04\] dla Zaplanowane, Delegata \[G-AKT-03\] dla Czekam na, Rezultat \[G-PRJ-02\] i co najmniej jedno Otwarte działanie \[G-ELM-12\] dla Projektu. Kontekst \[G-ATR-01\], Szacowany czas \[G-ATR-02\], Wymagana energia \[G-ATR-03\] i Lista przygotowania \[G-PRZ-01\] są opcjonalne (D-46). Przy wynikach Następne działanie, Zaplanowane i Czekam na Użytkownik może opcjonalnie wskazać istniejący Projekt Aktywny \[G-PRJ-03\] (D-44). Przypadek kończy się, gdy Element ma nowy Stan \[G-ELM-02\] albo stał się Projektem.

| Wynik Doprecyzowania | Operacja | Stan końcowy |
| --- | --- | --- |
| Wykonane od razu (reguła 2 minut) | G-OPR-05 Wykonanie natychmiastowe | G-ELM-09 Zakończony |
| Jedna czynność do zrobienia w dowolnym momencie | G-OPR-04 Doprecyzowanie | G-ELM-04 Następne działanie |
| Czynność przypisana do dnia lub godziny | G-OPR-04 Doprecyzowanie | G-ELM-05 Zaplanowane |
| Czynność powierzona komuś innemu | G-OPR-07 Delegowanie | G-ELM-06 Czekam na |
| Rezultat wymagający >1 Działania | G-OPR-06 Przekształcenie w Projekt | G-PRJ-03 Projekt Aktywny (Element przestaje istnieć) |
| Bez zobowiązania teraz | G-OPR-04 Doprecyzowanie | G-ELM-07 Kiedyś/może |
| Tylko informacja | G-OPR-04 Doprecyzowanie | G-ELM-08 Referencja |
| Niepotrzebne | G-OPR-10 Przeniesienie do Kosza | G-ELM-10 W Koszu |
| Kilka spraw w jednym Elemencie | G-OPR-15 Podział | nowe Elementy W Inboxie; Element pierwotny przestaje istnieć |

- *Gwarancja minimalna:* anulowanie zostawia Element W Inboxie bez zmian; Element nie traci treści.
- *Gwarancja sukcesu:* Element ma dokładnie jeden nowy Stan albo został Podzielony; nigdy nie wraca do Inboxu.


### UC-04 Przygotować Działanie

*Poziom:* cel użytkownika (morze) · *Zakres:* G-AKT-01 GTD-App · *Aktor główny:* G-AKT-02 Użytkownik · *Wyzwalacz:* wezwanie „Przygotuj się” przy Działaniu nieprzygotowanym \[G-PRZ-04\] lub Projekcie \[G-PRJ-09\], albo wejście w Widok Kontekstu sklepu \[G-ETK-04\]

Użytkownik \[G-AKT-02\] otwiera Widok przygotowania \[G-PRZ-05\] i odhacza Pozycje przygotowania \[G-PRZ-02\] w miarę ich zdobywania: Pozycje do Zakupu w sklepach, Pozycje do Skompletowania w domu \[G-PRZ-03\]. Po każdym odhaczeniu GTD-App przelicza Gotowość Działania \[G-PRZ-06\]. Przypadek kończy się sukcesem, gdy Gotowość zmienia się na Przygotowane; GTD-App pokazuje wtedy przy Działaniu wezwanie „Zacznij” (ZP-01). Użytkownik może przerwać w dowolnym momencie; odhaczenia zostają zachowane.

- *Warianty wejścia:* z Działania (zakres: to Działanie), z Projektu, ze sklepu (zakres: wszystkie Działania, Miejsce = ten sklep).
- *Pojęcia i decyzje:* G-PRZ-01…06, G-PRJ-09; D-16…D-23.
- *Ustalenia:* domyślny zakres to Działanie, z którego otwarto Widok (D-24); Widok Kontekstu sklepu ma sekcje „Do kupienia” i „Działania” (D-25).

# GTD-App — Słownik pojęć

Oct 10, 2026 · @Michał

## Zasady projektowe

**ZP-01 Prowadzenie do postępu** (Drive the user home). GTD-App nie jest biernym rejestrem. Wszędzie, gdzie może wskazać Użytkownikowi następny krok, proponuje go aktywnie jako wezwanie do działania (np. „Przygotuj się”), zamiast tylko oznaczać stan.

## Zasady słownika

Każdy termin ma jedno znaczenie w całej specyfikacji (przypadki użycia, EARS, maszyna stanów, testy). Termin spoza słownika nie może wystąpić w wymaganiu.

- Terminy pisane są wielką literą (Element, Projekt), gdy używa się ich w znaczeniu ze słownika.
- W nawiasie podany jest odpowiednik angielski używany w wymaganiach EARS.
- Definicja ma postać: rodzaj nadrzędny + cecha odróżniająca. Ograniczenia i krotności są częścią definicji.
- „Nie mylić z” wskazuje pojęcie najbliższe, z którym termin bywa mylony.

**Identyfikatory.** Każde pojęcie ma identyfikator `G-<grupa>-<nn>`: AKT (aktorzy), ELM (Element i Stany), PRJ (Projekt), ATR (atrybuty), ETK (Etykiety), OPR (Operacje), PRZ (Przygotowanie). Zasady projektowe mają identyfikatory ZP-nn. Identyfikator jest niezmienny i nigdy nie jest używany ponownie, także po usunięciu pojęcia. Przypadki użycia, wymagania EARS i testy powołują się na pojęcia przez identyfikator.

**Terminy zakazane** (wieloznaczne, nie występują w specyfikacji):

| Termin zakazany | Dlaczego | Użyj zamiast |
| --- | --- | --- |
| zadanie, task | potocznie znaczy Element, Działanie lub Projekt | Element / Działanie / Projekt |
| lista (jako miejsce przechowywania) | sugeruje, że Element leży „w” liście | Stan Elementu; „Widok” dla filtrowanego zestawienia |
| deadline, termin (bez przymiotnika) | myli datę wykonania z ostatecznym terminem | Data wykonania / Termin ostateczny |
| zrobione, gotowe | myli Działanie z Projektem | Zakończone (z nazwą obiektu) |
| usunąć (bez dopełnienia) | nie wiadomo, czy trwale | Przenieść do Kosza / Trwale usunąć |

## Aktorzy i system

| Termin | Definicja | Nie mylić z |
| --- | --- | --- |
| **G-AKT-01 GTD-App** (GTD-App) | System oprogramowania objęty specyfikacją, przechowujący Elementy jednego Użytkownika i wykonujący na nich Operacje. | Metoda GTD (sposób pracy, nie oprogramowanie) |
| G-AKT-02 **Użytkownik** (User) | Osoba posiadająca konto w GTD-App, właściciel wszystkich swoich Elementów. Jedyny aktor główny inicjujący Operacje. W wersji 1.0 konto ma dokładnie jednego Użytkownika. | Delegat |
| G-AKT-03 **Delegat** (Delegate) | Osoba, której Użytkownik powierzył wykonanie Działania. Nie ma konta i nie wchodzi w interakcję z GTD-App; w systemie występuje wyłącznie jako Kontekst typu Osoba \[G-ETK-02\]. | Użytkownik; Kontekst „osoba” |
| G-AKT-04 **Czas** (Scheduler) | Aktor systemowy generujący zdarzenia w określonych momentach (np. upływ 7 dni od Przeglądu tygodniowego). | Data wykonania (atrybut, nie aktor) |
| G-AKT-05 **Kalendarz zewnętrzny** (External Calendar) | System trzeci, z którym GTD-App wymienia Działania zaplanowane i odczytuje wydarzenia. Aktor wspierający. | Widok kalendarza w GTD-App |
| G-AKT-06 **Serwer poczty** (Mail Server) | System trzeci dostarczający wiadomości przekazane przez Użytkownika na adres Przechwycenia. Aktor wspierający. | — |

## Element i jego stany

G-ELM-01 **Element** (Item) to jednostka treści zapisana w GTD-App przez Użytkownika. Każdy Element ma w każdej chwili dokładnie jeden Stan. Element należy do 0..1 Projektu.

G-ELM-02 **Stan Elementu** (Item State) to klasyfikacja określająca, czy i jak Element wymaga działania. Element nie „leży” na liście; ma Stan, a listy GTD to Widoki Stanów.

| Stan | Definicja | Ograniczenia |
| --- | --- | --- |
| G-ELM-03 **W Inboxie** (In Inbox) | Element przechwycony i jeszcze niedoprecyzowany. | Jedyny Stan po Przechwyceniu. Nie wymaga Projektu, Kontekstu ani dat. Nie może mieć Delegata. |
| G-ELM-04 **Następne działanie** (Next Action) | Działanie, które Użytkownik może wykonać w dowolnym momencie. | Brak Daty wykonania i brak Delegata. Ma 0..\* Kontekstów. |
| G-ELM-05 **Zaplanowane** (Scheduled) | Działanie, które musi być wykonane w określonym dniu lub o określonej godzinie. | Ma dokładnie jedną Datę wykonania. Brak Delegata. |
| G-ELM-06 **Czekam na** (Waiting For) | Działanie powierzone Delegatowi, którego rezultatu Użytkownik oczekuje. | Ma dokładnie jednego Delegata i jedną Datę delegowania; 0..1 Daty kontroli. |
| G-ELM-07 **Kiedyś/może** (Someday/Maybe) | Element, do którego Użytkownik nie zobowiązał się w bieżącym okresie. | Nie pojawia się w Widokach Następnych działań. Brak dat. Może należeć do Projektu Aktywnego i nie liczy się wtedy jako Otwarte działanie. |
| G-ELM-08 **Referencja** (Reference) | Element niewymagający działania, przechowywany wyłącznie jako informacja. | Brak Kontekstu, dat i Delegata. Nigdy nie zostaje Zakończony. |
| G-ELM-09 **Zakończony** (Completed) | Działanie oznaczone przez Użytkownika jako wykonane. | Ma Datę zakończenia. Stan dostępny tylko dla Działań. |
| G-ELM-10 **W Koszu** (Trashed) | Element odrzucony przez Użytkownika, możliwy do przywrócenia. | Nie pojawia się w żadnym Widoku poza Koszem. Nie jest trwale usunięty. |

G-ELM-11 **Działanie** (Action) to Element opisujący jedną fizyczną, widoczną czynność, którą da się wykonać za jednym podejściem, bez dalszego planowania. Działaniem jest każdy Element w Stanie Następne działanie, Zaplanowane, Czekam na lub Zakończony. Tytuł Działania zaczyna się od czasownika („Zadzwonić do wulkanizacji”, nie „Opony”). *Nie mylić z:* Projekt.

G-ELM-12 **Otwarte działanie** (Open Action) to Działanie w Stanie Następne działanie, Zaplanowane lub Czekam na.

G-ELM-13 **Widok** (View) to filtrowane zestawienie Elementów według Stanu i atrybutów (np. Następne działania z Kontekstem @telefon). Wyświetlenie Widoku nie zmienia żadnego Elementu. Każdy atrybut Elementu i Projektu (Stan, Projekt, Obszar odpowiedzialności, Kontekst, Typ Kontekstu, Kategoria Miejsca, Charakter Działania, Delegat, każda data, Szacowany czas, Wymagana energia) może być kryterium filtrowania Widoku, także w połączeniu z innymi.

G-ELM-14 **Inbox** (Inbox) to Widok Elementów w Stanie W Inboxie. **G-ELM-15 Pusty Inbox (Empty Inbox)** oznacza zero Elementów w tym Stanie.

## Projekt i Obszar odpowiedzialności

G-PRJ-01 **Projekt** (Project) to zobowiązanie Użytkownika do osiągnięcia Rezultatu, które wymaga więcej niż jednego Działania i ma zostać osiągnięte w ciągu 12 miesięcy. Granica 12 miesięcy jest wskazówką dla Użytkownika; GTD-App jej nie sprawdza. Projekt nie jest Elementem; grupuje 0..\* Elementów i należy do 0..1 Obszaru odpowiedzialności. *Nie mylić z:* Działanie (jedna czynność), Obszar odpowiedzialności (nigdy się nie kończy).

G-PRJ-02 **Rezultat** (Outcome) to obowiązkowy atrybut Projektu: opis stanu świata po zakończeniu Projektu, sformułowany jako fakt dokonany („Nowa strona firmy działa pod adresem firmy”).

| Stan Projektu | Definicja | Ograniczenia |
| --- | --- | --- |
| G-PRJ-03 **Aktywny** (Active) | Projekt, nad którym Użytkownik pracuje w bieżącym okresie. | Musi mieć ≥1 Otwarte działanie, inaczej jest Utknięty. |
| G-PRJ-04 **Utknięty** (Stalled) | Stan wyliczany: Projekt Aktywny z zerem Otwartych działań. | Nie ustawia go Użytkownik; GTD-App wylicza go automatycznie. |
| G-PRJ-05 **Kiedyś/może** (Someday/Maybe) | Projekt odłożony bez zobowiązania w bieżącym okresie. | Nie wymaga Otwartych działań; nigdy nie jest Utknięty. |
| G-PRJ-06 **Zakończony** (Completed) | Projekt, którego Rezultat Użytkownik uznał za osiągnięty. | Nie ma Otwartych działań. Ma Datę zakończenia. |
| G-PRJ-07 **W Koszu** (Trashed) | Projekt odrzucony przez Użytkownika, możliwy do przywrócenia. | Jego Elementy trafiają do Kosza razem z nim. |

Działanie w Stanie Czekam na liczy się jako Otwarte działanie, więc Projekt czekający wyłącznie na Delegata nie jest Utknięty.

G-PRJ-09 **Wymaga przygotowania** (Needs Preparation) to status wyliczany Projektu Aktywnego, którego wszystkie Otwarte działania mają Gotowość Nieprzygotowane \[G-PRZ-06\]. Taki Projekt nie jest Utknięty. GTD-App pokazuje przy nim wezwanie „Przygotuj się” (ZP-01).

G-PRJ-08 **Obszar odpowiedzialności** (Area of Focus) to sfera życia lub pracy, w której Użytkownik utrzymuje stały standard (np. Zdrowie, Finanse, Zespół). Nie ma Rezultatu i nigdy nie zostaje Zakończony. Grupuje 0..\* Projektów i 0..\* Działań spoza Projektów. *Nie mylić z:* Projekt, Kontekst.

## Atrybuty Działań

| Atrybut | Definicja | Dziedzina wartości | Krotność |
| --- | --- | --- | --- |
| G-ATR-01 **Kontekst** (Context) | Warunek konieczny do wykonania Działania, sprawdzalny obserwacją chwili (teraz prawda albo fałsz). Ma dokładnie jeden Typ Kontekstu \[G-ETK-05\]. Synonim: Etykieta. | Kontekst zdefiniowany przez Użytkownika (np. @dom, @Castorama, @wiertarka, @Marek, @pogoda) | 0..\* |
| G-ATR-02 **Szacowany czas** (Time Estimate) | Przewidywany czas potrzebny na wykonanie Działania. | Liczba całkowita minut > 0 | 0..1 |
| G-ATR-03 **Wymagana energia** (Energy Level) | Poziom koncentracji i wysiłku potrzebny do wykonania Działania. „Wysiłek” jest synonimem tego atrybutu, nie osobnym pojęciem. | niska / średnia / wysoka | 0..1 |
| G-ATR-04 **Data wykonania** (Scheduled Date) | Dzień lub dzień z godziną, w którym Działanie musi zostać wykonane i ani wcześniej, ani później nie ma sensu. Jej obecność oznacza Stan Zaplanowane. | Data lub data + godzina | 0..1 |
| G-ATR-05 **Termin ostateczny** (Due Date) | Najpóźniejsza data, do której Działanie lub Projekt musi być Zakończony, bo inaczej wystąpi realna konsekwencja. Nie zmienia Stanu. | Data | 0..1 |
| G-ATR-06 **Data delegowania** (Delegation Date) | Dzień, w którym Użytkownik powierzył Działanie Delegatowi. | Data, domyślnie dzień Delegowania | 1 w Stanie Czekam na |
| G-ATR-07 **Data kontroli** (Follow-up Date) | Dzień, w którym Użytkownik chce sprawdzić postęp u Delegata. Od tego dnia GTD-App wyróżnia Działanie w Widokach jako zaległe; nie wysyła powiadomienia. | Data ≥ Data delegowania | 0..1 |
| G-ATR-08 **Data zakończenia** (Completion Date) | Moment oznaczenia Działania lub Projektu jako Zakończonego. | Data + godzina, ustawiana przez GTD-App | 1 w Stanie Zakończony |

*Nie mylić:* Kontekst „@Marek” oznacza, że do wykonania Działania potrzebna jest obecność Marka (np. temat na spotkanie). Delegat Marek oznacza, że to Marek wykonuje Działanie.

G-ATR-09 **Charakter Działania** (Action Nature) to jakościowa cecha samego Działania, która wpływa na wybór momentu wykonania, ale nie jest ani Kontekstem (warunkiem świata), ani kosztem (G-ATR-02, G-ATR-03). Wartości definiuje Użytkownik (np. brudna robota, głośna praca). Krotność 0..\*. *Nie mylić z:* Kontekst typu Okoliczność (stan świata, np. dobra pogoda).

G-ETK-01 **Etykieta** (Label) to synonim Kontekstu \[G-ATR-01\] używany w interfejsie. Nie jest osobnym pojęciem. Nazwa Kontekstu jest unikalna w obrębie konta, bez rozróżniania wielkości liter.

G-ETK-05 **Typ Kontekstu** (Context Type) to klasyfikacja Kontekstu według tego, jaki warunek opisuje. Każdy Kontekst ma dokładnie jeden Typ:

| Typ | Warunek | Przykłady |
| --- | --- | --- |
| G-ETK-06 **Miejsce** (Place) | gdzie Użytkownik musi być, w tym sklep internetowy | @dom, @NaMieście, @Castorama, @Allegro |
| G-ETK-07 **Narzędzie** (Tool) | co Użytkownik musi mieć przy sobie | @komputer, @telefon, @wiertarka |
| G-ETK-02 **Osoba** (Person) | kto musi być dostępny; osoba spoza GTD-App | @Marek, @Gosia |
| G-ETK-08 **Okoliczność** (Circumstance) | stan świata, na który Użytkownik nie ma wpływu | @pogoda |

Ta sama Osoba może być Delegatem \[G-AKT-03\] jednego Działania i Kontekstem innego.

G-ETK-09 **Kategoria Miejsca** (Place Category) to opcjonalne grupowanie Kontekstów typu Miejsce (np. Sklep). Krotność 0..1 na Miejsce. Służy filtrowaniu, np. wszystkie Miejsca kategorii Sklep.

G-ETK-10 **Reguła dopasowania Kontekstów** (Context Matching Rule): Działanie pasuje do bieżącej sytuacji, gdy pasuje co najmniej jedno z jego Miejsc (LUB) oraz wszystkie jego Konteksty pozostałych Typów (I). Działanie bez Miejsca pasuje w każdym Miejscu.

G-ETK-03 **Wybór Kontekstu** (Label Picker): przy edycji Działania Użytkownik wybiera Kontekst z listy istniejących. Gdy wpisze nazwę nieistniejącą, GTD-App proponuje utworzenie nowego Kontekstu, prosi o jego Typ i tworzy go dopiero po potwierdzeniu.

G-ETK-04 **Widok Kontekstów** (Contexts View) to Widok wszystkich Kontekstów pogrupowanych według Typu, z liczbą przypisanych Otwartych działań, z filtrem po Typie i Kategorii Miejsca. Wybranie Kontekstu otwiera Widok jego Działań; dla Miejsca kategorii Sklep Widok pokazuje także nieodhaczone Pozycje do Zakupu ze wszystkich Działań \[G-PRZ-03\].

## Przygotowanie

G-PRZ-01 **Lista przygotowania** (Preparation List) to opcjonalna część Działania \[G-ELM-11\]: zbiór Pozycji przygotowania, które trzeba odhaczyć, zanim Działanie można zacząć (mise en place). Działanie ma 0..1 Listy; Lista ma 1..\* Pozycji.

G-PRZ-02 **Pozycja przygotowania** (Preparation Item) to punkt Listy przygotowania: rzecz, którą trzeba zdobyć lub zebrać przed rozpoczęciem Działania. Nie jest Elementem \[G-ELM-01\]: nie ma Stanu, Kontekstu, dat ani Projektu. Ma nazwę, Sposób pozyskania i znacznik odhaczenia (tak / nie). *Nie mylić z:* Działanie (np. „Kupić farbę” jako osobne Działanie).

G-PRZ-03 **Sposób pozyskania** (Acquisition Mode) Pozycji ma jedną z dwóch wartości. **Zakup**: Pozycja ma 1..\* Miejsc \[G-ETK-06\] kategorii Sklep, traktowanych jako alternatywa (LUB, jak w G-ETK-10). **Skompletowanie**: rzecz posiadana przez Użytkownika, do zebrania z domu lub innego Miejsca.

G-PRZ-04 **Działanie nieprzygotowane** (Unprepared Action) to Działanie o Gotowości Nieprzygotowane \[G-PRZ-06\]. Pozostaje widoczne w Widokach Następnych działań, z wezwaniem do działania „Przygotuj się” (ZP-01).

G-PRZ-05 **Widok przygotowania** (Preparation View) to Widok jednej Listy przygotowania, otwierany wezwaniem „Przygotuj się”. Pokazuje najpierw Pozycje do Zakupu pogrupowane według sklepu, pod nimi Pozycje do Skompletowania. Ma przełącznik zakresu: to Działanie albo wszystkie Działania nieprzygotowane. Użytkownik odhacza w nim Pozycje.

G-PRZ-06 **Gotowość Działania** (Readiness) to atrybut wyliczany Działania o dwóch wartościach. **Przygotowane**: Działanie nie ma Listy przygotowania albo wszystkie jej Pozycje są odhaczone. **Nieprzygotowane**: w przeciwnym razie. Gotowość jest niezależna od Stanu (Działanie może być jednocześnie Zaplanowane i Nieprzygotowane). Użytkownik jej nie ustawia.

## Operacje

G-OPR-01 Operacja (Operation) to czynność Użytkownika lub GTD-App zmieniająca Stan lub atrybuty Elementu albo Projektu. Wyświetlenie Widoku nie jest Operacją.

| Operacja | Definicja | Zmiana Stanu |
| --- | --- | --- |
| G-OPR-02 **Przechwycenie** (Capture) | Utworzenie nowego Elementu z treści podanej przez Użytkownika dowolnym Kanałem przechwycenia. | brak → W Inboxie |
| G-OPR-03 **Kanał przechwycenia** (Capture Channel) | Sposób dostarczenia treści do Przechwycenia: pole tekstowe, widżet, dyktowanie, udostępnienie z innej aplikacji, adres e-mail. Wariant technologiczny, nie osobna Operacja. | — |
| G-OPR-04 **Doprecyzowanie** (Clarification) | Decyzja Użytkownika o jednym Elemencie W Inboxie: czy wymaga działania i jakiego. Kończy się dokładnie jednym z wyników poniżej. | W Inboxie → dowolny inny Stan |
| G-OPR-05 **Wykonanie natychmiastowe** (Do Now) | Wynik Doprecyzowania, gdy Użytkownik wykonał Działanie od razu (reguła 2 minut). Decyzję o czasie podejmuje Użytkownik, nie GTD-App. Element pozostaje w GTD-App jako Zakończony. | W Inboxie → Zakończony |
| G-OPR-06 **Przekształcenie w Projekt** (Convert to Project) | Wynik Doprecyzowania: utworzenie Projektu, którego Rezultat powstaje z treści Elementu, wraz z ≥1 Otwartym działaniem. Element przechwycony przestaje istnieć. | W Inboxie → (Projekt Aktywny) |
| G-OPR-07 **Delegowanie** (Delegate) | Powierzenie Działania Delegatowi z zapisem Daty delegowania. Możliwe z Doprecyzowania lub z Następnego działania. GTD-App nie powiadamia Delegata. | W Inboxie / Następne działanie → Czekam na |
| G-OPR-08 **Zakończenie Działania** (Complete Action) | Oznaczenie Otwartego działania jako wykonanego. | Otwarte działanie → Zakończony |
| G-OPR-09 **Zakończenie Projektu** (Complete Project) | Uznanie Rezultatu Projektu za osiągnięty. Jedno potwierdzenie Użytkownika zmienia Stan wszystkich Otwartych działań Projektu na Zakończony. | Aktywny / Utknięty → Zakończony |
| G-OPR-10 **Przeniesienie do Kosza** (Trash) | Odrzucenie Elementu lub Projektu z możliwością przywrócenia. | dowolny → W Koszu |
| G-OPR-11 **Przywrócenie** (Restore) | Cofnięcie Przeniesienia do Kosza. | W Koszu → Stan sprzed Przeniesienia |
| G-OPR-12 **Trwałe usunięcie** (Permanent Delete) | Nieodwracalne usunięcie Elementu lub Projektu z GTD-App, wyłącznie na polecenie Użytkownika. GTD-App nigdy nie usuwa trwale automatycznie. | W Koszu → brak |

G-OPR-13 **Przegląd tygodniowy** (Weekly Review) to sesja Użytkownika, w której przechodzi on kolejno wszystkie Punkty kontrolne, aby doprowadzić system do stanu aktualnego. Przegląd jest **ukończony**, gdy Użytkownik odhaczył wszystkie Punkty kontrolne; GTD-App zapisuje wtedy datę ostatniego ukończonego Przeglądu.

G-OPR-14 **Punkt kontrolny** (Checklist Item) to pojedynczy krok Przeglądu tygodniowego. **Systemowy** Punkt kontrolny wskazuje Widok GTD-App (np. Projekty Utknięte). **Własny** Punkt kontrolny to tekst Użytkownika opisujący czynność poza GTD-App (np. „Opróżnić papierowy notatnik”).

## Otwarte decyzje do walidacji

Siedem pytań, które słownik celowo zostawia otwarte. Każde zmienia co najmniej jedną definicję powyżej.

- [x] **Kosz:** brak automatycznego Trwałego usunięcia; tylko na polecenie Użytkownika.
- [x] **Wykonanie natychmiastowe:** Element zostaje w Stanie Zakończony.
- [x] **Zakończenie Projektu:** zbiorcze zamknięcie wszystkich Otwartych działań jednym potwierdzeniem.
- [x] **Delegat:** Etykieta rodzaju Osoba, wybierana z listy lub tworzona przy wpisaniu nowej nazwy; wszystkie atrybuty filtrowalne, Widok etykiet.
- [x] **Data kontroli:** bez powiadomienia; tylko wyróżnienie zaległego Działania w Widokach.
- [x] **Granica 12 miesięcy:** wyłącznie wskazówka w definicji, bez sprawdzania przez GTD-App.
- [x] **Kiedyś/może w Projekcie:** dozwolone; takie Elementy nie są Otwartymi działaniami.

## Przypadki użycia — krótkie opisy

Krótkie opisy (use case briefs) według Cockburna, w terminach ze słownika. Identyfikatory UC są niezmienne i nie oznaczają kolejności.

### UC-01 Przechwycić Element

*Poziom:* cel użytkownika (morze) · *Zakres:* G-AKT-01 GTD-App · *Aktor główny:* G-AKT-02 Użytkownik · *Aktor wspierający:* G-AKT-06 Serwer poczty (tylko kanał e-mail)

Użytkownik \[G-AKT-02\] przekazuje GTD-App \[G-AKT-01\] treść dowolnym Kanałem przechwycenia \[G-OPR-03\]. GTD-App wykonuje Przechwycenie \[G-OPR-02\]: tworzy jeden nowy Element \[G-ELM-01\] w Stanie W Inboxie \[G-ELM-03\], nie wymagając Projektu \[G-PRJ-01\], Etykiety \[G-ETK-01\] ani żadnej daty \[G-ATR-04…08\]. Przypadek kończy się, gdy Element jest trwale zapisany i widoczny w Inboxie \[G-ELM-14\]. Użytkownik nie decyduje tu o dalszym losie Elementu; należy to do Doprecyzowania \[G-OPR-04\] w UC-02.

- *Warianty kanału \[G-OPR-03\]:* pole tekstowe, widżet, dyktowanie, udostępnienie z innej aplikacji, adres e-mail \[G-AKT-06\].
- *Ślad:* CAP-01, CAP-02, CAP-03.
- *Do rozstrzygnięcia:* „trwale zapisany” oznacza zapis lokalny na urządzeniu, nie synchronizację (definicja przy CAP-03).

### UC-02 Opróżnić Inbox

*Poziom:* cel użytkownika (morze) · *Zakres:* G-AKT-01 GTD-App · *Aktor główny:* G-AKT-02 Użytkownik · *Aktor wspierający:* G-AKT-05 Kalendarz zewnętrzny (tylko gdy wynikiem jest Zaplanowane i integracja jest włączona) · *Zawiera:* UC-03 Doprecyzować Element (ryba) · *Wywoływany też z:* Przeglądu tygodniowego \[G-OPR-13\]

Użytkownik \[G-AKT-02\] przegląda po kolei Elementy \[G-ELM-01\] w Stanie W Inboxie \[G-ELM-03\] i dla każdego wykonuje Doprecyzowanie \[G-OPR-04\] (UC-03). Każde Doprecyzowanie kończy się dokładnie jednym wynikiem, który zmienia Stan Elementu \[G-ELM-02\] na inny niż W Inboxie; Element nigdy nie wraca do Inboxu. Przypadek kończy się sukcesem, gdy Inbox jest Pusty \[G-ELM-15\]. Użytkownik może przerwać w dowolnym momencie: Elementy już doprecyzowane zachowują nowy Stan, pozostałe zostają W Inboxie.

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

- *Gwarancja minimalna:* żaden Element nie zostaje utracony; każdy ma po przerwaniu albo nowy Stan, albo nadal W Inboxie.
- *Ślad:* CLR-01, CLR-02, CLR-03.
- *Kolejność:* GTD-App prezentuje Elementy od najstarszego (według chwili Przechwycenia \[G-OPR-02\]). Elementy przechwycone w trakcie (UC-01) dołączają na koniec bieżącego opróżniania.

### UC-04 Przygotować Działanie

*Poziom:* cel użytkownika (morze) · *Zakres:* G-AKT-01 GTD-App · *Aktor główny:* G-AKT-02 Użytkownik · *Wyzwalacz:* wezwanie „Przygotuj się” przy Działaniu nieprzygotowanym \[G-PRZ-04\] lub Projekcie \[G-PRJ-09\], albo wejście w Widok Kontekstu sklepu \[G-ETK-04\]

Użytkownik \[G-AKT-02\] otwiera Widok przygotowania \[G-PRZ-05\] i odhacza Pozycje przygotowania \[G-PRZ-02\] w miarę ich zdobywania: Pozycje do Zakupu w sklepach, Pozycje do Skompletowania w domu \[G-PRZ-03\]. Po każdym odhaczeniu GTD-App przelicza Gotowość Działania \[G-PRZ-06\]. Przypadek kończy się sukcesem, gdy Gotowość zmienia się na Przygotowane; GTD-App pokazuje wtedy przy Działaniu wezwanie „Zacznij” (ZP-01). Użytkownik może przerwać w dowolnym momencie; odhaczenia zostają zachowane.

- *Warianty wejścia:* z Działania (zakres: to Działanie), z Projektu, ze sklepu (zakres: wszystkie Działania, Miejsce = ten sklep).
- *Ślad:* G-PRZ-01…06, G-PRJ-09; decyzje D-16…D-23.
- *Do rozstrzygnięcia:* domyślny zakres Widoku przygotowania (D-24), układ Widoku Kontekstu sklepu (D-25).

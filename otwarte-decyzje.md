# Otwarte decyzje

Rejestr decyzji projektu GTD-App prowadzony według Kontraktu decyzji. Aktualizowany po każdej odpowiedzi; identyfikatory D i K są niezmienne. Źródło prawdy: ten plik (D-41).

## Otwarte

| ID | Decyzja | Opcje | Propozycja |
| --- | --- | --- | --- |
| D-53 | Tryb powrotu do aplikacji | A) gtd2 samodzielnie na obecnym procesie, bez migracji na szablon iso-template-agent; proces rozwijany osobno · B) najpierw pilot szablonu na gtd2 · C) nowy projekt z copiera | A |
| D-54 | Miejsce kodu | A) w gtd2 obok specyfikacji (src/, tests/) · B) od zera w osobnym repozytorium (repozytorium gtd pomijamy, Użytkownik 2026-11-11) | A |
| D-55 | Pierwszy przyrost | A) UC-01 i UC-02: zatwierdzić ich wymagania, testy akceptacyjne, potem kod; wcześniej K-01 · B) najpierw pełna specyfikacja (fale 3–4) · C) inny wycinek | A |
| D-56 | Technologia | A) lokalna aplikacja bez pracy offline; CAP-03 odłożone · B) od razu praca offline z synchronizacją · C) najpierw krótka analiza opcji wobec CAP-02 i CAP-03 | C |
| D-58 | Wypchnięcie do m1981/gtd2 (zdalne ma niezwiązaną historię: jeden commit z README „# gtd2-iso”; repozytorium publiczne) | A) najpierw zmiana na prywatne, potem wypchnięcie z nadpisaniem tamtego commita (nieodwracalne na GitHubie) · B) to samo bez zmiany widoczności · C) scalenie obu historii (commit z README zostaje, nasz README wygrywa konflikt), bez nadpisywania | A |

## W kolejce

| ID | Temat |
| --- | --- |
| K-07 | Pozycja wspólna dla kilku Działań |
| K-08 | Ponowne odznaczenie Pozycji (np. zużyta) |
| K-01 | Znaczenie „trwale zapisany” w przechwyceniu (UC-01) |
| K-03 | Cel „Zarządzać Kontekstami” na liście aktor–cel |
| K-04 | Reguła „Element nie wraca do Inboxu” jako wymaganie EARS |
| K-10 | Suspect links: flaga przeglądu po zmianie rodzica |
| K-11 | Niezależny przegląd wymagań przez osobnego agenta |
| K-12 | Lekka analiza ryzyka (scenariusze „co pójdzie źle”); odłożona przez Użytkownika 2026-10-12 |
| K-13 | Identyfikatory ekranów (E-xx) w słowniku i ślad wymagań |

## Rozstrzygnięte

| ID | Decyzja | Wybór | Data |
| --- | --- | --- | --- |
| D-57 | Kopia zapasowa i porządek | A — kopia na GitHubie w m1981/gtd2 (dawne gtd2-iso); przypadkowe „cc” w przypadki-uzycia.md usunięte; zapis sesji REF w doc/sessions/ dodany; sposób wypchnięcia: D-58 | 2026-11-11 |
| D-52 | Szablon: model śladu | model z uzupełnieniami; przeniesione do ai-sldc-template jako D-06 | 2026-10-13 |
| D-51 | Szablon: schematy ID | narzedzia/id.toml; przeniesione do ai-sldc-template jako D-05 | 2026-10-13 |
| D-50 | Szablon: moduły dziedzinowe | katalog moduly/; przeniesione do ai-sldc-template jako D-04 | 2026-10-13 |
| D-49 | Szablon: język | polski, EARS po angielsku; przeniesione do ai-sldc-template jako D-03 | 2026-10-13 |
| D-48 | Szablon: sposób powstania | nowe repozytorium PycharmProjects/ai-sldc-template; przeniesione jako D-02 | 2026-10-13 |
| D-47 | Wskaźnik w projekcie „GTD” w claude.ai | dokument claude/start-tutaj.md: lokalizacja repo i kolejność czytania, bez kopii treści | 2026-10-12 |
| D-46 | Pola obowiązkowe przy Doprecyzowaniu | tylko minimum: Data wykonania, Delegat, Rezultat + Otwarte działanie (CLR-09) | 2026-10-12 |
| D-45 | Rozbicie Elementu na kilka | operacja Podział (G-OPR-15, CLR-08) | 2026-10-12 |
| D-44 | Element do istniejącego Projektu przy Doprecyzowaniu | opcjonalny wybór Projektu przy Następne działanie / Zaplanowane / Czekam na (CLR-07) | 2026-10-12 |
| D-43 | Tabela wyników Doprecyzowania w UC-03 | zostawić; CLR-01…03 ze źródłem UC-03 | 2026-10-12 |
| D-42 | Zakres planu projektu | tylko etap specyfikacji (AGENTS.md) | 2026-10-12 |
| D-41 | Jedno źródło prawdy | repozytorium gtd2 dla wszystkich artefaktów; dokumenty w Claude Docs jako archiwum | 2026-10-12 |
| D-40 | Baseline na zamkniętym etapie | tag baseline-01-slownik-briefy | 2026-10-12 |
| D-39 | Jednostronicowy plan projektu dla agenta | AGENTS.md | 2026-10-12 |
| D-38 | Wymagania EARS w repo ze śladem w pre-commit | wymagania.md + slad.py + slad.md | 2026-10-12 |
| D-37 | Skład paska nawigacji | Start · Inbox · Działania · Projekty · Konteksty · (+) Przechwyć (nawigacja/ekrany.mmd) | 2026-10-11 |
| D-36 | Przechwyć (E-02) bez kroku naprzód | celowy wyjątek od ZP-01: przechwycenie ma być błyskawiczne | 2026-10-11 |
| D-35 | Ekran „Projekt zakończony” (E-19) | wezwanie „Pokaż Projekty Utknięte” (G-OPR-09) | 2026-10-11 |
| D-34 | Przegląd tygodniowy | tryb prowadzony, Punkt po Punkcie (G-OPR-13) | 2026-10-11 |
| D-33 | Reguła 2 minut w Doprecyzowaniu | „Zrób teraz” jako pierwsza opcja (G-OPR-05) | 2026-10-11 |
| D-32 | Niepusty Inbox | wezwanie „Opróżnij Inbox (N)” na ekranie głównym (G-ELM-15) | 2026-10-11 |
| D-31 | Przygotowanie przed Datą wykonania | „Przygotuj się” z wyprzedzeniem, domyślnie 2 dni (G-PRZ-04) | 2026-10-11 |
| D-30 | Data kontroli przy Czekam na | bez powiadomień; wezwania „Skontaktuj się” i „Przesuń kontrolę” (G-ATR-07) | 2026-10-11 |
| D-29 | Folder .idea w repozytorium | dodany do .gitignore | 2026-10-11 |
| D-28 | Sprzątanie po gicie w gtd2 | zgoda na usuwanie w PycharmProjects na sesję; usuwane tylko pliki blokad i tymczasowe w gtd2/.git | 2026-10-11 |
| D-27 | Gdzie trzymać repozytorium na stałe | komputer Użytkownika: PycharmProjects/gtd2 | 2026-10-11 |
| D-26 | Wezwanie przy Projekcie Utkniętym | trzy wyjścia: dodaj następne działanie / odłóż na Kiedyś/może / zakończ Projekt (G-PRJ-04) | 2026-10-11 |
| D-25 | Układ Widoku Kontekstu sklepu | dwie sekcje: „Do kupienia” nad „Działania” (G-ETK-04) | 2026-10-11 |
| D-24 | Domyślny zakres Widoku przygotowania | to Działanie, przełącznik „Wszystkie” (G-PRZ-05) | 2026-10-11 |
| D-21 | Narzędzie a rzecz z domu do skompletowania | Narzędzie tylko dla rzeczy sprawdzanych w chwili; rzeczy przynoszone przed zadaniem to Pozycje do Skompletowania (G-ETK-07) | 2026-10-11 |
| D-23 | Przygotowanie jako przypadek użycia | nowy cel UC-04 Przygotować Działanie | 2026-10-11 |
| D-22 | Pozycje do Zakupu w Widoku Kontekstów sklepu | własna odpowiedź: w Widoku przygotowania przełącznik „to Działanie / wszystkie”; od strony Kontekstu sklepu od razu wszystkie (jak widok etykiety w Todoist) | 2026-10-11 |
| D-19 | Projekt, którego jedynym krokiem jest przygotowanie | status wyliczany „Wymaga przygotowania” (G-PRJ-09); Utknięty tylko bez żadnego kroku | 2026-10-11 |
| D-18 | Gotowość Działania w modelu | atrybut wyliczany (G-PRZ-06), Stany bez zmian | 2026-10-11 |
| ZP-01 | Zasada projektowa | System prowadzi do postępu, nie jest biernym rejestrem (Drive the user home) | 2026-10-11 |
| D-20 | Zakupy jako przypadek użycia | własna odpowiedź: kliknięcie Działania pokazuje listę zakupów, pod nią rzeczy z domu; dalej D-21…D-23 | 2026-10-11 |
| D-17 | Widoczność Działania nieprzygotowanego | widoczne, z wezwaniem „Przygotuj się” (G-PRZ-04, G-PRZ-05) | 2026-10-11 |
| D-16 | Czym jest Pozycja przygotowania | lekki punkt listy, nie Element (G-PRZ-02) | 2026-10-11 |
| D-15 | Osoba w modelu | Kontekst typu Osoba; Etykieta to synonim Kontekstu | 2026-10-11 |
| D-14 | Jak opisać zakupy | własny pomysł: Lista przygotowania jako kryterium startu; rozbite na D-16…D-20 | 2026-10-11 |
| D-13 | Gdzie „brudna robota” | Charakter Działania (G-ATR-09) | 2026-10-11 |
| D-12 | Logika filtrowania kilku Kontekstów | Miejsca LUB, pozostałe Typy I (G-ETK-10) | 2026-10-11 |
| D-11 | Jeden model warunków wykonania | Kontekst z Typami Miejsce, Narzędzie, Osoba, Okoliczność | 2026-10-11 |
| D-10 | Sekcja z linkami do rejestrów w kontrakcie | zostawić | 2026-10-11 |
| D-09 | Etykiety tematyczne (Fix, marketing) | poza zakresem wersji 1.0 | 2026-10-11 |
| D-08 | Gdzie w modelu jest sklep | zastąpione przez D-11 | 2026-10-11 |
| D-07 | Co oznacza Etykieta sklepu | konkretny sklep | 2026-10-11 |
| D-06 | Czym jest „wysiłek” | synonim Wymaganej energii (G-ATR-03) | 2026-10-11 |
| D-05 | Elementy przechwycone w trakcie opróżniania Inboxu | dołączają na koniec bieżącego opróżniania | 2026-10-11 |
| D-04 | Kolejność Elementów przy opróżnianiu Inboxu | od najstarszego | 2026-10-11 |
| D-03 | Rodzaje Etykiet | własna odpowiedź; rozbita na D-06…D-09 | 2026-10-11 |
| D-02 | Miejsce listy otwartych decyzji | ta karta w dokumencie GTD-App | 2026-10-11 |
| D-01 | Miejsce kontraktu | osobny dokument „Kontrakt decyzji” | 2026-10-11 |

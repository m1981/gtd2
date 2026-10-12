# AGENTS.md — GTD-App, etap specyfikacji

Przeczytaj na start każdej sesji. Kontrakt decyzji (kontrakt-decyzji.md) obowiązuje zawsze.

## Zakres
Specyfikacja wymagań GTD-App v1.0 dla jednego Użytkownika. Bez kodu i bez certyfikacji (D-42).

## Artefakty i źródła prawdy
P-01 Repozytorium jest jedynym źródłem prawdy dla wszystkich artefaktów (D-41).

| Artefakt           | Plik                  | ID                  | Stan        |
| ------------------ | --------------------- | ------------------- | ----------- |
| Słownik pojęć      | slownik.md            | G-<GRUPA>-nn, ZP-nn | jest        |
| Rejestr decyzji    | otwarte-decyzje.md    | D-nn, K-nn          | jest        |
| Przypadki użycia   | przypadki-uzycia.md   | UC-nn               | jest        |
| Wymagania (EARS)   | wymagania.md          | <OBSZAR>-nn         | jest        |
| Macierz śladu      | slad.md (generowany)  | —                   | jest        |
| Nawigacja          | nawigacja/ekrany.mmd  | E-nn                | jest        |
| Ryzyka             | ryzyka.md             | RYZ-nn              | fala 3      |
| Testy akceptacyjne | testy/*.feature       | AT-<wymaganie>-n    | fala 4      |

P-02 ID są niezmienne i nigdy nie są używane ponownie.

## Ślad
P-03 Dziecko podaje tylko rodzica: wymaganie → `źródło:` (UC, D, ZP, G, RYZ); test → komentarz `# weryfikuje: <ID>`.
P-04 Macierz w obie strony generuje slad.py do slad.md; nie edytuje się jej ręcznie.
P-05 Pre-commit (.githooks/pre-commit) odrzuca: błędy śladu B1–B5, nieaktualny slad.md, łamanie reguł R1–R5 nawigacji, nieaktualną mapa-nawigacji.html. Brak testu dla wymagania jest ostrzeżeniem do fali 4, potem błędem.

## Wymaganie jest gotowe, gdy (P-06)
jeden wzorzec EARS · tekst zaczyna się zgodnie ze wzorcem · dokładnie jedno „shall” · podmiot GTD-App · terminy wyłącznie ze słownika · mierzalne · ma źródło · status: draft | zatwierdzone. Pierwsze cztery punkty sprawdza slad.py, resztę przegląd.

## Zmiana
P-07 Każda zmiana: edycja pliku → `git diff` → kontrole → jeden commit na wiadomość; w opisie ID zmienionych elementów i decyzji.
P-08 Zatwierdzenie lub zmiana zatwierdzonego wymagania wymaga decyzji D-nn w rejestrze.
P-09 Zamknięty etap = tag `baseline-nn-<nazwa>`. Ostatni: baseline-01-slownik-briefy.

## Agent
P-10 Bez decyzji Użytkownika agent nie: zmienia znaczenia pojęć, zatwierdza wymagań, usuwa plików spoza .git. Może: poprawiać format, dodawać ślad, uruchamiać kontrole, sprzątać blokady gita.

## Kolejność wdrażania praktyk
1 plan + baseline (zrobione) · 2 wymagania + ślad (zrobione) · 3 lekka analiza ryzyka · 4 testy akceptacyjne z pokryciem · 5 suspect links · 6 niezależny przegląd przez osobnego agenta.

## Świadomie pomijamy
Komisję zmian, formalne plany V&V, audyty procesu, kwalifikację narzędzi, metryki pokrycia kodu.

## Polecenia
    python3 slad.py                                     # macierz i kontrole śladu
    python3 nawigacja/sprawdz.py nawigacja/ekrany.mmd   # reguły nawigacji
    (cd nawigacja && python3 zbuduj.py)                 # odśwież mapę
    git config core.hooksPath .githooks                 # w nowym klonie

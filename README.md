# GTD-App — specyfikacja wymagań

Kopie robocze dokumentów projektu, wersjonowane w git. Źródłem prawdy są dokumenty w Claude Docs; pliki tutaj to ich eksport do Markdown po każdej zmianie.

| Plik | Źródło |
| --- | --- |
| `slownik.md` | GTD-App — Słownik pojęć, karta główna: https://claude.ai/code/artifact/680a2cbf-766d-41d9-ae38-afdaa4e7c6b6 |
| `otwarte-decyzje.md` | ten sam dokument, karta „Otwarte decyzje” |
| `kontrakt-decyzji.md` | Kontrakt decyzji: https://claude.ai/code/artifact/a880acc0-0b43-4e25-9dbc-694c09719222 |

## Zasady pracy

1. Edycja w Claude Docs.
2. Eksport zmienionej karty do Markdown i nadpisanie pliku.
3. `git diff` — przegląd, czy zmiana jest dokładnie tą zamierzoną.
4. Commit raz na wiadomość, z opisem zmian i identyfikatorami decyzji (D-nn) lub pojęć (G-…).

## Mapa nawigacji

`nawigacja/ekrany.mmd` to model ekranów i przejść w Mermaid (źródło prawdy dla nawigacji).

- `python3 nawigacja/sprawdz.py nawigacja/ekrany.mmd`: reguły R1 osiągalność, R2 brak pułapek, R3 wyjście z każdego modala, R4–R5 zasada ZP-01, R6 liczba kliknięć. Świadomy wyjątek od ZP-01 deklaruje się komentarzem `%% wyjatek-zp01: ID (decyzja)`.
- `cd nawigacja && python3 zbuduj.py`: odświeża `mapa-nawigacji.html`.

## Pre-commit

Hook `.githooks/pre-commit` blokuje commit, gdy mapa łamie reguły R1–R5 albo `mapa-nawigacji.html` nie odpowiada `ekrany.mmd`. Sprawdza pliki w katalogu roboczym. W nowym klonie włącz go poleceniem:

    git config core.hooksPath .githooks

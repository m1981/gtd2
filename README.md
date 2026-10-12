# GTD-App — specyfikacja wymagań

Specyfikacja aplikacji GTD dla jednej osoby. Zasady pracy, artefakty i reguły: **AGENTS.md**. Kontrakt decyzji: kontrakt-decyzji.md.

Repozytorium jest jedynym źródłem prawdy (D-41). Dokumenty w Claude Docs („GTD-App — Słownik pojęć”, „Kontrakt decyzji”) są archiwum stanu z 2026-10-12.

## Mapa nawigacji

`nawigacja/ekrany.mmd` to model ekranów i przejść w Mermaid.

- `python3 nawigacja/sprawdz.py nawigacja/ekrany.mmd`: reguły R1 osiągalność, R2 brak pułapek, R3 wyjście z każdego modala, R4–R5 zasada ZP-01, R6 liczba kliknięć. Świadomy wyjątek od ZP-01 deklaruje się komentarzem `%% wyjatek-zp01: ID (decyzja)`.
- `cd nawigacja && python3 zbuduj.py`: odświeża `mapa-nawigacji.html`.

## Pre-commit

Hook `.githooks/pre-commit` blokuje commit, gdy ślad wymagań ma błędy, `slad.md` jest nieaktualny, mapa łamie reguły R1–R5 albo `mapa-nawigacji.html` nie odpowiada `ekrany.mmd`. Sprawdza pliki w katalogu roboczym. W nowym klonie włącz go poleceniem:

    git config core.hooksPath .githooks

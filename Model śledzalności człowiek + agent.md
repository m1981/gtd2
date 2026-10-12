# Model śledzalności człowiek + agent

Każdy rodzaj elementu i pole, którym wskazuje swojego rodzica. Strzałka biegnie od dziecka do rodzica, tak jak zapisuje się ją w pliku (P-03). Kierunek w dół nie jest nigdzie zapisany, tylko liczony przez odwrócenie, więc ślad jest dwukierunkowy z konstrukcji.

jest w gtd2 i sprawdzane brakuje: proponuję do szablonu przyszły etap (kod)

```mermaid
flowchart BT
  SC["SC-nn Scenka · scenki.md"]
  IO["IO-nn Zakres In/Out · zakres.md"]
  D["D-nn Decyzja · decyzje.md"]
  ZP["ZP-nn Zasada · zasady.md"]
  G["G-GRP-nn Pojęcie · slownik.md"]
  UC["UC-nn Przypadek użycia · przypadki-uzycia.md"]
  RYZ["RYZ-nn Ryzyko · ryzyka.md"]
  REQ["OBS-nn Wymaganie EARS · wymagania.md"]
  E["E-nn Ekran · ekrany.mmd"]
  AT["AT-nn Test akceptacyjny · testy/*.feature"]
  CM["Commit · git"]
  KOD["Moduł kodu · src/"]
  WYN["Wynik testu · raport"]

  UC -->|"scenki:"| SC
  UC -->|"zakres:"| IO
  ZP -->|"ustanawia: D-nn"| D
  RYZ -->|"źródło:"| UC
  REQ -->|"źródło:"| UC
  REQ -->|"źródło:"| D
  REQ -->|"źródło:"| ZP
  REQ -->|"źródło:"| RYZ
  REQ -->|"źródło: (ograniczenie Out)"| IO
  REQ -.->|"używa pojęć (auto)"| G
  G -.->|"zmienione przez: D-nn"| D
  E -->|"realizuje:"| UC
  E -.->|"krawędź: D-nn"| D
  AT -->|"weryfikuje:"| REQ
  CM -->|"ID w opisie"| D
  CM -->|"ID w opisie"| REQ
  KOD -->|"implementuje:"| REQ
  WYN -->|"dla:"| AT

  classDef jest fill:#dff1e3,stroke:#2f7d4a,color:#12301c
  classDef brak fill:#fdf0d5,stroke:#b07d18,color:#3a2a06
  classDef przyszly fill:#eeeeee,stroke:#777777,color:#222222,stroke-dasharray:4 3
  class D,ZP,G,UC,REQ,E jest
  class SC,IO,RYZ,AT,CM brak
  class KOD,WYN przyszly
```

## Warunki pełnej śledzalności

Model daje pełną śledzalność dwukierunkową, gdy spełnia pięć warunków. Każdy da się sprawdzić skryptem.

1. **Korzeń albo rodzic.** Każdy rodzaj jest korzeniem (SC, IO, D) albo ma obowiązkowe pole rodzica.
2. **Kierunek w dół liczony.** Nigdzie nie zapisuje się dzieci; macierz odwraca pola rodziców, więc oba kierunki nie mogą się rozjechać.
3. **Rozwiązywalność.** Każde ID w polu rodzica istnieje i jest unikalne.
4. **Pokrycie.** Dla każdego rodzaju wiadomo, czy brak dzieci to błąd, ostrzeżenie czy stan dopuszczalny.
5. **Przyczyna zmiany.** Każda zmiana (commit) wskazuje decyzję albo element, którego dotyczy.

## Reguły dla każdego rodzaju

| Rodzaj | Pole rodzica | Oczekiwane dzieci | Brak dzieci | W gtd2 |
| --- | --- | --- | --- | --- |
| SC Scenka | korzeń | ≥ 1 UC | ostrzeżenie | brak pliku |
| IO Zakres | korzeń | In: ≥ 1 UC · Out: opcjonalnie wymaganie-ograniczenie | ostrzeżenie dla In | tylko w rozmowie |
| D Decyzja | korzeń | ≥ 1 artefakt albo commit | ostrzeżenie | jest |
| ZP Zasada | `ustanawia: D` | ≥ 1 wymaganie | ostrzeżenie | ZP-01 bez D |
| UC Przypadek | `scenki:`, `zakres:` | ≥ 1 wymaganie, ≥ 1 ekran (projekty z UI) | ostrzeżenie | bez rodzica |
| RYZ Ryzyko | `źródło: UC` | ≥ 1 wymaganie If–then | błąd | odłożone |
| Wymaganie | `źródło:` (UC, D, ZP, RYZ, IO) | ≥ 1 test | ostrzeżenie → błąd | B1–B5 |
| E Ekran | `realizuje: UC` | — | — | brak powiązania |
| AT Test | `weryfikuje:` | wynik (etap kodu) | — | fala 4 |
| Commit | ID w opisie | — | błąd (hook commit-msg) | tylko zwyczaj |
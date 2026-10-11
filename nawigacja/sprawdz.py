"""Sprawdza mapę nawigacji GTD-App zapisaną w Mermaid (ekrany.mmd).

Reguły:
  R1 Osiągalność      - każdy ekran da się osiągnąć ze Startu (E01).
  R2 Brak pułapek     - z każdego ekranu da się wrócić do Startu.
  R3 Wyjście z modala - każdy modal ma krawędź wyjścia (-.->) do ekranu spoza modali.
  R4 ZP-01 sukces     - każdy ekran sukcesu ma wezwanie (==>) do dalszej pracy.
  R5 ZP-01 wycieki    - ekrany, z których wychodzi się tylko wyjściem/powrotem,
                        bez żadnego kroku naprzód (miejsca bez następnego kroku).
  R6 Elastyczność     - najkrótsze ścieżki (liczba kliknięć) dla par kluczowych.
Ekrany klasy `ekran` mają pasek nawigacji, więc dostają niejawną krawędź do NAV.
Użycie: python3 sprawdz.py ekrany.mmd
"""
import re
import sys
from collections import deque

EDGE = re.compile(r'^\s*(\w+)\s*(-->|==>|-\.->)\s*(?:\|"?(.*?)"?\|)?\s*(\w+)\s*$')
CLASS = re.compile(r'^\s*class\s+([\w,]+)\s+(\w+)\s*$')
NODE = re.compile(r'^\s*(\w+)\s*[\[\(\/]+"?([^"\]\)]*)')

KLUCZOWE = [
    ("E01", "E07", "Start → przygotowanie"),
    ("E11", "E07", "Sklep → przygotowanie Działania"),
    ("E07", "E11", "Przygotowanie → sklep"),
    ("E06", "E09", "Działanie → jego Projekt"),
    ("E09", "E06", "Projekt → jego Działanie"),
    ("E12", "E06", "Czekam na → Działanie"),
    ("E16", "E05", "Inbox pusty → wybór działania"),
    ("E04", "E05", "Doprecyzowanie → Następne działania"),
    ("E06", "E10", "Działanie → Konteksty"),
]


def wczytaj(path):
    krawedzie, klasy, nazwy = [], {}, {}
    for line in open(path, encoding="utf-8"):
        if line.strip().startswith("%%"):
            continue
        m = EDGE.match(line)
        if m:
            krawedzie.append((m.group(1), m.group(2), m.group(3) or "", m.group(4)))
            continue
        m = CLASS.match(line)
        if m:
            for n in m.group(1).split(","):
                klasy[n] = m.group(2)
            continue
        m = NODE.match(line)
        if m and not line.strip().startswith(("classDef", "flowchart")):
            nazwy[m.group(1)] = m.group(2).strip()
    return krawedzie, klasy, nazwy


def graf(krawedzie, klasy):
    g = {}
    for a, _, _, b in krawedzie:
        g.setdefault(a, set()).add(b)
        g.setdefault(b, set())
    for n, k in klasy.items():
        if k == "ekran":
            g.setdefault(n, set()).add("NAV")
    return g


def bfs(g, start):
    dist = {start: 0}
    q = deque([start])
    while q:
        u = q.popleft()
        for v in g.get(u, ()):
            if v not in dist:
                dist[v] = dist[u] + 1
                q.append(v)
    return dist


def kroki(g, a, b):
    """Kliknięcia: przejście przez NAV liczy się jako jedno kliknięcie (pasek)."""
    g2 = {u: set(vs) for u, vs in g.items()}
    for u, vs in g2.items():
        if "NAV" in vs:
            vs.discard("NAV")
            vs |= g.get("NAV", set())
    return bfs(g2, a).get(b)


def main(path):
    kr, kl, nazwy = wczytaj(path)
    g = graf(kr, kl)
    ekrany = [n for n in g if n != "NAV" and kl.get(n) != "zewn"]
    nm = lambda n: nazwy.get(n, n)
    wyniki = []

    osiag = bfs(g, "E01")
    r1 = [n for n in ekrany if n not in osiag]
    wyniki.append(("R1 Osiągalność ze Startu", r1))

    r2 = [n for n in ekrany if "E01" not in bfs(g, n)]
    wyniki.append(("R2 Brak pułapek (powrót do Startu)", r2))

    r3 = []
    for n in ekrany:
        if kl.get(n) != "modal":
            continue
        ok = any(a == n and t == "-.->" and kl.get(b) != "modal" for a, t, _, b in kr)
        if not ok:
            r3.append(n)
    wyniki.append(("R3 Każdy modal ma wyjście", r3))

    r4 = []
    for n in ekrany:
        if kl.get(n) != "sukces":
            continue
        if not any(a == n and t == "==>" for a, t, _, _ in kr):
            r4.append(n)
    wyniki.append(("R4 ZP-01: sukces z wezwaniem do dalszej pracy", r4))

    r5 = []
    for n in ekrany:
        wych = [(t, b) for a, t, _, b in kr if a == n and b != n]
        if wych and all(t == "-.->" for t, _ in wych):
            r5.append(n)
    wyniki.append(("R5 ZP-01: miejsca bez kroku naprzód", r5))

    print("| Reguła | Wynik | Ekrany |")
    print("| --- | --- | --- |")
    for r, lista in wyniki:
        print(f"| {r} | {'OK' if not lista else 'UWAGA'} | {', '.join(nm(x) for x in lista) or '—'} |")
    print()
    print("| R6 Para | Kliknięcia |")
    print("| --- | --- |")
    for a, b, opis in KLUCZOWE:
        k = kroki(g, a, b)
        print(f"| {opis} | {k if k is not None else 'brak ścieżki'} |")
    return 1 if any(l for r, l in wyniki if not r.startswith("R5")) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "ekrany.mmd"))

"""Ślad dwukierunkowy GTD-App (AGENTS.md, P-03…P-06).

Zbiera identyfikatory ze wszystkich artefaktów, sprawdza wymagania i generuje
macierz w obie strony do slad.md. Kod wyjścia 1 = błędy (blokują commit).

Błędy:   B1 brak pola · B2 nieznane ID w źródle/odnośniku · B3 zdublowane ID
         B4 nieznany wzorzec · B5 tekst niezgodny z wzorcem EARS / nie jedno „shall”
Ostrzeżenia: O1 przypadek użycia bez wymagań · O2 wymaganie bez testu (do fali 4)
Użycie: python3 slad.py [plik_wyjściowy=slad.md]
"""
import glob
import re
import sys
from collections import defaultdict

ID = r"(?:G-[A-Z]{3}-\d{2}|ZP-\d{2}|UC-\d{2}|D-\d{2}|K-\d{2}|E-\d{2}|RYZ-\d{2}|(?<![A-Z-])[A-Z]{3}-\d{2})"
POLA = ("wzorzec", "tekst", "źródło", "status")
WZORCE = {
    "ubiquitous": lambda t: t.startswith("GTD-App shall"),
    "event": lambda t: t.startswith("When "),
    "state": lambda t: t.startswith("While "),
    "unwanted": lambda t: t.startswith("If ") and ", then " in t,
    "optional": lambda t: t.startswith("Where "),
    "complex": lambda t: t.startswith("While ") and " when " in t.lower(),
}


def czytaj(p):
    try:
        return open(p, encoding="utf-8").read()
    except FileNotFoundError:
        return ""


def zdefiniowane():
    ids = set()
    ids |= set(re.findall(r"G-[A-Z]{3}-\d{2}", czytaj("slownik.md")))
    ids |= set(re.findall(r"\*\*(ZP-\d{2})", czytaj("slownik.md")))
    ids |= set(re.findall(r"^### (UC-\d{2})", czytaj("przypadki-uzycia.md"), re.M))
    ids |= set(re.findall(r"^\| ([DK]-\d{2}) \|", czytaj("otwarte-decyzje.md"), re.M))
    ids |= set(re.findall(r"^\s*(E\d{2})\b", czytaj("nawigacja/ekrany.mmd"), re.M))
    ids = {("E-" + i[1:]) if re.fullmatch(r"E\d{2}", i) else i for i in ids}
    ids |= set(re.findall(r"^### (RYZ-\d{2})", czytaj("ryzyka.md"), re.M))
    return ids


def wymagania():
    wym, bledy = {}, []
    for blok in re.split(r"^### ", czytaj("wymagania.md"), flags=re.M)[1:]:
        lines = blok.splitlines()
        rid = lines[0].strip()
        pola = {}
        for l in lines[1:]:
            m = re.match(r"^- ([^:]+): (.*)$", l)
            if m:
                pola[m.group(1).strip()] = m.group(2).strip()
        if rid in wym:
            bledy.append(f"B3 {rid}: zdublowane ID")
        wym[rid] = pola
    return wym, bledy


def testy():
    pokrycie = defaultdict(list)
    for f in sorted(glob.glob("testy/*.feature")):
        for m in re.finditer(r"#\s*weryfikuje:\s*([^\n]+)", czytaj(f)):
            for rid in re.findall(ID, m.group(1)):
                pokrycie[rid].append(f)
    return pokrycie


def main(wyjscie):
    znane = zdefiniowane()
    wym, bledy = wymagania()
    znane |= set(wym)
    ostrz = []
    w_dol = defaultdict(list)
    for rid, p in wym.items():
        brak = [f for f in POLA if not p.get(f)]
        if brak:
            bledy.append(f"B1 {rid}: brak pola {', '.join(brak)}")
            continue
        if p["wzorzec"] not in WZORCE:
            bledy.append(f"B4 {rid}: nieznany wzorzec „{p['wzorzec']}”")
        elif not WZORCE[p["wzorzec"]](p["tekst"]):
            bledy.append(f"B5 {rid}: tekst nie pasuje do wzorca {p['wzorzec']}")
        if p["tekst"].count(" shall ") != 1:
            bledy.append(f"B5 {rid}: tekst musi mieć dokładnie jedno „shall”")
        for src in re.findall(ID, p["źródło"]):
            if src not in znane:
                bledy.append(f"B2 {rid}: nieznane źródło {src}")
            w_dol[src].append(rid)
    for plik in ("przypadki-uzycia.md",):
        for ref in sorted(set(re.findall(ID, czytaj(plik)))):
            if ref not in znane:
                bledy.append(f"B2 {plik}: nieznany odnośnik {ref}")
    t = testy()
    for f_ref, pliki in t.items():
        if f_ref not in znane:
            bledy.append(f"B2 testy: nieznane wymaganie {f_ref} w {', '.join(pliki)}")
    ucs = sorted(i for i in znane if i.startswith("UC-"))
    for uc in ucs:
        if not w_dol.get(uc):
            ostrz.append(f"O1 {uc}: przypadek użycia bez wymagań")
    bez_testu = [r for r in wym if r not in t]
    if bez_testu:
        ostrz.append(f"O2 {len(bez_testu)} z {len(wym)} wymagań bez testu (fala 4)")

    out = ["# Macierz śladu GTD-App", "",
           "Plik generowany przez slad.py; nie edytuj ręcznie (P-04).", "",
           f"Wymagania: {len(wym)} · ze źródłem: {sum(1 for p in wym.values() if p.get('źródło'))} · z testem: {len(wym) - len(bez_testu)} · błędy: {len(bledy)} · ostrzeżenia: {len(ostrz)}", "",
           "## W górę: wymaganie → źródła", "",
           "| Wymaganie | Wzorzec | Status | Źródła | Testy |", "| --- | --- | --- | --- | --- |"]
    for rid, p in wym.items():
        out.append(f"| {rid} | {p.get('wzorzec', '')} | {p.get('status', '')} | {p.get('źródło', '')} | {', '.join(t.get(rid, [])) or '—'} |")
    out += ["", "## W dół: źródło → wymagania", "", "| Źródło | Wymagania |", "| --- | --- |"]
    for src in sorted(w_dol):
        out.append(f"| {src} | {', '.join(w_dol[src])} |")
    for uc in ucs:
        if uc not in w_dol:
            out.append(f"| {uc} | — |")
    if bledy or ostrz:
        out += ["", "## Błędy i ostrzeżenia", ""] + [f"- {x}" for x in bledy + ostrz]
    open(wyjscie, "w", encoding="utf-8").write("\n".join(out) + "\n")

    for x in bledy + ostrz:
        print(x)
    print(f"slad.py: {len(wym)} wymagań, {len(bledy)} błędów, {len(ostrz)} ostrzeżeń")
    return 1 if bledy else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "slad.md"))

# ❌⭕ Terminálové Piškvorky (Gomoku) v Pythonu

Klasická desková hra Piškvorky (Gomoku), vyhrává 5 symbolů v řadě, naprogramováná pro terminál. Projekt je plně objektově orientovaný (OOP) a nabízí plynulý zážitek s dynamicky nastavitelnou herní plochou. Hratelné proti živému soupeři nebo proti počítači.

## ✨ Hlavní funkce

* **Tři herní režimy:** Hráč vs AI, AI vs AI, a klasický režim: Hráč vs Hráč
* **Taktická umělá inteligence:** AI vyhodnocuje hrozby v reálném čase. Prioritizuje okamžitou výhru, blokuje soupeřovy pokusy o 5 symbolů v řadě, a pokud hrozba nehrozí, takticky staví vlastní útok.
* **Dynamická herní deska:** Možnost si nastavit libovolnou herní desku.
* **Barevné rozhraní a vizualizace:** Terminál využivá ANSI escape kódy pro barevné odlišení hráčů.
* **Systém skóre:** Hra si pamatuje výsledky jednotlivých hráčů napříč opakovanými koly.

## 🗂️ Struktura logiky

* `Board` - Třída spravující herní pole, jeho vykreslení v terminálu a komplexní algoritmus pro ověření výhry (kontroluje řádky, sloupce i obě diagonály pro jakoukoliv velikost desky).
* `PLayer / HumanPlayer / AIPlayer` - Dědičná struktura hráčů. `AIPlayer` obsahuje logiku s 5 úrovni rozhodování (Útok na 5 -> Blok na 5 -> Útok na 4 -> Blok na 4 -> Střed/Random).
* `GameManager` - Hlavní smyčka hry, která se stará o menu, inicializaci hráčů,střídání tahů a průběžné skóre.

## 🎮 Ovládání

Hra v každém tahu vyzve hráče k zadání souřadnic.
Hráč zadá **číslo řádku**, které potvrdí  klávesou `Enter` a poté **číslo sloupce**, taktéž potvrzující klávesou `Enter`.
Kdykoli během zadávání muže hráč napsat `quit` pro ukončení hry.

## 🚀 Instalace a spuštění

Projekt nevyžaduje instalaci žádných externích knihoven přes `pip`. Vše běží čistě na standardních knihovnách Pythonu (`random`, `os`, `time`).

1. Naklonuj repositář [gomoku](https://github.com/Badsoul01/Gomoku):
  ```bash
  git clone https://github.com/Badsoul01/Gomoku.git
  ```
2. Přejdi do složky s projektem:
   ```bash
   cd Gomoku 
   ```
3. Spusť hru přes hlavní soubor:
    ```bash
   python3 gomoku.py
   ```
   
## 🛠️ Použité technologie
* **Python 3**
* **Objektově orientované programování (OOP)**
* **ANSI Escape Codes (Barevné formátování textu v terminálu)**
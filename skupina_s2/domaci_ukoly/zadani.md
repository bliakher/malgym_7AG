# Domácí úkoly

*Na úkolech můžete spolupracovat v menších skupinkách, ale řešení sepisujte samostatně. Pouze vyzrazení řešení není spolupráce. Pokud jste s někým spolupracovali, napište mi s kým.*

### 1. Hry s páskou - 4 body
- **Dva kameny** Hrací pole je páska s levým okrajem (doprava nekonečná), někde na pásce (na dvou různých polích) jsou umístěné 2 stejné kameny. Tah: hráč si vybere jeden kámen a posune ho o libovolný počet polí doleva, nesmí přeskakovat přes druhý kámen ani spadnout z pásky. Ten hráč, který už nemá žádný tah prohrál. 
- **Páska a nůžky** Hráči dostanou pásku sudé délky, na které jsou napsaná kladná čísla. Tah: hráč si vybere jeden z okrajů pásky, který ustřihne. Podle toho, kolik je na ústřižku napsáno, tolik má bodů. Vyhrává hráč s nejvíce body.
- Existuje neprohrávající strategie? Pro kterého hráče? Na čem závisí?
- Sepsané řešení prosím odevzdejte do Microsoft Teams skupiny
- Stačí vyřešit jednu z úloh (druhá je za 2 bonusové body).
- **Deadline** 20. 9. 2020 23:59

### 2. Vývojový diagram - 5 bodů
- Na vstupu jsou zadaná **různá** 3 čísla - a, b, c. Úkolem je vymyslet algoritmus, který čísla seřadí podle velikosti (vzestupně).
- Algoritmus zakreslete do **vývojového diagramu**. Doporučuju si ho nejdřív sepsat v bodech.
- Nápověda: zamyslete se, kolik je možných výstupů (seřazení 3 čísel)
- **Deadline** 4. 10. 2020 23:59

### 3. Python (instalace) - 1 bod
- Nainstalujte si Python na svůj domácí počítač podle návodu, který najdete v MS Teams -> Files -> Class Materials.
- Pošlete mi screenshot textového editoru IDLE (měl by se nainstalovat automaticky s Pythonem).
- V případě problémů mi pište.
- **Deadline** 11. 10. 2020 23:59

### BONUS: Placení mincemi - 4 body
- Úkol primárně pro ty, kdo z nějakého důvodu dostali z 2. úkolu 0 bodů.
- Mějme mince 1, 2, 5, 10, 20 a 50 korun.
- Na vstupu dostanete částku k zaplacení menší než 100 korun. Vymyslete algoritmus, pomocí kterého robot zaplatí dannou částku **nejmenším možným počtem** mincí. Tj. na výstupu bude posloupnost mincí, které dohromady dávají potřebnou částku. Mince se můžou opakovat. Nejmenší možný počet mincí znamená, že např. nelze částku zaplatit samými jednokorunovými mincemi.
- Algoritmus sepište do vývojového diagramu.
- Řešení mi pošlete na email.
- **Deadline** 14. 10. 2020 23:59

### 4. Prohození proměnných - 3 body
- úkol slouží hlavně k tomu, abyste si připomněli, co jsme dělali na poslední hodině
- úkol: Napsat program v pythonu, který načte 2 čísla z uživatelského vstupu, uloží je do proměnných a proměnné vypíše. Poté prohodí obsah proměnných (tak aby v první proměnné bylo uložené to, co bylo ve druhé a obráceně), proměnné znovu vypíše. Nestačí jen vypsat proměnné v opačném pořadí.
- **Deadline** 25. 10. 2020 23:59

### 5. Dělitelnost dvěma - 4 body
- Napište program v pythonu, který načte číslo od uživatele a vypíše, jestli je dělitelné dvěma.
- V úloze byste měli použít podmínku (if), nejspíš se bude hodit operace % (modulo).
- **Deadline** 31. 10. 2020 23:59

### 6. Typ trojúhelníku - 5 bodů
- Přepište danný vývojový diagram do kódu v Pythonu.
- Diagram na vstupu načte 3 čísla (délky stran trojúhelníku) a vypíše o jaký typ trojúhelníku se jedná (rovnostranný, rovnoramenný, obecný)
- **Deadline** 8. 11. 2020 23:59

### BONUS: Rozklad na prvočísla - 8 bodů
- Napište program v pythonu, který načte číslo ze vstupu a vypíše jeho rozklad na prvočísla.
- Výstup bude na jednom řádku, čísla oddělená mezerami a seřazená od nejmenšího po největší.
- Např. pro vstup "5" bude výstup "5", pro "12" bude výstup "2 2 3", pro "60" bude "2 2 3 5".
- **Deadline** 22. 11. 2020 23:59

### 7. Násobky čísla - 5 bodů
- Napište program v Pythonu, který načte číslo z uživatelského vstupu a vypíše všechny násobky toho čísla menší než 100.
- Můžete předpokládat, že na vstupu dostanete kladné celé číslo menší než 100 (nemusíte kontrolovat vstup).
- Nápověda: využijte while cyklus a podmínku
- **Deadline** 22. 11. 2020 23:59

### 8. Index - 7 bodů
- Napište program, který bude mít fungovat jako funkce index() pro pole.
- Máte v programu nějaké pole čísel a chcete zjistit, na které pozici se nachází nějaký prvek. Načtěte od uživatele číslo a vypište jeho pozici v poli (pozor, indexujeme od nuly). Pokud prvek v poli není, vypiše -1.
- Pro pole `[1, 3, 5, 4, 7]` a vstup 5 bude výstup 2, pro vstup 4 bude výstup 3 a pro vstup 17 bude výstup -1.
- **Deadline** 20. 12. 2020 23:59

### 9. Funkce - 6 bodů
- Úkolem je vzít části kódu, které jsme programovali na hodinách a jako domácí úkoly, přepracovat je na funkce a spojit do jednoho programu.
- Program dostane na vstupu posloupnost kladných čísel ukončenou -1. Načtěte posloupnost a uložte ji do pole. Poté budete opět číst čísla ze vstupu, dokud nedostanete -1. Pro každé načtené číslo (hledaný prvek pole) vypište první index, na kterém se prvek v poli nachází (-1 pokud tam není). 
- Cílem je dosáhnout hezké funkční dekompozice (rozdělení na funkce) - každá funkce dělá pouze jednu věc. Např. zvlášť funkce pro načítání, funkce index, funkce, která to celé dá dohromady.
- **Deadline** 24. 1. 2021 23:59




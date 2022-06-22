# PBSPrediction
Cílem projektu je vyzkoušet účinnost metod strojového učení v předpovídání aktivních míst 
na proteinech z jejich primární struktury. 

## Motivace

Ačkoliv jsou v předpovědi aktivních míst na proteinech účinější metody využívající 3-D model molekuly, tak metody používající primární strukturu jsou stále užitečné.
Nevýhodou těchto metod je absence 3-D modelu pro většinu proteinů. Z tohoto důvodu se vyplatí mít 
nástroj, který umí předpovědět aktivní místa pouze ze sekvence aminokyselin tvořících danou molekulu.

## Program

Program na vstupu dostane sekvenci ve Fasta formátu a klasifikuje jednotlivé aminokyseliny jedničkou,
když mají být součástí aktivního místa, nebo nulou v opačném případě.



## Postup 
### Příprava dat 
Cílem je připravit data, která poté budou sloužit k natrénování programu. 

   - [ ] načtení dat.
   Data pocházejí z: <https://github.com/rdk/p2rank-datasets>. Pomocí nástroje P2RANK (<https://github.com/rdk/p2rank>) se
   z dat získájí primární struktury proteinů a jejich známá aktivní místa. 
   - [ ] přiřezení aktivních míst ke každé sekvenci a rozdělení na jednotlivé řetezce
   - [ ] kontrola spracovaných dat
### Strojové učení

   - [ ] vyzkoušení různých metod strojového učení na predikci aktivních míst
### Závěr 

   - [ ] porovnání účinosti jednotlivých metod
   - [ ] porovnání s P2RANK

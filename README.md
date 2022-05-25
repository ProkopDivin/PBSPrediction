# PBSPrediction
Cílem projektu je vyzkoušet účinnost metod strojového učení v předpovídání aktivních míst 
na bílkovinách z jejich primární struktury. 

## Motivace

Na předpověd aktivních míst na bílkovynách jsou účinější metody využívající 3-D model molekuly.
Nevýhodou těchto metod je absence 3-D modelu pro většinu proteinů. Z tohoto důvodu se vyplatí mít 
nástroj, který umí předpovědět aktivní místa pouze ze sekvence aminokyselin tvořících danou molekulu.

## Program 

Program na vstupu dostane sekvenci ve Fasta formátu a klasifikuje jednotlivé aminokyseliny jedničkou,
když mají být součástí aktivního místa, nebo nulou v opačném případě.

## Postup 
### Příprava dat 
Cílem je připravit data pro strojové učení. 

   - [ ] načtení dat.
   Data pocházejí z: <https://github.com/rdk/p2rank-datasets>. Pomocí nástroje P2RANK (<https://github.com/rdk/p2rank>) se
   z dat získájí primární struktury bílkovin a jejich známá aktivní místa. 
   - [ ] přiřezení aktivních míst ke každé sekvenci, případné rozdělení na  
   - [ ] kontrola spracovaných dat
### Strojové učení

   - [ ] vyzkoušení různých metod strojového učení na predikci aktivních míst
### Závěr 

   - [ ] porovnání účinosti jednotlivých metod
   - [ ] porovnání s P2RANK

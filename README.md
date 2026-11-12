# Pràctica 02: Introducció a la programació amb Python

- **Alumne/a:** Cristian Reverte
- **Curs:** 2n SMX 
- **Mòdul:** Projecte Intermodular

## Resum del projecte

Pràctica 0: Configuració i GitHub:

En aquesta primera part vaig preparar l'ordinador des de zero per poder començar a programar. Vaig instal·lar les eines principals com l'editor de codi VS Code i el llenguatge Python, i vaig crear una carpeta compartida a GitHub anomenada Projecte-2. També vaig aprendre a fer servir la terminal per desar i pujar els meus treballs al núvol amb les comandes git add ., git commit i git push. A més, vaig resoldre un error habitual de permisos a Windows canviant les variables de la carpeta Temp.

Pràctica 1: Entrades, Sortides i Variables:

En aquesta pràctica vaig aprendre com un programa rep dades de l'usuari, les guarda i mostra els resultats. Vaig utilitzar la funció print() per ensenyar missatges i respostes per pantalla, i la funció input() per demanar informació a la persona que fa servir el programa. També vaig veure com convertir el text introduït a números realitzant canvis amb int() per a números enters i amb float() per a números que tenen decimals.

Pràctica 2: Càlculs Bàsics:

A la segona pràctica vaig començar a fer servir Python per realitzar operacions matemàtiques automàtiques amb les variables. Vaig crear codi per fer sumes, restes, multiplicacions i divisions senzilles. A més, vaig introduir l'ús del símbol % (mòdul), que serveix per obtenir el residu d'una divisió i és molt útil per saber si un número és parell, senar o si és múltiple d'un altre número.

Pràctica 3: Decisions amb Condicionals:

A la tercera pràctica vaig ensenyar al programa a prendre diferents camins segons les dades introduïdes, fent servir les instruccions if, elif i else. Vaig aplicar aquesta lògica en tres exercicis: primer per comprovar si una persona és major d'edat (>= 18), segon per comparar tres números diferents i trobar quin és el més gran, i tercer per identificar si un número és positiu, negatiu o igual a zero.

Pràctica 4: Bucles i Repeticions:

En aquesta pràctica vaig aprendre a automatitzar feines repetitives fent servir els bucles for i while. En el primer exercici vaig mostrar els números parells de l'1 al 200 de forma ràpida amb range(2, 201, 2). En el segon exercici vaig demanar notes una rere l'altra fins que es posés un -1 per comprovar si hi havia cap 10. En el tercer exercici vaig demanar 10 números per veure si almenys un d'ells era un número negatiu.

Pràctica 5: Funcions en Python:

En aquesta pràctica vaig aprendre a crear, estructurar i reutilitzar funcions per organitzar millor el codi i fer programes més modulars. En el primer exercici vaig fer una funció bàsica per calcular el cost total d'una reparació sumant el preu de les peces i la mà d'obra. En el segon exercici vaig crear una funció amb condicionals (if, elif, else) i el mètode .lower() per aplicar diferents percentatges de descompte segons el tipus de client. En el tercer exercici vaig desenvolupar dues funcions que treballen juntes: una per calcular el 21% d'IVA i una altra que crida les funcions anteriors per obtenir l'import final de la factura. Finalment, en el quart exercici vaig muntar un programa complet amb un menú interactiu dins d'un bucle while per registrar noves reparacions d'un servei tècnic informàtic, mostrar les factures detallades i consultar el nombre de reparacions i la facturació acumulada.

Respostes a les preguntes de la Pràctica 5:

Exercici 1:

Quants paràmetres té la funció?

La funció calcular_preu que vaig crear té 2 paràmetres d'entrada, que són peces i ma_obra. Els vaig posar per poder rebre els imports econòmics necessaris i fer el càlcul dins de la funció.

Quin valor retorna?

Vaig fer que retornés un únic valor numèric que correspon al resultat de sumar el cost de les peces més el cost de la mà d'obra, és a dir, el preu base total abans d'aplicar cap descompte ni impost.

Què passaria si eliminéssim el return?

Si hagués eliminat la instrucció return, la meva funció hauria fet la suma internament però no hauria enviat el resultat cap a fora, retornant automàticament el valor buit None. Això m'hauria impedit desar el preu en una variable o fer-lo servir més endavant per calcular els descomptes i l'IVA.

Exercici 5:

Quina diferència hi ha entre print() i return?

Segons el que vaig veure fent els exercicis, la diferència principal és que print() només em serveix per mostrar text o valors per pantalla perquè l'usuari els pugui llegir, però no puc aprofitar aquest resultat per fer altres càlculs. En canvi, amb return finalitzo l'execució de la funció i envio el resultat calculat de tornada al lloc des d'on l'he cridada, cosa que em permet guardar-lo en una variable o reutilitzar-lo en altres operacions.

Per què és millor dividir un programa en funcions?

Vaig comprovar que dividir un programa llarg en funcions més petites em permet tenir el codi molt més endreçat, net i fàcil de llegir. A més, em facilita molt la feina a l'hora de buscar i corregir errors, ja que cada part té una tasca concreta, i m'evita haver d'escriure el mateix codi repetidament en diferents llocs del meu programa.

Què és un paràmetre?

És una variable especial que escric dins dels parèntesis quan defineixo una funció. Actua com una porta d'entrada que em permet passar dades des de l'exterior cap a l'interior de la funció perquè aquesta pugui treballar amb elles.

Què és una variable local?

És una variable que creo i utilitzo exclusivament dins del bloc de codi d'una funció. Aquesta variable només existeix mentre la funció s'està executant i no la puc llegir ni modificar des de fora d'ella, cosa que m'evita conflictes amb altres variables de la resta del programa.

Quins avantatges té reutilitzar una funció?

Reutilitzar una funció m'estalvia molt de temps i redueix considerablement la quantitat de línies de codi que he d'escriure. A més, em garanteix que una mateixa operació (com calcular un descompte o l'IVA) s'apliqui sempre exactament de la mateixa manera en tot el programa, minimitzant el risc de cometre errors i facilitant qualsevol canvi futur que vulgui fer.
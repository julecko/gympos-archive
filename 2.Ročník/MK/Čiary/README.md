## Poznámky k úlohám
#### Čiary
Čo sa týka úloh s čiarami, je to viac menej jasné:
- V prvom príklade sa zvyšuje Y-ova súradnica aby čiary išli postupne nižšie s tým, že X-ove zostáva rovnaká aby čiary boli vodorovné tak ako na obrázku
- V druhom príklade čiary zostávajú vodorovné a skracujú sa, teda X-ova súradnica sa zľava zväčšuje, ide bližšie k pravej súradnici a teda čiara medzi nimi je kratšia
- V treťom príklade sa čiary nakláňajú čoraz viac a viac a to sa zaručuje tak, že sa druhá Y-ova súradnica zväčšuje viac ako prvá. V našom prípade zostáva prvá súradnica konštantá a druhá sa každou iteráciou (loopom/opakovaním) zväčšuje viac a viac

| Vo všetkých prípadoch bola k Y-ovej súradnici pripočítaná hodnota 10 z dôvodu viditeľnosti. Bez daného prídavku by pri prvom opakovaní bola Y-ova hodnota 0 a teda by čiara nebola veľmi viditeľná
#### Schody
Tu je to už kúsok komplikovanejšie
- V oboch prípadoch v jednom opakovaní sa tvorí čiara aj vodorovná aj horizontálna a to tak, že pri vodorovnej sú Y-ove hodnoty rovnaké na oboch stranách a druhá X-ova súradnica je o 50 väčšia ako prvá X-ova súradnica. To, že sa zväčšuje o 50 pixelov je len náhodný výber dĺžky/výšky schoda. V prípade horizontálnej čiary sú X-ove súradnice identické a druhá Y-ova o 50 väčšia ako prvá.
- Pri schodoch dole sa mení len to, že Y-ova súradnica sa nazväčšuje každým opakovaním, ale zmenšuje. Keďže sa ale zmenšuje, tak nemôže začínať na 0, pretože by sme nič nevideli a preto začína na súradnici 400
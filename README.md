Art Gallery Backend" je proširenje na postojeću web
aplikaciju "Art Gallery", koja je izgrađena u sklopu kolegija
Programsko inženjerstvo i omogućuje stvaranje i pregled virtualnih galerija.
Novi backend sustav omogućava spremanje i dohvat podataka o korisnicima,
izložbama i djelima. Registrirani korisnici mogu stvarati izložbe, dodavati
djela i komentirati tuđe radove, dok posjetitelji mogu samo pregledavati
izložbe.
Aplikacija će koristiti FastAPI u Pythonu za izradu backend
dijela, koji obrađuje zahtjeve poput spremanja i dohvaćanja podataka, a može se
pokretati unutar Docker kontejnera. Time backend postaje lako skalabilan jer se
može pokrenuti na više računala ako se poveća broj korisnika.
Podaci o korisnicima, izložbama i djelima pohranjuju se u
DynamoDB, distribuiranu bazu podataka koja se nalazi u oblaku. DynamoDB
osigurava brz pristup podacima s različitih uređaja i lokacija te pruža visoku
pouzdanost.
Kombinacijom FastAPI, Docker kontejnera i distribuirane baze
podataka u oblaku (DynamoDB), aplikacija "Art Gallery Backend" je
raspodijeljeni sustav.

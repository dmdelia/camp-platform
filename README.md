# CAMP

## Cosplay Animatronic Module Platform

### Engineering Design Document

**Dokumentversion:** 1.0

**Status:** In Entwicklung

**Projektbeginn:** Langfristiges Eigenprojekt

**Autor:** @dmdelia [YouTube](https://www.youtube.com/channel/UCyUWYqNNc91BDptC6sKk82Q)

---

# Vorwort

CAMP (Cosplay Animatronic Module Platform) ist ein langfristiges Forschungs- und Entwicklungsprojekt mit dem Ziel, eine modulare Plattform für tragbare und autonome Animatronics zu entwickeln.

Der Schwerpunkt liegt dabei nicht auf der Konstruktion einzelner Cosplays, sondern auf der Entwicklung einer universellen technischen Plattform, welche verschiedene Charaktere unterstützen kann.

In klassischen Cosplay-Projekten entsteht jede Figur als eigenständiges Einzelstück. Mechanik, Elektronik und Software werden häufig speziell für diesen einen Charakter entwickelt. Dadurch lassen sich nur wenige Komponenten wiederverwenden.

CAMP verfolgt einen anderen Ansatz.

Das Projekt behandelt einen Animatronic als ein modulares Robotersystem, dessen einzelne Komponenten unabhängig voneinander entwickelt, getestet und verbessert werden können.

Dadurch soll erreicht werden, dass zukünftige Charaktere auf derselben technischen Grundlage entstehen.

Ein einmal entwickeltes Endoskelett soll beispielsweise sowohl einen Freddy-, Bonnie-, Chica-, Foxy- oder Roxanne-Suit tragen können, ohne dass die gesamte Robotik neu entwickelt werden muss.

Ebenso soll jeder Suit sowohl von einem Menschen getragen als auch autonom vom Endoskelett betrieben werden können.

Dieses Dokument beschreibt sämtliche Entwurfsentscheidungen, langfristigen Ziele, technischen Konzepte sowie Entwicklungsrichtlinien des Projekts.

---

# 1. Projektphilosophie

CAMP basiert auf fünf grundlegenden Prinzipien.

## 1.1 Modularität

Kein Bauteil soll ausschließlich für einen einzigen Charakter entwickelt werden.

Mechanische Komponenten, Elektronik, Software und Kommunikationsprotokolle sollen möglichst universell einsetzbar sein.

Je höher die Wiederverwendbarkeit, desto geringer werden zukünftiger Entwicklungsaufwand, Wartungskosten und Fehlerrisiken.

---

## 1.2 Trennung von Charakter und Technik

Der Charakter stellt lediglich die äußere Erscheinung dar.

Die technische Plattform bleibt unabhängig davon bestehen.

Dadurch wird zwischen folgenden Ebenen unterschieden:

• Plattform

* Endoskelett
* Steuerung
* Energieversorgung
* KI
* Sensorik
* Software

und

• Charakter

* Kopf
* Fell
* Kleidung
* Farben
* Persönlichkeit
* Stimme
* Animationen

Diese Trennung ermöglicht den Austausch einzelner Charaktere ohne Änderungen an der Grundplattform.

---

## 1.3 Wartbarkeit

Jede Komponente muss einzeln austauschbar sein.

Kein Defekt soll den vollständigen Ausbau eines Suits erforderlich machen.

Deshalb gelten folgende Grundregeln:

* Schraubverbindungen statt Klebeverbindungen, sofern möglich.
* Standardisierte Steckverbinder.
* Modulare Kabelbäume.
* Dokumentierte Kabelführung.
* Austauschbare Elektronikmodule.
* Klare Zugänglichkeit für Wartungsarbeiten.

---

## 1.4 Erweiterbarkeit

Bereits während der Entwicklung muss berücksichtigt werden, dass zukünftige Funktionen derzeit noch unbekannt sind.

Deshalb soll jede Baugruppe genügend Reserven besitzen.

Beispiele:

* freie GPIO-Pins
* freie Stromleitungen
* Reserveplatz im Gehäuse
* zusätzliche Kommunikationsschnittstellen
* Software-Plugin-System
* standardisierte Datenprotokolle

---

## 1.5 Sicherheit

Obwohl CAMP primär ein Hobbyprojekt darstellt, besitzt die Sicherheit höchste Priorität.

Insbesondere tragbare Robotik stellt besondere Anforderungen an:

* Temperaturentwicklung
* Stromversorgung
* Kurzschlussschutz
* Notabschaltung
* mechanische Belastungen
* bewegliche Gelenke
* Sichtfeld
* Gewichtsverteilung

Jede Baugruppe muss unter dem Gesichtspunkt betrachtet werden, dass sie unmittelbar am menschlichen Körper betrieben werden kann.

---

# 2. Projektziele

Das Gesamtprojekt verfolgt sowohl kurzfristige als auch langfristige Ziele.

## Kurzfristige Ziele

* Entwicklung eines universellen Endoskeletts.
* Entwicklung einer modularen Elektronikplattform.
* Entwicklung einer einheitlichen Softwarearchitektur.
* Entwicklung erster Charakter-Suits.
* Entwicklung einer Entwicklungsumgebung.

---

## Mittelfristige Ziele

* autonome Charaktersteuerung
* KI-gestützte Gespräche
* Computer Vision
* Gesichtserkennung
* Gestenerkennung
* Telemetrie
* Remote-Debugging
* HUD-System
* Motion-Capture

---

## Langfristige Ziele

Langfristig soll CAMP eine Plattform darstellen, auf welcher sämtliche zukünftigen Animatronics aufbauen.

Neue Charaktere sollen überwiegend durch neue Gehäuseteile, Animationen und Konfigurationsdateien entstehen.

Die eigentliche Robotik bleibt dabei unverändert.

Dadurch reduziert sich die Entwicklungszeit zukünftiger Charaktere erheblich.

---

# 3. Systemübersicht

Die CAMP-Plattform besteht aus drei vollständig getrennten Systemen.

## System A - Endoskelett

Das Endoskelett bildet den eigentlichen Roboter.

Es enthält sämtliche Hochleistungskomponenten.

Dazu gehören unter anderem:

* Hauptcomputer
* KI-System
* Bewegungsplanung
* Kommunikationsmodule
* Sensorfusion
* Energieverwaltung
* Diagnosesystem
* Telemetrie
* Softwareplattform

Das Endoskelett besitzt keinerlei charakterbezogene Eigenschaften.

Es stellt ausschließlich die universelle Robotikplattform dar.

---

## System B - Suit

Der Suit stellt ausschließlich den Charakter dar.

Er enthält sämtliche sichtbaren Komponenten.

Dazu gehören:

* Kopf
* Gesicht
* Augen
* Mund
* Ohren
* Fell
* Kleidung
* Lautsprecher
* LEDs
* Servomechanismen
* Lüfter
* interne Verkabelung
* Sensoren
* Mikrocontroller

Der Suit besitzt bewusst keine komplexe Entscheidungslogik.

Er interpretiert lediglich Steuerbefehle der Plattform.

Dadurch bleibt jeder Suit möglichst einfach austauschbar.

---

## System C - Development Station

Die Development Station umfasst sämtliche Werkzeuge außerhalb des Roboters.

Hierzu zählen beispielsweise:

* Laptop
* Desktop-PC
* Tablet
* Smartphone
* Entwicklerkonsole
* Firmware-Manager
* Diagnosesoftware
* CAD-Arbeitsplatz
* Trainingsumgebung für KI

Dieses System dient ausschließlich Entwicklung, Wartung und Analyse.

Der reguläre Betrieb eines Animatronics darf nicht von einer permanenten Verbindung zur Development Station abhängig sein.

---

# 4. Designprinzipien

Vor jeder technischen Entscheidung soll geprüft werden, ob sie den folgenden Grundsätzen entspricht.

## Standardisierung

Jede wiederkehrende Baugruppe erhält einen definierten Standard.

Beispiele:

* Steckverbinder
* Schraubengrößen
* Servoanschlüsse
* Dateiformate
* Kommunikationsprotokolle
* Software-Schnittstellen

---

## Austauschbarkeit

Jede Baugruppe muss innerhalb weniger Minuten ersetzt werden können.

Dies betrifft insbesondere:

* Augenmodule
* Lautsprecher
* Servos
* Mikrocontroller
* Kameras
* Akkus
* Kabelbäume

Ein Defekt einzelner Komponenten darf niemals den vollständigen Neuaufbau eines Charakters erforderlich machen.

---

## Dokumentation

Jede entwickelte Baugruppe wird vollständig dokumentiert.

Zu jeder Baugruppe gehören mindestens:

* CAD-Modell
* technische Zeichnung
* Materialliste
* Verdrahtungsplan
* Firmware-Version
* Software-Schnittstellen
* bekannte Einschränkungen
* Wartungshinweise

Eine vollständige Dokumentation ist Bestandteil der Entwicklung und kein nachträglicher Arbeitsschritt.

# 5. Systemarchitektur

Die CAMP-Plattform ist als verteiltes, modulares Robotiksystem konzipiert. Anstatt sämtliche Funktionen auf einer einzelnen Hardware auszuführen, werden Aufgaben auf spezialisierte Komponenten verteilt. Dadurch steigt die Wartbarkeit, Skalierbarkeit und Fehlertoleranz des Gesamtsystems.

Jede Baugruppe besitzt eine klar definierte Aufgabe sowie eindeutig dokumentierte Schnittstellen.

Die grundsätzliche Systemarchitektur gliedert sich in folgende Ebenen:

* Mechanik
* Elektronik
* Embedded Software
* Hochleistungssoftware
* Künstliche Intelligenz
* Benutzerinteraktion
* Externe Entwicklungsumgebung

Keine Ebene soll direkt von der internen Implementierung einer anderen Ebene abhängig sein. Stattdessen erfolgt die Kommunikation ausschließlich über definierte Protokolle.

Dadurch können einzelne Komponenten ersetzt werden, ohne das Gesamtsystem neu entwickeln zu müssen.

---

## 5.1 Mechanische Ebene

Die mechanische Ebene umfasst sämtliche physischen Komponenten des Systems.

Hierzu gehören insbesondere:

* Endoskelett
* Gelenke
* Lager
* Servohalterungen
* Verbindungselemente
* Kabelkanäle
* Montagepunkte
* Charaktergehäuse
* Instrumente
* Zubehör

Die Mechanik besitzt keinerlei Kenntnis über Software oder KI.

Ihre einzige Aufgabe besteht darin, Bewegungen präzise und zuverlässig umzusetzen.

---

## 5.2 Elektronikebene

Die Elektronik verbindet Sensorik, Aktoren und Recheneinheiten miteinander.

Sie übernimmt unter anderem:

* Spannungsversorgung
* Stromverteilung
* Kommunikation
* Sensorschnittstellen
* Servoansteuerung
* Audio
* Video
* Sicherheitsfunktionen

Die Elektronik bildet die Brücke zwischen Mechanik und Software.

---

## 5.3 Embedded-Ebene

Embedded-Systeme übernehmen zeitkritische Aufgaben.

Beispiele:

* Servopositionierung
* PWM-Erzeugung
* Sensorabfrage
* Temperaturmessung
* Lüftersteuerung
* LED-Steuerung
* Akkumanagement

Diese Aufgaben werden bewusst nicht vom Hauptcomputer übernommen.

Dadurch bleibt die Steuerung auch bei hoher CPU-Auslastung stabil.

---

## 5.4 Hochleistungsebene

Der Hauptcomputer übernimmt sämtliche rechenintensiven Aufgaben.

Hierzu gehören beispielsweise:

* KI
* Sprachmodelle
* Kameraverarbeitung
* Computer Vision
* Bewegungsplanung
* Netzwerktechnik
* Logging
* Diagnosesysteme

Die Kommunikation mit den Embedded-Systemen erfolgt ausschließlich über standardisierte Schnittstellen.

---

## 5.5 Benutzerebene

Diese Ebene beschreibt sämtliche Interaktionsmöglichkeiten zwischen Mensch und System.

Dazu zählen:

* HUD
* interne Bedienelemente
* Spracheingabe
* Fernsteuerung
* Wartungsmodus
* Entwicklerkonsole

Sie bildet die Schnittstelle zwischen Bediener und Plattform.

---

# 6. Das Endoskelett

## 6.1 Zielsetzung

Das Endoskelett stellt die wichtigste Komponente der gesamten CAMP-Plattform dar.

Es ist nicht speziell für einen Charakter konstruiert, sondern dient als universeller Träger sämtlicher zukünftiger Suits.

Somit ist das Endoskelett kein "Freddy-Endo" oder "Bonnie-Endo".

Es ist lediglich die technische Plattform.

Jeder Charakter entsteht erst durch den aufgesetzten Suit.

---

## 6.2 Anforderungen

Das Endoskelett muss folgende Anforderungen erfüllen:

* modulare Bauweise
* hohe Stabilität
* möglichst geringes Gewicht
* einfache Wartbarkeit
* standardisierte Befestigungspunkte
* universelle Anschlussmöglichkeiten
* möglichst geringe Geräuschentwicklung
* hohe Zuverlässigkeit

Da das Endoskelett über viele Jahre weiterentwickelt werden soll, muss jedes Bauteil austauschbar sein.

---

## 6.3 Baugruppen

Das Endoskelett wird in mehrere Hauptmodule unterteilt.

### Kopfmodul

Der Kopf bildet die zentrale Plattform für:

* Kameras
* Mikrofone
* Lautsprecher
* Rechner
* Sensorik
* Kommunikationsmodule

Zusätzlich dient er als Befestigungspunkt für den Charakterkopf.

---

### Halsmodul

Der Hals verbindet Kopf und Oberkörper.

Er muss folgende Bewegungen ermöglichen:

* Drehen
* Neigen
* Anheben
* Absenken

Die Konstruktion muss ausreichend steif sein, um auch schwere Charakterköpfe sicher tragen zu können.

---

### Torso

Der Torso bildet den tragenden Kern des Endoskeletts.

Hier befinden sich unter anderem:

* Akku
* Stromverteilung
* Hauptplatine
* Mini-PC
* Kühlung
* Sicherungen

Der Torso dient gleichzeitig als strukturelles Rückgrat des gesamten Roboters.

---

### Arme

Die Arme bestehen aus standardisierten Segmenten.

Jedes Segment besitzt:

* Befestigungspunkte
* Kabelkanäle
* Servoaufnahmen
* Wartungsöffnungen

Die Segmentierung soll spätere Verbesserungen vereinfachen.

---

### Hände

Die Hände gehören zu den komplexesten mechanischen Baugruppen.

Sie müssen langfristig folgende Aufgaben ermöglichen:

* Greifen
* Zeigen
* Winken
* Instrumente halten
* Schalter bedienen
* Gesten darstellen

Eine vollständige menschenähnliche Hand besitzt zunächst keine Priorität.

Wichtiger sind robuste und zuverlässige Bewegungsabläufe.

---

# 7. Der Suit

## 7.1 Definition

Innerhalb von CAMP bezeichnet der Begriff "Suit" sämtliche charakterbezogenen Komponenten.

Der Suit ist kein gewöhnliches Cosplay.

Er stellt vielmehr ein intelligentes Peripheriegerät dar, welches über definierte Schnittstellen mit dem Endoskelett kommuniziert.

Dadurch kann derselbe Suit sowohl von einem Menschen als auch von einem Roboter verwendet werden.

---

## 7.2 Bestandteile

Ein Suit besteht grundsätzlich aus mehreren Modulen.

### Charakterkopf

Der Charakterkopf bestimmt maßgeblich die Wirkung des Animatronics.

Er enthält:

* äußere Hülle
* Augen
* Augenlider
* Mund
* Ohren
* LEDs
* Lautsprecher
* interne Mechanik

Die Konstruktion soll möglichst wartungsfreundlich erfolgen.

---

### Körper

Der Körper umfasst:

* Brust
* Rücken
* Schultern
* Bauch
* Hüfte

Er dient hauptsächlich der äußeren Darstellung des Charakters.

Gleichzeitig müssen sämtliche Kabel geschützt und sauber geführt werden.

---

### Arme und Beine

Die äußeren Extremitäten dienen hauptsächlich der optischen Gestaltung.

Sie müssen ausreichend Bewegungsfreiheit besitzen, um sowohl vom Menschen als auch vom Endoskelett genutzt werden zu können.

---

## 7.3 Suit-Elektronik

Jeder Suit besitzt eine eigene Elektronik.

Diese übernimmt ausschließlich lokale Aufgaben.

Beispiele:

* Servoansteuerung
* LED-Steuerung
* Sensoren
* Temperaturmessung
* Lüfter
* Audioverstärkung

Komplexe Entscheidungen werden grundsätzlich nicht im Suit getroffen.

Dadurch bleiben alle Charaktere technisch vergleichbar.

---

# 8. Docking-Konzept

Eines der zentralen Merkmale von CAMP ist das Docking-System.

Das Ziel besteht darin, einen Suit innerhalb weniger Minuten zwischen Mensch und Endoskelett wechseln zu können.

Hierfür müssen sowohl mechanische als auch elektrische Schnittstellen standardisiert werden.

---

## 8.1 Mechanisches Docking

Der Suit soll definierte Befestigungspunkte besitzen.

Diese ermöglichen eine reproduzierbare Montage.

Anforderungen:

* werkzeugarme Montage
* spielfreie Verbindung
* reproduzierbare Position
* einfache Wartung
* geringe Montagezeit

Langfristig soll jeder Suit dieselben Grundabmessungen der Plattform verwenden.

---

## 8.2 Elektrisches Docking

Zwischen Suit und Endoskelett soll möglichst nur eine einzige Hauptverbindung bestehen.

Über diese Verbindung werden übertragen:

* Versorgungsspannung
* Daten
* Audio
* Diagnosedaten
* Statusinformationen

Die Anzahl externer Kabel soll auf ein Minimum reduziert werden.

---

## 8.3 Automatische Erkennung

Nach dem Verbinden erkennt das Endoskelett automatisch den angeschlossenen Suit.

Anschließend wird die passende Konfiguration geladen.

Diese kann beispielsweise enthalten:

* Charaktername
* Servozuordnung
* LED-Konfiguration
* Audiobibliothek
* Bewegungsprofile
* Persönlichkeitsparameter
* Sicherheitsgrenzen

Dadurch wird kein manuelles Umkonfigurieren erforderlich.

Der Wechsel eines Charakters soll ähnlich einfach sein wie das Anschließen eines neuen Eingabegerätes an einen Computer.

---

# 9. Modulare Philosophie

Ein grundlegender Gedanke von CAMP besteht darin, dass nicht Figuren entwickelt werden.

Es wird eine Plattform entwickelt.

Jede neue Figur stellt lediglich eine neue Kombination bereits existierender Technologien dar.

Dadurch wächst das Projekt nicht linear, sondern exponentiell.

Mit jeder neu entwickelten Komponente steigt gleichzeitig die Anzahl möglicher zukünftiger Charaktere.

Das langfristige Ziel besteht deshalb nicht darin, möglichst schnell einen einzelnen Animatronic fertigzustellen.

Das eigentliche Ziel ist die Entwicklung einer technischen Plattform, auf der zukünftige Animatronics mit deutlich geringerem Entwicklungsaufwand entstehen können.

# 10. Mechanische Designphilosophie

Die Mechanik bildet das Fundament der gesamten CAMP-Plattform. Jede spätere Funktion - unabhängig davon, ob sie durch Software, Elektronik oder KI gesteuert wird - ist letztendlich durch die mechanischen Möglichkeiten begrenzt.

Aus diesem Grund besitzt die mechanische Konstruktion höchste Priorität.

Eine gut entwickelte Mechanik ermöglicht spätere Softwareverbesserungen.

Eine schlechte Mechanik kann dagegen selbst durch perfekte Software nicht vollständig kompensiert werden.

---

## 10.1 Entwicklungsreihenfolge

Die Entwicklung mechanischer Baugruppen erfolgt grundsätzlich in folgender Reihenfolge:

1. Konzept
2. CAD-Modell
3. Belastungsanalyse
4. 3D-Druck-Prototyp
5. Funktionstest
6. Überarbeitung
7. Finales Bauteil

Jede Baugruppe soll mindestens einen vollständigen Prototypen durchlaufen.

Direkt fertige Bauteile zu entwickeln widerspricht der Entwicklungsphilosophie von CAMP.

---

## 10.2 Konstruktionsrichtlinien

Alle mechanischen Komponenten sollen möglichst folgenden Grundsätzen entsprechen:

* geringe Teileanzahl
* einfache Montage
* möglichst wenige Spezialwerkzeuge
* hohe Steifigkeit
* geringes Gewicht
* standardisierte Schrauben
* möglichst wenige unterschiedliche Lagergrößen
* definierte Wartungszugänge

Komplexität soll nur dort entstehen, wo sie funktional notwendig ist.

---

## 10.3 Modulare Baugruppen

Jede größere Baugruppe wird unabhängig konstruiert.

Beispiele:

* Kopf
* Hals
* Schulter
* Oberarm
* Unterarm
* Hand
* Brust
* Rücken
* Hüfte

Jede Baugruppe besitzt definierte mechanische Schnittstellen.

Dadurch kann beispielsweise eine komplette Schulter ersetzt werden, ohne den gesamten Torso zerlegen zu müssen.

---

# 11. CAD-Richtlinien

Da CAMP überwiegend mittels 3D-Druck entwickelt wird, besitzt die CAD-Struktur einen hohen Stellenwert.

Alle Modelle sollen konsistent aufgebaut werden.

---

## 11.1 Dateistruktur

Jedes Bauteil erhält einen eindeutigen Namen.

Empfohlenes Schema:

CAMP-[System]-[Baugruppe]-[Bauteil]-vX.X

Beispiele:

* CAMP-ENDO-HEAD-NECKFRAME-v1.0
* CAMP-SUIT-FREDDY-EYEFRAME-v2.3
* CAMP-CORE-SERVOBRACKET-v1.1

Versionsnummern werden niemals überschrieben.

Änderungen erzeugen neue Versionen.

---

## 11.2 Baugruppenstruktur

Komplexe Modelle werden niemals als einzelnes CAD-Modell erstellt.

Stattdessen werden Baugruppen verwendet.

Beispiel:

Kopf

├── Schädel
├── Augenmodul
├── Augenlider
├── Kiefer
├── Ohren
├── Lautsprecherhalter
├── Kamerahalter
├── Servohalter
└── Wartungsdeckel

Dadurch können einzelne Komponenten unabhängig verbessert werden.

---

## 11.3 Parametrisches Design

Wo möglich sollen Maße parametrisiert werden.

Dadurch können beispielsweise später:

* größere Servos
* andere Lager
* andere Schrauben
* neue Sensoren

integriert werden, ohne sämtliche Modelle neu zu erstellen.

---

# 12. Der Charakterkopf

Der Kopf besitzt für den Betrachter die höchste Priorität.

Schon kleinste Ungenauigkeiten bei Blickrichtung oder Mimik wirken sofort unnatürlich.

Deshalb wird der Kopf als eigenständiges Teilprojekt behandelt.

---

## 12.1 Anforderungen

Ein Charakterkopf muss:

* stabil sein
* leicht sein
* wartbar sein
* realistische Bewegungen ermöglichen
* Kameras aufnehmen
* Lautsprecher aufnehmen
* Luftzirkulation ermöglichen
* Elektronik aufnehmen

Der Kopf darf niemals vollständig verklebt werden.

Alle wichtigen Komponenten müssen erreichbar bleiben.

---

## 12.2 Augen

Die Augen stellen wahrscheinlich die wichtigste Baugruppe des gesamten Charakters dar.

Menschen erkennen unnatürliche Augenbewegungen innerhalb von Millisekunden.

Deshalb besitzt ihre Entwicklung höchste Priorität.

Langfristig sollen die Augen folgende Bewegungen ermöglichen:

* links/rechts
* oben/unten
* gemeinsames Schielen
* unabhängige Bewegung
* Blinzeln
* Blickfokus
* Mikrobewegungen

Insbesondere Mikrobewegungen tragen erheblich zur Natürlichkeit eines Animatronics bei.

Ein vollständig statischer Blick wirkt bereits nach wenigen Sekunden künstlich.

---

## 12.3 Mund

Der Mund dient sowohl der Sprache als auch der Mimik.

Er soll langfristig verschiedene Bewegungen unterstützen.

Beispiele:

* geschlossen
* geöffnet
* leicht geöffnet
* Lächeln
* Überraschung
* Synchronisation mit Sprache

Die exakte Konstruktion wird zu einem späteren Zeitpunkt entwickelt.

---

## 12.4 Ohren

Je nach Charakter besitzen Ohren unterschiedliche Funktionen.

Sie können beispielsweise verwendet werden für:

* Aufmerksamkeit
* Emotionen
* Begrüßungen
* Überraschung
* Synchronisation mit Sprache
* Idle-Animationen

Da Ohren vergleichsweise leicht sind, können bereits kleine Servos überzeugende Bewegungen erzeugen.

---

# 13. Sichtsystem (Vision System)

Einer der wichtigsten Unterschiede zwischen einem klassischen Cosplay und CAMP besteht darin, dass der Träger den Charakter nicht durch Öffnungen im Kostüm beobachtet.

Stattdessen soll langfristig ausschließlich ein kamerabasiertes Sichtsystem verwendet werden.

Dadurch können die äußeren Proportionen deutlich originalgetreuer umgesetzt werden.

---

## 13.1 Frontkamera

Im Kopf wird mindestens eine Frontkamera installiert.

Sie übernimmt zwei Aufgaben.

Erstens:

Sicht für den Träger.

Zweitens:

Computer Vision für die KI.

Dadurch müssen keine getrennten Kameras installiert werden.

---

## 13.2 HUD

Das Kamerabild wird auf ein internes Display übertragen.

Zusätzlich können Informationen eingeblendet werden.

Beispiele:

SYSTEM ONLINE

Battery: 84 %

CPU: 46 °C

Suit Connected

Camera Active

Mic Level

Recording

Character: Freddy

Network: Connected

Warnings: None

Das HUD soll möglichst minimalistisch gestaltet werden, um den Träger nicht abzulenken.

---

## 13.3 Nachtsicht

Langfristig soll untersucht werden, ob zusätzliche Kameras integriert werden können.

Mögliche Erweiterungen:

* Infrarot
* Wärmebild
* Tiefenkamera
* Ultraweitwinkel
* Stereo-Vision

Nicht alle Funktionen müssen gleichzeitig verfügbar sein.

Die Plattform soll jedoch zukünftige Erweiterungen ermöglichen.

---

# 14. Audiosystem

Das Audiosystem dient sowohl der Darstellung des Charakters als auch der technischen Kommunikation.

Es besteht aus mehreren Komponenten.

---

## 14.1 Mikrofone

Mindestens ein Mikrofon wird dauerhaft installiert.

Anwendungsgebiete:

* Spracheingabe
* KI
* Geräuscherkennung
* Sprachaufzeichnung
* Kommunikation

Später können mehrere Mikrofone für Richtungsbestimmung ergänzt werden.

---

## 14.2 Lautsprecher

Die Lautsprecher übernehmen:

* Voice Lines
* Musik
* KI-Ausgabe
* Systemmeldungen

Je nach Charakter können unterschiedliche Klangprofile verwendet werden.

Beispielsweise:

Freddy

* tiefe Stimme

Bonnie

* leicht metallisch

Roxanne

* aggressiver Klang

Diese Unterschiede werden softwareseitig erzeugt.

---

## 14.3 Voice-Line-System

Alle Charaktere besitzen eigene Sprachbibliotheken.

Diese können bestehen aus:

* Begrüßungen
* Verabschiedungen
* Witzen
* Reaktionen
* Bühnensprüchen
* Systemmeldungen

Die Wiedergabe kann erfolgen durch:

* Tastendruck
* KI
* Skripte
* Fernsteuerung

Dadurch können sowohl vollständig autonome als auch manuell gesteuerte Auftritte realisiert werden.

---

# 15. Charakterkonfiguration

Jeder Charakter erhält eine eigene Konfigurationsdatei.

Diese beschreibt sämtliche Unterschiede zwischen den Charakteren.

Beispielsweise:

* Servoanzahl
* Servorichtung
* maximale Winkel
* LED-Farben
* Sprachprofil
* Lautstärke
* Audioeffekte
* Persönlichkeitsparameter
* Bewegungsprofile

Die Software des Endoskeletts arbeitet unabhängig vom jeweiligen Charakter.

Lediglich die Konfiguration verändert das Verhalten.

Dadurch kann dieselbe Softwareplattform beliebig viele Animatronics unterstützen.

Dieses Prinzip ist einer der wichtigsten Grundgedanken von CAMP und bildet die Grundlage für die langfristige Skalierbarkeit des gesamten Projekts.

# 16. Elektronikarchitektur

Die Elektronik der CAMP-Plattform bildet die Verbindung zwischen Mechanik und Software. Sie stellt sicher, dass sämtliche Sensoren, Aktoren und Recheneinheiten zuverlässig miteinander kommunizieren und mit Energie versorgt werden.

Ein wesentliches Ziel besteht darin, die Elektronik nicht als unübersichtliches Kabelsystem zu betrachten, sondern als klar strukturiertes, modulares Netzwerk.

Jede Platine besitzt eine definierte Aufgabe.

Jeder Steckverbinder besitzt eine definierte Funktion.

Jedes Kabel besitzt einen dokumentierten Verlauf.

Die Elektronik muss jederzeit nachvollziehbar, wartbar und erweiterbar bleiben.

---

## 16.1 Elektronikphilosophie

Während viele Robotikprojekte sämtliche Komponenten direkt miteinander verbinden, verfolgt CAMP einen modularen Bus-Ansatz.

Anstatt jede Baugruppe individuell zu verdrahten, erhält jedes Modul eine standardisierte Schnittstelle.

Beispiele:

* Kopfmodul
* Halsmodul
* Brustmodul
* Schultermodul
* Armmodul
* Handmodul
* HUD
* Audio
* Beleuchtung

Dadurch kann jedes Modul unabhängig entwickelt und getestet werden.

---

## 16.2 Hauptsysteme

Die Elektronik gliedert sich in mehrere Hauptbereiche.

### Energieversorgung

Verantwortlich für:

* Akkus
* Spannungswandlung
* Sicherungen
* Ladeüberwachung
* Stromverteilung

---

### Kommunikationssystem

Verantwortlich für:

* USB
* UART
* CAN (optional)
* I²C
* SPI
* Bluetooth
* WLAN

---

### Embedded Controller

Verantwortlich für:

* Servos
* LEDs
* Lüfter
* Sensoren
* Sicherheitssysteme

---

### Hochleistungsrechner

Verantwortlich für:

* KI
* Kameras
* Sprachmodelle
* Navigation
* Computer Vision
* Netzwerkdienste

---

# 17. Energieversorgung

Die Energieversorgung ist sicherheitskritisch.

Ein Ausfall darf niemals zu unkontrollierten Bewegungen oder gefährlichen Situationen führen.

Deshalb wird das Stromsystem redundant überwacht.

---

## 17.1 Energiequellen

Langfristig sollen mehrere Energiequellen unterstützt werden.

Beispiele:

* interner Akku
* externes Netzteil
* Laborstromversorgung
* stationärer Demonstrationsbetrieb

Die Plattform soll automatisch erkennen, welche Energiequelle aktuell verwendet wird.

---

## 17.2 Spannungsbereiche

Unterschiedliche Komponenten benötigen unterschiedliche Versorgungsspannungen.

Beispielsweise:

* Servos
* Mini-PC
* LEDs
* Mikrocontroller
* Kameras
* Displays
* Audioverstärker

Diese Spannungen werden zentral erzeugt und überwacht.

---

## 17.3 Sicherheitsfunktionen

Folgende Schutzmechanismen sind verpflichtend.

* Kurzschlussschutz
* Überstromschutz
* Temperaturüberwachung
* Spannungsüberwachung
* Notabschaltung
* Akkuwarnung

Sicherheitsfunktionen besitzen grundsätzlich höhere Priorität als Komfortfunktionen.

---

# 18. Embedded-Systeme

Embedded-Systeme übernehmen sämtliche zeitkritischen Aufgaben.

Sie arbeiten unabhängig vom Hauptcomputer.

Selbst wenn das KI-System neu startet, sollen grundlegende Funktionen weiterhin verfügbar bleiben.

---

## 18.1 Aufgaben

Embedded Controller übernehmen beispielsweise:

* Servoansteuerung
* LED-Steuerung
* Lüfter
* Temperaturmessung
* Taster
* Statusanzeigen
* Sensordatenerfassung

Sie besitzen keine komplexe Entscheidungslogik.

---

## 18.2 Firmware

Jedes Embedded-Modul erhält eine eigene Firmware.

Diese Firmware besitzt:

* Versionsnummer
* Änderungsprotokoll
* Konfigurationsdatei
* Diagnosemodus
* Updatefunktion

Dadurch können einzelne Module unabhängig aktualisiert werden.

---

## 18.3 Watchdog

Alle Embedded-Systeme besitzen einen Watchdog.

Sollte die Software abstürzen, erfolgt automatisch ein Neustart.

Dadurch wird die Betriebssicherheit erhöht.

---

# 19. Softwarearchitektur

Die Software bildet das eigentliche Nervensystem der CAMP-Plattform.

Sie verbindet sämtliche Hardwarekomponenten zu einem gemeinsamen System.

Die Architektur orientiert sich an modernen Robotiksystemen.

Anstatt ein großes Programm zu entwickeln, besteht CAMP aus vielen unabhängigen Diensten.

Jeder Dienst übernimmt genau eine Aufgabe.

---

## 19.1 Serviceorientierte Architektur

Beispiele möglicher Dienste:

Camera Service

   ↓

liefert Kamerabilder

---

Audio Service

   ↓

spielt Sounds ab

---

Servo Service

   ↓

bewegt Aktoren

---

Vision Service

   ↓

erkennt Personen

---

Speech Service

   ↓

Spracherkennung

---

AI Service

   ↓

entscheidet über Verhalten

---

Telemetry Service

   ↓

zeichnet Systemdaten auf

Jeder Dienst kommuniziert ausschließlich über definierte Schnittstellen.

---

## 19.2 Vorteile

Diese Architektur besitzt mehrere Vorteile.

Ein Fehler im Audio-System beeinflusst beispielsweise nicht das Kamerasystem.

Ebenso kann die KI aktualisiert werden, ohne den Servo-Controller zu verändern.

Dadurch bleibt das Gesamtsystem stabil und wartbar.

---

# 20. Kommunikationsmodell

Die CAMP-Plattform besitzt mehrere voneinander getrennte Kommunikationskanäle.

Jeder Kanal erfüllt einen bestimmten Zweck.

---

## Kanal 1

Embedded ↔ Embedded

Für:

* Sensordaten
* LEDs
* Servos
* Temperatur

---

## Kanal 2

Embedded ↔ Hauptcomputer

Für:

* Steuerbefehle
* Diagnosedaten
* Statusmeldungen

---

## Kanal 3

Suit ↔ Endoskelett

Für:

* Aktoren
* Sensoren
* Stromversorgung
* Audio
* Konfiguration

---

## Kanal 4

Endoskelett ↔ Laptop

Für:

* Entwicklung
* Telemetrie
* Konsole
* Firmware
* Dateien
* Video

---

# 21. Telemetriesystem

Jedes System erzeugt kontinuierlich Diagnosedaten.

Diese dienen sowohl der Entwicklung als auch der Fehlersuche.

---

## 21.1 Aufzuzeichnende Daten

Beispiele:

CPU-Auslastung

RAM-Auslastung

Temperaturen

Akkuspannung

Stromaufnahme

Lüfterdrehzahl

Signalstärke

Netzwerkstatus

Servoauslastung

Audiopegel

Fehlercodes

---

## 21.2 Logging

Jede relevante Aktion wird protokolliert.

Beispiele:

Systemstart

Suit verbunden

Firmware aktualisiert

Akku gewechselt

Temperaturwarnung

Servo deaktiviert

Benutzer angemeldet

Voice Line gestartet

Dadurch lassen sich Fehler auch nach längerer Zeit nachvollziehen.

---

## 21.3 Entwicklerkonsole

Die Entwicklerkonsole dient ausschließlich Wartung und Entwicklung.

Mögliche Funktionen:

* Live-Logs
* Prozessübersicht
* Sensordaten
* Neustart einzelner Dienste
* Kalibrierung
* Bewegungseditor
* Audioeditor
* Kamerakonfiguration
* Firmwareverwaltung

Die Entwicklerkonsole soll langfristig als eigenständige Desktop-Anwendung entwickelt werden.

---

# 22. Software-Module

Um die Komplexität der Plattform zu reduzieren, wird die Software in Module unterteilt.

Ein Modul besitzt:

* klar definierte Aufgabe
* klar definierte Eingaben
* klar definierte Ausgaben
* dokumentierte Schnittstellen

Beispiele:

CAMP.Core

Grundfunktionen der Plattform

---

CAMP.Audio

Musik

Voice Lines

TTS

Audioverwaltung

---

CAMP.Vision

Kameras

Personenerkennung

Objekterkennung

Gesichtserkennung

---

CAMP.Motion

Servoverwaltung

Animationen

Inverse Kinematik

Bewegungsplanung

---

CAMP.Telemetry

Monitoring

Logs

Diagnose

---

CAMP.Network

Bluetooth

WLAN

Remote-Verbindungen

---

CAMP.Character

Charakterprofile

Konfigurationen

Animationen

Persönlichkeiten

---

# 23. Designregel: Plattform vor Funktion

Während der gesamten Entwicklung gilt eine übergeordnete Regel.

Neue Funktionen werden niemals speziell für einen einzelnen Charakter entwickelt.

Stattdessen wird stets gefragt:

"Kann diese Funktion zukünftig auch von anderen Charakteren genutzt werden?"

Falls ja, wird sie Bestandteil der Plattform.

Falls nein, gehört sie in die Charakterkonfiguration.

Diese Denkweise verhindert, dass CAMP mit der Zeit zu einer Sammlung einzelner Sonderlösungen wird.

Stattdessen wächst eine konsistente technische Plattform, deren Fähigkeiten mit jedem Entwicklungsabschnitt zunehmen und auf der zukünftige Animatronics nahezu ausschließlich durch neue Mechanik, neue Charakterprofile und neue kreative Ideen entstehen.

# Teil IV - Künstliche Intelligenz und Robotik

# 24. Künstliche Intelligenz innerhalb von CAMP

## 24.1 Zielsetzung

Künstliche Intelligenz stellt innerhalb von CAMP keinen Selbstzweck dar.

Das Ziel besteht nicht darin, möglichst viele moderne KI-Technologien einzusetzen, sondern einen glaubwürdigen Charakter zu erschaffen, der mit Menschen natürlich interagieren kann.

Die KI dient somit als "Persönlichkeits-Engine" des Animatronics.

Sie entscheidet nicht ausschließlich über Bewegungen oder Sprache, sondern verbindet Wahrnehmung, Charakterwissen und Verhaltensregeln zu einer konsistenten Darstellung der jeweiligen Figur.

Ein erfolgreicher Animatronic zeichnet sich nicht dadurch aus, dass er möglichst intelligent wirkt, sondern dadurch, dass er glaubwürdig wie **Freddy**, **Bonnie**, **Roxanne**, **Chica** oder jeder andere dargestellte Charakter handelt.

---

## 24.2 Grundprinzip

Die KI wird vollständig vom eigentlichen Charakter getrennt.

Das KI-System besitzt zunächst keinerlei Wissen darüber, welchen Charakter es gerade steuert.

Erst beim Start wird eine Charakterdefinition geladen.

Diese definiert unter anderem:

* Name
* Stimme
* Sprachstil
* bevorzugte Gesten
* Blickverhalten
* Bewegungsintensität
* Humor
* Höflichkeit
* Lautstärke
* bevorzugte Animationen

Dadurch bleibt dieselbe KI für sämtliche zukünftigen Charaktere nutzbar.

---

## 24.3 Entscheidungsmodell

Die KI trifft Entscheidungen nicht direkt.

Zwischen Wahrnehmung und Bewegung befinden sich mehrere Verarbeitungsschichten.

Beispiel:

Kamera

   ↓

Person erkannt

   ↓

Vision-System

   ↓

"Erwachsene Person"

   ↓

Charakterlogik

   ↓

"Freddy begrüßt Gäste."

   ↓

Animationssystem

   ↓

Winken

   ↓

Servo Controller

   ↓

Bewegung

Dadurch bleibt jede Verarbeitungsebene unabhängig.

---

# 25. Wahrnehmung (Perception)

Die Grundlage jeder intelligenten Entscheidung ist die Wahrnehmung der Umgebung.

CAMP betrachtet sämtliche Sensoren als gemeinsame Informationsquelle.

Kein Sensor arbeitet isoliert.

---

## 25.1 Kameras

Die Kamera liefert kontinuierlich Bilddaten.

Mögliche Anwendungen:

* Personen erkennen
* Gesichter erkennen
* Gesten erkennen
* Hindernisse erkennen
* Position bestimmen
* Instrumente erkennen
* Marker erkennen

Langfristig kann dieselbe Kamera sowohl vom Träger als auch von der KI verwendet werden.

---

## 25.2 Mikrofone

Mikrofone dienen nicht ausschließlich Spracheingaben.

Sie können ebenfalls verwendet werden für:

* Geräuscherkennung

* Richtungsbestimmung

* Musik

* Applaus

* Klatschen

* Zurufe

* Lautstärkemessung

Dadurch entsteht eine zusätzliche Wahrnehmungsebene.

---

## 25.3 Interne Sensorik

Neben der Außenwelt überwacht CAMP ständig seinen eigenen Zustand.

Hierzu zählen beispielsweise:

* Temperaturen

* Akkuzustand

* CPU-Auslastung

* Lüfter

* Servopositionen

* Spannungen

* Motorströme

* Netzwerkstatus

Diese Informationen beeinflussen ebenfalls das Verhalten.

Ein Animatronic mit niedrigem Akkustand soll beispielsweise keine besonders energieintensiven Animationen mehr auswählen.

---

# 26. Charaktersystem

Das Charaktersystem stellt einen der wichtigsten Bestandteile der Plattform dar.

Es sorgt dafür, dass dieselbe KI unterschiedliche Persönlichkeiten darstellen kann.

---

## 26.1 Charakterdefinition

Jeder Charakter besitzt eine eigene Konfigurationsdatei.

Diese beschreibt unter anderem:

Name

Alter (Lore)

Franchise

Stimme

Sprechgeschwindigkeit

Emotionen

Animationsstil

Lieblingsgesten

Leerlaufanimationen

Musikstil

Instrument

Farbschema

Sicherheitsparameter

Dadurch kann später jeder neue Charakter ausschließlich über Konfigurationsdateien erweitert werden.

---

## 26.2 Persönlichkeitsparameter

Anstatt komplette Programme für jeden Charakter zu schreiben, verwendet CAMP Parameter.

Beispiele:

Freddy

Freundlich: 95 %

Neugierig: 70 %

Ruhig: 90 %

Verspielt: 55 %

---

Roxanne

Selbstbewusst: 100 %

Ungeduldig: 60 %

Dynamisch: 95 %

Bewegungsintensität: Hoch

---

Bonnie

Locker

Musikalisch

Aktiv

Verspielt

Diese Parameter beeinflussen später Entscheidungen der KI.

---

## 26.3 Wissensbasis

Jeder Charakter besitzt eine eigene Wissensbasis.

Sie enthält beispielsweise:

* Name

* Geschichte

* Beziehungen

* Lieblingssprüche

* Bühnenprogramm

* Instrument

* typische Begrüßungen

Die Wissensbasis enthält ausschließlich Informationen, welche zum jeweiligen Charakter passen.

Dadurch bleibt die Immersion erhalten.

---

# 27. Bewegungsintelligenz

Die KI entscheidet niemals direkt über einzelne Servowinkel.

Stattdessen arbeitet sie mit abstrakten Aktionen.

Beispielsweise:

"Zum Gast schauen"

"Nach links winken"

"Nicken"

"Lachen"

"Gitarrenhaltung einnehmen"

Erst das Bewegungsmodul übersetzt diese Aktionen in konkrete Gelenkbewegungen.

Dadurch können dieselben Aktionen auch bei zukünftigen Endoskeletten verwendet werden.

---

## 27.1 Bewegungsbibliothek

CAMP verwendet eine Bibliothek vorbereiteter Animationen.

Beispiele:

Idle

Begrüßung

Winken

Applaus

Lachen

Denken

Überrascht

Instrument halten

Kopf neigen

Blickkontakt herstellen

Diese Animationen werden später von der KI kombiniert.

---

## 27.2 Dynamische Animationen

Langfristig sollen Animationen nicht ausschließlich abgespielt werden.

Stattdessen können sie angepasst werden.

Beispielsweise:

Winken

   ↓

Person steht rechts

   ↓

Animation wird gespiegelt

   ↓

Winken nach rechts

Dadurch muss nicht jede Variante separat erstellt werden.

---

# 28. Verhaltenssystem

Ein Animatronic besteht nicht nur aus Sprache und Bewegung.

Mindestens ebenso wichtig ist sein Verhalten zwischen Interaktionen.

Diese Zeit wird als "Idle State" bezeichnet.

---

## 28.1 Idle-Verhalten

Während kein Benutzer aktiv mit dem Charakter spricht, soll dieser dennoch lebendig wirken.

Beispiele:

* leichtes Atmen

* zufällige Blickbewegungen

* Ohren bewegen

* Blinzeln

* Gewichtsverlagerung

* Umgebung beobachten

Diese kleinen Bewegungen erzeugen einen deutlich realistischeren Eindruck als vollständig statische Figuren.

---

## 28.2 Aufmerksamkeit

Die KI bewertet kontinuierlich ihre Umgebung.

Mögliche Ereignisse:

Eine Person nähert sich.

   ↓

Blickkontakt herstellen.

   ↓

Begrüßen.

---

Musik startet.

   ↓

Zum Rhythmus bewegen.

---

Jemand winkt.

   ↓

Zurückwinken.

---

Instrument wird erkannt.

   ↓

Spielanimation vorbereiten.

---

Die eigentliche Interaktion entsteht dadurch nicht erst durch Sprache, sondern bereits durch das Verhalten des Charakters.

Dadurch wirkt der Animatronic wesentlich präsenter und glaubwürdiger.

# 29. Sprachsystem

## 29.1 Zielsetzung

Das Sprachsystem bildet die primäre Kommunikationsschnittstelle zwischen Animatronic und Mensch.

Dabei verfolgt CAMP zwei unterschiedliche Betriebsarten:

1. Manuell gesteuerte Sprache
2. Autonome KI-gestützte Sprache

Beide Modi verwenden dieselbe Audioinfrastruktur und können jederzeit gewechselt werden.

Dadurch bleibt das System sowohl für Cosplay-Einsätze als auch für autonome Demonstrationen geeignet.

---

## 29.2 Sprachpipeline

Die Sprachverarbeitung erfolgt in mehreren Schritten.

Mikrofon

   ↓

Audioverarbeitung

   ↓

Speech-to-Text

   ↓

Sprachmodell

   ↓

Antwortgenerierung

   ↓

Text-to-Speech

   ↓

Audioeffekte

   ↓

Lautsprecher

Jede Stufe kann unabhängig ersetzt oder verbessert werden.

---

## 29.3 Charakterstimme

Die eigentliche Stimme setzt sich aus mehreren Komponenten zusammen.

Beispiele:

* Stimmlage
* Sprechgeschwindigkeit
* Lautstärke
* Sprachstil
* Betonung
* Filter
* Nachhall
* Verzerrung

Dadurch kann dieselbe zugrunde liegende Sprachsynthese unterschiedlichste Charaktere erzeugen.

---

## 29.4 Sprachregeln

Nicht jede Antwort des Sprachmodells wird unmittelbar ausgegeben.

Vor jeder Ausgabe erfolgt eine Charakterprüfung.

Dabei wird überprüft:

* Passt die Antwort zur Persönlichkeit?
* Passt sie zur Lore?
* Ist sie verständlich?
* Ist sie angemessen?
* Widerspricht sie früheren Aussagen?

Erst anschließend wird die endgültige Ausgabe erzeugt.

Dadurch bleibt das Verhalten konsistent.

---

# 30. Motion Engine

Während das Charaktersystem entscheidet, *was* passieren soll, entscheidet die Motion Engine, *wie* die Bewegung ausgeführt wird.

Sie bildet die Verbindung zwischen KI und Mechanik.

---

## 30.1 Bewegungsmodell

Anstatt einzelne Servos anzusteuern, arbeitet die Motion Engine mit abstrakten Körperteilen.

Beispiele:

Kopf

Hals

Augen

Augenlider

Mund

Schultern

Arme

Hände

Torso

Ohren

Dadurch bleibt die Software unabhängig vom mechanischen Aufbau.

---

## 30.2 Bewegungsprioritäten

Nicht jede Bewegung besitzt dieselbe Priorität.

Beispielsweise:

Not-Aus

   ↓

höchste Priorität

---

Balance

   ↓

sehr hoch

---

Kopfbewegungen

   ↓

hoch

---

Armbewegungen

   ↓

mittel

---

Idle-Animationen

   ↓

niedrig

Sollten mehrere Bewegungen gleichzeitig ausgeführt werden, entscheidet die Priorität über ihre Reihenfolge.

---

## 30.3 Bewegungsmischung

Mehrere Animationen können gleichzeitig aktiv sein.

Beispiel:

Idle-Animation

*

Blickkontakt

*

Sprechen

*

Ohren bewegen

*

Blinzeln

Alle Bewegungen werden miteinander kombiniert.

Dadurch entstehen wesentlich natürlichere Animationen.

---

# 31. Sicherheitslogik

Sicherheit besitzt innerhalb der KI höchste Priorität.

Eine fehlerhafte Bewegung darf niemals Personen gefährden.

---

## 31.1 Bewegungsgrenzen

Jedes Gelenk besitzt definierte Grenzwerte.

Diese umfassen unter anderem:

* Minimalwinkel

* Maximalwinkel

* Maximalgeschwindigkeit

* Maximalbeschleunigung

* Maximalstrom

Diese Werte werden niemals überschritten.

---

## 31.2 Kollisionsschutz

Die KI berücksichtigt mögliche Kollisionen.

Beispiele:

Arm würde Kopf treffen.

   ↓

Bewegung abbrechen.

---

Finger würden Instrument einklemmen.

   ↓

Alternative Bewegung wählen.

---

Kopf würde Suit berühren.

   ↓

Bewegung begrenzen.

Mechanische Grenzen besitzen grundsätzlich Vorrang vor Bewegungswünschen.

---

## 31.3 Menschenschutz

Wird der Suit von einer Person getragen, gelten zusätzliche Einschränkungen.

Beispiele:

* keine schnellen Bewegungen im Kopfbereich
* begrenzte Armgeschwindigkeit
* reduzierte Servokräfte
* zusätzliche Temperaturüberwachung

Der Schutz des Trägers besitzt stets höchste Priorität.

---
# 32. Motion Capture

## 32.1 Motivation

Realistische Bewegungen gehören zu den schwierigsten Aufgaben eines Animatronics.

Von Hand programmierte Animationen wirken häufig künstlich oder wiederholen sich zu stark.

CAMP verfolgt daher langfristig den Einsatz von Motion Capture.

Dabei werden reale Bewegungen aufgezeichnet und anschließend analysiert.

---

## 32.2 Ziel

Das Motion-Capture-System soll nicht lediglich fertige Animationen erzeugen.

Vielmehr entsteht eine Datenbasis, welche später zum Training intelligenter Bewegungsmodelle verwendet werden kann.

Somit wird jede aufgezeichnete Bewegung gleichzeitig Bestandteil der zukünftigen KI.

---

## 32.3 Datenaufzeichnung

Während einer Aufnahme werden möglichst viele Informationen synchron gespeichert.

Beispiele:

Zeitstempel

Kopfrotation

Armwinkel

Handposition

Blickrichtung

Augenbewegung

Mundstellung

Instrumentposition

Audio

Videobild

Tasten

Sensorwerte

Je vollständiger die Datenbasis ist, desto vielseitiger kann sie später genutzt werden.

---

# 33. Trainingsdaten

## 33.1 Datensatzstruktur

Alle Trainingsdaten sollen standardisiert gespeichert werden.

Jeder Datensatz besitzt mindestens:

* eindeutige ID
* Datum
* Charakter
* Version
* Aufnahmebedingungen
* Sensorliste
* Autor
* Softwareversion

Dadurch bleibt auch Jahre später nachvollziehbar, unter welchen Bedingungen die Aufnahme entstanden ist.

---

## 33.2 Bewegungsbibliothek

Nicht jede Aufnahme dient unmittelbar dem Training.

Viele Sequenzen werden zunächst als Bewegungsbibliothek gespeichert.

Beispiele:
- Winken
- Nicken
- Lachen
- Gitarrenhaltung
- Bücken
- Instrument aufnehmen
- Auf Publikum zeigen
- Verbeugen

Diese Bibliothek dient später als Grundlage für komplexere Animationen.

---

## 33.3 Datenqualität

Eine große Datenmenge ist wertlos, wenn ihre Qualität unzureichend ist.

Deshalb gelten folgende Anforderungen:

* vollständige Sensoraufzeichnung
* konstante Bildrate
* saubere Synchronisation
* eindeutige Beschriftung
* reproduzierbare Bewegungen

Lieber wenige hochwertige Aufnahmen als tausende unbrauchbare Datensätze.

---

# 34. Imitationslernen

Langfristig soll CAMP untersuchen, inwieweit Bewegungen durch Demonstration erlernt werden können.

Dieses Verfahren wird häufig als "Imitation Learning" oder "Behavior Cloning" bezeichnet.

Der Grundgedanke besteht darin, dass der Roboter menschliche Demonstrationen nachahmt.

---

## 34.1 Demonstration

Ein Mensch führt eine Bewegung aus.

   ↓

Alle Sensoren zeichnen auf.

   ↓

Datensatz entsteht.

   ↓

Modell wird trainiert.

   ↓

Animatronic wiederholt die Bewegung.

Dieser Ansatz eignet sich besonders für flüssige, organische Bewegungen.

---

## 34.2 Grenzen

Nicht jede menschliche Bewegung kann direkt übernommen werden.

Gründe:

* andere Gelenkgeometrie
* andere Freiheitsgrade
* andere Gewichtsverteilung
* andere Geschwindigkeit
* mechanische Grenzen

Deshalb müssen Bewegungen stets auf das Endoskelett angepasst werden.

---

# 35. Lernen durch Erfahrung

Neben Demonstrationen soll langfristig untersucht werden, ob bestimmte Fähigkeiten durch wiederholtes Üben verbessert werden können.

Mögliche Anwendungsfälle:

* Instrumente greifen
* Blickkontakt halten
* Gegenstände aufnehmen
* Gesten wiederholen
* Bewegungen präziser ausführen

Hierbei steht nicht Geschwindigkeit im Vordergrund, sondern Wiederholbarkeit und Zuverlässigkeit.

---

# 36. Bewegungsdatenbank

Mit fortschreitender Entwicklung entsteht eine umfangreiche Bibliothek sämtlicher Animationen.

Diese umfasst:

Standardanimationen

Charakteranimationen

Instrumentenanimationen

Idle-Animationen

Motion-Capture-Aufnahmen

Trainingsdaten

Experimentelle Bewegungen

Historische Versionen

Die Bewegungsdatenbank bildet langfristig einen der wertvollsten Bestandteile der CAMP-Plattform.

Während Hardware im Laufe der Jahre ersetzt wird, wächst diese Datenbasis kontinuierlich weiter und ermöglicht es zukünftigen Versionen des Systems, auf den Erfahrungen aller vorherigen Entwicklungsphasen aufzubauen.

Aus diesem Grund wird sie als eigenständige Kernkomponente der Plattform betrachtet und entsprechend versioniert, gesichert und dokumentiert.
---

# 37. Funktionierende Instrumente

## 37.1 Grundidee

Ein wesentliches Alleinstellungsmerkmal der CAMP-Plattform besteht darin, dass sämtliche Instrumente nicht ausschließlich als Requisiten dienen.

Sie sollen vollständig spielbar sein.

Dadurch unterscheiden sich die Charaktere nicht nur optisch von klassischen Cosplays, sondern können ihre Rolle auch funktional erfüllen.

Bonnie soll tatsächlich Gitarre spielen können.

Roxanne soll ihre Keytar tatsächlich verwenden können.

Chica könnte Percussion-Elemente integrieren.

Das Ziel besteht darin, Instrumente zu entwickeln, die sowohl auf einer Bühne als auch im Alltag als vollwertige Musikinstrumente genutzt werden können.

---

## 37.2 Designphilosophie

Die Instrumente werden nach folgenden Grundsätzen entwickelt:

* vollständige Spielbarkeit
* optische Nähe zur Vorlage
* hohe Wartbarkeit
* modulare Elektronik
* austauschbare Komponenten
* sichere Montage am Suit
* langfristige Erweiterbarkeit

Das Instrument ist nicht Teil des Suits.

Es stellt ein eigenständiges Modul der CAMP-Plattform dar.

Dadurch kann dasselbe Instrument unabhängig getestet, transportiert und verbessert werden.

---

## 37.3 Elektronik

Instrumente können je nach Charakter unterschiedliche Elektronik enthalten.

Beispiele:

* MIDI
* Audiointerfaces
* Effektprozessoren
* LEDs
* Sensorik
* Taster
* Displays
* Funkmodule

Dabei bleibt das eigentliche Instrument vollständig spielbar.

Zusätzliche Elektronik dient ausschließlich der Integration in CAMP.

---

# 38. Integration in CAMP

Instrumente werden als intelligente Peripheriegeräte betrachtet.

Sie besitzen definierte Kommunikationsschnittstellen zur Plattform.

Dadurch können sie sowohl mit dem Suit als auch mit dem Endoskelett kommunizieren.

---

## 38.1 Betriebsarten

Jedes Instrument unterstützt mehrere Modi.

### Freier Spielmodus

Das Instrument funktioniert unabhängig von CAMP.

Es kann wie ein gewöhnliches Musikinstrument verwendet werden.

---

### Cosplaymodus

Das Instrument kommuniziert mit dem getragenen Suit.

Beispiele:

* LEDs reagieren auf Musik.
* Animationen werden ausgelöst.
* Voice Lines werden gestartet.
* HUD zeigt Instrumentendaten.

---

### Animatronicmodus

Das Instrument kommuniziert mit dem Endoskelett.

Hierdurch können zusätzliche Funktionen entstehen.

Beispiele:

Der Animatronic erkennt automatisch, welches Instrument verbunden wurde.

↓

Passendes Bewegungsprofil wird geladen.

↓

Passende Voice Lines werden aktiviert.

↓

Passende Bühnenanimationen stehen zur Verfügung.

---

## 38.2 Instrumentenerkennung

Instrumente besitzen eine eindeutige Gerätekennung.

Beim Verbinden erkennt CAMP automatisch:

* Instrumententyp
* Firmwareversion
* Konfiguration
* verfügbare Funktionen

Dadurch entfällt eine manuelle Einrichtung.

---

# 39. Bühnenmodus

Langfristig soll CAMP einen speziellen Betriebsmodus für Auftritte besitzen.

Dieser unterscheidet sich deutlich vom normalen Interaktionsmodus.

---

## 39.1 Eigenschaften

Während eines Bühnenauftritts ändern sich verschiedene Prioritäten.

Beispiele:

* längere Animationen
* synchronisierte Bewegungen
* Musiksteuerung
* Showbeleuchtung
* feste Choreografien
* reduzierte Sprachinteraktionen

Dadurch kann sich der Animatronic vollständig auf die Performance konzentrieren.

---

## 39.2 Showskripte

Komplexe Bühnenauftritte werden als Skripte gespeichert.

Ein Skript beschreibt beispielsweise:

* Startposition
* Musik
* Licht
* Animationen
* Voice Lines
* Instrumenteneinsatz
* Abschluss

Dadurch können komplette Vorführungen reproduzierbar abgespielt werden.

---

## 39.3 Synchronisation

Mehrere CAMP-Systeme sollen langfristig gemeinsam auftreten können.

Beispiele:

Freddy

↓

Bonnie

↓

Chica

↓

Roxanne

↓

Synchronisierte Show

Hierfür wird ein gemeinsamer Zeitgeber verwendet.

Dadurch können Musik, Bewegungen und Licht exakt synchron bleiben.

---

# Teil VII - Benutzererlebnis und Mensch-Maschine-Interaktion

# 40. Human Interface

Die CAMP-Plattform besitzt zwei unterschiedliche Benutzergruppen.

1. Der Träger des Suits.

2. Der externe Entwickler.

Beide besitzen unterschiedliche Anforderungen.

---

## 40.1 Benutzer im Suit

Während des Tragens muss der Benutzer sämtliche wichtigen Informationen erhalten, ohne von ihnen überfordert zu werden.

Priorität besitzen:

* Übersichtlichkeit
* Lesbarkeit
* geringe Ablenkung
* schnelle Bedienbarkeit

Das System darf niemals erfordern, während eines Auftritts komplexe Menüs zu bedienen.

---

## 40.2 Externer Entwickler

Der Entwickler benötigt dagegen möglichst viele Informationen.

Beispiele:

* Prozessstatus
* Speicherverbrauch
* Netzwerk
* Diagnosen
* Sensorwerte
* Kamerabilder
* Debugdaten

Diese Informationen gehören ausschließlich in die Entwicklungssoftware.

---

# 41. HUD (Head-Up Display)

Das HUD bildet die wichtigste Benutzeroberfläche des Trägers.

Es ersetzt klassische Anzeigen und ermöglicht eine vollständig geschlossene Kopfkonstruktion.

---

## 41.1 Designziele

Das HUD soll:

* unauffällig
* kontrastreich
* schnell erfassbar
* modular
* konfigurierbar

sein.

Informationen werden nur angezeigt, wenn sie tatsächlich benötigt werden.

---

## 41.2 Informationsbereiche

Das HUD kann in mehrere Bereiche unterteilt werden.

Linke obere Ecke

Systemstatus

---

Rechte obere Ecke

Akku

---

Untere linke Ecke

Netzwerk

---

Untere rechte Ecke

Temperaturen

---

Zentrum

Kamerabild

Warnungen erscheinen ausschließlich bei Bedarf.

Dadurch bleibt das Sichtfeld möglichst frei.

---

## 41.3 Erweiterungen

Langfristig könnten zusätzliche Anzeigen integriert werden.

Beispiele:

Kompass

FPS

Audiopegel

Gesichtserkennung

Objekterkennung

Musiktempo

Bühnenposition

Motion-Capture-Status

Diese Erweiterungen sollen modular aktivierbar sein.

---

# 42. Bedienkonzept

Während eines Auftritts darf die Bedienung möglichst wenig Aufmerksamkeit erfordern.

Deshalb wird eine Kombination verschiedener Eingabemethoden vorgesehen.

---

## 42.1 Physische Bedienelemente

Mögliche Eingaben:

* Taster
* Schalter
* Joysticks
* Drehencoder
* Pedale

Sie dienen vor allem schnellen Funktionen.

---

## 42.2 Sprachbefehle

Langfristig können interne Sprachbefehle genutzt werden.

Beispiele:

"CAMP, Showmodus."

"CAMP, Diagnose."

"CAMP, Lautstärke fünfzig Prozent."

Diese Befehle unterscheiden sich von der eigentlichen Charakterkommunikation.

Sie richten sich ausschließlich an die Plattform selbst.

---

## 42.3 Entwicklerbefehle

Für Wartung und Entwicklung existiert ein separater Betriebsmodus.

Dieser erlaubt beispielsweise:

* Kalibrierung
* Firmwareupdates
* Servotests
* Sensorprüfung
* Netzwerkdiagnose
* Logexport

Diese Funktionen sind im normalen Betrieb nicht verfügbar.

---

## 42.4 Ziel der Benutzeroberfläche

Die Benutzeroberfläche soll sich nicht wie ein Computerprogramm anfühlen.

Sie soll den Eindruck vermitteln, als würde der Träger selbst zum Endoskelett werden.

Während eines Auftritts soll die Technik möglichst in den Hintergrund treten.

Die Bedienung muss intuitiv, schnell und zuverlässig erfolgen, sodass sich der Benutzer vollständig auf den Charakter konzentrieren kann.

Dieses Prinzip bildet die Grundlage sämtlicher zukünftiger Benutzeroberflächen innerhalb der CAMP-Plattform.

# 43. Netzwerkarchitektur

## 43.1 Grundprinzip

Die CAMP-Plattform ist so konzipiert, dass sie vollständig ohne Internetverbindung betrieben werden kann.

Alle Kernfunktionen müssen lokal verfügbar sein.

Dazu gehören insbesondere:

* Bewegungssteuerung
* Sprachsystem
* KI
* Kameraverarbeitung
* Telemetrie
* Audio
* HUD
* Charaktersteuerung

Internetzugang stellt lediglich eine optionale Erweiterung dar und darf niemals Voraussetzung für den Betrieb sein.

Dadurch bleibt das System unabhängig von Veranstaltungsorten, Netzwerkqualität oder externen Diensten.

---

## 43.2 Kommunikationsarten

Innerhalb der Plattform existieren drei Kommunikationsarten.

### Interne Kommunikation

Kommunikation zwischen einzelnen Komponenten des Roboters.

Beispiele:

* Hauptcomputer ↔ Mikrocontroller
* Mikrocontroller ↔ Sensoren
* Mikrocontroller ↔ Servotreiber
* Suit ↔ Endoskelett

Diese Kommunikation besitzt höchste Priorität.

---

### Lokale Kommunikation

Kommunikation zwischen CAMP und einem Entwicklergerät.

Beispiele:

Laptop

Tablet

Smartphone

Steam Deck

Entwicklungs-PC

Hierfür werden ausschließlich lokale Verbindungen verwendet.

---

### Externe Kommunikation

Kommunikation über das Internet.

Diese ist optional.

Mögliche Anwendungen:

* Datensicherung
* Softwareupdates
* Synchronisation
* Fernwartung

Ein Ausfall der Internetverbindung darf den Animatronic nicht beeinflussen.

---

# 44. Drahtlose Kommunikation

## 44.1 Bluetooth

Bluetooth dient als energiesparende Kurzstreckenverbindung.

Typische Anwendungen:

* Pairing
* Telemetrie
* Controller
* Notfallsteuerung
* Diagnose
* Gerätestatus

Aufgrund der begrenzten Bandbreite eignet sich Bluetooth nicht für größere Datenströme wie Videobilder.

---

## 44.2 WLAN

Für datenintensive Anwendungen wird WLAN verwendet.

Typische Anwendungen:

* Kamerastream
* Entwicklerkonsole
* Firmwareübertragung
* Logdateien
* Motion-Capture
* Dateiverwaltung

Das Netzwerk wird lokal erstellt.

Internet ist hierfür nicht notwendig.

---

## 44.3 Netzwerkrollen

Je nach Situation kann CAMP unterschiedliche Rollen übernehmen.

### Access Point

Das Endoskelett erstellt selbst ein WLAN.

Andere Geräte verbinden sich mit ihm.

Geeignet für:

* Conventions
* Messen
* Demonstrationen

---

### Client

Das Endoskelett verbindet sich mit einem vorhandenen Netzwerk.

Geeignet für:

* Werkstatt
* Zuhause
* Labor

---

### Offline

Keine Funkverbindung.

Alle Systeme arbeiten ausschließlich intern.

Dieser Modus besitzt die höchste Ausfallsicherheit.

---

# 45. Telemetrie

## 45.1 Ziel

Telemetrie dient der kontinuierlichen Überwachung sämtlicher Systemzustände.

Sie unterstützt sowohl Entwicklung als auch Wartung.

Alle wichtigen Messwerte sollen in Echtzeit verfügbar sein.

---

## 45.2 Kategorien

### Energie

* Akkustand
* Spannung
* Stromaufnahme
* Restlaufzeit

---

### Rechner

* CPU-Auslastung
* RAM
* Datenträger
* Temperaturen

---

### Mechanik

* Servopositionen
* Motorströme
* Gelenktemperaturen
* Bewegungsstatus

---

### Netzwerk

* Signalstärke
* Datenrate
* Paketverlust
* Latenz

---

### Sensorik

* Kamerastatus
* Mikrofone
* IMU
* Temperatur
* Luftfeuchtigkeit (optional)

---

## 45.3 Dashboard

Die Telemetrie wird über ein Dashboard dargestellt.

Das Dashboard besitzt mehrere Ansichten.

Operator

Nur wichtige Informationen.

---

Entwickler

Alle Messwerte.

---

Diagnose

Fehleranalyse.

---

Wartung

Kalibrierung.

Jede Ansicht ist auf ihre jeweilige Aufgabe optimiert.

---

# 46. Fehlermanagement

Eine komplexe Plattform benötigt ein strukturiertes Fehlersystem.

Fehlermeldungen dürfen nicht ausschließlich aus technischen Codes bestehen.

Sie müssen sowohl für Entwickler als auch für den späteren Betrieb verständlich sein.

---

## 46.1 Fehlerklassen

Information

Keine Aktion erforderlich.

Beispiel:

Update verfügbar.

---

Warnung

Das System funktioniert weiterhin.

Eine Überprüfung wird empfohlen.

Beispiel:

Akkustand niedrig.

---

Fehler

Eine Funktion ist eingeschränkt.

Beispiel:

Kamera ausgefallen.

---

Kritisch

Der sichere Betrieb ist nicht mehr gewährleistet.

Beispiel:

Überhitzung.

---

Notfall

Das System führt eine sofortige Sicherheitsreaktion aus.

Beispiel:

Kurzschluss erkannt.

---

## 46.2 Fehlercodes

Jeder Fehler erhält eine eindeutige Kennung.

Beispiel:

CAMP-001

Akku kritisch.

---

CAMP-014

Kamera getrennt.

---

CAMP-083

Servo nicht erreichbar.

---

CAMP-104

Temperaturgrenze überschritten.

Diese Kennungen vereinfachen Dokumentation und Fehlersuche erheblich.

---

## 46.3 Selbstdiagnose

Während des Startvorgangs überprüft CAMP sämtliche Kernkomponenten.

Unter anderem:

✓ Prozessor

✓ Speicher

✓ Kameras

✓ Mikrofone

✓ Lautsprecher

✓ Netzwerk

✓ Sensoren

✓ Controller

✓ Aktoren

✓ Konfigurationsdateien

Erst nach erfolgreicher Prüfung wird das System vollständig freigegeben.

---

## 46.4 Laufende Überwachung

Die Selbstdiagnose endet nicht nach dem Start.

Während des gesamten Betriebs werden alle Komponenten kontinuierlich überwacht.

Erkennt das System einen Defekt, entscheidet es abhängig von der Fehlerklasse über geeignete Maßnahmen.

Beispiele:

Neustart eines Softwaredienstes.

Deaktivierung eines Servos.

Reduzierung der Bewegungsgeschwindigkeit.

Warnung im HUD.

Information an den Entwickler.

Aktivierung des Sicherheitsmodus.

Dadurch kann CAMP auf viele Fehler reagieren, ohne dass der gesamte Animatronic ausfällt.

---

# 47. Sicherheitskonzept

Sicherheit besitzt in CAMP eine höhere Priorität als jede andere Funktion.

Ein spektakulärer Animatronic ist wertlos, wenn er den Träger oder andere Personen gefährdet.

Aus diesem Grund wird jede neue Funktion unter Sicherheitsaspekten bewertet.

---

## 47.1 Sicherheitsprinzipien

Für die gesamte Plattform gelten folgende Grundregeln.

**Safety before Performance**

Eine langsamere Bewegung ist einer gefährlichen Bewegung vorzuziehen.

**Predictable Behaviour**

Das System soll sich jederzeit nachvollziehbar verhalten.

Überraschende oder unkontrollierte Bewegungen sind zu vermeiden.

**Fail Safe**

Kann ein Fehler nicht sicher behandelt werden, geht das System automatisch in einen sicheren Zustand über.

---

## 47.2 Notfallmodus

Der Notfallmodus dient ausschließlich dem Schutz von Mensch und Hardware.

Beim Eintritt in diesen Zustand können beispielsweise folgende Maßnahmen erfolgen:

* Deaktivierung aller Hochlast-Aktoren
* Stoppen laufender Animationen
* Abschalten nicht benötigter Verbraucher
* Speichern der Logdateien
* Anzeige einer Warnung im HUD
* Akustische Rückmeldung für den Träger

Erst nach einer bewussten Bestätigung darf der normale Betrieb wieder aufgenommen werden.

---

## 47.3 Sicherheitsphilosophie

Während der Entwicklung wird jede Funktion anhand einer einfachen Frage bewertet:

> "Falls diese Funktion genau jetzt ausfällt - was passiert?"

Kann diese Frage nicht zufriedenstellend beantwortet werden, gilt die Funktion als unvollständig.

Diese Denkweise soll sicherstellen, dass CAMP nicht nur technisch beeindruckend, sondern auch langfristig zuverlässig und sicher betrieben werden kann.

# 48. Fertigungskonzept

## 48.1 Zielsetzung

Die CAMP-Plattform wird überwiegend als Eigenentwicklung gefertigt.

Dabei kommen moderne Fertigungsverfahren zum Einsatz, welche eine schnelle Iteration, hohe Flexibilität und kosteneffiziente Prototypen ermöglichen.

Das Ziel besteht nicht darin, jedes Bauteil möglichst hochwertig oder teuer herzustellen.

Stattdessen soll jedes Bauteil den Anforderungen seiner jeweiligen Aufgabe entsprechen.

Je nach Einsatzgebiet können daher unterschiedliche Fertigungsverfahren kombiniert werden.

---

## 48.2 Fertigungsmethoden

Die Plattform soll verschiedene Fertigungstechnologien unterstützen.

Beispiele:

* FDM-3D-Druck
* SLA-3D-Druck
* CNC-Bearbeitung
* Laserschneiden
* Wasserstrahlschneiden
* Frästeile
* Metallprofile
* Carbonrohre
* Aluminiumbauteile

Die Auswahl erfolgt nach technischen Anforderungen und nicht nach persönlicher Präferenz.

---

## 48.3 Prototyping

Jede neue Baugruppe beginnt als Prototyp.

Ein Prototyp besitzt ausdrücklich nicht das Ziel, perfekt zu sein.

Seine Aufgabe besteht darin, Fragen zu beantworten.

Beispiele:

Passt das Bauteil?

Ist die Mechanik ausreichend stabil?

Sind Wartungsöffnungen erreichbar?

Lässt sich das Kabel verlegen?

Kann der Servo ausreichend Kraft übertragen?

Erst nach erfolgreicher Beantwortung dieser Fragen erfolgt die Entwicklung einer verbesserten Version.

---

# 49. 3D-Druck-Richtlinien

Da der Großteil der Plattform additiv gefertigt wird, gelten verbindliche Konstruktionsrichtlinien.

Diese dienen sowohl der Druckbarkeit als auch der späteren Wartung.

---

## 49.1 Druckorientierung

Bereits während der Konstruktion muss berücksichtigt werden, in welcher Orientierung ein Bauteil gedruckt wird.

Dadurch lassen sich vermeiden:

* unnötige Stützstrukturen
* schwache Layerausrichtung
* schlechte Oberflächen
* lange Druckzeiten

Die Druckorientierung ist Bestandteil des CAD-Entwurfs.

---

## 49.2 Schraubverbindungen

Nach Möglichkeit werden verschraubte Verbindungen verwendet.

Vorteile:

* zerstörungsfreie Demontage
* Austauschbarkeit
* Wartbarkeit
* Wiederverwendbarkeit

Klebungen werden ausschließlich verwendet, wenn keine sinnvolle Alternative existiert.

---

## 49.3 Gewindeeinsätze

Bei häufig montierten Komponenten sollen Gewindeeinsätze verwendet werden.

Dadurch wird verhindert, dass Kunststoffgewinde durch wiederholtes Verschrauben beschädigt werden.

Dies betrifft insbesondere:

* Wartungsdeckel
* Servohalter
* Elektronikgehäuse
* Kameramodule
* Sensorhalter

---

## 49.4 Kabelmanagement

Bereits im CAD-Modell müssen Kabel berücksichtigt werden.

Jede Baugruppe erhält:

* Kabelkanäle
* Zugentlastungen
* Befestigungspunkte
* Wartungsreserven

Kabel dürfen niemals nachträglich "irgendwo" verlegt werden.

Sie sind Bestandteil der Konstruktion.

---

# 50. Versionsmanagement

Im Verlauf der Entwicklung entstehen hunderte CAD-Dateien, Firmwarestände und Softwareversionen.

Ohne klare Versionierung wird das Projekt langfristig unwartbar.

---

## 50.1 Versionierung

Jede Änderung erzeugt eine neue Version.

Versionen werden niemals überschrieben.

Beispiel:

v1.0

Erste funktionierende Version.

↓

v1.1

Kleine Verbesserungen.

↓

v1.2

Bugfixes.

↓

v2.0

Grundlegende Überarbeitung.

Dadurch bleibt jede Entwicklungsstufe nachvollziehbar.

---

## 50.2 Änderungsprotokoll

Zu jeder Version gehört ein Changelog.

Es beschreibt:

* neue Funktionen
* Fehlerbehebungen
* bekannte Probleme
* offene Aufgaben

Das Änderungsprotokoll ist Bestandteil jeder Veröffentlichung.

---

## 50.3 Archivierung

Historische Versionen werden dauerhaft archiviert.

Auch scheinbar veraltete Konstruktionen können später wertvolle Informationen enthalten.

Die Entwicklungsgeschichte der Plattform soll jederzeit nachvollziehbar bleiben.

---

# 51. Teststrategie

## 51.1 Philosophie

Jede Baugruppe wird getestet, bevor sie in das Gesamtsystem integriert wird.

Komplexe Systeme lassen sich wesentlich einfacher entwickeln, wenn ihre Komponenten bereits einzeln zuverlässig funktionieren.

---

## 51.2 Teststufen

Die Entwicklung erfolgt in mehreren Testphasen.

### Komponententest

Prüfung eines einzelnen Bauteils.

Beispiel:

Ein Servo.

---

### Modultest

Prüfung einer vollständigen Baugruppe.

Beispiel:

Augenmechanik.

---

### Integrationstest

Mehrere Module arbeiten gemeinsam.

Beispiel:

Augen

*

Kamera

*

HUD

---

### Systemtest

Der vollständige Animatronic wird getestet.

Alle Komponenten arbeiten gleichzeitig.

---

## 51.3 Dokumentation

Jeder Test wird dokumentiert.

Mindestens festgehalten werden:

* Datum
* Version
* Tester
* Ziel
* Ergebnis
* Beobachtungen
* Verbesserungen

Dadurch entsteht langfristig eine vollständige Entwicklungsdokumentation.

---

# 52. Wartung

Ein CAMP-System soll nicht nur funktionieren.

Es soll über Jahre hinweg instand gehalten und weiterentwickelt werden können.

---

## 52.1 Wartungsintervalle

Bestimmte Komponenten müssen regelmäßig überprüft werden.

Beispiele:

* Schrauben
* Lager
* Kabel
* Lüfter
* Akkus
* Steckverbinder
* Servos

Auch wenn kein Fehler sichtbar ist.

Vorbeugende Wartung erhöht die Zuverlässigkeit erheblich.

---

## 52.2 Austauschbarkeit

Kein einzelnes Bauteil soll dauerhaft fest mit einer anderen Baugruppe verbunden sein.

Idealerweise kann jede Komponente innerhalb weniger Minuten ersetzt werden.

Hierdurch reduziert sich sowohl die Reparaturzeit als auch das Risiko weiterer Beschädigungen.

---

## 52.3 Ersatzteile

Für häufig belastete Komponenten sollen Ersatzteile dauerhaft verfügbar sein.

Beispiele:

* Servohebel
* Zahnräder
* Lager
* Kabel
* Schrauben
* Halterungen

Dadurch können Reparaturen unmittelbar durchgeführt werden.

---

# 53. Entwicklungsphilosophie

Während der gesamten Projektlaufzeit gelten einige grundlegende Prinzipien.

Diese Regeln sollen sicherstellen, dass CAMP auch nach vielen Jahren konsistent bleibt.

---

## Regel 1

**Plattform vor Charakter.**

Technische Lösungen werden grundsätzlich für die Plattform entwickelt.

Nicht für einzelne Figuren.

---

## Regel 2

**Modularität vor Perfektion.**

Eine austauschbare Lösung ist einer perfekt optimierten Speziallösung vorzuziehen.

---

## Regel 3

**Dokumentation ist Teil der Entwicklung.**

Ein fertig konstruiertes Bauteil ohne Dokumentation gilt als unvollständig.

---

## Regel 4

**Prototypen sind Lernwerkzeuge.**

Ein gescheiterter Prototyp ist kein Misserfolg.

Er liefert Informationen, die in die nächste Version einfließen.

---

## Regel 5

**Mechanik begrenzt Software.**

Eine gute Software kann schlechte Mechanik nur begrenzt ausgleichen.

Deshalb wird mechanischer Qualität hohe Priorität eingeräumt.

---

## Regel 6

**Einfachheit gewinnt.**

Vor jeder neuen Funktion soll geprüft werden, ob das gleiche Ziel mit einer einfacheren Lösung erreicht werden kann.

Komplexität wird nur akzeptiert, wenn sie einen klaren technischen Nutzen bietet.

---

## Regel 7

**Langfristigkeit.**

CAMP ist kein Wochenendprojekt.

Die Plattform wird über viele Jahre hinweg wachsen.

Entscheidungen werden daher nicht ausschließlich für den aktuellen Entwicklungsstand getroffen, sondern sollen auch zukünftige Erweiterungen ermöglichen.

Jede neu entwickelte Baugruppe soll einen Beitrag zu einer langfristig wartbaren, modularen und technisch konsistenten Robotikplattform leisten.

Dieses Prinzip bildet den Kern der gesamten CAMP-Philosophie und dient als Orientierung für sämtliche zukünftigen Entwicklungsentscheidungen.

# 54. CAMP OS

## 54.1 Zielsetzung

CAMP OS ist das zentrale Betriebssystem der CAMP-Plattform.

Es bildet die Softwaregrundlage sämtlicher Endoskelette und verwaltet alle Hardware-, Software- und Charakterkomponenten.

Während das Endoskelett die physische Plattform darstellt, bildet CAMP OS deren digitales Gegenstück.

Sämtliche Funktionen – von der Servosteuerung über Kameraverarbeitung bis hin zur Künstlichen Intelligenz – werden durch CAMP OS koordiniert.

Dadurch entsteht eine klar definierte Trennung zwischen Hardware, Betriebssystem und Charakter.

---

## 54.2 Designphilosophie

CAMP OS verfolgt dieselben Grundprinzipien wie die restliche Plattform.

* Modularität
* Wartbarkeit
* Erweiterbarkeit
* Wiederverwendbarkeit
* Dokumentierte Schnittstellen

Das Betriebssystem besitzt keinerlei fest eingebauten Charakter.

Nach dem Systemstart existiert zunächst lediglich die technische Plattform.

Erst nach dem Laden eines Charakterpakets erhält der Animatronic seine Identität.

---

## 54.3 Verantwortlichkeiten

CAMP OS übernimmt unter anderem folgende Aufgaben.

* Hardwareverwaltung
* Servosteuerung
* Audioverwaltung
* Kameraverarbeitung
* Sensorverwaltung
* Netzwerk
* Bluetooth
* WLAN
* Telemetrie
* Diagnose
* Pluginverwaltung
* Charakterverwaltung
* Benutzerverwaltung
* Logging
* Fehlermanagement
* Updateverwaltung
* Sicherheitsfunktionen

Alle höheren Softwarekomponenten bauen auf diesen Diensten auf.

---

# 55. Charakterpakete

## 55.1 Grundidee

Innerhalb von CAMP wird jeder Charakter als eigenständiges Paket behandelt.

Ein Charakter besteht nicht aus einzelnen Dateien, sondern aus einem einzigen Container.

Die Dateiendung lautet:

`.campp`

(**Cosplay Animatronic Modular Platform Package**)

Dadurch kann ein vollständiger Charakter als eine einzige Datei archiviert, installiert, aktualisiert oder zwischen Entwicklungsständen verwaltet werden.

Dieses Konzept orientiert sich an etablierten Containerformaten wie Anwendungs- oder Projektdateien, ist jedoch vollständig auf die Anforderungen der CAMP-Plattform zugeschnitten.

---

## 55.2 Ziele

Ein Charakterpaket soll sämtliche charakterbezogenen Inhalte enthalten.

Beispiele:

* Konfiguration
* Persönlichkeitsparameter
* Bewegungsbibliothek
* Voice Lines
* Soundeffekte
* LED-Profile
* Animationen
* Charakterwissen
* HUD-Layouts
* Instrumentenprofile
* Symbole
* Metadaten

Das Betriebssystem benötigt dadurch lediglich eine einzige Datei, um einen vollständigen Charakter bereitzustellen.

---

## 55.3 Containerformat

Das Dateiformat `.campp` ist als Containerformat definiert.

Intern besteht es aus einer strukturierten Sammlung verschiedener Dateien.

Die konkrete Speicherstruktur bleibt vollständig unter Kontrolle der CAMP-Plattform.

Dadurch können zukünftige Versionen erweitert werden, ohne bestehende Charaktere grundsätzlich neu entwerfen zu müssen.

Ein Charakterpaket wird vom Betriebssystem als logische Einheit behandelt.

Die interne Ordnerstruktur ist für den Anwender nicht relevant.

---

## 55.4 Magic Number

Jede `.campp`-Datei beginnt mit einer eindeutigen Dateisignatur.

Magic Number:

**`camp_module67`**

Diese Kennung dient ausschließlich der eindeutigen Identifikation des Dateiformats.

Sie verhindert, dass Dateien versehentlich als andere bekannte Dateiformate interpretiert werden.

Beim Öffnen eines Pakets überprüft CAMP OS zunächst diese Signatur.

Nur Dateien mit gültiger Kennung werden akzeptiert.

---

## 55.5 Manifest

Jedes Charakterpaket enthält eine Manifestdatei.

Sie beschreibt den Inhalt des Pakets.

Typische Informationen sind beispielsweise:

* Charaktername
* Version
* Paket-ID
* Ersteller
* Erstellungsdatum
* CAMP OS-Version
* Kompatibilitätsinformationen
* benötigte Module
* unterstützte Instrumente
* unterstützte Suit-Typen
* Prüfsummen

Das Manifest bildet den Einstiegspunkt jedes Pakets.

Ohne gültiges Manifest kann ein Charakter nicht geladen werden.

---

## 55.6 Digitale Signaturen

CAMP unterstützt optional digitale Signaturen.

Sie dienen ausschließlich der Integritätsprüfung.

Dadurch kann festgestellt werden, ob ein Charakterpaket seit seiner Erstellung verändert wurde.

Die Signatur dient nicht der Lizenzierung oder dem Vertrieb.

Sie schützt ausschließlich die Konsistenz der Entwicklungsdaten.

---

# 56. Charakterverwaltung

Beim Systemstart durchsucht CAMP OS die verfügbaren Charakterpakete.

Jedes gültige Paket wird registriert.

Anschließend stehen sämtliche installierten Charaktere zur Auswahl.

Ein Charakterwechsel erfolgt ohne Änderungen am Betriebssystem.

Lediglich ein anderes Charakterpaket wird geladen.

Dadurch bleibt die Plattform vollständig unabhängig von einzelnen Figuren.

---

## 56.1 Lebenszyklus

Der Lebenszyklus eines Charakterpakets besteht aus mehreren Phasen.

Installation

↓

Validierung

↓

Registrierung

↓

Laden

↓

Aktivierung

↓

Betrieb

↓

Deaktivierung

↓

Entladen

↓

Archivierung

Jede Phase besitzt definierte Zustände und Fehlermeldungen.

---

## 56.2 Entwicklungsmodus

Während der Entwicklung kann ein Charakterpaket im Entwicklungsmodus geladen werden.

Änderungen an Konfigurationen, Animationen oder Audiodateien müssen dadurch nicht jedes Mal vollständig neu installiert werden.

Nach Abschluss der Entwicklung wird daraus ein finales `.campp`-Paket erzeugt.

Dadurch bleiben Entwicklungsdaten und veröffentlichungsreife Pakete klar voneinander getrennt.

---

# 57. Eigentum und Projektcharakter

CAMP ist als privates Langzeitprojekt konzipiert.

Ziel der Entwicklung ist der Aufbau einer persönlichen, über viele Jahre gepflegten Robotikplattform.

Eine kommerzielle Vermarktung der Hardware, Software oder Charakterpakete ist derzeit nicht vorgesehen.

Alle technischen Entscheidungen werden daher ausschließlich unter den Gesichtspunkten Wartbarkeit, Erweiterbarkeit, Zuverlässigkeit und persönlicher Nutzung getroffen.

Die Plattform ist nicht mit dem Ziel entstanden, ein Produkt zu werden.

Sie dient als persönliche Forschungs-, Entwicklungs- und Kreativplattform, auf der Robotik, Embedded Systems, Softwareentwicklung, Künstliche Intelligenz und Cosplay in einem gemeinsamen System zusammengeführt werden.

# 58. Dateisystemstruktur

## 58.1 Zielsetzung

CAMP OS verwendet eine klar definierte Verzeichnisstruktur.

Jeder Systembestandteil besitzt einen festen Speicherort.

Dadurch bleiben sowohl Entwicklung als auch Wartung langfristig übersichtlich.

Die Struktur orientiert sich an modernen Betriebssystemen und vermeidet unstrukturierte Ablageorte.

---

## 58.2 Systemverzeichnis

Das System selbst wird getrennt von Benutzerdaten gespeichert.

Beispiel:

`/system`

Enthält unter anderem:

* Systemdienste
* Standardbibliotheken
* Treiber
* Kernmodule
* Standardkonfigurationen

Dieses Verzeichnis wird ausschließlich durch CAMP OS verwaltet.

---

## 58.3 Charakterverzeichnis

Alle installierten Charakterpakete werden zentral verwaltet.

`/characters`

Beispiel:

* `Freddy.campp`
* `Bonnie.campp`
* `Roxanne.campp`
* `Chica.campp`

Die eigentlichen Container bleiben unverändert gespeichert.

Beim Laden wird das Paket lediglich eingelesen.

---

## 58.4 Datenverzeichnis

Laufende Daten werden getrennt gespeichert.

`/data`

Beispiele:

* Telemetrie
* Logdateien
* Kalibrierungen
* Benutzerprofile
* Aufnahmen
* Diagnosen

Diese Daten gehören nicht zum Charakterpaket.

---

## 58.5 Medien

Große Dateien werden separat organisiert.

`/media`

Beispiele:

* Videos
* Motion-Capture-Aufnahmen
* Fotos
* Entwicklungsaufnahmen
* Referenzmaterial

Dadurch bleibt das eigentliche Betriebssystem kompakt.

---

# 59. Plugin-System

## 59.1 Motivation

Nicht jede Funktion gehört zum Kern von CAMP OS.

Spezielle Erweiterungen werden als Plugins entwickelt.

Dadurch bleibt das Betriebssystem klein und wartbar.

Neue Funktionen können ergänzt werden, ohne den Systemkern zu verändern.

---

## 59.2 Plugin-Typen

Beispiele:

Audio-Plugins

---

Vision-Plugins

---

Sensor-Plugins

---

Instrumenten-Plugins

---

Diagnose-Plugins

---

HUD-Plugins

---

KI-Plugins

---

Netzwerk-Plugins

Jeder Typ besitzt definierte Schnittstellen.

---

## 59.3 Lebenszyklus

Ein Plugin durchläuft mehrere Zustände.

Installiert

↓

Registriert

↓

Initialisiert

↓

Aktiv

↓

Pausiert

↓

Beendet

↓

Entladen

Dadurch kann CAMP OS einzelne Plugins neu starten, ohne das gesamte System neu zu starten.

---

## 59.4 Abhängigkeiten

Plugins können andere Module benötigen.

Beispiele:

Ein Instrumenten-Plugin benötigt:

* Audio
* Motion
* Telemetrie

Sind erforderliche Module nicht vorhanden, wird das Plugin nicht gestartet.

Dadurch entstehen keine undefinierten Zustände.

---

# 60. Programmierschnittstellen (API)

## 60.1 Zielsetzung

Alle Module kommunizieren ausschließlich über dokumentierte Programmierschnittstellen.

Direkte Zugriffe auf interne Komponenten sollen vermieden werden.

Dadurch bleibt CAMP OS langfristig erweiterbar.

---

## 60.2 Hardware-API

Die Hardware-API stellt grundlegende Funktionen bereit.

Beispiele:

Servo bewegen.

LED setzen.

Temperatur lesen.

Kamera öffnen.

Lautsprecher verwenden.

Mikrofon starten.

Dadurch muss ein Plugin die zugrunde liegende Hardware nicht kennen.

---

## 60.3 Charakter-API

Die Charakter-API stellt Informationen über den aktuell geladenen Charakter bereit.

Beispiele:

Name

Persönlichkeit

Animationsbibliothek

Voice Lines

Instrument

Standardfarben

Emotionen

Jedes Modul erhält dadurch dieselbe Informationsquelle.

---

## 60.4 Ereignissystem

Viele Komponenten reagieren auf Ereignisse.

Beispiele:

Person erkannt.

↓

Charakter informiert.

---

Musik gestartet.

↓

Animation starten.

---

Akku niedrig.

↓

HUD aktualisieren.

---

Instrument verbunden.

↓

Charakterprofil erweitern.

Dieses Ereignissystem reduziert direkte Abhängigkeiten zwischen einzelnen Diensten.

---

# 61. Bootvorgang

## 61.1 Ziel

Der Start von CAMP OS erfolgt in einer klar definierten Reihenfolge.

Jeder Schritt baut auf dem vorherigen auf.

Fehler können dadurch eindeutig lokalisiert werden.

---

## 61.2 Startsequenz

Stufe 1

Hardwareinitialisierung

↓

Stufe 2

Systemkern

↓

Stufe 3

Treiber

↓

Stufe 4

Systemdienste

↓

Stufe 5

Pluginverwaltung

↓

Stufe 6

Hardwareprüfung

↓

Stufe 7

Charakterverwaltung

↓

Stufe 8

Laden eines `.campp`-Pakets

↓

Stufe 9

Kalibrierung

↓

Stufe 10

Bereit

Erst nach erfolgreichem Abschluss aller Stufen gilt das System als einsatzbereit.

---

## 61.3 Startdiagnose

Während des Bootvorgangs wird jede Komponente geprüft.

Beispiele:

✓ Kamera

✓ Lautsprecher

✓ Mikrofone

✓ Sensoren

✓ Akkus

✓ Speicher

✓ Servotreiber

✓ Controller

✓ Netzwerk

✓ Display

Alle Ergebnisse werden protokolliert.

---

## 61.4 Fehlerbehandlung

Schlägt eine Initialisierung fehl, entscheidet CAMP OS über das weitere Vorgehen.

Beispiele:

Nicht kritischer Fehler

↓

Dienst deaktivieren

↓

System startet weiter.

---

Kritischer Fehler

↓

Bootvorgang stoppen.

↓

Diagnose anzeigen.

Dadurch bleibt jederzeit nachvollziehbar, weshalb ein Start fehlgeschlagen ist.

---

# 62. Entwicklungswerkzeuge

## 62.1 Zielsetzung

Neben dem eigentlichen Betriebssystem entsteht eine Sammlung von Werkzeugen zur Entwicklung der Plattform.

Diese Werkzeuge bilden gemeinsam das CAMP Development Kit.

Sie dienen ausschließlich der Entwicklung und Wartung.

Sie sind kein Bestandteil des normalen Betriebs.

---

## 62.2 Bestandteile

Langfristig soll das Development Kit unter anderem folgende Werkzeuge enthalten:

* Character Editor
* Motion Editor
* Servo Calibration Tool
* Instrument Manager
* Telemetry Viewer
* Package Builder
* Firmware Manager
* Log Analyzer
* Vision Debugger
* AI Console

Jedes Werkzeug konzentriert sich auf einen klar abgegrenzten Aufgabenbereich.

---

## 62.3 Package Builder

Der Package Builder erstellt `.campp`-Dateien.

Er überprüft unter anderem:

* Magic Number
* Manifest
* Versionsnummer
* Paketstruktur
* Prüfsummen
* Signaturen
* Kompatibilität

Erst nach erfolgreicher Prüfung wird ein gültiges Charakterpaket erzeugt.

Dadurch wird sichergestellt, dass CAMP OS ausschließlich konsistente und vollständige Pakete lädt.

---

## 62.4 Langfristige Vision

Mit zunehmender Entwicklung soll CAMP nicht mehr aus einzelnen Programmen bestehen, sondern aus einem zusammenhängenden Entwicklungsökosystem.

Von der Konstruktion eines Endoskeletts über das Trainieren neuer Bewegungen bis hin zum Erstellen eines Charakterpakets sollen sämtliche Arbeitsschritte innerhalb derselben Plattform erfolgen.

Dadurch entsteht eine konsistente Entwicklungsumgebung, in der Mechanik, Elektronik, Software, Künstliche Intelligenz und Charakterdesign nicht als getrennte Disziplinen betrachtet werden, sondern als Bestandteile eines gemeinsamen Systems.

# 63. CAMP Software Development Kit (SDK)

## 63.1 Zielsetzung

Das CAMP SDK stellt sämtliche Werkzeuge, Bibliotheken und Dokumentationen bereit, welche zur Entwicklung neuer Komponenten innerhalb der CAMP-Plattform erforderlich sind.

Es bildet die offizielle Entwicklungsgrundlage sämtlicher Softwaremodule.

Das SDK dient ausschließlich der internen Entwicklung des Projekts und gewährleistet, dass neue Module denselben Qualitäts- und Schnittstellenstandards folgen wie der bestehende Systemkern.

---

## 63.2 Bestandteile

Das SDK umfasst unter anderem:

* API-Dokumentation
* Bibliotheken
* Beispieldateien
* Testprojekte
* Plugin-Vorlagen
* Build-Werkzeuge
* Debugging-Hilfen
* Simulationsschnittstellen

---

## 63.3 Ziel

Neue Software soll entwickelt werden können, ohne bestehende Kernkomponenten verändern zu müssen.

Dadurch bleibt CAMP OS langfristig stabil und erweiterbar.

---

# 64. CAMP CLI

## 64.1 Motivation

Für Entwicklungs-, Wartungs- und Automatisierungsaufgaben stellt CAMP ein Kommandozeilenwerkzeug bereit.

Die CAMP CLI ermöglicht den Zugriff auf nahezu alle Funktionen des Systems.

---

## 64.2 Beispielbefehle

````npm
camp build Freddy
camp install Freddy.campp
camp uninstall Freddy
camp telemetry
camp logs
camp diagnose
camp update
camp calibrate eyes
camp calibrate neck
camp package Bonnie
camp verify Freddy.campp
camp simulator
````

Diese Befehle dienen als standardisierte Schnittstelle zwischen Entwickler und Plattform.

---

## 64.3 Automatisierung

Die CLI ermöglicht außerdem die Erstellung automatisierter Entwicklungsabläufe.

Beispielsweise:

* automatisches Erstellen von Charakterpaketen
* Ausführen von Tests
* Firmware-Updates
* Datensicherungen
* Simulationen
* Export von Diagnosedaten

---

# 65. Character Editor

## 65.1 Zielsetzung

Der Character Editor dient der Erstellung und Verwaltung sämtlicher Charaktere.

Er ersetzt die direkte Bearbeitung von Konfigurationsdateien.

Alle Änderungen erfolgen über eine grafische Benutzeroberfläche.

---

## 65.2 Funktionen

Bearbeitung von:

* Persönlichkeit
* Voice Lines
* Wissensbasis
* Bewegungsbibliothek
* Instrumentenzuweisung
* Farbprofilen
* HUD-Konfiguration
* Animationen
* Metadaten

---

## 65.3 Live-Vorschau

Änderungen sollen unmittelbar getestet werden können.

Die Vorschau umfasst beispielsweise:

* Sprachausgabe
* Animationen
* Blickverhalten
* LED-Effekte
* Instrumentenzuweisungen

---

# 66. Motion Editor

## 66.1 Zweck

Der Motion Editor dient der Erstellung sämtlicher Bewegungsabläufe.

Animationen werden unabhängig von konkreten Servowinkeln entwickelt.

Stattdessen arbeitet der Editor mit einem abstrahierten Skelettmodell.

---

## 66.2 Funktionen

* Keyframes
* Interpolation
* Geschwindigkeitsprofile
* Schleifen
* Übergänge
* Spiegelung
* Import von Motion Capture
* Export in Charakterpakete

---

## 66.3 Testmodus

Jede Animation kann innerhalb einer Simulation überprüft werden.

Dabei werden unter anderem sichtbar:

* Gelenkwinkel
* Geschwindigkeit
* Kollisionen
* Schwerpunkt
* Bewegungsablauf

---

# 67. AI Studio

## 67.1 Ziel

Das AI Studio bildet die Entwicklungsumgebung sämtlicher KI-Komponenten.

Hier werden Charaktere nicht programmiert, sondern trainiert, konfiguriert und analysiert.

---

## 67.2 Aufgaben

* Prompt-Entwicklung
* Wissensverwaltung
* Trainingsdatensätze
* Verhaltensparameter
* Gesprächsanalysen
* Bewegungsanalyse
* Testszenarien

---

## 67.3 Simulation

Die KI kann vollständig innerhalb der Simulationsumgebung getestet werden.

Dadurch können neue Verhaltensweisen entwickelt werden, ohne den realen Animatronic zu verwenden.

---

# 68. Telemetry Studio

## 68.1 Zielsetzung

Das Telemetry Studio dient der Analyse sämtlicher Systemdaten.

Es richtet sich ausschließlich an Entwicklungs- und Wartungsarbeiten.

---

## 68.2 Funktionen

* Live-Diagramme
* Temperaturverläufe
* CPU-Auslastung
* RAM
* Akkuzustand
* Stromaufnahme
* Netzwerk
* Servoaktivität
* Kamerastatus
* Sensorstatus

---

## 68.3 Analyse

Vergangene Sitzungen können erneut geladen werden.

Dadurch lassen sich Fehler auch nach längerer Zeit nachvollziehen.

---

# 69. Firmware Manager

## 69.1 Motivation

Da CAMP zahlreiche Mikrocontroller verwendet, wird deren Verwaltung zentralisiert.

---

## 69.2 Funktionen

* Firmware installieren
* Versionen vergleichen
* Rollback
* Prüfsummen
* Geräteerkennung
* Updatehistorie

---

## 69.3 Kompatibilität

Vor jeder Installation überprüft der Firmware Manager:

* Controller-Typ
* Hardwareversion
* Firmwareversion
* Abhängigkeiten

Fehlerhafte Aktualisierungen sollen dadurch verhindert werden.

---

# 70. Digital Twin

## 70.1 Definition

Der Digital Twin stellt eine virtuelle Repräsentation eines realen CAMP-Systems dar.

Er besitzt dieselbe Mechanik, dieselben Gelenke und dieselben Softwarekomponenten wie das physische Endoskelett.

---

## 70.2 Ziel

Neue Funktionen sollen zunächst virtuell entwickelt werden.

Erst nach erfolgreicher Simulation erfolgt die Übertragung auf die reale Hardware.

---

## 70.3 Synchronisation

Langfristig kann der Digital Twin mit dem realen System gekoppelt werden.

Dadurch lassen sich reale Bewegungen und virtuelle Modelle miteinander vergleichen.

Abweichungen können automatisch erkannt werden.

---

# 71. Simulationsumgebung

## 71.1 Zielsetzung

Die Simulationsumgebung dient als vollständig virtuelle Entwicklungsplattform.

Hier können sämtliche Komponenten getestet werden.

Beispiele:

* Servobewegungen
* Kameraverarbeitung
* Charakterverhalten
* Instrumente
* Animationen
* Netzwerk
* Telemetrie

---

## 71.2 Vorteile

Simulation reduziert:

* Entwicklungszeit
* Materialverschleiß
* Fehlersuche
* Risiken

Neue Ideen können schneller überprüft werden als auf realer Hardware.

---

# 72. Entwicklungsrichtlinien

Für sämtliche Entwicklungsbereiche gelten verbindliche Standards.

Hierzu gehören unter anderem:

* Benennungskonventionen
* Dokumentationspflicht
* Versionsverwaltung
* Codequalität
* CAD-Richtlinien
* Testverfahren
* Sicherheitsbewertungen

Diese Standards sorgen dafür, dass CAMP trotz seiner Größe langfristig konsistent bleibt.

---

# 73. Projektmanagement

## 73.1 Langzeitprojekt

CAMP wird als mehrjähriges Entwicklungsprojekt betrachtet.

Neue Funktionen werden in kleinen, abgeschlossenen Entwicklungsabschnitten umgesetzt.

---

## 73.2 Entwicklungsphasen

Jede Funktion durchläuft mehrere Schritte.

Idee

↓

Recherche

↓

Konzept

↓

CAD

↓

Prototyp

↓

Test

↓

Überarbeitung

↓

Dokumentation

↓

Integration

↓

Freigabe

---

## 73.3 Priorisierung

Neue Funktionen werden nach folgenden Kriterien bewertet:

* Sicherheitsrelevanz
* Nutzen
* Komplexität
* Abhängigkeiten
* Wartbarkeit

Dadurch entstehen nachvollziehbare Entwicklungsprioritäten.

---

# 74. Langfristige Roadmap

Die CAMP-Plattform wird schrittweise erweitert.

Eine mögliche Entwicklungsabfolge lautet:

Version 0.x

Grundlagen

Mechanik

Elektronik

Erste Software

↓

Version 1.x

Erstes vollständiges Endoskelett

↓

Version 2.x

Erster vollständiger Suit

↓

Version 3.x

Autonomer Betrieb

↓

Version 4.x

Mehrere Charaktere

↓

Version 5.x

Funktionierende Instrumente

↓

Version 6.x

Fortgeschrittene KI

↓

Version 7.x

Mehrere Animatronics gleichzeitig

↓

Version 8.x

Vollständiges CAMP-Ökosystem

Diese Roadmap stellt keinen festen Zeitplan dar.

Sie beschreibt vielmehr die langfristige Entwicklungsrichtung der Plattform.

---

# 75. Zukunftsperspektive

CAMP verfolgt nicht das Ziel, einen einzelnen Animatronic zu bauen.

Langfristig soll eine technische Plattform entstehen, welche über viele Jahre hinweg erweitert und verfeinert werden kann.

Mit jeder neuen Konstruktion, jeder verbesserten Softwareversion und jedem zusätzlichen Charakter wächst nicht nur die Anzahl der Funktionen, sondern auch die Reife der gesamten Plattform.

Der eigentliche Wert von CAMP liegt daher nicht in einem einzelnen Endoskelett oder einem einzelnen Suit, sondern in der Summe aller entwickelten Technologien, Erfahrungen und Dokumentationen.

Das Projekt verbindet Robotik, Embedded Systems, Softwareentwicklung, künstliche Intelligenz, Maschinenbau, additive Fertigung, Elektronik, Charakterdesign und Cosplay zu einem gemeinsamen Gesamtsystem.

Es versteht sich als persönliche technische Plattform, deren Architektur bewusst auf Langfristigkeit ausgelegt ist.

Auch wenn einzelne Komponenten im Laufe der Jahre ersetzt oder vollständig neu entwickelt werden, bleibt die grundlegende Philosophie unverändert:

* Ein modulares Endoskelett.
* Modulare Suits.
* Ein gemeinsames Betriebssystem.
* Installierbare Charaktere.
* Eine einheitliche Entwicklungsumgebung.
* Eine konsistente Dokumentation.

Und eine Plattform, die mit jedem Entwicklungsschritt leistungsfähiger wird, ohne ihre ursprünglichen Designprinzipien zu verlieren.

Mit diesem Dokument endet nicht die Planung von CAMP.

Es bildet vielmehr den Ausgangspunkt für die praktische Umsetzung einer langfristigen Robotikplattform, deren Entwicklung über viele Jahre hinweg fortgeführt werden soll.

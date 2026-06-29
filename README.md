# CAMP

## Cosplay Animatronic Module Platform

### Engineering Design Document

**Dokumentversion:** 0.3

**Status:** In Entwicklung

**Projektbeginn:** Langfristiges Eigenprojekt

**Autor:** @dmdelia

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

Die Mechanik bildet das Fundament der gesamten CAMP-Plattform. Jede spätere Funktion – unabhängig davon, ob sie durch Software, Elektronik oder KI gesteuert wird – ist letztendlich durch die mechanischen Möglichkeiten begrenzt.

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

# Teil IV – Künstliche Intelligenz und Robotik

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

# Teil VII – Benutzererlebnis und Mensch-Maschine-Interaktion

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

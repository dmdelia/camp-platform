# CAMP

## Cosplay Animatronic Module Platform

### Engineering Design Document

**Dokumentversion:** 0.1

**Status:** In Entwicklung

**Projektbeginn:** Langfristiges Eigenprojekt

**Autor:** dmdelia

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

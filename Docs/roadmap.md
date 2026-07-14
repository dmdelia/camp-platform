# Phase 0 – Fundament legen
**Ziel:** Alle grundlegenden Architekturentscheidungen treffen, bevor Zeit und Geld in Hardware fließen.

### 0.1 Projekt-Roadmap

* Vision → Meilensteine → Aufgaben herunterbrechen
* Ersten "Happy Path" definieren
* Quartalsziele statt Monatsziele
* Backlog für spätere Ideen anlegen

---

### 0.2 Systemarchitektur einfrieren (v1)

Entscheidungen, die möglichst früh getroffen werden:

* Servo-Standard
* Schraubenstandard (M2/M2.5/M3 ...)
* Steckverbinder
* Kabeltypen
* Spannungsversorgung
* Kommunikationsbus
* Hauptrechner
* Mikrocontroller
* Docking-Schnittstelle
* Batteriekonzept

Das sind Dinge, die später teuer werden, wenn man sie ständig ändert.

---

### 0.3 Entwicklungsumgebung

* CAD auswählen
* Git-Repositories erstellen
* Dokumentationsstruktur
* Dateibenennung
* Versionierung
* Backup-Strategie

---

### 0.4 Standards definieren

Zum Beispiel:

* Dateinamen
* Ordnerstruktur
* CAD-Regeln
* Druckprofile
* Materialnamen
* Farben
* Kabelkennzeichnung
* Fehlercodes
* Commit-Konventionen

Je früher, desto besser.

---

### 0.5 Happy Path definieren

Das ist wahrscheinlich der wichtigste Punkt.

Nicht:

> "Ich baue Freddy."

Sondern:

> "Was ist das **kleinstmögliche vollständige CAMP-System?**"

Zum Beispiel:

* Kopf-Endo
* 2 bewegliche Augen
* 1 Halsgelenk
* Lautsprecher
* Kamera
* einfacher Suit
* Docking
* Bluetooth-Debug-App

Wenn **das** funktioniert, existiert CAMP erstmals als Plattform.

---

### 0.6 Anforderungen (Requirements)

Nicht CAD.

Nicht Code.

Nur Anforderungen.

Beispielsweise:

> Der Suit muss in unter 30 Sekunden auf das Endoskelett montiert werden.

> Das Endoskelett muss alleine stehen können.

> Das Kopfmodul muss ohne Zerlegen wartbar sein.

> Das Kamerabild muss unter 100 ms Latenz besitzen.

Solche Anforderungen helfen später bei Entscheidungen.

---

### 0.7 Forschung

Jetzt beginnt das eigentliche Engineering.

Nicht kaufen.

Erst recherchieren.

Zum Beispiel:

* Servos vergleichen
* Getriebearten
* Kugellager
* Materialien
* Akkus
* Displays
* Kameras
* Mikrofone
* IMUs
* Mikrocontroller
* SBCs

Dabei entsteht automatisch eine erste BOM (Bill of Materials).

---

## Was ich als Phase 0 **nicht** machen würde

* KI entwickeln
* Firmware schreiben
* PCB designen
* CAD bis ins Detail modellieren
* Komponenten bestellen "zum Ausprobieren"

Diese Dinge sollten aus den Entscheidungen der Phase 0 folgen, nicht umgekehrt.

---

### Phase 0.5 – Proof of Architecture

Noch bevor erstem echten Animatronic einen extrem einfachen Architekturtest machen:

* Ein ESP32
* Ein Servo
* Ein Lautsprecher
* Eine LED
* Ein Taster
* Eine kleine Debug-Oberfläche

Nicht als Roboter, sondern als **Technologieträger**.

Damit wird getestet:

* Kommunikationskonzept
* Softwarearchitektur
* Telemetrie
* Updates
* Logging
* Modulstruktur


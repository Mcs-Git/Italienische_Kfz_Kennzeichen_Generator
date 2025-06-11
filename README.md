# Dokumentation: Italienischer KFZ-Kennzeichen-Generator

## 0. Anzahl an Kfz-Kennzeichen in Italien

### **Italien (I)**
**System:**

- **Aktuelles Format** (seit 1994): **AA 000 AA**
- **Zwei Buchstaben**, **drei Ziffern** und **zwei Buchstaben**

- **Keine Ortskennung** mehr im Kennzeichen.

- Buchstaben wie **I**, **O**, **Q**, **U** nicht verwendet (Verwechslungsgefahr).

**Mögliche Kombinationen**:

- **Buchstaben**: **22** (lateinische Buchstaben **ohne I, O, Q, U**).

- **Ziffern**: von **000** bis **999** (**1000 Ziffern**).

- **Kombinationen**: 22² × 1000 × 22² =  **234,256,000 mögliche Kennzeichen**.


## I. Ziel des Projekts

Ziel dieses Projekts ist die Entwicklung eines konsolenbasierten Python-Programms zur:

- Generierung **aller möglichen italienischen KFZ-Kennzeichen** (Format: **2 Buchstaben + 3 Ziffern + 2 Buchstaben**).

- Berechnung des **SHA-256-Hashwerts** jedes Kennzeichens.

- Speicherung aller generierten Kennzeichen mit zugehörigem Hash in einer **Textdatei**.

- Suche nach bestimmten Hashwerten in dieser Datenbank.

- Benutzerfreundlichen Anzeige aller gespeicherten Kennzeichen über ein Menü.

## II. Anforderungen

### Funktionale Anforderungen

**Generierung**: Vollständige Generierung aller Kennzeichenkombinationen (basierend auf den erlaubten Buchstaben und dreistelligen Ziffern).

**Hashing**: Berechnung des **SHA-256-Hashes** für jede Kombination.

**Speicherung**: Ausgabe aller Kennzeichen mit zugehörigem Hash in eine **Textdatei**.

**Suche**: Vergleich gespeicherter Hashes mit einer **Ziel-Hashliste**.

**Anzeige**: Konsolenausgabe aller Kennzeichen aus der Datei.

### Nicht-funktionale Anforderungen

**Performance**: Möglichst effiziente Kombinationserzeugung und Dateispeicherung.

**Benutzerfreundlichkeit**: Klar strukturiertes, textbasiertes Menü mit Wiederaufrufbarkeit.

**Fehlertoleranz**: Fehlerbehandlung für fehlende Dateien und ungültige Formate.

## III. Funktionsübersicht

**buchstaben_kombination()**: Erzeugt alle erlaubten 2-Buchstaben-Kombinationen.

**ziffern_kombination()**: Erzeugt alle 3-stelligen Ziffern als String.

**kennzeichen_generierung(arr1, arr2)**: Kombiniert Buchstaben und Ziffern zu gültigen Kennzeichen und erstellt deren SHA-256-Hashwerte.

**kennzeichen_speicherung(kennzeichen_dict)**: Speichert das Ergebnis von der kennzeichen_generierung-Funktion als ein **Dictionary** in eine Textdatei.

**generator()**: Führt den Generierungsprozess aus , misst die Laufzeit und speichert das Ergebnis.

**kennzeichen_datei()**: Gibt alle gespeicherten Kennzeichen aus.

**suche()**: Sucht Ziel-Hashwerte in gespeicherter Textdatei.

**menu()**: Konsolenmenü zur Benutzerinteraktion.

## IV. Benutzerperspektive

### Zielgruppe

IT-interessierte Anwender oder Studierende mit Interesse an **Hashfunktionen**, **Brute-Force-Analyse** oder **Datenkombinationen**.

### Interaktionen

Der Benutzer navigiert über ein numerisches Konsolenmenü.

Aktionen umfassen:

- **Anzeige aller Kennzeichen**

- **Neugenerierung**

- **Hash-Suche**

- **Programm beenden**

## V. Entwicklungsverlauf

1. Definition des **Kennzeichenformats** und Einschränkung der verwendbaren Buchstaben.

2. Implementierung von Kombinationsfunktionen für **Buchstaben** und **Zahlen**.

3. **SHA-256** Hashfunktion über **hashlib** integriert.

4. Optimierte Dateiausgabe mit **kennzeichen_datei()**.

5. Suchfunktion zur Prüfung, ob **bestimmte Hashes** vorkommen.

6. Konsolenmenü mit **rekursiver Aufrufstruktur** für wiederholte Bedienung.

7. Testlauf für **Speicherzeit** und **Genauigkeit**.

## VI. Benutzerhandbuch

### Start

Programmstart erfolgt über python **IT-KFZ_Kennzeichen.py**

### Menüpunkte

Ausgabe:


![](https://codi.ide3.de/uploads/e1a2ff05-f8c9-4d2e-b18f-1e040e14b2f5.png)


#### **Alle KFZ-Kennzeichen anzeigen:** 
Gibt alle gespeicherten Kennzeichen in der Textdatei aus.

Ausgabe:

![](https://codi.ide3.de/uploads/7d3b5082-6248-4504-8327-6b14f4b34c56.png)


#### **KFZ-Kennzeichen generieren:**
- Generiert alle möglichen Kombinationen (mit deren SHA-256-Hashwerte) und speichert sie.
- Zeigt Startzeit, Endzeit und Laufzeit.

Ausagbe:

![](https://codi.ide3.de/uploads/b9ad61d9-ff05-424d-82cd-21edcfa66a9c.png)


#### **Nach Hashwerten suchen (SHA-256):**
Vergleicht gespeicherte Hashwerte mit einer Ziel-Hashliste.

Ausagbe:

![](https://codi.ide3.de/uploads/a94465aa-97bd-44ef-b635-ff9ff9be4f6b.png)


#### **Beenden:**
Beendet das Programm.

Ausagbe:

![](https://codi.ide3.de/uploads/d89024ea-c41a-49aa-94af-1be7ef55da05.png)

### \*Hinweise

- Die Datenbank wird als **kfz_kennzeichen_db.txt** gespeichert.

- Bei fehlender Datei wird eine **Fehlermeldung** angezeigt.

## VII. Technische Dokumentation

### **Architektur**

- **Konsolenbasiertes Python-Skript** *ohne GUI*.

- Lineare, menügesteuerte Benutzerinteraktion.

### **Datenstrukturen**

Kennzeichen-Datenbank (**kfz_kennzeichen_db.txt**):
[](https://)[](https://)
Format: **ABC123DE: HASHWERT**

**Ziel-Hashliste** im Code als **such_liste** definiert.

### **Algorithmen und Bibliotheken**

**Hashing**: **SHA-256** über **hashlib.sha256()**.

**Zeitmessung**: **time.perf_counter()**  zur Laufzeitberechnung.

**Dateioperationen**: Lesen/Schreiben per **with open()**.

**Datum/Zeit**: Formatierung via **datetime.now()**.

### **Bibliotheken**

**hashlib** für **SHA-256 Hashes**

**time** für **Performance-Messung**

**datetime** für **Start-/Endzeit-Ausgabe**

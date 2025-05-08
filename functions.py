from hashlib import  sha256 # Importiert SHA-256 Hashfunktion aus hashlib
import  time # Für Zeitmessung
from datetime import datetime # Für aktuelle Uhrzeit/Datum

# Italienisches KFZ-kennzeichnungsformat : 2 Buchstaben 3 Ziffern 2 Buchstaben

# -----------------------------
# KONSTANTEN UND VORGABEN
# -----------------------------

# Gültige Buchstaben für italienische Kfz-Kennzeichen (22 von 26, I, O, Q, U ausgeschlossen)
erlaubte_buchstaben = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
anzahl_ziffern = 1000 # Zahlen von 000 bis 999

#Ziel-Hashwerte, nach denen später gesucht wird (SHA-256 Werte)
such_liste = ["c7fbd00442a86fc08866daa438ec2a546e006c26d11d1750516f04ea9bc36586",
              "f1eb03bef14a79da6fb8561413f02cf5dec836bdeb3f1faf35c2a1c39581a5c1",
              "abd12f05e5626012b5b5d70a77f2fc3d786ee2dafc17e11741b99ad31fc7eb79",
              ]

# -----------------------------
# HILFSFUNKTIONEN
# -----------------------------

# Generiert alle Kombinationen aus 2 Buchstaben (z.B: AA, AB, ..., ZZ)
def buchstaben_kombination():
    arr = erlaubte_buchstaben
    buchstaben_auswahl = [x+y for x in arr for y in arr]
    return  buchstaben_auswahl

# Generiert alle dreistelligen Ziffernkombinationen als Strings ("000" bis "999")
def ziffern_kombination():
    ziffern_auswahl = [f"{i:03}" for i in range(anzahl_ziffern)]
    return  ziffern_auswahl

# Erzeugt alle möglichen Kombinationen im Format: 2 Buchstaben + 3 Ziffern + 2 Buchstaben
# Berechnet den SHA-256-Hash jedes Kennzeichens
def kennzeichen_generierung(arr1,arr2):
    alle_kennzeichen = {}
    for vorne in arr1:
        for nummer in arr2:
            for hinten in arr1:
                kennzeichen = vorne + nummer + hinten
                kennzeichen_hash = sha256(kennzeichen.encode('utf-8')).hexdigest()
                alle_kennzeichen[kennzeichen] = kennzeichen_hash
    return  alle_kennzeichen



# Führt den Generierungsprozess aus, misst die Laufzeit und speichert die Ergebnisse
def generator():
    buchstaben_liste = buchstaben_kombination()
    ziffern_liste = ziffern_kombination()
    start = time.perf_counter() # Zeitmessung Start
    ergebnis = kennzeichen_generierung(buchstaben_liste, ziffern_liste)
    kennzeichen_speicherung(ergebnis)
    end = time.perf_counter() # Zeitmessung Ende
    dauer = end - start
    return  dauer

# Speichert das Dictionary mit den Kennzeichen und Hashes in einer Datei
def kennzeichen_speicherung(kennzeichen_dict):
    with open("kfz_kennzeichen_db.txt", "w") as f:
        for key,value in kennzeichen_dict.items():
            f.write(f"{key}: {value}\n") # Format: ABC123DE: HASH

# Liest die gespeicherten Kennzeichen-Datei und gibt nur die Kennzeichen aus
def kennzeichen_datei():
    try:
        with open("kfz_kennzeichen_db.txt", "r") as f:
            for line in f:
                key, _ = line.strip().split(": ", 1) # Nur den Kennzeichen-Teil anzeige
                print(key)
    except FileNotFoundError:
        print("Keine Kfz-Kennzeichen-Datei vorhanden.")
    except:
        print("Ungültiger Eintrag in der Kfz-Kennzeichen-Datei.")

# Sucht nach den Ziel-Hashwerten in der gespeicherten Kennzeichen-Datenbank
def suche():
    print("Suche nach: ")
    for hash_value in such_liste:
        print(hash_value)

    print("\nEinen Moment bitte ...")
    try:
        gefunden = False
        treffer = 0
        print("Suchergebnis:")
        with open("kfz_kennzeichen_db.txt", "r") as f:
            kennzeichen_dict = {}
            for line in f:
                key, value = line.strip().split(": ", 1)
                kennzeichen_dict[key] = value
            for ziel_hash in such_liste:
                for key,value in kennzeichen_dict.items():
                    if ziel_hash == value:
                        print(f"{ziel_hash} - {key}")
                        gefunden = True
                        treffer +=1
                        break
        if not gefunden:
            print("Keinen Treffer.")
        print(f"{treffer} von {len(such_liste)} gefunden.")
    except FileNotFoundError:
        print("Keine Kfz-Kennzeichen-Datei vorhanden.")
    except:
        print("Ungültiger Eintrag in der Kfz-Kennzeichen-Datei.")



# -----------------------------
# MENÜSYSTEM
# -----------------------------

# Textbasiertes Konsolenmenü für den Benutzer
def menu():
    print("############### Italienisches KFZ-Kennzeichen-Generator ###############")
    print("1. Alle KFZ-Kennzeichen anzeigen.")
    print("2. KFZ-Kennzeichen generieren.")
    print("3. Nach Hashwerten suchen(SHA-256).")
    print("Q. Beenden")

    auswahl = input("Wählen Sie eine Option: ")
    print("\n--------------------------------------------------------------------------\n")

    match auswahl.upper():
        case "1":
            print("********** Alle KFZ-Kennzeichen **********")
            kennzeichen_datei()
            print("\n--------------------------------------------------------------------------\n")
            time.sleep(2)
            menu()
        case "2":
            print("********** KFZ-Kennzeichen Generierung **********")
            print(f"Start: {datetime.now().strftime('%H:%M:%S')}")
            print("Generierung ...")
            dauer = generator()
            print("Prozess erfolgreich beendet.")
            print(f"Ende: {datetime.now().strftime('%H:%M:%S')}")
            print(f"Benötigte Dauer für den Prozess: {dauer:.4f} seconds.")
            print("\n--------------------------------------------------------------------------\n")
            time.sleep(2)
            menu()
        case "3":
            print("********** Suche **********")
            suche()
            print("\n--------------------------------------------------------------------------\n")
            time.sleep(2)
            menu()
        case "Q":
            print("Arrivederci / Auf Wiedersehen. ;)")
            print("\n--------------------------------------------------------------------------\n")
        case _:
            print("Bitte treffen Sie eine gültige Auswahl.")
            print("\n--------------------------------------------------------------------------\n")
            time.sleep(2)
            menu()







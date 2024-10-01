## Lass uns loslegen - Circuitpython (und mehr) installieren

> [!NOTE]
> 
> Je nach Modell gibt es verschiedene Varianten Circuitpython zu installieren. Hier wird versucht die meisten Möglichkeiten abzudecken. Bei Problemen, die durch diese Seite nicht gelöst werden können, würden wir uns sehr über eine Nachricht oder Fehlermeldung freuen, damit wir auch diesen Fall abdecken können, um das Problem auch für andere Bastler in Zukunft zu lösen.

### Was Du brauchst:

Deinen **Mikrocontroller** und ein passendes **USB-Kabel**, einen Computer mit **Windows, Linux oder MacOS** und die **passende Circuitpython-Software**, die Du [hier runterladen](https://circuitpython.org/downloads?q=esp32) kannst.

> [!IMPORTANT]
> 
> Nicht jedes USB-Kabel ist geeignet. Es gibt welche, die intern ausschliesslich zum Laden verdrahtet und geeignet sind (d.h. nur Strom übertragen, aber keine Daten). Gehe sicher, dass Dein Kabel eines ist das auch Daten übertragen kann. Wenn Du nicht sicher bist, probiere zum Beispiel Dein Handy mit dem Computer zu verbinden und dann siehst Du, ob es vom Computer erkannt wird.

### Thonny hilft Dir!

Als nächstes solltest Du [**Thonny** runterladen und installieren](https://thonny.org). **Thonny** gibt es für Windows, MacOS und Linux und ist hervorragend geeignet für Einstieger und bietet auch für erfahrene Programmierer ein paar nützliche Features.

Du kannst Circuitpython-Code mit jedem Programm schreiben das einfache Textdateien abspeichern kann. In der Praxis allerdings, ist eine **Entwicklungsumgebung** (Oft auch **IDE** gennant, das steht für **Integrated Development Environment**) gleich auf mehreren Ebenen nützlich:

- **Automatische Vervollständigung** von Code und Vorschläge bei der Eingabe

- **Debugging** - Also (unschätzbare) Hilfen, die es Dir ermöglichen Fehler leichter zu finden und auszumerzen

- Die **Console** - Für viele das wohl **wichtigste Werkzeug** bei der Programmierung von... naja.. fast Allem. Das gilt gleich doppelt für das Programmieren von Hardware, wie z.B. Mikrocontrollern

- **Dateiverwaltung** und **Starten/Stoppen** von Programmen auf Knopfdruck

- > [!TIP]
  > 
  > **<u>Thonny bietet Dir darüber hinaus die Möglichkeit, Circuitpython auf einige Mikrocontroller automatisch zu installieren</u>** inklusive Download und dergleichen!
  > 
  > Wie das geht kannst Du hier nochmal im Einzelnen nachlesen (TODO: Link hinzufügen mit bebilderter Installationsanleitung von MCUs mit Thonny)

### Der Boot-Modus

Jede Installation von hardwarenaher Firmware, Arduino-Sketches und eben Circuitpython benötigt einen speziellen Modus in den Du den Mikrocontroller versetzen musst, bevor Du eben jene Installation vornehmen kannst. Je nach Familie und Modell gibt es verschiedene Wege in diesen Modus zu bekommen (der oft Boot- oder DFU-Modus genannt wird). Zu Deinem MCU (so nennen wir den Mikrocontroller in Zukunft) gibt es eine Anleitung wie das gemacht wird und auch auf der Download-Seite steht es im Detail, nur halt auf Englisch

> [!INFO]
> 
> Es gibt verschiedene Controller und Modi, die so eingerichtet sind, dass das nicht nötig ist. Wir gehen hier aber den sicheren Weg. Sollte Circuitpython bereits installiert sein, kannst Du diese Schritte auslassen oder lieber doch machen, um die aktuellste Version zu installieren. 

#### Ein paar Beispiele/Normalerweise

###### ESP32 - Modelle (z.B. ESP32C2, ESP32C3, ESP32S3, ESP32C6)

> [!TIP]
> 
> Solltest Du **[Thonny](http://thonny.org)** benutzen, was wir DRINGEND empfehlen, kannst Du auch[ hier lesen wie Dir Thonny bei der Installation hilft](thonny_instcp.md). Es kann jedoch nicht schaden, zu lernen wie Du Circuitpython auch ohne **[Thonny](http://thonny.org)** installierst. Es funktioniert auch nur mit einer begrenzten Zahl von Controllern
> 
> [Installation von Circuitpython mit Thonny](thonny_instcp.md)

1. Schliesse den Mikrocontroller mit dem USB-Kabel am Computer an

2. Meistens haben die ESP32 (mind.) 2 Knöpfe: "BOOT" oder "0" und "RESET" oder "RST". Halte den BOOT (oder 0) Knopf gedrückt und drücke zusätzlich den RESET (oder RST) Knopf. 

3. Wenn Dein MCU einen UF2-Bootloader hat, sollte Dein Computer kurz darauf ein neues Laufwerk finden, ganz so wie wenn Du einen USB-Stick einsteckst. 

4. Ziehe nun die UF2-Datei (die Datei vom Download oben) einfach auf das Laufwerk was erschienen ist. 

5. Warte einen Moment! Nein.. ernsthaft.. Warte! Je nach Gerät kann es ein paar Momente dauern, aber wenn Du es unterbrichst kann es schwierig werden. 

6. Sollte alles geklappt haben verschwindet das Laufwerk nach einigen Momenten und taucht dann wieder mit Namen "CIRCUITPY" auf. 

7. Das war es schon. Öffne das Laufwerk und gucke Dir die Dateien und Ordner an. Aktuell müsstest Du 2 Ordner sehen *lib* und *sd*, sowie mindestens 1 Datei mit Namen *code.py* oder *main.py*. Je nach Version kann das auch ein wenig variieren. 

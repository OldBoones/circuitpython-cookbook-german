## Lass uns loslegen - Circuitpython (und mehr) installieren

### Was Du brauchst:

Deinen **Mikrocontroller** und ein passendes **USB-Kabel**, einen Computer mit **Windows, Linux oder MacOS** und die **passende Circuitpython-Software**

>[!INFO]
> 
> Nicht jedes USB-Kabel ist geeignet. Es gibt welche, die intern nur so verdrahtet sind, dass sie ausschliesslich zum Laden geeignet sind (d.h. nur Strom übertragen). Gehe sicher, dass Dein Kabel eines ist das auch Daten übertragen kann. Wenn Du nicht sicher bist, probiere zum Beispiel Dein Handy mit dem Computer zu verbinden und dann siehst Du, ob es vom Computer erkannt wird.

> [!NOTE]
> 
> Je nach Modell gibt es verschiedene Varianten Circuitpython zu installieren. Hier wird versucht die meisten Möglichkeiten abzudecken. Bei Problemen, die durch diese Seite nicht gelöst werden können, würden wir uns sehr über eine Nachricht oder Fehlermeldung freuen, damit wir auch diesen Fall abdecken können, um das Problem auch für andere Bastler in Zukunft zu lösen.



### Der Boot-Modus

Jede Installation von hardwarenaher Firmware, Arduino-Sketches und eben Circuitpython benötigt einen speziellen Modus in den Du den Mikrocontroller versetzen musst, bevor Du eben jene Installation vornehmen kannst. Je nach Familie und Modell gibt es verschiedene Wege in diesen Modus zu bekommen (der oft Boot- oder DFU-Modus genannt wird). Zu Deinem MCU (so nennen wir den Mikrocontroller in Zukunft) gibt es eine Anleitung wie das gemacht wird und auch auf der Download-Seite steht es im Detail, nur halt auf Englisch

> [!INFO]
> 
> Es gibt verschiedene Controller und Modi, die so eingerichtet sind, dass das nicht nötig ist. Wir gehen hier aber den sicheren Weg. Sollte Circuitpython bereits installiert sein, kannst Du diese Schritte auslassen oder lieber doch machen, um die aktuellste Version zu installieren. 

#### Ein paar Beispiele/Normalerweise

###### ESP32 - Modelle (ESP32C2, ESP32C3, ESP32S3, ESP32C6)

1. Schliesse den MCU mit dem USB-Kabel am Computer an

2. Meistens haben die ESP32 2 Knöpfe: "BOOT" oder "0" und "RESET" oder "RST"



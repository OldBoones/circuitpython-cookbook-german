#### Was ist eigentlich [Circuitpython](http://circuitpython.org)?

CircuitPython ist eine einfache Programmiersprache, die speziell für Mikrocontroller entwickelt wurde, also Geräte wie Sensoren, Roboter oder Heizungs- und Lichtsysteme steuern können. 

Das Tolle daran: Du programmierst damit in **Python**, einer der weltweit beliebtesten und am leichtesten zu lernenden Programmiersprachen. CircuitPython ist ideal für Anfänger, weil man ohne grosse Einstiegshürde oder komplizierte *Toolchains*, *Installationen* oder *Treiberabhängigkeiten* loslegen kann – einfach den Mikrocontroller per USB anschließen, Code in einer Textdatei schreiben und das Gerät führt den Code sofort aus! (Hierzu später mehr)

Ein grosser Vorteil von CircuitPython ist, dass du **nichts installieren** musst (abgesehen von Circuitpyhton selbst), keine komplizierten Umgebungen oder Abhängigkeiten. Dein Mikrocontroller verhält sich wie ein USB-Stick – du ziehst deinen Code einfach per Drag-and-Drop auf das Gerät. Ein weiterer Clou: Es gibt eine riesige Auswahl an vorgefertigten **Bibliotheken**, sowohl vom Hersteller selbst als auch einer sehr aktiven Community, die dir Aufgaben wie die Steuerung von Sensoren oder das Anzeigen von Informationen auf Bildschirmen enorm erleichtern.
[!INFO]Es gibt durchaus Bibliotheken und Abhängigkeiten, die wichtigsten sind nur schon in Circuitpython integriert. Weitere kannst Du ebenso leicht, einfach auf das Gerät kopieren. In späteren Teilen zeigen wir, wie Du Bibliotheken erstellen oder Deine eigene Version von Circuitpython mit eingebauten Bibliotheken erstellen kannst

Die Sprache gibt es seit **2017** und wurde von **[Adafruit](http://circuitpython.org)**, einem führenden Hersteller im Bereich Open-Source-Elektronik, ins Leben gerufen. Seitdem hat sich eine riesige, freundliche und sehr aktive **Community** entwickelt, die immer wieder neue Projekte und Ideen teilt. Die Entwickler bei Adafruit bringen auch ständig Updates heraus und sorgen dafür, dass die Sprache auf immer mehr Geräten läuft.

Egal, ob du kompletter Anfänger(m/w/d) bist oder schon Erfahrung mit Programmierung hast – CircuitPython macht einfach Spaß! Mit seinem einfachen, Python-basierten Ansatz und der breiten Unterstützung ist es der perfekte Einstieg in die Welt der Mikrocontroller und das Tüfteln mit Elektronik!

###### (Als Einsteiger kannst Du hier aufhören zu lesen (wenn Du möchtest) und musst nicht unbedingt alles verstehen was hier steht, das kommt noch)

#### Auch als Profi erleichtert Dir Circuitpython die Arbeit.

Durch universelle Schnittstellen und schnelle Updates ist das (rapid-)Prototyping deutlich einfacher. Kein langes Warten auf den Compiler und keine Notwendigkeit ständig in den DFU-Modus zu wechseln. Durch die REPL-Console lassen sich Befehle direkt auf ihre Auswirkung testen und das Debuggen ist vereinfacht. Ausserdem lässt sich der Code mit jedem Editor anpassen und auf vielfältige Weise übertragen, wodurch man auch mit Handy, Tablett und nahezu jedem anderen System, den Code anpassen kann.  Wer sich auskennt kann die circuitpython Firmware direkt anpassen und eine neue Version kompilieren, die dann nur die benötigten Komponenten enthält oder Funktionen, die man nur hardwarenah erreicht. (Ich binde z.B. HomeSpan in alle ESP32 SmartHome Projekte mit ein und benutze circuitpython für Kommunikation und Steuerung mit anderen Geräten, um jederzeit kurze Anpassungen vornehmen zu können)



##### Natürlich gibt es auch Nachteile

Es verbraucht mehr Speicher, ist selbstverständlich langsamer in vielen Fällen und lässt sich nicht so gut vor Manipulationen von aussen schützen, wie gute gebrannte Firmware. Doch gerade in der Entwicklungsphase und zum Experimentieren wiegen die Vorteile die meisten Nachteile auf. 



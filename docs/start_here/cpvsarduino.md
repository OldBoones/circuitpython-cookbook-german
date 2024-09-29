### Circuitpython vs. [Arduino IDE](https://www.arduino.cc/en/software)

Die Arduino IDE (Inzwischen in der Version 2) ist der Standard in der Entwicklung von und mit Mikrocontrollern. Inzwischen nehmen zwar auch Weitere (Wie VSCode mit PlatformIO) mehr und mehr Platz ein, doch noch kommt man um Arduino IDE nicht herum wenn man professionellen und direkten Zugriff auf die Funktionen des Mikrocontrollers haben möchte. 

> [!NOTE]  
> Ein vielversprechendes Projekt ist [Embedded Swift]([Swift.org - Get Started with Embedded Swift on ARM and RISC-V Microcontrollers](https://www.swift.org/blog/embedded-swift-examples/)), jedoch noch ziemlich am Anfang und recht begrenzt in der Unterstützung. Man sollte es im Auge behalten

#### Möglichkeiten und Funktionsweise/-umfang sind quasi unendlich

und würden den Rahmen dieses Projekts deutlich sprengen. Schliesslich sind wir ja hier für Circuitpython. 

#### Nur so viel:

Nahezu jeder Hersteller von (open-source) Hardware bietet Beispiele und Bibliotheken für die Arduino IDE und eine Beschäftigung damit lohnt sich immer. Leider ist die Einstiegshürde grösser und ohne bessere Kenntnisse in c/c++ ist es nahezu unmöglich, Fehler und Probleme in Beispielen und/oder Bibliotheken zu lösen. 

Wer in Mikrocontroller oder Elektronik einsteigen, sein SmartHome ausbauen, nur mal rumprobieren, ein Hobby-/Bastelprojekt realisieren oder mit dem Kind etwas über Technologie lernen und lehren möchte, für den wird Circuitpython in jedem Fall ausreichen und empfohlen sein. 

Mit steigender Komplexität der Projekte wird man vermutlich irgendwann an die Grenzen von Circuitpython stossen (vielleicht.. weil auch Hardware und Circuitpython entwickeln sich weiter) und man wird zur Arduino IDE (oder ein Pendant) greifen.

Es schadet keinesfalls sich früher oder später in Richtung professionelle Entwicklung zu bewegen und es empfiehlt sich die Beispiele und Bibliotheken der Hersteller anzusehen. Es ist nur kein "mal eben" sondern erfordert Kenntnisse zu erlangen und eine hohe Frustrationstoleranz. Detailliertes Können auf diesem Gebiet deckt schliesslich ganze Berufe ab (die auch entsprechend vergütet werden). 

Oft genug haben (auch Profis) schon Stunden und Tage damit verbracht, Fehler in Bibliotheken zu suchen, oder zu verstehen warum ihnen gerade der Sensor verbrannt ist. Schwierigkeiten die mit Circuitpython eher nicht passieren. 

#### Dennoch:

Wer **<u>so richtig</u>** lernen will und/oder professionell und für die Produktion geeignete Firmware schreiben will, braucht die Arduino IDE (oder ein passendes Pendant) und tiefe Kenntnisse über Hardware und deren Funktionsweise. Doch es lohnt sich.

Wissen lohnt sich immer aber Dieses schafft einen tiefen Einblick in die (elektronische) Welt die uns umgibt und wer weiss.. vielleicht stellt der eine oder andere fest, dass er damit in Zukunft seinen Lebensunterhalt verdienen will. 

#### Also:

Circuitpython ist hervorragend für den Einstieg und/oder Experimente und verschiedene, nicht zu komplexe oder Ressourcen(Zeit, Speicher, Energie, uvm.) abhängige Projekte. ArduinoIDE ist die Lösung für das Meiste was Mikrocontroller können, jedoch bezahlt man mit den eigenen Ressourcen oder sehr viel Wissen. 

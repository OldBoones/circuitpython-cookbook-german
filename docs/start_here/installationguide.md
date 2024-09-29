### Download und Installation von Circuitpython

Je nach Mikrocontroller-Familie gibt es verschiedene Wege wie man Circuitpython auf den Mikrocontroller bekommt. Wir versuchen hier die meisten Wege zu besprechen.

##### 1. Finde die richtige Software

Suche auf der [Circuitpython Website](https://circuitpython.org/downloads) nach dem Modell Deines Mikrocontrollers

[!TIP]

> Das Suchfeld (direkt unter "Downloads") lässt Dich leicht die richtige Seite finden. 
> 
> Wenn Du nicht sicher bist was genau Dein Modell ist, dann gucke noch einmal auf die Beschreibung des Herstellers oder gib den Namen des Herstellers ein und gucke, ob Du Dein Modell an der Abbildung erkennst.

<img src="installationguide/2024-09-29-02-33-32-image.png" title="" alt="" width="545">

[!IMPORTANT]

> Es gibt verschiedene Architekturen (auch Familien genannt) von Mikrocontrollern, wie z.B. ESP32, Raspberry Pi, Arduino. Eine **<u>Plattform</u>** ist das gesamte System inklusive der installierten Software (z.B. ESP32S3), eine **<u>Architektur</u>** im technischen Sinn, ist nochmal was anderes aber hier nicht relevant (ToDo: Hier ein Link zu einer detaillierten Erklärung)
> 
> Benutzt Du die Bezeichnung des Herstellers findest Du den Richtigen. Sollte das nicht klappen, schicke gerne eine Nachricht

#### 2. Lade die Software runter

Wenn Du Dein Modell gefunden hast, klicke es an und es müsste sich eine Seite öffnen die so ähnlich aussieht wie im Bild (hier drunter). Mit dem Bild links kannst Du noch einmal prüfen ob Deine Auswahl auch dem entspricht was Du vor Dir liegen hast.

<img title="" src="file:///Users/hr/Documents/Entwicklung/circuitpython-cookbook/docs/start_here/installationguide/download_esp.jpg" alt="download_esp.jpg" width="552">

Je nach Modell variiert die rechte Seite: 

- Zuerst steht ganz oben die aktuellste (getestete/stabile) Version, die für Dein Modell zur Verfügung steht. 

- [!NOTE]  
  
  > Hier im Bild ist die aktuellste Version 9.1.4. Es gibt auch die Möglichkeit ältere Versionen herunterzuladen und auch neuere, aber beta Software (das heisst Software in Arbeit, die noch auf Fehler untersucht wird).
  > 
  > In manchen Fällen kann es Sinn machen auf eines von beidem zurückzugreifen, es wird allerdings nicht empfohlen und kann unvorhergesehene Probleme bereiten

- Die 3 Buttons sind nicht immer 3, meistens kann man lediglich die .uf2 Datei runterladen. 

- Klicke nun auf "Download .UF2 NOW" und warte bis der Download abgeschlossen ist. 

- [!IMPORTANT]  
  
  > Solltest Du alle 3 Optionen haben, kannst Du Circuitpython unter Umständen auch direkt aus dem Browser installieren. Mehr dazu in der Installationsanweisung

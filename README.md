[english version](#introduction)

# Einleitung
Viele (aktuell so angesagte) smarte Assistenten wie Amazon Alexa, Google Home, Apple Siri und Microsoft Cortana benötigen zwingend eine Internetverbindung um u.a. die Funktionen STT (Sprache in Text) und TTS (Text in Sprache) in ordentlicher Qualität anzubieten. Es gibt aber auch Open Source Projekte die alternative Assistenten entwickeln, die teils offline funktionieren.

Für den Bereich "STT/TTS" werden dazu jedoch gute Trainings-Testdaten (bspw. zum Deep-Learning) benötigt. Hier kommt das Projekt Mozilla Common Voice ins Spiel.

# Und?!
Ich möchte meinen kleinen bescheidenen Beitrag leisten und stelle meine Stimme unter der CC0 Lizenz zur Verfügung. Die notwendigen Sätze entstammen dem Mozilla Common Voice Projekt und die Aufzeichnung der Stimme habe ich mit Mimic-Recording-Studio (von MyCroft) vorgenommen.

# Klingt gut. Was genau gibt es hier.
* Der gesamte deutsche Corpus wie er von Common Voice zur Verfügung gestellt wird (Basis clips.tsv)
* Der Corpus als CSV Format, dass er vom Mimic-Recording-Studio verwendet werden kann
* Die SQlite DB vom Mimic-Recording-Studio mit meinen (bisher) eingesprochenen Sätzen
* Die LJSpeech-1.1 Struktur (metadata.csv und zugehörige WAV-Dateien) zur Verarbeitung mit mimic2 (basiert auf Tacotron)

# Sonstiges
Bitte verwende es nicht für Böses!
Solltest Du meine (konkrete) TTS Stimme verwenden wäre ich für eine Info zum Projekt und eine Demo dankbar

Außerdem gilt mein Dank an die Projekte/Communities von Mozilla Common Voice und MyCroft / Mimic.
Besonds an Lindsay Saunders (Mozilla) für den netten Kontakt und eltocino, gras64, dominik von der MyCroft Community für die Gedult meine Anfängerfragen gedultig zu beantworten :-).

# introduction
bla bla

# Links
* https://github.com/MycroftAI/mimic2
* https://github.com/MycroftAI/mimic-recording-studio
* https://community.mycroft.ai/
* https://voice.mozilla.org/
* https://github.com/mozilla/CorporaCreator

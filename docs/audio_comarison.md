# Vocoder Vergleich auf Basis des "thorsten" Tacotron 2 Modells
Hier sind Hörproben mit unterschiedlichen Vocodern. Alle gesprochenen Texte (Sample 1 - 4) basieren auf Aufnahmen im Dataset, jedoch nicht auf dem Spektogramm von "ground truth", sondern auf Basis des trainierten Tacotron 2 Modells. Sample 5 ist der Beginn des Märchens "Der Froschkönig" und wurde nicht für das Dataset aufgezeichnet.

## Sätze
* **Sample #01**: Eure Schoko-Bonbons sind sagenhaft lecker!
* **Sample #02**: Eure Tröte nervt.
* **Sample #03**: Europa und Asien zusammengenommen wird auch als Eurasien bezeichnet.
* **Sample #04**: Euer Plan hat ja toll geklappt.
* *Sample #05: "In den alten Zeiten, wo das Wünschen noch geholfen hat, lebte ein König, dessen Töchter waren alle schön ..." (Anfang vom "Froschkönig")*

# Ground truth
Originalaufnahmen aus dem "thorsten" Dataset.

<dl>
  <ul>
    <li>Sample #01 - Eure Schoko-Bonbons sind sagenhaft lecker!: <audio controls="" preload="none"><source src="../samples/sample01-gt.wav"></audio></li>
    <li>Sample #02 - Eure Tröte nervt.: <audio controls="" preload="none"><source src="../samples/sample02-gt.wav"></audio></li>
    <li>Sample #03 - Europa und Asien zusammengenommen wird auch als Eurasien bezeichnet.: <audio controls="" preload="none"><source src="../samples/sample03-gt.wav"></audio></li>
    <li>Sample #04 - Euer Plan hat ja toll geklappt.: <audio controls="" preload="none"><source src="../samples/sample04-gt.wav"></audio></li>
  </ul>
</dl>


# Griffin Lim
> Details zum Model: (todo: link)
> Tacotron2 + DDC: 460k Schritte trainiert

# ParallelWaveGAN
> Tacotron2 + DDC: 360k Schritte trainiert
> PWGAN Vocoder: 925k Schritte trainiert

<dl>
  <ul>
    <li>Sample #01 - Eure Schoko-Bonbons sind sagenhaft lecker!:
    <audio controls="" preload="none"><source src="../samples/sample01-pwgan.wav"></audio></li>
    
    <li>Sample #02 - Eure Tröte nervt.:
    <audio controls="" preload="none"><source src="../samples/sample02-pwgan.wav"></audio></li>
    
    <li>Sample #03 - Europa und Asien zusammengenommen wird auch als Eurasien bezeichnet.:
    <audio controls="" preload="none"><source src="../samples/sample03-pwgan.wav"></audio></li>
    
    <li>Sample #04 - Euer Plan hat ja toll geklappt.:
    <audio controls="" preload="none"><source src="../samples/sample04-pwgan.wav"></audio></li>
    
    <li>Sample #05 - Anfang vom Froschkönig:
    <audio controls="" preload="none"><source src="../samples/sample04-pwgan.wav"></audio></li>
  </ul>
</dl>


# WaveGrad
> todo

# HifiGAN
> todo

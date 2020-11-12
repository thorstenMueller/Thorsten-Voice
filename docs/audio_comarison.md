# Vocoder Vergleich auf Basis des "thorsten" Tacotron 2 Modells
Hier sind Hörproben mit unterschiedlichen Vocodern. Alle gesprochenen Texte (*Sample 1 - 4*) basieren auf Aufnahmen im Dataset, jedoch nicht auf dem Spektogramm von "ground truth", sondern auf Basis des trainierten Tacotron 2 Modells. Sample 5 ist der Beginn des Märchens "Der Froschkönig" und wurde nicht für das Dataset aufgezeichnet.

## Sätze
* **Sample #01**: Eure Schoko-Bonbons sind sagenhaft lecker!
* **Sample #02**: Eure Tröte nervt.
* **Sample #03**: Europa und Asien zusammengenommen wird auch als Eurasien bezeichnet.
* **Sample #04**: Euer Plan hat ja toll geklappt.
* *Sample #05: "In den alten Zeiten, wo das Wünschen noch geholfen hat, lebte ein König, dessen Töchter waren alle schön ..." (Anfang vom "Froschkönig")*

# Ground truth
Originalaufnahmen aus dem "thorsten" Dataset.

<dl>
<html>
<body>
<table>
<thead>
  <tr>
    <th>Sample</th>
    <th>Text</th>
    <th>Audio</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>01</td>
    <td>Eure Schoko-Bonbons sind sagenhaft lecker</td>
    <td><audio controls="" preload="none"><source src="sample01-gt.wav"></td></tr>
  <tr>
    <td>02</td>
    <td>Eure Tröte nervt</td>
    <td><audio controls="" preload="none"><source src="sample02-gt.wav"></td></tr>
  <tr>
    <td>03</td>
    <td>Europa und Asien zusammengenommen wird auch als Eurasien bezeichnet</td>
    <td><audio controls="" preload="none"><source src="sample03-gt.wav"></td>
  </tr>
  <tr>
    <td>04</td>
    <td>Euer Plan hat ja toll geklappt.</td>
    <td><audio controls="" preload="none"><source src="sample04-gt.wav"></td>
  </tr>
</tbody>
</table>
</body>
</html>
</dl>


# Griffin Lim
> Details zum Model: (todo: link)
> Tacotron2 + DDC: 460k Schritte trainiert

# ParallelWaveGAN
> Tacotron2 + DDC: 360k Schritte trainiert
> PWGAN Vocoder: 925k Schritte trainiert

<dl>
<html>
<body>
<table>
<thead>
  <tr>
    <th>Sample</th>
    <th>Text</th>
    <th>Audio</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>01</td>
    <td>Eure Schoko-Bonbons sind sagenhaft lecker</td>
    <td><audio controls="" preload="none"><source src="sample01-pwgan.wav"></td>
  </tr>
  <tr>
    <td>02</td>
    <td>Eure Tröte nervt</td>
    <td><audio controls="" preload="none"><source src="sample02-pwgan.wav"></td>
  </tr>
  <tr>
    <td>03</td>
    <td>Europa und Asien zusammengenommen wird auch als Eurasien bezeichnet</td>
    <td><audio controls="" preload="none"><source src="sample03-pwgan.wav"></td>
  </tr>
  <tr>
    <td>04</td>
    <td>Euer Plan hat ja toll geklappt.</td>
    <td><audio controls="" preload="none"><source src="sample04-pwgan.wav"></td>
  </tr>
  <tr>
    <td>05</td>
    <td>Anfang vom Froschkönig</td>
    <td><audio controls="" preload="none"><source src="sample05-pwgan.wav"></td>
  </tr>
</tbody>
</table>
</body>
</html>
</dl>








# WaveGrad
> todo

# HifiGAN
> todo

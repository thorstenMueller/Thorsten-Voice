# Vocoder Vergleich auf Basis des "thorsten" Tacotron 2 Modells
Hier sind Hörproben mit unterschiedlichen Vocodern. Alle gesprochenen Texte (*Sample 1 - 4*) basieren auf Aufnahmen im Dataset, jedoch nicht auf dem Spektogramm von "ground truth", sondern auf Basis des trainierten Tacotron 2 Modells. Sample 5 ist der Beginn des Märchens "Der Froschkönig" und wurde nicht für das Dataset aufgezeichnet.

## Sätze
* **Sample #01**: Eure Schoko-Bonbons sind sagenhaft lecker!
* **Sample #02**: Eure Tröte nervt.
* **Sample #03**: Europa und Asien zusammengenommen wird auch als Eurasien bezeichnet.
* **Sample #04**: Euer Plan hat ja toll geklappt.
* *Sample #05: "In den alten Zeiten, wo das Wünschen noch geholfen hat, lebte ein König, dessen Töchter waren alle schön." (Anfang vom "Froschkönig")*

# Ground truth
Originalaufnahmen aus dem "thorsten" Dataset.

<dl>

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
    <td><audio controls="" preload="none"><source src="samples/sample01-gt.wav"></audio></td>
  </tr>
  <tr>
    <td>02</td>
    <td>Eure Tröte nervt</td>
    <td><audio controls="" preload="none"><source src="samples/sample02-gt.wav"></audio></td>
  </tr>
  <tr>
    <td>03</td>
    <td>Europa und Asien zusammengenommen wird auch als Eurasien bezeichnet</td>
    <td><audio controls="" preload="none"><source src="samples/sample03-gt.wav"></audio></td>
  </tr>
  <tr>
    <td>04</td>
    <td>Euer Plan hat ja toll geklappt.</td>
    <td><audio controls="" preload="none"><source src="samples/sample04-gt.wav"></audio></td>
  </tr>
</tbody>
</table>

</dl>


# Griffin Lim
> Details zum Model: (todo: link)  
> Tacotron2 + DDC: 460k Schritte trainiert

<dl>

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
    <td><audio controls="" preload="none"><source src="samples/sample01-griffin-lim.wav"></audio></td>
  </tr>
  <tr>
    <td>02</td>
    <td>Eure Tröte nervt</td>
    <td><audio controls="" preload="none"><source src="samples/sample02-griffin-lim.wav"></audio></td>
  </tr>
  <tr>
    <td>03</td>
    <td>Europa und Asien zusammengenommen wird auch als Eurasien bezeichnet</td>
    <td><audio controls="" preload="none"><source src="samples/sample03-griffin-lim.wav"></audio></td>
  </tr>
  <tr>
    <td>04</td>
    <td>Euer Plan hat ja toll geklappt.</td>
    <td><audio controls="" preload="none"><source src="samples/sample04-griffin-lim.wav"></audio></td>
  </tr>
  <tr>
    <td>05</td>
    <td>In den alten Zeiten, wo das Wünschen noch geholfen hat, lebte ein König, dessen Töchter waren alle schön.</td>
    <td><audio controls="" preload="none"><source src="samples/sample05-griffin-lim.wav"></audio></td>
  </tr>
</tbody>
</table>

</dl>

# ParallelWaveGAN
> Details: [Notebook von Olaf](https://colab.research.google.com/drive/15kJHTDTVxyIjxiZgqD1G_s5gUeVNLkfy?usp=sharing)  
> Tacotron2 + DDC: 360k Schritte trainiert, PWGAN Vocoder: 925k Schritte trainiert
<dl>

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
    <td><audio controls="" preload="none"><source src="samples/sample01-pwgan.wav"></audio></td>
  </tr>
  <tr>
    <td>02</td>
    <td>Eure Tröte nervt</td>
    <td><audio controls="" preload="none"><source src="samples/sample02-pwgan.wav"></audio></td>
  </tr>
  <tr>
    <td>03</td>
    <td>Europa und Asien zusammengenommen wird auch als Eurasien bezeichnet</td>
    <td><audio controls="" preload="none"><source src="samples/sample03-pwgan.wav"></audio></td>
  </tr>
  <tr>
    <td>04</td>
    <td>Euer Plan hat ja toll geklappt.</td>
    <td><audio controls="" preload="none"><source src="samples/sample04-pwgan.wav"></audio></td>
  </tr>
  <tr>
    <td>05</td>
    <td>In den alten Zeiten, wo das Wünschen noch geholfen hat, lebte ein König, dessen Töchter waren alle schön.</td>
    <td><audio controls="" preload="none"><source src="samples/sample05-pwgan.wav"></audio></td>
  </tr>
</tbody>
</table>

</dl>


# WaveGrad
> todo

# HifiGAN
> todo

# VocGAN
> **Diese Beispiele basieren auf "ground truth" und nicht auf dem Tacotron 2 Modell**  
> 200 Epochen / 284k Trainingsschritte

<dl>

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
    <td><audio controls="" preload="none"><source src="samples/sample01-vocgan.wav"></audio></td>
  </tr>
  <tr>
    <td>02</td>
    <td>Eure Tröte nervt</td>
    <td><audio controls="" preload="none"><source src="samples/sample02-vocgan.wav"></audio></td>
  </tr>
  <tr>
    <td>03</td>
    <td>Europa und Asien zusammengenommen wird auch als Eurasien bezeichnet</td>
    <td><audio controls="" preload="none"><source src="samples/sample03-vocgan.wav"></audio></td>
  </tr>
  <tr>
    <td>04</td>
    <td>Euer Plan hat ja toll geklappt.</td>
    <td><audio controls="" preload="none"><source src="samples/sample04-vocgan.wav"></audio></td>
  </tr>
</tbody>
</table>

</dl>

# GlowTTS / Waveglow
> Details: [Github von Synesthesiam](https://github.com/rhasspy/de_larynx-thorsten)
> GlowTTS trainiert für 380k und Vocoder für 500k Schritte.

<dl>

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
    <td><audio controls="" preload="none"><source src="samples/sample01-waveglow.wav"></audio></td>
  </tr>
  <tr>
    <td>02</td>
    <td>Eure Tröte nervt</td>
    <td><audio controls="" preload="none"><source src="samples/sample02-waveglow.wav"></audio></td>
  </tr>
  <tr>
    <td>03</td>
    <td>Europa und Asien zusammengenommen wird auch als Eurasien bezeichnet</td>
    <td><audio controls="" preload="none"><source src="samples/sample03-waveglow.wav"></audio></td>
  </tr>
  <tr>
    <td>04</td>
    <td>Euer Plan hat ja toll geklappt.</td>
    <td><audio controls="" preload="none"><source src="samples/sample04-waveglow.wav"></audio></td>
  </tr>
  <tr>
    <td>05</td>
    <td>In den alten Zeiten, wo das Wünschen noch geholfen hat, lebte ein König, dessen Töchter waren alle schön.</td>
    <td><audio controls="" preload="none"><source src="samples/sample05-waveglow.wav"></audio></td>
  </tr>
</tbody>
</table>

</dl>



# TensorFlowTTS / Multiband MelGAN
> Thanks [Monatis](https://github.com/monatis)  
> Details: [Notebook von Monatis](https://colab.research.google.com/drive/1W0nSFpsz32M0OcIkY9uMOiGrLTPKVhTy?usp=sharing#scrollTo=SCbWCChVkfnn)  
> Taco2 Modell für 80k Schritte trainiert, Multiband MelGAN für 800k Schritte.

<dl>

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
    <td><audio controls="" preload="none"><source src="samples/sample01-TensorFlowTTS.wav"></audio></td>
  </tr>
  <tr>
    <td>02</td>
    <td>Eure Tröte nervt</td>
    <td><audio controls="" preload="none"><source src="samples/sample02-TensorFlowTTS.wav"></audio></td>
  </tr>
  <tr>
    <td>03</td>
    <td>Europa und Asien zusammengenommen wird auch als Eurasien bezeichnet</td>
    <td><audio controls="" preload="none"><source src="samples/sample03-TensorFlowTTS.wav"></audio></td>
  </tr>
  <tr>
    <td>04</td>
    <td>Euer Plan hat ja toll geklappt.</td>
    <td><audio controls="" preload="none"><source src="samples/sample04-TensorFlowTTS.wav"></audio></td>
  </tr>
  <tr>
    <td>05</td>
    <td>In den alten Zeiten, wo das Wünschen noch geholfen hat, lebte ein König, dessen Töchter waren alle schön.</td>
    <td><audio controls="" preload="none"><source src="samples/sample05-TensorFlowTTS.wav"></audio></td>
  </tr>
</tbody>
</table>

</dl>
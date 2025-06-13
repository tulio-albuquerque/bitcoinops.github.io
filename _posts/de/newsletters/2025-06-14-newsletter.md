---
title: 'Bitcoin Optech Newsletter #357'
permalink: /en/newsletters/2025/06/06/
name: 2025-06-06-newsletter
slug: 2025-06-06-newsletter
type: newsletter
layout: newsletter
lang: en
---
Der Newsletter dieser Woche teilt eine Analyse über die Synchronisierung vollständiger Knoten
Ohne alte Zeugen.  Ebenfalls enthalten sind unsere regulären Abschnitte mit
Beschreibungen von Diskussionen über den Änderung des Konsenses, Ankündigungen von
Neuveröffentlichungen und Veröffentlichungskandidaten sowie Zusammenfassungen bemerkenswerter Änderungen an
Beliebte Bitcoin -Infrastruktur -Software.

## Nachricht

- ** Synchronisieren vollständige Knoten ohne Zeugen: ** Jose SK [gepostet] [SK Nowit]
  Bitcoin eine Zusammenfassung einer [Analyse] [SK Nowit Gist] er
  über die Sicherheitskompromisse des Neu gestarteten
  Knoten mit einer bestimmten Konfiguration, um das Herunterladen einiger zu vermeiden
  Historische Blockchain -Daten.  Standardmäßig verwenden Bitcoin -Kernknoten die
  `AsumeValid` Konfigurationseinstellung, die die Validierung von Skripten überspringt
  in Blöcken mehr als ein oder zwei Monate vor der Veröffentlichung der
  Version des Bitcoin -Kerns.  Obwohl standardmäßig deaktiviert, viele
  Benutzer von Bitcoin Core setzen auch eine Konfigurationseinstellung von "Prune", die
  Löscht Blöcke einige Zeit nach der Validierung (wie lange Blöcke sind
  Aufbewahrt hängt von der Größe der Blöcke und der ausgewählten spezifischen Einstellung ab
  vom Benutzer).

  SK argumentiert, dass Zeugendaten, die nur zur Validierung verwendet werden
  Skripte sollten nicht von geschnittenen Knoten für Asumevalid heruntergeladen werden
  Blöcke, weil sie es nicht zur Validierung von Skripten verwenden und werden
  Löschen Sie es schließlich.  Überspringen des Zeugen -Downloads "kann schneiden
  Bandbreitennutzung um über 40%“, schreibt er.

  Ruben Somsen [argumentiert] [Somsen Nowit], dass dies die Sicherheit ändert
  Modell in gewissem Maße.  Obwohl Skripte nicht validiert sind, die
  heruntergeladene Daten werden gegen die Verpflichtung aus dem Block validiert
  Header Merkle Root auf die Coinbase -Transaktion zu den Zeugendaten.
  Dies stellt sicher
  Der Knoten wurde zunächst synchronisiert.  Wenn niemand routinemäßig die validiert
  Existenz der Daten könnte möglicherweise verloren gehen, wie [hat
  geschah] [Ripple -Verlust] an mindestens einen Altcoin.

  Die Diskussion wurde zum Zeitpunkt des Schreibens fortgesetzt.

## Konsens ändern

_A monatlicher Abschnitt Zusammenfassungen von Vorschlägen und Diskussionen über Änderungen
Bitcoins Konsensregeln._

- ** Quantencomputerbericht: ** Clara Shikhelman [veröffentlicht] [Shikelman
  Quantum] Bitcoin Die Zusammenfassung eines [Berichts] [SM -Bericht] sie
  gemeinsam mit Anthony Milton über die Risiken für Bitcoin-Benutzer von verfasst
  Schnelle Quantencomputer, ein Überblick über mehrere Wege zu [Quanten
  Resistenz] [Thema Quantenwiderstand] und eine Analyse von Kompromissen
  Beteiligung an der Aktualisierung des Bitcoin -Protokolls.  Die Autoren finden 4 bis 10
  Millionen BTC sind potenziell anfällig für Quantendiebstahl, einige
  Minderung ist jetzt möglich, Bitcoin -Bergbau ist es unwahrscheinlich
  bedroht durch Quantum Computing kurz oder mittelfristig und
  Das Upgrade erfordert eine weit verbreitete Vereinbarung.

- ** Transaktionsgewichtsgrenze mit Ausnahme zur Verhinderung der Beschlagnahme: **
  Vojtěch strnad [veröffentlicht] [strnad limit] to deling bitcoin, um vorzuschlagen
  Die Idee für eine Konsensänderung, um das maximale Gewicht der meisten zu begrenzen
  Transaktionen in einem Block.  Die einfache Regel würde nur eine Transaktion zulassen
  größer als 400.000 Gewichtseinheiten (100.000 VByte) in einem Block, wenn es war
  Die einzige Transaktion in diesem Block neben der Coinbase -Transaktion.
  Strnad und andere beschrieben die Motivation, das Maximum einzuschränken
  Transaktionsgewicht:

  - _esisier Block -Vorlagenoptimierung: _ Es ist einfacher, a zu finden
    nahezu optimale Lösung für das [Rucksack-Problem] [] desto kleiner die
    Artikel werden mit der Gesamtgrenze verglichen.  Dies ist teilweise
    Aufgrund der Minimierung der am Ende übrig gebliebenen Platz
    Kleinere Gegenstände, die weniger ungenutzten Raum lassen.

  - _esisier Relay -Richtlinie: _ Die Richtlinie für die Weitergabe unbestätigter
    Transaktionen zwischen Knoten sagen voraus, welche Transaktionen aussehen werden
    abgebaut, um eine Bandbreite zu verschwenden.  Riesentransaktionen machen
    Genaue Vorhersagen schwieriger, da selbst eine kleine Veränderung im oberen Feeration verursachen kann
    sie verzögert oder vertrieben werden.

  - _avoiding Mining Centralization: _ Sicherstellen
    In der Lage, fast alle Transaktionen zu handhaben, verhindert Benutzer von Special
    Transaktionen von der Bezahlung von Gebühren außerhalb des Bandes] [Thema
    Gebühren außerhalb des Bandes], was zu einer Zentralisierung des Bergbaus führen kann.

  Gregory Sanders [notiert] [Sanders Grenze] Es könnte angemessen sein
  Einfach weiche Gabel eine maximale Gewichtsbegrenzung ohne Ausnahmen basiert
  über die 12 Jahre konsistenten Staffelrichtlinie von Bitcoin Core.  Gregory
  Maxwell [hinzugefügt] [Maxwell Limit], dass Transaktionen nur UTXOS ausgeben
  Erstellt, bevor die Softgabel eine Ausnahme zu verhindern kann
  Beschlagnahme und eine [vergängliche Softgabel] [Thema Übergangsweiche
  gabeln] würde es der Einschränkung ermöglichen, abzulaufen, wenn der
  Community beschloss, es nicht zu erneuern.

  Zusätzliche Diskussion untersuchte die Bedürfnisse von Parteien, die wollen
  Große Transaktionen, hauptsächlich [BITVM] [Thema ACC] Nutzer kurzfristig,
  und ob ihnen alternative Ansätze zur Verfügung standen.

- ** Entfernen von Ausgängen aus dem UTXO -Set basierend auf Wert und Zeit: ** Robin

Linus [veröffentlicht] [Linus Dust] an das Deling -Bitcoin, um eine weiche Gabel vorzuschlagen
  zum Entfernen von Ausgängen mit niedrigem Wert aus dem UTXO-Set nach einigen
  Zeit.  Mehrere Variationen der Idee wurden mit den beiden diskutiert
  Hauptalternativen sind:

  - _destroy alte unwirtschaftliche Fonds: _ kleine Wertausgänge, die nicht hatten
    Es würde lange Zeit verbracht werden, unpassbar zu sein.

  - _Rire alte unwirtschaftliche Fonds, die mit einem Nachweis der Existenz ausgegeben werden sollen: _
    [UTreexo] [Thema UTreexo] oder ein ähnliches System könnte verwendet werden, um zuzulassen
    eine Transaktion, um zu beweisen, dass die Ausgaben, die sie ausgeben
    UTXO -Set.  Alte und [unwirtschaftliche Ausgaben] [Thema unwirtschaftliche Ausgaben] würden
    müssen diesen Beweis einbeziehen, aber neuere und höherwertige Ausgaben würden es tun
    immer noch im UTXO -Set aufbewahrt werden.

  Jede Lösung würde die maximale Größe des UTXO effektiv einschränken
  SET (unter der Annahme eines Mindestwerts und der 21 Millionen Bitcoin -Grenze).
  Es wurden einige interessante technische Aspekte eines Designs diskutiert,
  einschließlich Alternativen zu UTreexo -Proofs für diese Anwendung, die
  könnte praktischer sein.

## veröffentlicht und veröffentlichen Kandidaten

_New -Veröffentlichungen und Veröffentlichung von Kandidaten für die beliebte Bitcoin -Infrastruktur
Projekte.  Bitte erwägen Sie ein Upgrade auf neue Veröffentlichungen oder helfen beim Testen
Kandidaten veröffentlichen._

- [Core Lightning 25.05RC1] [] ist ein Veröffentlichungskandidat für das nächste Major
  Version dieser beliebten LN -Knoten -Implementierung.

- [Lnd 0.19.1-beta.rc1] [] ist ein Freisetzungskandidat für eine Wartung
  Version dieser beliebten LN -Knoten -Implementierung.

## Bemerkenswerte Code- und Dokumentationsänderungen

_NOTABLE LEIGSCHEINE RECHNUNGEN IN [BITCOIN CORE] [Bitcoin Core Repo], [Core
Lightning] [Core Lightning Repo], [Eclair] [Eclair Repo], [LDK] [LDK Repo],
[Lnd] [lnd repo], [libSecp256k1] [libSecp256k1 repo], [Hardware -Brieftasche
Schnittstelle (HWI)] [HWI Repo], [Rost Bitcoin] [Rust Bitcoin Repo], [BTCPay
Server] [BTCPAY Server Repo], [BDK] [BDK Repo], [Bitcoin -Verbesserung
Vorschläge (BIPS)] [BIPS Repo], [Lightning Bolts] [Bolts Repo],
[Lightning Blips] [Blips Repo], [Bitcoin Inquisition] [Bitcoin Inquisition
Repo] und [Binanas] [Binana Repo] ._

- [Bitcoin Core #32582] [] fügt eine neue Protokollierung hinzu, um die Leistung von zu messen
  [Kompaktblockrekonstruktion] [Thema Compact Block Relay] durch Verfolgung der
  Gesamtgröße der Transaktionen, die ein Knoten von seinen Kollegen anfordert
  (`getBlocktxn`), die Anzahl und Gesamtgröße der Transaktionen, die ein Knoten sendet
  zu seinen Kollegen (`blocktxn`) und Hinzufügen eines Zeitstempels zu Beginn von
  `Teilweise indownloadedblock :: initdata ()` verfolgen, wie lange der Mempool -Lookup lange
  Schritt allein dauert (in Modi mit hohem und niedrigem Bandbreiten). Siehe Newsletter
  [#315] [News315 Compact] Für einen früheren Statistikbericht zum Kompaktblock
  Wiederaufbau.

- [Bitcoin Core #31375] [] fügt ein neues `Bitcoin -m` -CLI -Tool hinzu, das sich umhüllt und
  führt die [Multiprocess] [Multiprocess -Projekt] Binärdateien `Bitcoin -Knoten aus
  (`bitcoind`),` bitcoin gui` (`bitcoinqt`),` bitcoin rpc` (`bitcoin-cli
  -named`). Derzeit funktionieren diese auf die gleiche Weise wie die monolithischen
  Binärdateien, außer dass sie die Option `-ipcbind` unterstützen (siehe Newsletter
  [#320] [News320 IPC]), aber zukünftige Verbesserungen werden es einem Knotenläufer ermöglichen
  Starten und stoppen die Komponenten unabhängig voneinander auf verschiedenen Maschinen und
  Umgebungen. Siehe [Newsletter #353] [News353 PR Review] für einen Bitcoin Core PR
  Bewertungsclub über diese PR.

- [BIPS #1483] [] Fusions [bip77] [], der vorschlägt [Payjoin v2] [Topic Payjoin], und ein
  Asynchrone serverlose Variante, in der der Absender und der Empfänger ihre übergeben
  Verschlüsseltes PSBTS auf einen Payjoin -Verzeichnisserver, der nur gespeichert und weiterleitet
  Nachrichten. Da das Verzeichnis die Nutzlasten weder lesen noch ändern kann, weder die Brieftasche
  muss einen öffentlichen Server hosten oder gleichzeitig online sein. Siehe Newsletter
  [#264] [news264 payjoin] Für zusätzlichen Kontext zu Payjoin v2.

{ % enthalten Snippets/recap-ad.md, wenn = "2025-06-10 16:30" %}
{ % enthalten Referenzen.md %}
{ % enthalten Linker/Ausgaben.
[Core Lightning 25.05RC1]: https://github.com/elementsproject/lightning/releases/tag/v25.05rc1
[Ripple Loss]: https://x.com/joelkatz/status/191923214750892305
[SK Nowit]: https://delvingbitcoin.org/t/witnessless-sync-forpuned-nodes/1742/
[SK Nowit Gist]: https://gist.github.com/josesk999/df0a2a014c7d9b626df1e2b19ccc7fb1
[Somsen Nowit]: https://gist.github.com/josesk999/df0a2a014c7d9b626df1e2b19ccc7fb1?perMalink_Coment_ID=5597316#gistComent-5597316
[Shikelman Quantum]: https://delvingbitcoin.org/t/bitcoin-and-quantum-computing/1730/
[SM-Bericht]: https://chaincode.com/bitcoin-post-quantum.pdf
[Strnad Limit]: https://delvingbitcoin.org/t/non-confiscatory-transaction-weight-limit/1732/
[Knapsack Problem]: https://en.wikipedia.org/wiki/knapsack_problem
[Sanders Limit]: https://delvingbitcoin.org/t/non-confiscatory-transaction-weight-limit/1732/2
[Maxwell Limit]: https://delvingbitcoin.org/t/non-confiscatory-transaction-weight-limit/1732/4
[Linus Dust]: https://delvingbitcoin.org/t/dust-expiry-clean-txo-set-from-spam/1707/

[lnd 0.19.1-beta.rc1]: https://github.com/lightningNetwork/lnd/releass/v0.19.1-beta.rc1
[News315 Compact]:/en/Newsletter/2024/08/09/#Statistik-auf-kompakt-Block-Rekonstruktion
[Multiprocess -Projekt]: https://github.com/ryanofsky/bitcoin/blob/pr/ipc/doc/design/multiprocess.md
[News320 IPC]:/en/Newsletter/2024/09/13/#Bitcoin-Core-30509
[news264 payjoin]:/en/Newsletter/2023/08/16/#Serverless-Payjoin
[News353 PR Review]:/en/Newsletter/2025/05/09/#Bitcoin-Core-Pr-Review-Club
---
title: 'Bitcoin Optech Newsletter #357'
permalink: /en/newsletters/2025/06/06/
name: 2025-06-06-newsletter
slug: 2025-06-06-newsletter
type: newsletter
layout: newsletter
lang: en
---
Informační bulletin tohoto týdne sdílí analýzu o synchronizaci plného uzlů
bez starých svědků.  Zahrnuty jsou také naše pravidelné sekce s
popisy diskusí o změně konsensu, oznámení
Nová vydání a uvolnění kandidátů a shrnutí významných změn
Populární bitcoinový infrastrukturní software.

## News

- ** synchronizace úplných uzlů bez svědků: ** Jose SK [zveřejněno] [SK nowit]
  Ponoření bitcoinu shrnutí [analýzy] [SK nowit gist]
  provedeno o bezpečnostních kompromisech, které umožňují nově spuštění plného
  uzly s konkrétní konfigurací, aby se zabránilo stahování některých
  Historická data blockchainu.  Ve výchozím nastavení používají uzly bitcoinů jádro
  Nastavení konfigurace assumevalid`, které přeskočí ověření skriptů
  v blocích vytvořených více než měsíc nebo dva před vydáním
  Verze Bitcoin Core běží.  Přestože je ve výchozím nastavení zakázáno, mnoho
  Uživatelé bitcoinového jádra také nastavili nastavení konfigurace `
  Odstraní bloky nějakou dobu po jejich ověření (jak dlouhé jsou bloky
  Udržováno závisí na velikosti bloků a konkrétním vybraném nastavení
  od uživatele).

  SK tvrdí, že data svědků, která se používají pouze k ověření
  Skripty, neměly by být staženy prořezanými uzly pro Assumevalid
  bloky, protože jej nepoužívají k ověření skriptů a vůli
  Nakonec to smažte.  Přeskočení stahování svědků "
  Využití šířky pásma o více než 40%, “píše.

  Ruben Somsen [tvrdí] [Somsen Nowit], že to mění bezpečnost
  Model do určité míry.  Ačkoli skripty nejsou ověřeny,
  Stažená data jsou ověřena proti závazku z bloku
  Záhlaví Merkle Root do transakce Coinbase k údajům o svědcích.
  Tím je zajištěno, že data byla k dispozici a neporušená v době, kdy
  uzel byl zpočátku synchronizován.  Pokud nikdo běžně ověřuje
  existence dat by mohla být ztracena, stejně jako [
  Stalo se] [Ztráta zvlnění] alespoň na jeden altcoin.

  Diskuse probíhala v době psaní.

## Změna konsensu

_A měsíční sekce shrnutí návrhů a diskuse o změně
Bitcoinovy ​​konsensuální pravidla._

- ** Quantum Computing Report: ** Clara Shikhelman [zveřejněno] [Shikelman
  kvantum] ponořit bitcoiny shrnutí [Zprávy] [SM Report] ona
  spoluautor s Anthonym Miltonem o rizicích pro bitcoinové uživatele
  Rychlé kvantové počítače, přehled několika cest k [Quantum
  odpor] [Téma Quantum Resistance] a analýza kompromisů
  zapojený do upgradu bitcoinového protokolu.  Autoři najdou 4 až 10
  milion BTC je potenciálně zranitelný vůči kvantové krádeži, někteří
  nyní je možné zmírnit, těžba bitcoinů je nepravděpodobná
  v krátkodobém nebo střednědobém horizontu ohroženo kvantovým výpočtem a
  Upgradování vyžaduje rozsáhlou dohodu.

- ** Limit hmotnosti transakcí s výjimkou, aby se zabránilo zabavení: **
  Vojtěch Strnad [Zveřejněno] [limit strnad] na ponoření bitcoinu k navrhování
  Myšlenka na změnu konsensu za účelem omezení maximální hmotnosti nejvíce
  transakce v bloku.  Jednoduché pravidlo by umožnilo pouze transakci
  větší než 400 000 hmotnostních jednotek (100 000 Vbytes) v bloku, pokud to bylo
  Jediná transakce v tomto bloku kromě transakce Coinbase.
  Strnad a další popsali motivaci k omezení maximálního
  Transakční hmotnost:

  - _Easier Block Template Optimization: _ Je snazší najít a
    téměř optimální řešení [problému s knofy] [] tím menší
    Položky jsou porovnány s celkovým limitem.  To je částečně
    kvůli minimalizaci množství prostoru zbývajícího na konci, s
    Menší předměty opouštějící méně nevyužitého prostoru.

  - _Easier Relay Policy: _ Zásady pro předání nepotvrzeného
    Transakce mezi uzly předpovídají, jaké transakce budou
    těženo, aby se zabránilo plýtvání šířkou pásma.  Obří transakce dělají
    Přesné předpovědi těžší, jak může způsobit i malá změna v horním feearu
    jsou zpožděny nebo vystěhovány.

  - _Avoiding Mining Centralization: _ Zajištění předávání plného uzlů
    Schopnost zvládnout téměř všechny transakce zabraňuje uživatelům speciálních
    Transakce z potřeby platit [Out-of-band poplatky] [Téma
    Poplatky mimo pásmo), které mohou vést k centralizaci těžby.

  Gregory Sanders [známý] [limit Sanders] to může být rozumné
  Jednoduše měkká vidlička maximální limit hmotnosti bez výjimek založených
  Na 12 let Bitcoin Core konzistentní reléové politiky.  Gregory
  Maxwell [přidán] [limit Maxwell], že transakce utratí pouze UTXOS
  Vytvořeno předtím, než by měkká vidlička mohla být povolena výjimkou, aby se zabránilo
  konfiskace, a že [přechodná měkká vidlička] [Téma přechodné měkké
  vidlice] by umožnilo omezení vypršit, pokud
  Komunita se rozhodla to neobnovit.

  Další diskuse zkoumala potřeby stran, které chtějí
  Velké transakce, hlavně [bitvm] [téma ACC] uživatelé v nejbližší době,
  a zda jim byly k dispozici alternativní přístupy.

- ** Odstranění výstupů ze sady UTXO na základě hodnoty a času: ** Robin

Linus [Publikováno] [Linus Dust], aby ponořil bitcoin, aby navrhl měkkou vidličku
  za odstranění výstupů s nízkou hodnotou z sady UTXO po některých
  čas.  Bylo diskutováno několik variací této myšlenky, s nimi
  Hlavní alternativy jsou:

  - _destroy staré neekonomické fondy: _ Malé hodnotové výstupy, které ne
    Byly stráveny po dlouhou dobu by se staly nesnázetelnými.

  - _Require staré neekonomické fondy, které mají být vynaloženy s důkazem existence: _
    [Utreexo] [Téma utreexo] nebo podobný systém lze použít k povolení
    transakce, která prokáže, že výstupy, které utratí, jsou součástí
    Sada UTXO.  Staré a [neekonomické výstupy] [téma neekonomické výstupy]
    musí zahrnout tento důkaz, ale novější a vyšší hodnoty by to
    stále být uložen v sadě UTXO.

  Obě řešení by účinně omezilo maximální velikost UTXO
  set (za předpokladu minimální hodnoty a limit 21 milionů bitcoinů).
  Bylo diskutováno několik zajímavých technických aspektů designu,
  včetně alternativ k důkazům utreexo pro tuto aplikaci
  může být praktičtější.

## Vydává a vydává kandidáty

_New vydává a uvolní kandidáty na populární bitcoinové infrastrukturu
projekty.  Zvažte prosím upgrade na nová vydání nebo pomoc při testování
Uvolněte kandidáty._

- [Core Lightning 25.05RC1] [] je kandidát na vydání pro další major
  Verze této populární implementace uzlu LN.

- [lnd 0.19.1-beta.rc1] [] je kandidátem na uvolnění pro údržbu
  Verze této populární implementace uzlu LN.

## Pozoruhodné změny kódu a dokumentace

_ Nepřirozené nedávné změny v [bitcoinové jádro] [bitcoinové jádro repo], [Core
Lightning] [Core Lightning Repo], [Eclair] [Eclair Repo], [LDK] [LDK Repo],
[LND] [LND Repo], [LIBSECP256K1] [LIBSECP256K1 Repo], [Hardwarová peněženka
Rozhraní (HWI)] [HWI Repo], [Rust Bitcoin] [Rust Bitcoin Repo], [BTCPay
Server] [BTCPay Server Repo], [BDK] [BDK Repo], [Vylepšení bitcoinů
Návrhy (BIPS)] [BIPS Repo], [Lightning Bolts] [Bolts Repo],
[Lightning Blips] [Blips Repo], [Bitcoin Inquisition] [Inkvizice bitcoinů
repo] a [binanas] [binana repo] ._

- [Bitcoin Core #32582] [] přidává nové protokolování pro měření výkonu
  [Kompaktní rekonstrukce bloku] [Téma Compact Block Relay] sledováním
  Celková velikost transakcí, které uzel požaduje od svých vrstevníků
  (`getblocktxn`), číslo a celková velikost transakcí, které uzel odesílá
  svým vrstevníkům (`blocktxn`) a na začátku přidání časového razítka
  `Částečně odsouzená blokování :: initData ()` Chcete -li sledovat, jak dlouho vyhledávání Mempool
  krok sám je (v režimech s vysokou i nízkou šířkou pásma). Viz zpravodaj
  [#315] [News315 Compact] Pro předchozí statistickou zprávu o kompaktním bloku
  rekonstrukce.

- [Bitcoin Core #31375] [] přidává nový nástroj Bitcoin -m` CLI, který se zabalí a
  Provádí [multiprocess] [MultiProcess Project] binární soubory `bitcoin node`
  (`bitcoind`),` bitcoin Gui` (`bitcoinqt`),` bitcoin RPC` (`bitcoin-cli
  -Mamed`). V současné době tyto fungují stejným způsobem jako monolitické
  binární soubory, kromě toho, že podporují možnost `-ipcbind` (viz zpravodaj
  [#320] [News320 IPC]), ale budoucí vylepšení umožní běžci uzlů
  Spusťte a zastavte komponenty nezávisle na různých strojích a
  prostředí. Viz [Newsletter #353] [News353 PR recenze] pro bitcoinové jádro PR
  Recenze klubu pokrývající tento PR.

- [BIPS #1483] [] Sloučení [BIP77] [], který navrhuje [payjoin v2] [téma Payjoin], an
  Asynchronní varianta bez serverů, ve které odesílatel a přijímač předává jejich
  Šifrované PSBTS na server PayJoin adresář, který pouze ukládá a dopředu
  zprávy. Protože adresář nemůže číst nebo měnit užitečná zatížení, ani peněženka
  musí hostit veřejný server nebo být online současně. Viz zpravodaj
  [#264] [News264 PayJoin] za další kontext na PayJoin V2.

{ % zahrnuje úryvky/recap-ad.md, když = "2025-06-10 16:30" %}
{ % zahrnuje reference.md %}
{ % zahrnuje linkers/issues.md v = 2 vydání = "32582,31375,1483" %}
[Core Lightning 25.05RC1]: https://github.com/elementsproject/lightning/releases/tag/v25.05rc1
[Ztráta zvlnění]: https://x.com/joelkatz/status/1919233214750892305
[SK nowit]: https://delvingbitcoin.org/t/witnessless-Syn-for-Pruned-nodes/1742/
[SK nowit gist]: https://gist.github.com/josesk999/df0a2a014c7d9b626df1e2b19ccc7fb1
[Somsen Nowit]: https://gist.github.com/josesk999/df0a2a014C7D9B626DF1E2B19CCC7FB1?PERMALINK_COMMENT_ID=5597316#GISTCOMENT-5597316
[Shikelman Quantum]: https://delvingbitcoin.org/t/bitcoin-and-quantum-computing/1730/
[SM Report]: https://chaincode.com/bitcoin-post-quantum.pdf
[STRNAD limit]: https://delvingbitcoin.org/t/non-confiscatory-transaction-weight-limit/1732/
[Problém s bazénem]: https://en.wikipedia.org/wiki/knapsack_problem
[Limit Sanders]: https://delvingbitcoin.org/t/non-confiscatory-transaction-weight-limit/1732/2
[Limit Maxwell]: https://delvingbitcoin.org/t/non-confiscatory-transaction-weight-limit/1732/4
[Linus Dust]: https://delvingbitcoin.org/t/dust-expiry-clean-the-utxo-set-from-spam/1707/

[lnd 0.19.1-beta.rc1]: https://github.com/lightningnetwork/lnd/releases/tag/v0.19.1-beta.rc1
[News315 Compact]:/en/zpravodaje/2024/08/09/#Statistika-on-Compact-Block-Reconstruction
[Projekt Multiprocess]: https://github.com/ryanofsky/bitcoin/blob/pr/ipc/doc/design/multiprocess.md
[News320 IPC]:/en/zpravodaje/2024/09/13/#bitcoin-core-30509
[News264 payjoin]:/en/zpravodaje/2023/08/16/#serverless-payjoin
[News353 PR recenze]:/en/zpravodaje/2025/05/09/#bitcoin-core-PR-review-Club
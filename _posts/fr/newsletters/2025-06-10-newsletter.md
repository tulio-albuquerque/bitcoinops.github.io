---
title: 'Bitcoin Optech Newsletter #357'
permalink: /en/newsletters/2025/06/06/
name: 2025-06-06-newsletter
slug: 2025-06-06-newsletter
type: newsletter
layout: newsletter
lang: en
---
La newsletter de cette semaine partage une analyse sur la synchronisation des nœuds complets
sans vieux témoins.  Sont également inclus nos sections régulières avec
Descriptions des discussions sur la modification du consensus, des annonces de
Nouvelles versions et relâchez des candidats, et des résumés de changements notables
Logiciel populaire d'infrastructure Bitcoin.

## Nouvelles

- ** Synchronisation des nœuds complets sans témoins: ** jose sk [posté] [Sk Nowit]
  Pour plonger le bitcoin un résumé d'une [analyse] [sk nowit gist] il
  effectué sur les compromis de sécurité de l'autorisation nouvellement démarrée
  nœuds avec une configuration particulière pour éviter de télécharger certains
  Données historiques de la blockchain.  Par défaut, les nœuds de noyau bitcoin utilisent le
  Paramètre de configuration `AssuMevalid` qui saute la validation des scripts
  en blocs créés plus d'un mois ou deux avant la libération du
  Version du noyau Bitcoin en cours d'exécution.  Bien que handicapé par défaut, beaucoup
  Les utilisateurs de Bitcoin Core définissent également un paramètre de configuration «prune»
  Supprime les blocs un peu de temps après les valider (combien de temps les blocs sont
  maintenu dépend de la taille des blocs et du paramètre spécifique sélectionné
  par l'utilisateur).

  SK fait valoir que les données des témoins, qui ne sont utilisées que pour valider
  Les scripts ne doivent pas être téléchargés par des nœuds élagués pour AssuMevalid
  blocs car ils ne l'utiliseront pas pour valider les scripts et
  supprimez-le finalement.  Sauter Télécharger le témoin "peut couper
  Utilisation de la bande passante de plus de 40% ", écrit-il.

  Ruben Somsen [plaide] [Somsen Nowit] que cela change la sécurité
  modèle dans une certaine mesure.  Bien que les scripts ne soient pas validés, le
  Les données téléchargées sont validées par rapport à l'engagement du bloc
  En-tête Merkle rooter à la transaction Coinbase aux données des témoins.
  Cela garantit que les données étaient disponibles et non corrompues au moment
  Le nœud a été initialement synchronisé.  Si personne ne valide régulièrement le
  existence des données, elle pourrait être perdue, comme [a
  s'est produit] [perte d'entraînement] contre au moins un altcoin.

  La discussion a été en cours au moment de la rédaction.

## Modification du consensus

_ Une section mensuelle résumant les propositions et la discussion sur le changement
Règles de consensus de Bitcoin._

- ** Rapport informatique quantique: ** Clara Shikhelman [Publié] [Shikelman
  quantum] pour déviner le bitcoin le résumé d'un [rapport] [rapport SM] elle
  co-écrit avec Anthony Milton sur les risques pour les utilisateurs de Bitcoin de
  Ordinateurs quantiques rapides, un aperçu de plusieurs voies vers [quantum
  résistance] [résistance quantique du sujet] et une analyse des compromis
  impliqué dans la mise à niveau du protocole Bitcoin.  Les auteurs trouvent 4 à 10
  Les millions de BTC sont potentiellement vulnérables au vol quantique, certains
  L'atténuation est maintenant possible, la mine de bitcoin est peu susceptible d'être
  menacé par l'informatique quantique à court ou à moyen terme, et
  La mise à niveau nécessite un accord généralisé.

- ** Limite de poids de transaction avec exception pour éviter la confiscation: **
  Vojtěch strnad [posté] [limite de strnad] au bitcoin à proposer
  L'idée d'un changement de consensus pour limiter le poids maximum de la plupart
  transactions dans un bloc.  La règle simple ne permettrait qu'une transaction
  supérieur à 400 000 unités de poids (100 000 vbytes) dans un pâté de maisons si elle était
  La seule transaction dans ce bloc en plus de la transaction Coinbase.
  Strnad et d'autres ont décrit la motivation pour limiter le maximum
  Poids de la transaction:

  - _Easier Optimisation du modèle de bloc: _ Il est plus facile de trouver un
    solution presque optimale au [problème de sac à dos] [] Plus le petit
    Les articles sont comparés à la limite globale.  C'est en partie
    en raison de la minimisation de la quantité d'espace restant à la fin, avec
    Des articles plus petits laissant un espace moins inutilisé.

  - _Easier Relais Politique: _ La politique de relayation non confirmée
    Les transactions entre les nœuds prédisent quelles transactions seront
    exploité afin d'éviter de gaspiller la bande passante.  Les transactions géantes font
    des prédictions précises plus difficiles car même un petit changement dans le haut feeate peut provoquer
    pour être retardés ou expulsés.

  - _évocation de la centralisation de l'exploitation: _ Assurer le relais des nœuds complets sont
    capable de gérer presque toutes les transactions empêche les utilisateurs de
    Transactions de la nécessité de payer [frais hors bande] [Sujet
    Frais hors bande], ce qui peut conduire à une centralisation miniers.

  Gregory Sanders [noté] [limite Sanders] Il pourrait être raisonnable de
  Fork simplement doux une limite de poids maximale sans aucune exception basée
  sur les 12 années de politique de relais cohérente de Bitcoin Core.  Grégoire
  Maxwell [ajouté] [limite maxwell] qui transactions les dépenses uniquement UTXOS
  créé avant que la fourche souple puisse être autorisée à éviter
  confiscation, et qu'une [fourchette douce transitoire] [sujet transitoire doux
  Forks] permettrait à la restriction d'expirer si le
  La communauté a décidé de ne pas le renouveler.

  Discussion supplémentaire a examiné les besoins des parties souhaitant
  de grandes transactions, principalement [Bitvm] [Sujet ACC] utilisateurs à court terme,
  et si des approches alternatives étaient à leur disposition.

- ** Suppression des sorties de l'ensemble UTXO en fonction de la valeur et du temps: ** Robin

Linus [Publié] [Linus Dust] pour plonger le bitcoin pour proposer une fourchette douce
  pour éliminer les sorties de faible valeur de l'ensemble UTXO après certains
  temps.  Plusieurs variations de l'idée ont été discutées, avec les deux
  Les principales alternatives étant:

  - _destroy de vieux fonds non économiques: _ SPORTIONS DE PETIT
    été dépensé depuis longtemps deviendrait infondable.

  - _Require les anciens fonds non économiques à dépenser avec une preuve d'existence: _
    [utreexo] [Sujet utreexo] ou un système similaire pourrait être utilisé pour permettre
    Une transaction pour prouver que les sorties qu'il dépense fait partie du
    Set utxo.  Sorties anciennes et [non économiques] [Sujet Sorties non économiques]
    besoin d'inclure cette preuve, mais les sorties plus récentes et plus élevés
    être toujours stocké dans l'ensemble UTXO.

  L'une ou l'autre solution limiterait efficacement la taille maximale de l'UTXO
  Définir (en supposant une valeur minimale et la limite de 21 millions de bitcoins).
  Plusieurs aspects techniques intéressants d'une conception ont été discutés,
  y compris des alternatives aux preuves utreexo pour cette application qui
  pourrait être plus pratique.

## Sortie et relâchez les candidats

_New publie et relâchez les candidats pour une infrastructure bitcoin populaire
projets.  Veuillez envisager de passer à de nouvelles versions ou d'aider à tester
libérer les candidats._

- [Core Lightning 25.05rc1] [] est un candidat à la publication pour la prochaine majeure
  Version de cette populaire implémentation de nœud LN.

- [LND 0.19.1-beta.rc1] [] est un candidat à la libération pour un entretien
  Version de cette populaire implémentation de nœud LN.

## Code notable et modifications de documentation

_ Changements récents récent dans [Bitcoin Core] [Bitcoin Core Repo], [Core
Lightning] [Core Lightning Repo], [Eclair] [Eclair Repo], [LDK] [LDK Repo],
[LND] [LND Repo], [LiBSecp256K1] [Rebsecp256K1 Repo], [portefeuille matériel
Interface (HWI)] [HWI Repo], [Rust Bitcoin] [Rust Bitcoin Repo], [BTCPAY
Serveur] [BTCPay Server Repo], [BDK] [BDK Repo], [Bitcoin Amélioration
Propositions (BIPS)] [Repo Bips], [Lightning Bolts] [REPO BOLTS],
[Lightning Blips] [Blips Repo], [Bitcoin Inquisition] [Bitcoin Inquisition
repo], et [binanas] [binana repo] ._

- [Bitcoin Core # 32582] [] ajoute une nouvelle journalisation pour mesurer les performances de
  [Reconstruction compacte du bloc] [Relais de blocs compacts du sujet] en suivant le
  Taille totale des transactions qu'un nœud demande à ses pairs
  (`getblocktxn`), le nombre et la taille totale des transactions qu'un nœud envoie
  à ses pairs (`blocktxn`), et ajoutant un horodatage au début de
  `Partiellement downloadedblock :: initdata ()` pour suivre la durée de la recherche de mempool
  L'étape seule prend (dans les modes de largeur de bande haute et de faible bande passante). Voir newsletter
  [# 315] [News315 Compact] pour un rapport de statistiques précédent sur le bloc compact
  reconstruction.

- [Bitcoin Core # 31375] [] Ajoute un nouvel outil CLI `Bitcoin -M` qui s'enroule et
  Exécute le [multiprocesse] [Projet multiprocesse] Binaires «Bitcoin Node»
  (`BitCoind`),` Bitcoin Gui` (`Bitcoinqt`),` Bitcoin RPC` (`Bitcoin-Cli
  -named`). Actuellement, ces fonctions de la même manière que le monolithique
  Binaires, sauf qu'ils soutiennent l'option «-ipcbind» (voir la newsletter
  [# 320] [News320 IPC]), mais les améliorations futures permettront à un coureur de nœud de
  Démarrer et arrêter les composants indépendamment sur différentes machines et
  environnements. Voir [Newsletter # 353] [News353 PR Review] pour un PR Bitcoin Core PR
  Club de révision couvrant ce PR.

- [BIPS # 1483] [] fusionne [bip77] [] qui propose [Payjoin v2] [
  variante asynchrone sans serveur dans laquelle l'expéditeur et le récepteur remettent leur
  PSBS cryptant à un serveur d'annuaire de paiement qui ne stocke et transmet que
  messages. Comme le répertoire ne peut pas lire ou modifier les charges utiles, ni le portefeuille
  Doit héberger un serveur public ou être en ligne en même temps. Voir newsletter
  [# 264] [News264 Payjoin] Pour un contexte supplémentaire sur Payjoin v2.

{% Incluent des extraits / récapitulatif-ad.md quand = "2025-06-10 16:30"%}
{% Inclure des références.md%}
{% Inclure les lieurs / problèmes.md v = 2 problèmes = "32582,31375,1483"%}
[Core Lightning 25.05rc1]: https://github.com/elementsproject/lightning/releases/tag/v25.05rc1
[Perte Ripple]: https://x.com/joelkatz/status/1919233214750892305
[Sk Nowit]: https://delvingbitcoin.org/t/witnessless-sync-for-puned-nodes/1742/
[Sk Nowit Gist]: https://gist.github.com/josesk999/df0a2a014c7d9b626df1e2b19cccc7fb1
[Somsen Nowit]: https://gist.github.com/jossk999/df0a2a014c7d9b626df1e2b19ccc7fb1?permalink_comment_id=5597316#gistcomment-5597316
[Shikelman Quantum]: https://delvingbitcoin.org/t/bitcoin-and-quantum-computing/1730/
[Rapport SM]: https://chaincode.com/bitcoin-post-quantum.pdf
[Strnad Limit]: https://delvingbitcoin.org/t/non-confiscatory-transaction-weight-limit/1732/
[Problème de sac à dos]: https://en.wikipedia.org/wiki/knapsack_problemband
[Limite Sanders]: https://delvingbitcoin.org/t/non-confiscatory-transaction-weight-limit/1732/2
[MAXWELL LIMIT]: https://delvingbitcoin.org/t/non-confiscatory-transaction-weight-limit/1732/4
[Linus Dust]: https://delvingbitcoin.org/t/dust-expiry-clean-the-utxo-set-from-spam/1707/

[lnd 0.19.1-beta.rc1]: https://github.com/lightningwork/lnd/releases/tag/v0.19.1-beta.rc1
[News315 Compact]: / en / newsletters / 2024/08/09 / # Statistics-on-Compact-bloc-reconstitution
[Projet multiprocesse]: https://github.com/ryanofsky/bitcoin/blob/pr/ipc/doc/design/multiprocess.md
[news320 ipc]: / en / newsletters / 2024/09/13 / # bitcoin-core-30509
[news264 payjoin]: / en / newsletters / 2023/08/16 / # Serverless-Payjoin
[News353 PR Review]: / en / newsletters / 2025/05/09 / # bitcoin-core-pr-review-club
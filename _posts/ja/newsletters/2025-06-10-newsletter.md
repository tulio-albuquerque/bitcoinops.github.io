---
title: 'Bitcoin Optech Newsletter #357'
permalink: /en/newsletters/2025/06/06/
name: 2025-06-06-newsletter
slug: 2025-06-06-newsletter
type: newsletter
layout: newsletter
lang: en
---
今週のニュースレターは、完全なノードの同期に関する分析を共有しています
古い証人なしで。  また、通常のセクションも含まれています
コンセンサスの変化に関する議論の説明、の発表
候補者の新しいリリースとリリース、および顕著な変更の要約
人気のあるビットコインインフラストラクチャソフトウェア。

＃＃ ニュース

 -  **目撃者なしで完全なノードを同期する：** Jose SK [投稿] [Sk Nowit]
  [分析] [Sk nowit gist]の概要をビットコインに掘り下げる
  新しく開始できるようにするセキュリティトレードオフについて実行されました
  いくつかのダウンロードを避けるために、特定の構成を備えたノード
  歴史的なブロックチェーンデータ。  デフォルトでは、ビットコインコアノードはを使用します
  スクリプトの検証をスキップする「Asmavalid」設定
  ブロックでは、
  実行中のビットコインコアのバージョン。  デフォルトでは無効になっていますが、多く
  Bitcoin Coreのユーザーは、「Prune」設定も設定しています
  削除は、それらを検証した後しばらくブロックします（ブロックはどれくらいですか
  維持は、ブロックのサイズと選択された特定の設定に依存します
  ユーザーによって）。

  SKは、検証にのみ使用される証人データを主張します
  スクリプトは、assevalid用のプルーネドノードでダウンロードしないでください
  彼らはスクリプトを検証するためにそれを使用しないのでブロックします
  最終的に削除します。  目撃者のダウンロードをスキップする「カットできます
  帯域幅の使用は40％以上です」と彼は書いています。

  ルーベン・ソムセン[主張] [ソムセン・ノウィット]これがセキュリティを変えること
  ある程度モデル。  スクリプトは検証されていませんが、
  ダウンロードされたデータは、ブロックからのコミットメントに対して検証されます
  ヘッダーマークルルートは、証人データへのコインベーストランザクションです。
  これにより、データが利用可能であり、腐敗していないことが保証されます。
  ノードは最初に同期されました。  誰も日常的に検証しない場合
  データの存在、それはおそらく失われる可能性があります[
  起こった] [リップル損失]少なくとも1つのAltcoinに。

  議論は執筆時点で進行中でした。

##コンセンサスの変更

_A毎月のセクションの要約提案と変更に関する議論
ビットコインのコンセンサスルール。_

 -  ** Quantum Computing Report：** Clara Shikhelman [投稿] [Shikelman
  Quantum]ビットコインに[レポート] [SMレポート]の概要を掘り下げる
  のビットコインユーザーへのリスクについて、アンソニーミルトンと共著
  高速量子コンピューター、[Quantumへのいくつかの経路の概要
  抵抗] [トピック量子抵抗]、およびトレードオフの分析
  ビットコインプロトコルのアップグレードに関与します。  著者は4〜10を見つけます
  100万のBTCは、量子盗難に対して脆弱な可能性があります
  現在緩和が可能です、ビットコインマイニングはそうではありません
  短期的または中期的に量子コンピューティングによって脅かされ、
  アップグレードには、広範な契約が必要です。

 -  **没収を防ぐための例外を除いてトランザクションの重量制限：**
  vojtěchstrnad [sust] [strnad lime]を提案するためにビットコインを掘り下げます
  コンセンサスの変更のアイデアは、ほとんどの最大重量を制限する
  ブロック内のトランザクション。  単純なルールでは、トランザクションのみが許可されます
  ブロック内の400,000の重量単位（100,000 Vbytes）を超える
  コインベーストランザクション以外に、そのブロックでの唯一のトランザクション。
  strnadと他の人たちは、最大を制限する動機を説明しました
  トランザクションの重み：

   -  _ easierブロックテンプレート最適化：_見つける方が簡単です
    [ナップサックの問題] []が小さいほど最適に近いソリューションが小さくなります
    アイテムは全体の制限と比較されます。  これは部分的です
    最後に残っているスペースの量を最小限に抑えるために
    未使用のスペースが少ない小さなアイテム。

  -_EASIERリレーポリシー：_未確認のリレーのポリシー
    ノード間のトランザクションは、トランザクションがどのようなものになるかを予測します
    帯域幅を無駄にしないように採掘されました。  巨大なトランザクションが作成されます
    最上部の給油の小さな変化でさえも引き起こす可能性があるため、正確な予測はより硬くなります
    それらは遅れたり追い出されたりします。

   -  _マイニング集中化の廃止：_完全なノードを中継することを保証します
    ほぼすべてのトランザクションを処理できることで、特別なユーザーが妨げられます
    [帯域外料金] [トピック] [バンド外料金]の支払いの必要性からの取引
    鉱山の集中化につながる可能性のあるバンド外の手数料]。

  グレゴリー・サンダース[記録] [サンダースの制限]それは合理的かもしれません
  単にソフトフォークは、例外なく最大重量制限です
  Bitcoin Coreの12年間の一貫したリレーポリシーについて。  グレゴリー
  Maxwell [追加] [Maxwell Limit]は、トランザクションがUTXOSのみを支出するものです
  ソフトフォークが例外を防ぐ前に作成された
  没収、および[一時的なソフトフォーク] [トピックトロマリーソフト
  フォーク]は、制限が期限切れになることを許可します
  コミュニティはそれを更新しないことにしました。

  追加の議論では、当事者のニーズが求められていました
  大規模なトランザクション、主に[BITVM] [トピックACC]近い将来のユーザー、
  そして、代替アプローチが利用可能かどうか。

 -  **価値と時間に基づいてUTXOセットから出力を削除：**ロビン

linus [sosts] [linus dust]柔らかいフォークを提案するためにビットコインを掘り下げます
  いくつかの後にUTXOセットから低価値の出力を削除するため
  時間。  アイデアに関するいくつかのバリエーションが議論され、2つで議論されました
  主な代替案は次のとおりです。

   -  _Destroy Old Uneconomic Funds：_
    長い間費やされていたのは、dendめられないでしょう。

   -  _存在の証明で使われる古い不経済の資金を再Quire：_
    [utreexo] [トピックutreexo]または同様のシステムを使用して許可することができます
    それが費やす出力がの一部であることを証明するためのトランザクション
    utxoセット。  古い[非経済的出力] [トピック非経済的出力]はそうします
    この証明を含める必要がありますが、より新しい価値のある出力は
    まだUTXOセットに保管されています。

  どちらの解決策も、UTXOの最大サイズを効果的に制限します
  設定（最小値と2100万のビットコイン制限を仮定）。
  デザインのいくつかの興味深い技術的側面が議論されました、
  このアプリケーションのUtreexo証明の代替案を含む
  より実用的かもしれません。

##候補者のリリースとリリース

_New人気のあるビットコインインフラストラクチャの候補者をリリースおよびリリースします
プロジェクト。  新しいリリースへのアップグレードやテストの支援を検討してください
候補者を解放します。_

 -  [Core Lightning 25.05RC1] []は次のメジャーのリリース候補です
  この人気のあるLNノード実装のバージョン。

 -  [LND 0.19.1-Beta.rc1] []はメンテナンスのリリース候補です
  この人気のあるLNノード実装のバージョン。

##注目すべきコードとドキュメントの変更

_ [Bitcoin Core] [Bitcoin Core Repo]、[Core]、[Core
Lightning] [Core Lightning Repo]、[Eclair] [Eclair Repo]、[LDK] [LDK Repo]、
[LND] [LND Repo]、[libsecp256k1] [libsecp256k1 repo]、[ハードウェアウォレット
インターフェイス（HWI）] [HWI Repo]、[Rust Bitcoin] [Rust Bitcoin Repo]、[btcpay
サーバー] [btcpay server repo]、[bdk] [bdk repo]、[bitcoinの改善
提案（BIPS）] [BIPS REPO]、[Lightning Bolts] [Bolts Repo]、
[Lightning Blips] [Blips Repo]、[Bitcoin Inquisition] [Bitcoin Inquisition
repo]、および[binanas] [binana repo] ._

 -  [Bitcoin Core＃32582] []は、の新しいロギングを追加してパフォーマンスを測定します
  [コンパクトブロック再構築] [トピックコンパクトブロックリレー]を追跡します
  ノードがピアから要求するトランザクションの合計サイズ
  （ `getblocktxn`）、ノードが送信するトランザクションの数と総サイズ
  その仲間（ `blocktxn`）に、そしての開始時にタイムスタンプを追加する
  `部分的にダウンロードされたブロック:: initdata（）` Mempool Lookupの長さを追跡します
  ステップだけで（高帯域幅モードと低帯域幅モードの両方）。ニュースレターを参照してください
  [＃315] [News315 Compact]コンパクトブロックに関する以前の統計レポートの場合
  再建。

 -  [Bitcoin Core＃31375] []は、ラップして新しい `Bitcoin -M` CLIツールを追加します。
  [MultiProcess] [MultiProcess Project]バイナリ「ビットコインノード」を実行します
  （ `bitcoind`）、` bitcoin gui`（ `bitcoinq`）、 `bitcoin rpc`（` bitcoin-cli
  -Named`）。現在、これらはモノリシックと同じ方法で機能します
  バイナリは、「-ipcbind`オプションをサポートしています（ニュースレターを参照してください
  [＃320] [News320 IPC]）、しかし将来の改善により、ノードランナーが
  さまざまなマシンでコンポーネントを独立して開始および停止します
  環境。ビットコインコアPRについては[Newsletter＃353] [News353 PR Review]を参照してください
  このPRをカバーするクラブをレビューします。

 -  [bips＃1483] []合併[bip77] []
  送信者と受信者がそれらを渡す非同期サーバーレスバリアント
  保存および転送のみを保存してPayjoinディレクトリサーバーに暗号化したPSBTS
  メッセージ。ディレクトリはペイロードを読み取ったり変更したりできないため、どちらのウォレットもありません
  パブリックサーバーをホストするか、同時にオンラインである必要があります。ニュースレターを参照してください
  [＃264] [News264 Payjoin] Payjoin V2の追加コンテキストについて。

{％snippets/racap-ad.mdを含むwhen = "2025-06-10 16:30"％}
{％include references.md％}
{％Linkers/Issues.md V = 2 Issues = "32582,31375,1483"％}を含む
[Core Lightning 25.05RC1]：https：//github.com/elementsproject/lightning/releases/tag/v25.05rc1
[リップル損失]：https：//x.com/joelkatz/status/191923214750892305
[Sk nowit]：https：//delvingbitcoin.org/t/witnessless-sync-for-pruned-nodes/1742/
[SK Nowit Gist]：https：//gist.github.com/josesk999/df0a2a014c7d9b626df1e2b19ccc7fb1
[somsen nowit]：https：//gist.github.com/josesk999/df0a2a014c7d9b626df1e2b19ccc7fb1？permalink_comment_id = 5597316#gistcomment-559316
[Shikelman Quantum]：https：//delvingbitcoin.org/t/bitcoin-and-quantum-computing/1730/
[SMレポート]：https：//chaincode.com/bitcoin-post-quantum.pdf
[strnad lime]：https：//delvingbitcoin.org/t/non-confiscatory-transaction-weight-limit/1732/
[Knapsackの問題]：https：//en.wikipedia.org/wiki/knapsack_problem
[Sanders Limit]：https：//delvingbitcoin.org/t/non-confiscatory-transaction-weight-limit/1732/2
[Maxwell Limit]：https：//delvingbitcoin.org/t/non-confiscatory-transaction-weight-limit/1732/4
[Linus Dust]：https：//delvingbitcoin.org/t/dust-expiry-clean-the-utxo-set-from-spam/1707/

[LND 0.19.1-Beta.rc1]：https：//github.com/lightningnetwork/lnd/releases/tag/v0.19.1-beta.rc1
[News315 Compact]：/en/Newsletters/2024/08/09/＃Statistics-on-compact-block-Reconstruction
[MultiProcess Project]：https：//github.com/ryanofsky/bitcoin/blob/pr/ipc/doc/design/multiprocess.md
[News320 IPC]：/en/Newsletters/2024/09/13/＃Bitcoin-Core-30509
[News264 Payjoin]：/en/newsletters/2023/08/16/＃serverless-payjoin
[News353 PRレビュー]：/en/Newsletters/2025/05/09/＃Bitcoin-Core-PR-Review-Club
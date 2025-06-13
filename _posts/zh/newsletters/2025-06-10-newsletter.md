---
title: 'Bitcoin Optech Newsletter #357'
permalink: /en/newsletters/2025/06/06/
name: 2025-06-06-newsletter
slug: 2025-06-06-newsletter
type: newsletter
layout: newsletter
lang: en
---
本週的新聞通訊分享了有關同步完整節點的分析
沒有舊證人。  還包括我們的常規部分
關於改變共識的討論的描述，公告
新發布和發布候選人，以及明顯更改的摘要
流行的比特幣基礎架構軟件。

＃＃ 消息

 -  **無目擊者同步完整節點：** Jose SK [Post] [SK Nowit]
  探究比特幣的摘要[分析] [SK Nowit Gist]
  關於允許新完成的安全權衡執行
  帶有特定配置的節點以避免下載一些
  歷史性區塊鏈數據。  默認情況下，比特幣核心節點使用
  `pushvalid`配置設置，跳過腳本驗證
  在發布之前創建了一個或兩個多月之前
  比特幣核心的版本正在運行。  儘管默認情況下是禁用的，但
  比特幣核心的用戶還設置了“修剪”配置設置
  刪除驗證後的某個時間（塊有多長時間）
  保留取決於塊的大小和選定的特定設置
  由用戶）。

  SK認為僅用於驗證的證人數據
  腳本，不應由pushvalid的修剪節點下載
  塊是因為他們不會將其用於驗證腳本，並且會
  最終將其刪除。  跳過證人下載“可以剪切
  帶寬的用法超過40％，”他寫道。

  Ruben Somsen [爭論] [Somsen Nowit]這改變了安全性
  在某種程度上模型。  儘管腳本未驗證，但
  下載的數據已根據塊的承諾驗證
  標題Merkle根直到共同的交易到證人數據。
  這確保了數據可用並在
  節點最初是同步的。  如果沒有人經常驗證
  數據的存在，可以想像它可以丟失，因為
  發生了] [連鎖損失]至少一個Altcoin。

  在寫作時進行了討論。

##更改共識

_a每月部分匯總建議和有關更改的討論
比特幣的共識規則。

 -  **量子計算報告：** Clara Shikhelman [發布] [Shikelman
  量子]探究比特幣的摘要[報告] [SM報告]
  與安東尼·米爾頓（Anthony Milton）合著了有關比特幣使用者的風險
  快速量子計算機，概述[量子的幾種途徑
  阻力] [主題量子阻力]和對權衡的分析
  參與升級比特幣協議。  作者發現4至10
  百萬BTC可能容易受到量子盜竊的影響，有些
  現在可以緩解，比特幣採礦不太可能
  在短期或中期受到量子計算的威脅，
  升級需要廣泛的協議。

 -  **交易重量限制有例外以防止沒收：**
  vojtěchstrnad [post] [strnad限制]鑽探比特幣
  共識變化的想法以限制大多數的最大重量
  交易中的交易。  簡單的規則只允許交易
  如果是
  除Coinbase交易以外，該塊中唯一的交易。
  斯特納德（Strnad）和其他人描述了限制最大值的動機
  交易重量：

   -  _easier塊模板優化：_更容易找到一個
    [背包問題] [] [] [] [] []
    將項目與整體限制進行比較。  這部分是
    由於降低了末端留下的空間數量，
    較小的物品留下了較少的未使用空間。

   -  _easier繼電器策略：_未經證實的中繼的政策
    節點之間的交易預測什麼是交易
    開採以避免浪費帶寬。  巨型交易
    精確的預測更加困難，因為甚至最高的變化可能會導致
    他們被延遲或驅逐。

   -  _避免採礦集中化：_確保傳遞完整節點為
    能夠處理幾乎所有交易都可以阻止特殊用戶
    需要支付[帶外費用]的交易[主題
    帶外費用]，這可能導致採礦集中化。

  Gregory Sanders [註明] [桑德斯限制]
  簡單地叉一個最大重量限製而無需任何例外
  關於比特幣核心的12年一致的中繼政策。  格雷戈里
  麥克斯韋[添加] [麥克斯韋限制]交易僅支出UTXO
  在軟叉之前創建一個例外，以防止
  沒收，並且[暫時軟叉] [主題暫時軟
  叉]如果限製到期
  社區決定不續簽它。

  其他討論研究了想要的當事方的需求
  大型交易，主要是[BITVM] [主題ACC]在短期內
  以及是否可以使用其他方法。

 -  **根據價值和時間從UTXO集中刪除輸出：** Robin

linus [poins] [linus dust]挖掘比特幣以提出柔軟的叉子
  用於從UTXO集中刪除utxo集的低價值輸出
  時間。  討論了這兩個想法的幾種變化
  主要替代方法是：

   -  _ destroy舊的不經濟資金：_沒有的小價值輸出
    花了很長時間將變得不可能。

   -  _require舊的不經濟資金用於存在證明：_
    [utreexo] [主題utreexo]或類似的系統可用於允許
    交易證明其支出的輸出是
    UTXO集。  舊的和[不經濟的輸出] [主題不經濟輸出]將
    需要包含此證明，但是更新和更高價值的輸出將
    仍然存儲在UTXO集中。

  兩種解決方案都可以有效地限制UTXO的最大尺寸
  設置（假設最低值和2100萬比特幣限制）。
  討論了設計的幾個有趣的技術方面，
  在此應用程序中包括utreexo證明的替代方案
  可能更實用。

##發布和發布候選人

_新聞發布並發布流行比特幣基礎設施的候選人
項目。  請考慮升級到新版本或幫助測試
釋放候選人。

 -  [核心閃電25.05rc1] []是下一個專業的釋放候選者
  這個流行的LN節點實現的版本。

 -  [lnd 0.19.1-beta.rc1] []是維護的釋放候選者
  這個流行的LN節點實現的版本。

##著名代碼和文檔更改

_ [比特幣核心] [比特幣核心回購]的最新變化，[核心
閃電] [Core Lightning Repo]，[Eclair] [Eclair Repo]，[LDK] [LDK Repo]，
[lnd] [lnd repo]，[libsecp256k1] [libsecp256k1 repo]，[硬件錢包
界面（HWI）] [HWI回購]，[Rust Bitcoin] [Rust Bitcoin Repo]，[BTCPAY
服務器] [BTCPAY服務器repo]，[BDK] [BDK Repo]，[比特幣改進
提案（BIPS）] [BIPS REPO]，[閃電] [螺栓repo]，
[閃電片] [Blips Repo]，[比特幣詢問] [比特幣詢問
repo]和[binanas] [Binana repo] ._

 -  [比特幣核心＃32582] []添加了新的日誌記錄以測量
  [緊湊型塊重建] [主題緊湊型塊繼電器]通過跟踪
  節點向同行請求的交易總數
  （“ getBlocktxn”），節點發送的交易的數量和總大小
  在其同齡人（`blocktxn`）中，並在開始時添加時間戳
  `部分下載block :: initdata（）`要跟踪MEMPOOL查找多長時間
  單獨採用（以高帶寬模式和低帶寬模式）。請參閱新聞通訊
  [＃315] [news315緊湊型]對於以前的統計報告，關於緊湊型塊
  重建。

 -  [比特幣核心＃31375] []添加了一個新的`比特幣-M`CLI工具，可以包裝和
  執行[Multiprocess] [Multiprocess Project]二進制
  （`bitcoind'），`bitcoin gui'（`bitcoinqt`），`bitcoin rpc`（`bitcoin-cli
   - 命名為“）。目前，這些功能與整體化的方式相同
  二進製文件，除了它們支持`ipcbind`選項（請參閱新聞通訊）
  [＃320] [news320 ipc]），但是未來的改進將使節點跑步者能夠
  在不同的機器上獨立啟動和停止組件，
  環境。有關比特幣核心PR，請參見[新聞通訊＃353] [News353 PR評論]
  評論俱樂部涵蓋此公關。

 -  [BIPS＃1483] []合併[BIP77] []，提出[PAYJOIN V2] [主題Payjoin]，一個
  異步無服務器變體，發件人和接收器將其交付
  將PSBT加密到僅存儲和轉發的Payjoin目錄服務器
  消息。由於目錄無法讀取或更改有效載荷，因此沒有錢包
  需要託管公共服務器或同時在線。請參閱新聞通訊
  [＃264] [News264 Payjoin]有關Payjoin V2的其他上下文。

{％包含片段/recap-ad.md =“ 2025-06-10 16:30”％}
{％include references.md％}
{％include linkers/essess.md v = 2問題=“ 32582,31375,1483”％}
[核心閃電25.05RC1]：https：//github.com/elementsproject/lightning/releases/tag/v25.05rc1
[波紋損失]：https：//x.com/joelkatz/status/1919233214750892305
[sk nowit]：https：//delvingbitcoin.org/t/witnessless-sync-for-pruned-nodes/1742/
[SK Nowit GIST]：https：//gist.github.com/jossk999/df0a2a014c7d9b62626df1e2b19cccc7fb1
[somsen nowit]：https：//gist.github.com/jossk999/df0a2a014c7d9b6262626df1e2b19ccc7fb1?permalink_comment_id = 5597316 #gistcomment-5597316
[Shikelman Quantum]：https：//delvingbitcoin.org/t/bitcoin-and-quantum-computing/1730/
[SM報告]：https：//chaincode.com/bitcoin-post-quantum.pdf
[strnad限制]：https：//delvingbitcoin.org/t/non-confiscoration-transaction-weight-limit/1732/
[knapsack問題]：https：//en.wikipedia.org/wiki/knapsack_problem
[Sanders限制]：https：//delvingbitcoin.org/t/non-confiscoration-transaction-weight-limit/1732/2
[Maxwell限制]：https：//delvingbitcoin.org/t/non-confiscoration-transaction-weight-limit/1732/4
[linus dust]：https：//delvingbitcoin.org/t/dust-expiry-clean-the-the-utxo-set-from-pam/1707/

[lnd 0.19.1-beta.rc1]：https：//github.com/lightningnetwork/lnd/releases/tag/v0.19.1-beta.rc1
[news315 compact]：/en/en/entlempletters/2024/08/09/＃統計 - 統計 - 在compact-block-rectructions
[多進程項目]：https：//github.com/ryanofsky/bitcoin/blob/pr/pr/pr/pr/pr/doc/design/multiprocess.md
[news320 ipc]：/en/en/newsletters/2024/09/13/＃比特幣核-30509
[news264 Payjoin]：/en/en/newsletters/2023/08/16/＃無服務器payjoin
[news353 PR評論]：/en/en/entlempletters/2025/05/09/＃比特幣核-pr-review-club
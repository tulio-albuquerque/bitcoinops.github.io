---
title: 'Bitcoin Optech Newsletter #357'
permalink: /en/newsletters/2025/06/06/
name: 2025-06-06-newsletter
slug: 2025-06-06-newsletter
type: newsletter
layout: newsletter
lang: en
---
O boletim informativo desta semana compartilha uma análise sobre sincronizar nós completos
sem velhas testemunhas.  Também estão incluídas nossas seções regulares com
Descrições de discussões sobre a mudança de consenso, anúncios de
novos lançamentos e lançamento de candidatos e resumos de mudanças notáveis ​​para
Software popular de infraestrutura de Bitcoin.

## Notícias

- ** Sincronizando nós completos sem testemunhas: ** JOSE SK [Postado] [SK Nowit]
  Para investigar o Bitcoin, um resumo de uma [análise] [sk nowit gist] ele
  realizada sobre as compensações de segurança de permitir o início
  nós com uma configuração específica para evitar baixar alguns
  dados históricos da blockchain.  Por padrão, os nós principais do Bitcoin usam o
  `assumevalid` definição de configuração que ignora a validação de scripts
  em blocos criados mais de um mês ou dois antes do lançamento do
  Versão do núcleo de bitcoin sendo executado.  Embora desativado por padrão, muitos
  Os usuários do Bitcoin Core também definem uma configuração de configuração `Prune 'que
  exclui bloqueia algum tempo depois de validá -los (quanto tempo são os blocos
  Mantido depende do tamanho dos blocos e da configuração específica selecionada
  pelo usuário).

  SK argumenta que os dados da testemunha, que são usados ​​apenas para validar
  Scripts, não devem ser baixados por nós podados para assumir
  blocos porque eles não o usarão para validar scripts e irão
  Eventualmente exclua -o.  Pular o download da testemunha "pode ​​cortar
  Uso da largura de banda em mais de 40%", ele escreve.

  Ruben Somsen [argumenta] [Somsen Nowit] que isso muda a segurança
  modelo até certo ponto.  Embora os scripts não sejam validados, o
  Os dados baixados são validados com o compromisso do bloco
  Cabeçalho Merkle Root para a transação Coinbase para os dados da testemunha.
  Isso garante que os dados estivessem disponíveis e não corrompidos no momento em que
  O nó foi inicialmente sincronizado.  Se ninguém validar rotineiramente o
  existência dos dados, pode ser perdido, pois [tem [tem
  aconteceu] [perda de ondulação] para pelo menos um altcoin.

  A discussão estava em andamento no momento da redação.

## alterando o consenso

_ Uma seção mensal resumindo propostas e discussão sobre a mudança
Regras de consenso do Bitcoin._

- ** Relatório de computação quântica: ** Clara Shikhelman [Post] [Shikelman
  Quantum] para investigar o Bitcoin o resumo de um [relatório] [SM Relatório] ela
  co-autor de Anthony Milton sobre os riscos para os usuários de Bitcoin de
  Computadores quânticos rápidos, uma visão geral de vários caminhos para [Quantum
  Resistência] [Resistência quântica do tópico] e uma análise de compensações
  envolvido na atualização do protocolo Bitcoin.  Os autores encontram 4 a 10
  milhões de BTC são potencialmente vulneráveis ​​ao roubo quântico, alguns
  A mitigação agora é possível, é improvável que a mineração de bitcoin seja
  ameaçado pela computação quântica no curto ou médio prazo e
  A atualização requer um contrato generalizado.

- ** Limite de peso da transação com exceção para evitar confisco: **
  Vojtěch strnad [Postado] [Strnad Limit] para desenhar o Bitcoin para propor
  a ideia de uma mudança de consenso para limitar o peso máximo da maioria
  transações em um bloco.  A regra simples permitiria apenas uma transação
  maiores que 400.000 unidades de peso (100.000 vbytes) em um bloco se fosse
  A única transação nesse bloqueio além da transação da moeda.
  Strnad e outros descreveram a motivação para limitar o máximo
  Peso da transação:

  - _Easier Block Model Optimization: _ é mais fácil encontrar um
    solução quase ideal para o [problema da mochila] [] quanto menor o
    Os itens são comparados ao limite geral.  Isso é parcialmente
    devido a minimizar a quantidade de espaço que resta no final, com
    itens menores deixando espaço menos não utilizado.

  - Política de relé deasier: _ A política de retransmitir não confirmada
    As transações entre nós prevê que as transações serão
    minerado para evitar desperdiçar largura de banda.  Transações gigantes fazem
    previsões precisas mais difíceis, pois mesmo uma pequena mudança no topo da fera pode causar
    eles para serem atrasados ​​ou despejados.

  - _avoiding minering centralização: _ garantindo que os nós completos de retransmissão sejam
    capaz de lidar com quase todas as transações impede os usuários de especial
    Transações da necessidade de pagar [taxas fora da banda] [Tópico
    Taxas fora da banda], o que pode levar à centralização de mineração.

  Gregory Sanders [observou] [Limits de Sanders] pode ser razoável
  Simplesmente macio por um limite de peso máximo sem exceções baseadas
  nos 12 anos de política de relé consistentes do Bitcoin Core.  Gregory
  Maxwell [Adicionado] [MAXWELL LIMIT] que transações gastando apenas UTXOS
  criado antes que o garfo macio pudesse ter uma exceção para prevenir
  Confisco, e que um [Fork Soft de transmissão] [Tópico transitório Soft
  garfos] permitiriam que a restrição expirasse se o
  A comunidade decidiu não renová -lo.

  Discussão adicional examinou as necessidades das partes que desejam
  Grandes transações, principalmente [bitvm] [tópico acc] usuários no curto prazo,
  e se abordagens alternativas estavam disponíveis para eles.

- ** Remoção de saídas do conjunto UTXO com base no valor e no tempo: ** Robin

Linus [Postado] [Linus Dust] Para aproveitar o Bitcoin para propor um garfo macio
  para remover saídas de baixo valor do conjunto UTXO após alguns
  tempo.  Várias variações sobre a idéia foram discutidas, com os dois
  Principais alternativas sendo:

  - _Destroy antigos fundos não econômicos: _ Saídas de pequeno valor que não tinham
    Passado por um longo tempo se tornaria indescritível.

  - _Require fundos não econômicos antigos a serem gastos com uma prova de existência: _
    [utreexo] [tópico utreexo] ou um sistema semelhante pode ser usado para permitir
    uma transação para provar que as saídas que gasta fazem parte do
    Utxo set.  Saídas antigas e não econômicas] [saídas não econômicas]
    precisa incluir esta prova, mas saídas mais novas e de maior valor seriam
    ainda será armazenado no conjunto UTXO.

  Qualquer solução limitaria efetivamente o tamanho máximo do UTXO
  Definir (assumindo um valor mínimo e o limite de 21 milhões de bitcoin).
  Vários aspectos técnicos interessantes de um design foram discutidos,
  incluindo alternativas às provas utreexo para este aplicativo que
  pode ser mais prático.

## libera e libere candidatos

_Now lança e libere candidatos para infraestrutura popular de bitcoin
projetos.  Por favor, considere atualizar para novos lançamentos ou ajudar a testar
Libere candidatos._

- [Core Lightning 25.05rc1] [] é um candidato de lançamento para o próximo major
  Versão desta implementação popular de nó LN.

- [LND 0.19.1-beta.rc1] [] é um candidato de liberação para uma manutenção
  Versão desta implementação popular de nó LN.

## Código notável e alterações de documentação

_ Notável mudanças recentes no [Bitcoin Core] [Bitcoin Core Repo], [Core
Lightning] [Core Lightning Repo], [Eclair] [Eclair Repo], [LDK] [LDK Repo],
[LND] [LND REPO], [LIBSECP256K1] [LIBSECP256K1 REPO], [carteira de hardware
Interface (HWI)] [HWI Repo], [Rust Bitcoin] [Rust Bitcoin Repo], [BTCPay
Servidor] [Repo BTCPay Server], [BDK] [BDK Repo], [Melhoria do Bitcoin
Propostas (BIPS)] [BIPS repo], [Bolts Lightning] [Bolts repo],
[Lightning Blips] [Blips Repo], [Bitcoin Inquisition] [Bitcoin Inquisition
repo] e [binanas] [repo Binana] ._

- [Bitcoin Core #32582] [] adiciona um novo registro para medir o desempenho de
  [Reconstrução de blocos compactos] [Relé de bloco compacto de tópico] rastreando o
  Tamanho total das transações que um nó solicita de seus pares
  (`getBlocktxn`), o número e o tamanho total das transações que um nó envia
  a seus colegas (`blocktxn`) e adicionando um registro de data e hora no início de
  `Parcialmente parawownloadedBlock :: initdata ()` Para acompanhar quanto tempo a pesquisa do Mempool
  O passo sozinho toma (nos modos de largura de banda alta e baixa). Veja o boletim informativo
  [#315] [News315 Compact] Para um relatório de estatística anterior sobre bloco compacto
  reconstrução.

- [Bitcoin Core #31375] [] adiciona uma nova ferramenta `bitcoin -m` cli que envolve e
  Executa o [Projeto Multiprocess] [Projeto Multiprocess] Binários `Nó Bitcoin '
  (`bitcoind`),` bitcoin gui` (`bitcoinqt`),` bitcoin rpc` (`bitcoin-cli
  -Named`). Atualmente, estes funcionam da mesma maneira que o monolítico
  Binários, exceto eles apoiam a opção `-Ipcbind` (consulte o boletim informativo
  [#320] [News320 IPC]), mas melhorias futuras permitirão um corredor de nó para
  iniciar e parar componentes independentemente em diferentes máquinas e
  ambientes. Veja [NewsLetter #353] [News353 PR Review] para um Bitcoin Core PR
  Clube de revisão cobrindo este PR.

- [BIPS #1483] [] mescla [bip77] [] que propõe [PayJoin v2] [tópico payjoin], um um
  variante assíncrona sem servidor na qual o remetente e o receptor entregam seus
  PSBTS criptografado para um servidor de diretório PayJoin que apenas armazena e encaminham
  mensagens. Como o diretório não pode ler ou alterar as cargas úteis, nenhuma carteira
  precisa hospedar um servidor público ou ficar online ao mesmo tempo. Veja o boletim informativo
  [#264] [News264 PayJoin] Para um contexto adicional no PayJoin V2.

{ % inclua trechos/recap-ad.md quando = "2025-06-10 16:30" %}
{ % incluir referências.md %}
{ % inclui vinculadores/problemas.md v = 2 questões = "32582.31375.1483" %}
[Core Lightning 25.05RC1]: https://github.com/Elementsproject/lightning/releases/tag/v25.05rc1
[Perda de ondulação]: https://x.com/joelkatz/status/1919233214750892305
[SK Nowit]: https://delvingbitbitcoin.org/t/witnessless-sync-for-pruned-nodes/1742/
[sk nowit gist]: https://gist.github.com/josesk999/df0a2a014c7d9b626df1e2b19ccc7fb1
[Somsen Nowit]: https://gist.github.com/josesk999/df0a2a014c7d9b626df1e2b19ccc7fb1?permalink_comment_id=5597316#gistcomment -5597316
[Shikelman Quantum]: https://delvingbitcoin.org/t/bitcoin-and-quantum-computing/1730/
[SM RELATÓRIO]: https://chaincode.com/bitcoin-post-quantum.pdf
[Strnad Limit]: https://delvingbitbitcoin.org/t/non-confiscatory-transaction-weight-limit/1732/
[Problema do Knapsack]: https://en.wikipedia.org/wiki/knapsack_problem
[Limite de Sanders]: https://delvingbitcoin.org/t/non-confiscatory-transaction-weight-limit/1732/2
[MAXWELL LIMIT]: https://delvingbitcoin.org/t/non-confiscatory-transaction-weight-limit/1732/4
[Linus Dust]: https://delvingbitbitcoin.org/t/dust-expiry-chean-the-utxo-set-from-spam/1707/

[LND 0.19.1-beta.rc1]: https://github.com/lightningnetwork/lnd/releases/tag/v0.19.1-beta.rc1
[News315 Compact]:/pt/boletins/2024/08/09/#estatísticas-no-compacto-Reconstrução
[Projeto Multiprocess]: https://github.com/ryanofsky/bitcoin/blob/pr/ipc/doc/design/multiprocess.md
[NEWS320 IPC]:/EN/Newsletters/2024/09/13/#Bitcoin-core-30509
[News264 PayJoin]:/pt/boletins/2023/08/16/#Serverless-payJoin
[News353 PR Review]:/pt/boletins/2025/05/09/#bitcoin-core-pr-review-club
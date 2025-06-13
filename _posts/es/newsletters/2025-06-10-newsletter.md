---
title: 'Bitcoin Optech Newsletter #357'
permalink: /en/newsletters/2025/06/06/
name: 2025-06-06-newsletter
slug: 2025-06-06-newsletter
type: newsletter
layout: newsletter
lang: en
---
El boletín de esta semana comparte un análisis sobre la sincronización de nodos completos
sin viejos testigos.  También se incluyen nuestras secciones regulares con
Descripciones de las discusiones sobre el consenso cambiante, anuncios de
nuevos lanzamientos y candidatos de liberación, y resúmenes de cambios notables a
Software popular de infraestructura de Bitcoin.

## Noticias

- ** Sincronización de nodos completos sin testigos: ** Jose SK [Publicado] [SK Nowit]
  para desarrollar bitcoin un resumen de un [análisis] [sk Nowit Gist] Él
  realizó sobre las compensaciones de seguridad de permitir la recién iniciada completa
  nodos con una configuración particular para evitar descargar algunos
  Datos históricos de blockchain.  Por defecto, los nodos centrales de bitcoin usan el
  Configuración de configuración de `asumido" que omite la validación de los scripts
  en bloques creados más de un mes o dos antes del lanzamiento del
  Versión de Bitcoin Core que se ejecuta.  Aunque deshabilitado de forma predeterminada, muchos
  Los usuarios de Bitcoin Core también establecen una configuración de configuración `Prune` que
  elimina los bloques de tiempo después de validarlos (cuánto tiempo están los bloques
  mantenido depende del tamaño de los bloques y la configuración específica seleccionada
  por el usuario).

  SK argumenta que los datos de los testigos, que solo se usan para validar
  Los scripts, no deben descargarse mediante nodos podados para AssumeValid
  bloques porque no lo usarán para validar scripts y Will
  eventualmente eliminarlo.  Omitir testigo descargar "puede cortar
  Uso de ancho de banda en más del 40%", escribe.

  Ruben Somsen [argumenta] [Somsen Nowit] que esto cambia la seguridad
  modelo hasta cierto punto.  Aunque los scripts no están validados, el
  Los datos descargados se validan con el compromiso del bloque
  Encabezado Merkle Root a la transacción Coinbase a los datos de los testigos.
  Esto asegura que los datos estuvieran disponibles y no se corromieran en el momento en que el
  El nodo se sincronizó inicialmente.  Si nadie valida rutinariamente el
  existencia de los datos, posiblemente podría perderse, como [ha
  sucedió] [pérdida de ondulación] a al menos un altcoin.

  La discusión estaba en curso al momento de escribir.

## Cambio de consenso

_A sección mensual que resume las propuestas y la discusión sobre el cambio
Reglas de consenso de Bitcoin.

- ** Informe de computación cuántica: ** Clara Shikhelman [Publicado] [Shikelman
  Quantum] Para desarrollar bitcoin el resumen de un [informe] [Informe SM] Ella ella
  coautoría de Anthony Milton sobre los riesgos para los usuarios de Bitcoin de
  computadoras cuánticas rápidas, una descripción general de varias vías a [Quantum
  Resistencia] [Resistencia cuántica del tema], y un análisis de las compensaciones
  involucrado en la actualización del protocolo de bitcoin.  Los autores encuentran de 4 a 10
  millones de BTC son potencialmente vulnerables al robo cuántico, algunos
  La mitigación ahora es posible, es poco probable que la minería de bitcoin sea
  amenazado por la computación cuántica a corto o mediano plazo, y
  La actualización requiere un acuerdo generalizado.

- ** Límite de peso de la transacción con excepción para prevenir la confiscación: **
  Vojtěch Strnad [publicado] [Límite de Strnad] para desarrollar bitcoin para proponer
  la idea de un cambio de consenso para limitar el peso máximo de la mayoría
  transacciones en un bloque.  La regla simple solo permitiría una transacción
  más de 400,000 unidades de peso (100,000 VBytes) en un bloque si era
  La única transacción en ese bloque además de la transacción Coinbase.
  Strnad y otros describieron la motivación para limitar el máximo
  Peso de la transacción:

  - _Esciende la optimización de la plantilla de bloque: _ Es más fácil encontrar un
    Solución casi óptima al [problema de la mochila] [] cuanto más pequeño sea
    Los artículos se comparan con el límite general.  Esto es en parte
    Debido a minimizar la cantidad de espacio que queda al final, con
    Artículos más pequeños que dejan menos espacio no utilizado.

  - _Tiest Política de retransmisión: _ La política para transmitir no confirmado
    Las transacciones entre nodos predicen qué transacciones serán
    minado para evitar desperdiciar ancho de banda.  Las transacciones gigantes hacen
    Predicciones precisas más difíciles, ya que incluso un pequeño cambio en el Feerate superior puede causar
    que se retrasen o desalojen.

  - _ Evaluar la centralización de la minería: _ Asegurar que la retransmisión de los nodos completos sea
    capaz de manejar casi todas las transacciones evitan que los usuarios de especial
    Transacciones de la necesidad de pagar [tarifas fuera de banda] [tema
    Tarifas fuera de banda], que pueden conducir a la centralización minera.

  Gregory Sanders [notado] [Límite de Sanders] podría ser razonable
  Simplemente bifurcado suave un límite de peso máximo sin ninguna excepción basada
  en los 12 años de política de retransmisión consistente de Bitcoin Core.  Gregory
  Maxwell [agregado] [Límite de Maxwell] que las transacciones gastan solo Utxos
  creado antes de que la bifurcación suave podría permitirse una excepción para prevenir
  confiscación, y que una [bifurcación suave transitoria] [Tema Transitorio suave
  horquillas] permitiría que la restricción expire si el
  La comunidad decidió no renovarlo.

  La discusión adicional examinó las necesidades de las partes que desean
  Grandes transacciones, principalmente [bitvm] [tema ACC] usuarios en el corto plazo,
  y si los enfoques alternativos estaban disponibles para ellos.

- ** Eliminar salidas del conjunto UTXO según el valor y el tiempo: ** Robin

Linus [publicado] [Linus Dust] para profundizar Bitcoin para proponer una bifurcación suave
  para eliminar salidas de bajo valor del conjunto UTXO después de algunos
  tiempo.  Se discutieron varias variaciones sobre la idea, con las dos
  Las principales alternativas son:

  - _DestrOY fondos uneconómicos antiguos: _ Pequeños resultados de valor que no
    Se ha gastado durante mucho tiempo que no se podía asombrosar.

  - _ Requerir los viejos fondos uneconómicos que se gastarán con una prueba de existencia: _
    [UTREEXO] [Tema Utreexo] o se podría usar un sistema similar para permitir
    una transacción para demostrar que las salidas que gasta son parte de la
    Utxo Set.  Antiguas y [salidas uneconómicas] [Tema Salidas no económicas]
    Necesita incluir esta prueba, pero las salidas más nuevas y de mayor valor
    Todavía se almacena en el conjunto UTXO.

  Cualquiera de las solución limitaría efectivamente el tamaño máximo del UTXO
  Establecer (suponiendo un valor mínimo y el límite de 21 millones de bitcoin).
  Se discutieron varios aspectos técnicos interesantes de un diseño,
  incluyendo alternativas a las pruebas de Utreexo para esta aplicación que
  podría ser más práctico.

## Lanzamiento y liberación de candidatos

_Neo lanzamiento y lanzamiento de candidatos para la popular infraestructura de bitcoins
proyectos.  Considere la actualización a nuevas versiones o ayudando a probar
Libere candidatos._

- [Core Lightning 25.05RC1] [] es un candidato de lanzamiento para el próximo importante
  Versión de esta popular implementación del nodo LN.

- [LND 0.19.1-beta.rc1] [] es un candidato de liberación para un mantenimiento
  Versión de esta popular implementación del nodo LN.

## Código notable y cambios de documentación

_ Cambios recientes notables en [Bitcoin Core] [Bitcoin Core Repo], [Core
Lightning] [Core Lightning Repo], [Eclair] [Eclair Repo], [LDK] [LDK Repo],
[LND] [LND Repo], [libsecp256k1] [libsecp256k1 repo], [billetera de hardware
Interfaz (hwi)] [repo hwi], [Rust Bitcoin] [Rust Bitcoin Repo], [btcpay
Servidor] [BTCPay Repo del servidor], [BDK] [BDK Repo], [Mejora de bitcoins
Propuestas (Bips)] [Repo de Bips], [Lightning Bolts] [Repo de pernos],
[Lightning Blips] [BLIPS Repo], [Inquisición de Bitcoin] [Inquisición de Bitcoin
repose] y [binanas] [repositorio binana] ._

- [Bitcoin Core #32582] [] agrega un nuevo registro para medir el rendimiento de
  [Reconstrucción de bloques compactos] [Relé de bloques compactos de tema] rastreando el
  Tamaño total de transacciones que un nodo solicita a sus pares
  (`getBlocktxn`), el número y el tamaño total de las transacciones que envía un nodo
  a sus compañeros (`blocktxn`), y agregando una marca de tiempo al comienzo de
  `Parcialmente drogadedBlock :: initData ()` Para rastrear cuánto tiempo la búsqueda de Mempool
  Step solo toma (en modos de ancho de banda alto y bajo). Ver boletín
  [#315] [News315 Compact] para un informe estadístico anterior sobre el bloque compacto
  reconstrucción.

- [Bitcoin Core #31375] [] agrega una nueva herramienta CLI `bitcoin -m` que se envuelve y se envuelve
  Ejecuta los binarios [proyecto multiprocesos] [Multiprocess] `Bitcoin Node`
  (`bitcoind`),` bitcoin gui` (`bitcoinqt`),` bitcoin rpc` (`bitcoin-cli
  -named`). Actualmente, estos funcionan de la misma manera que el monolítico
  binarios, excepto que apoyan la opción `-ipcbind` (ver boletín
  [#320] [News320 IPC]), pero las mejoras futuras habilitarán un corredor de nodo para
  Iniciar y detener los componentes de forma independiente en diferentes máquinas y
  entornos. Ver [Newsletter #353] [News353 PR Review] para un bitcoin nore PR
  Club de revisión que cubre este PR.

- [Bips #1483] [] se fusiona [Bip77] [] que propone [Payjoin V2] [Topic Payjoin], An
  variante asíncrona sin servidor en la que el remitente y el receptor entregan su
  PSBT encriptados a un servidor de directorio de pagos que solo almacena y reenvía
  mensajes. Como el directorio no puede leer o alterar las cargas útiles, ninguna billetera
  necesita alojar un servidor público o estar en línea al mismo tiempo. Ver boletín
  [#264] [News264 Payjoin] para un contexto adicional en Payjoin V2.

{ % incluye fragmentos/recap-ad.md when = "2025-06-10 16:30" %}
{ % incluye referencias.md %}
{ % incluye enlazadores/problemas.md v = 2 problemas = "32582,31375,1483" %}
[Core Lightning 25.05RC1]: https://github.com/elementsproject/lightning/releases/tag/v25.05rc1
[Ripple pérdida]: https://x.com/joelkatz/status/1919233214750892305
[SK Nowit]: https://delvingbitcoin.org/t/witnessless-sync-for-pruned-nodes/1742/
[SK Nowit Gist]: https://gist.github.com/Jossk999/df0a2a014c7d9b626df1e2b19ccc7fb1
)
[Shikelman Quantum]: https://delvingbitcoin.org/t/bitcoin-and-quantum-computing/1730/
[Informe SM]: https://chaincode.com/bitcoin-post-quantum.pdf
[Límite de Strnad]: https://delvingbitcoin.org/t/non-confiscatory-transaction-weight-limit/1732/
[Problema de mochila]: https://en.wikipedia.org/wiki/knapsack_problem
[Límite de Sanders]: https://delvingbitcoin.org/t/non-confiscatory-transaction-weight-limit/1732/2
[Límite de Maxwell]: https://delvingbitcoin.org/t/non-confiscatory-transaction-weight-limit/1732/4
[Linus Dust]: https://delvingbitcoin.org/t/dust-expiry-clean-the-utxo-set-from-spam/1707/

[lnd 0.19.1-beta.rc1]: https://github.com/lightnnnetwork/lnd/releases/tag/v0.19.1-beta.rc1
[News315 Compact]:/en/Newsletters/2024/08/09/#estadística-on-compact-bloque
[Proyecto multiprocesos]: https://github.com/ryanofsky/bitcoin/blob/pr/ipc/doc/design/multiprocess.md
[News320 IPC]:/en/Newsletters/2024/09/13/#bitcoin-core-30509
[News264 Payjoin]:/en/Newsletters/2023/08/16/#Serverless-Payjoin
[News353 PR Review]:/en/Newsletters/2025/05/09/#bitcoin-core-pr-reviswlub
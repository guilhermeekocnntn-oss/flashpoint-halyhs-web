# Análise do pacote Flashpoint

## Conclusão

O SWF principal é `game/halYHS.swf`. A conclusão não se baseia no nome: a descompilação do ActionScript mostra que esse arquivo inicia a configuração e o idioma, carrega a introdução, a interface, os bancos de som e enfileira os módulos de jogo.

Formato do SWF principal: Flash 7 / ActionScript 2, palco 600 × 400, 31 fps, 74 quadros.

## Inventário original preservado em `game/`

| Arquivo | Bytes | Função observada |
|---|---:|---|
| `halYHS.swf` | 23.143 | Orquestrador/entrada principal |
| `config.xml` | 293 | Configuração do sistema; `mainPath` e `gateway` vazios, debug de rede desativado |
| `en.txt` | 744 | Textos em inglês carregados por `Language.loadVariables()` |
| `yamzsound.xml` | 1.841 | Mapa dos bancos de música e efeitos |
| `intro.swf` | 158.211 | Introdução |
| `interface.swf` | 95.456 | Interface, telas e navegação do jogo |
| `game.swf` | 35.985 | Controlador da partida |
| `player.swf` | 118.776 | Personagem/jogador |
| `level1.swf` | 249.037 | Nível 1 |
| `level2.swf` | 268.268 | Nível 2 |
| `level3.swf` | 302.002 | Nível 3 |
| `level4.swf` | 119.667 | Nível 4 |
| `card1.swf` | 56.745 | Tela/cartão do nível 1 |
| `card2.swf` | 71.579 | Tela/cartão do nível 2 |
| `card3.swf` | 58.326 | Tela/cartão do nível 3 |
| `card4.swf` | 60.559 | Tela/cartão do nível 4 |
| `end.swf` | 80.382 | Encerramento |
| `soundmain.swf` | 53.342 | Música/sons da interface |
| `soundgame.swf` | 404.531 | Música e efeitos da partida |
| `tracker.swf` | 30 | SWF mínimo usado para neutralizar/absorver a chamada de tracking |

Não há arquivos de imagem, vídeo, fonte, JSON de jogo ou áudio avulso. Esses recursos estão incorporados nos SWFs; o áudio é distribuído pelos dois SWFs de som.

## Grafo de carregamento confirmado

`halYHS.swf` carrega diretamente, por nomes relativos: `config.xml`, `en.txt`, `yamzsound.xml`, `intro.swf`, `interface.swf`, `soundmain.swf`, `card1.swf` a `card4.swf`, `game.swf`, `soundgame.swf`, `player.swf`, `level1.swf` a `level4.swf` e `end.swf`.

`game.swf` também referencia `player.swf` e os níveis. `yamzsound.xml` aponta para `soundmain.swf` e `soundgame.swf`. A interface forma dinamicamente `level<N>.swf` e chama `tracker.swf?<timestamp>` ao reiniciar.

Há código genérico de loader que contém `gettotalsize.php`, mas nesta execução `serverGet` é definido como `false`; portanto, essa rota não é necessária. Existe também uma referência condicional a `netDebugAlt.swf`, mas `config.xml` define `netDebug=false`, logo o arquivo não é solicitado.

## URLs, APIs e dependências do Flashpoint

Não foi encontrada URL HTTP/HTTPS, domínio antigo ou API externa codificada no pacote. `gateway` e `mainPath` estão vazios. Todos os assets efetivamente usados são relativos e permanecem como arquivos irmãos dentro de `game/`.

A árvore original de captura inclui o host virtual `syd.gamib.com/x/halYHS/`; ele funciona como origem histórica do Flashpoint, mas o código do jogo não depende desse domínio. A cópia web conserva a relação de diretório relevante (todos os arquivos juntos), sem modificar SWFs, XML ou TXT.

O único comportamento ligado a tracking é a carga relativa de `tracker.swf` com query string. O Flashpoint já fornece nesse lugar um SWF mínimo de 30 bytes; ele foi preservado e não envia dados a domínio externo.

## Tamanho e compatibilidade de hospedagem

Os assets do jogo somam menos de 3 MiB, e nenhum arquivo do jogo se aproxima dos limites usuais do GitHub ou Vercel. Os dois binários WebAssembly do Ruffle têm cerca de 14 MiB cada; eles também ficam abaixo do limite individual de 100 MiB do GitHub. O pacote completo fica perto de 33 MiB.

Não é necessário Git LFS. O projeto é totalmente estático e não exige funções serverless.

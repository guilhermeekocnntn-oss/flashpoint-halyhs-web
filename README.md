# Lunchroom Rumble — Ruffle web package

Pacote estático preparado a partir de uma cópia preservada do jogo no Flashpoint.

## Publicação

Envie **o conteúdo desta pasta inteira** para a raiz de um repositório GitHub. No Vercel, importe o repositório como um projeto sem framework e mantenha o diretório raiz padrão. Não há etapa de build.

## Teste local

Sirva esta pasta com um servidor HTTP local e abra a URL informada no navegador. Abrir `index.html` diretamente como `file://` não funciona de forma confiável por causa das regras de carregamento de WebAssembly e dos assets do Flash.

## Estrutura

- `index.html`: página responsiva e inicialização do Ruffle.
- `game/`: SWF principal e todos os assets originais, mantendo os nomes e as relações de caminho.
- `ruffle/`: Ruffle Web 0.5.0 self-hosted oficial.
- `vercel.json`: MIME/cache para WebAssembly e arquivos estáticos.
- `ANALISE.md`: inventário e conclusões técnicas da análise.

O SWF de entrada é `game/halYHS.swf` (Flash 7/ActionScript 2, palco original 600 × 400 a 31 fps).

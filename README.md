# dio-ia-podcast

<p align="center">
<img src="https://yt3.googleusercontent.com/Mf0G-qMMc769O6n1jEOdhYPiuJ_t5khw4BT6jSUuDcW1S8ZBzowZ3weE32UFQ5AsqZktxyDPTg=s160-c-k-c0x00ffffff-no-rj"/>
</p>

Projeto com o objetivo de gerar um podcast utilizando algumas ferramentas de inteligência artificial.

## Breve histórico
<details>
<summary>Clique aqui para expandir</summary>

* Na terceira atividade da terceira parte do bootcamp, chamada "Processos de Treinamento de LLMs", há uma seção chamada "Desafios Computacionais no Treinamento de LLMs", e no segundo vídeo dessa seção, chamado "Projeto Hands-On: Superando Desafios Computacionais", é apresentado um exemplo de geração de voz usando <a href="https://huggingface.co/nari-labs/Dia-1.6B">nari-labs/Dia-1.6B</a>.

* Com o intuito de gerar vozes em português, a princípio adotou-se uma abordagem utilizando <a href="https://github.com/anan235/dia-multilingual/tree/main">dia-multilingual</a>, porém o maior entrave encontrado foi a remoção do arquivo <code>hyperparams.yaml</code> (<a href="https://github.com/anan235/dia-multilingual/issues/5#issuecomment-2830030195">mais detalhes aqui</a>), portanto, foi preciso alterar o TTS que seria utilizado.

* Foi possível obter resultados satisfatórios utilizando uma combinação do Dockerfile do dia-multilingual modificado com o <a href="https://github.com/huggingface/parler-tts">Parler-TTS</a>.

---
</details>

## Como os áudios do podcast são feitos

* A parte que mais demora é a preparação do ambiente; porém, uma vez pronto, é possível gerar quantos áudios forem necessários. Os áudios são gerados localmente para não depender de moedas, tokens e vários outros tipos de limitações impostas quando se utiliza ferramentas de TTS gratuitas online.

* Primeiro, constrói-se a imagem a partir do Dockerfile (assim como no repositório dia-multilingual).

```
docker build -t dia-multilang -f docker/Dockerfile .
```

Depois, gera-se um container a partir dessa imagem.

```
docker run --gpus all -it -p 8000:8000 --name testcontainername dia-multilang
```

E por último, executa-se o script dentro do container (<code>python main.py</code>).

* A partir de então, é gerado o arquivo <code>model.safetensors</code> (formato moderno para modelos de aprendizado profundo).

![Imgur](https://i.imgur.com/VpzR0E3.png)

* O roteiro base é feito no ChatGPT, depois alterado para condizer com o assunto a ser tratado.

* Depois, o roteiro gerado é reinserido no ChatGPT, e finalmente temos as frases que serão convertidas em áudio (como visto no script <code>main.py</code>, na variável <code>prompt</code>).

## Lista de ferramentas utilizadas

* Roteiro: <a href="https://chatgpt.com/">ChatGPT</a>
* Áudio: <a href="https://github.com/huggingface/parler-tts">Parler-TTS</a>
* Imagens: <a href="https://lexica.art/">Lexica</a>

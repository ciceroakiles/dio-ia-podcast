# dio-ia-podcast

<p align="center">
<a href="https://www.youtube.com/@DIA_Lotus_Cast">@DIA_Lotus_Cast
<br/>
<img src="https://yt3.googleusercontent.com/Mf0G-qMMc769O6n1jEOdhYPiuJ_t5khw4BT6jSUuDcW1S8ZBzowZ3weE32UFQ5AsqZktxyDPTg=s160-c-k-c0x00ffffff-no-rj"/>
</a>
</p>

Projeto com o objetivo de criar um podcast, com o auxílio de algumas ferramentas de inteligência artificial.

## Breve histórico
<details>
<summary>Clique aqui para expandir</summary>

* Na terceira atividade da terceira parte de um bootcamp da DIO, chamada "Processos de Treinamento de LLMs", há uma seção chamada "Desafios Computacionais no Treinamento de LLMs", e no segundo vídeo dessa seção, chamado "Projeto Hands-On: Superando Desafios Computacionais", é apresentado um exemplo de geração de voz usando <a href="https://huggingface.co/nari-labs/Dia-1.6B">nari-labs/Dia-1.6B</a>.

* Com o intuito de gerar vozes em português, a princípio adotou-se uma abordagem utilizando <a href="https://github.com/anan235/dia-multilingual/tree/main">dia-multilingual</a>, porém o maior entrave encontrado foi a remoção do arquivo <code>hyperparams.yaml</code> (<a href="https://github.com/anan235/dia-multilingual/issues/5#issuecomment-2830030195">mais detalhes aqui</a>). Portanto, foi preciso alterar o mecanismo de _text-to-speech_ (TTS) que seria utilizado.

* Foi possível obter resultados satisfatórios utilizando uma combinação de dois elementos: o Dockerfile do dia-multilingual modificado, e o <a href="https://github.com/huggingface/parler-tts">Parler-TTS</a>.

---
</details>

## Como os áudios do podcast são feitos

* A parte que mais demora é a preparação do ambiente; porém, uma vez pronto, é possível gerar quantos áudios forem necessários. Os áudios são gerados localmente para não depender de créditos, moedas, tokens, limites diários e vários outros tipos de limitações impostas quando se utiliza ferramentas de TTS gratuitas online.

* Com o serviço do Docker em execução, primeiro constrói-se a imagem a partir do Dockerfile (assim como no repositório dia-multilingual) com o seguinte comando, dentro da pasta de scripts.

```
docker build -t dia-multilang -f Dockerfile .
```

Depois, gera-se um container a partir dessa imagem.

```
docker run --gpus all -it -p 8000:8000 --name testcontainername dia-multilang
```

E por último, executa-se o script dentro do container (<code>python main.py</code>).

* A partir de então, é gerado o arquivo <code>model.safetensors</code>, um formato moderno para modelos de _deep learning_.

![Imgur](https://i.imgur.com/VpzR0E3.png)

* Cada roteiro específico é feito a partir de um roteiro base, e vai para o ChatGPT.

* Como resultado, aparecem as frases que serão convertidas em áudio, como visto na variável <code>prompt</code> do script.

## Lista de ferramentas de IA utilizadas

* Roteiro: <a href="https://chatgpt.com/">ChatGPT</a>
* Áudio: <a href="https://github.com/huggingface/parler-tts">Parler-TTS</a>
* Imagens: <a href="https://lexica.art/">Lexica</a>

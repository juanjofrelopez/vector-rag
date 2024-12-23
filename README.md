# RAG-based Chatbot for drivers at a car delivery company

## Demonstration

question: `how can i move my car?`

https://github.com/user-attachments/assets/981a40b4-a8a9-457e-916b-173d42a39a2e

question: `im a driver and i had an accident, what should i do?`

https://github.com/user-attachments/assets/3508ade3-7a5d-45e2-b41c-7303ee7b5954


## How to launch

1.  Create virtual env and install dependencies by running:

```bash
./install.sh
```

2. Choose the virtual enviroment just created:

```bash
source .venv/bin/activate
```

3. Spin up services with docker compose:

```bash
cd infra
docker-compose up --build
```

4. Create embeddings from knowledge base:

```bash
python create_embeddings.py
```

5. Start chat session

```bash
python ask_chat.py
```

## Stack

### [LLamafile](https://github.com/Mozilla-Ocho/llamafile)

This is in charge of providing the llm engine. I choose Llama 1B to be able to run fast inference with just the CPU.
Download your prefered llamafile and in a separate bash run this to start the engine on port `8080`:

#### Python API

Llamafile is openai API compliant, so by using its python pkg we can interact with the llamafile from withing python.

### [PGVector](https://github.com/pgvector/pgvector)

This will be our main database with vector capabilities. Semantic search will be our battle horse.

After inserting the embeddings this is what we get in the vector table:
![](docs/vec.png)

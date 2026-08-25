# KI-Sprachmodelle: Nutzung und Kosten

Hier finden Sie Informationen über die Nutzung der KI-Sprachmodelle und die damit verbundenen Kosten/Budgets. Erklärungen zu den einzelnen Begriffen finden Sie im KI-Glossar.

## 1. Basismodelle

| Region | Provider | Alias | Model | Basis |
| :--- | :--- | :--- | :--- | :--- |
| HS* | gwdg | GWDG: Basismodel | `gwdg.latest-basemodel` | Qwen 3.6 (Schnell) |
| USA | openai | OpenAI: Basismodel | `openai.latest-basemodel` | GPT-5.6 Terra |

*Mehr Informationen über die Basismodelle*

---

## 2. Router-Modelle

| Region | Provider | Model (Alias) | Routing-Modelle |
| :--- | :--- | :--- | :--- |
| HS* | gwdg | **GWDG: Qwen-Complexity-Routing**<br>`gwdg.qwen-complexity-router` | **SIMPLE**: Qwen 3 Instruct<br>**MEDIUM**: Qwen 3.5 (Hohe Qualität - Ohne Thinking)<br>**COMPLEX**: Qwen 3.5 (Beste Qualität)<br>**REASONING**: Qwen 3.6 (Hohe Qualität) |
| USA | openai | **OpenAI: Complexity-Routing**<br>`openai.complexity-router` | **SIMPLE**: GPT-5.4 Mini<br>**MEDIUM**: GPT-5.6 Luna<br>**COMPLEX**: GPT-5.6 Terra<br>**REASONING**: GPT-5.6 Sol |

*Mehr Informationen über die Router-Modelle*

---

## 3. Alle Sprachmodelle

| Region           | Provider | Model                                                                       | Parameter | Input Preis (1M) | Output Preis (1M) | Max Input | Max Output | Max TPM | Max RPM | Parallele Anfr. | Einstellungen          |
| :--------------- | :------- | :-------------------------------------------------------------------------- | :-------- | :--------------- | :---------------- | :-------- | :--------- | :------ | :------ | :-------------- | :--------------------- |
| USA              | openai   | **GPT-5.6 Sol**<br>`openai.gpt-5.6-sol`                                     | N/A       | $5.00            | $30.00            | 1.05M     | 128k       | 2M      | 100     | 10              | N/A                    |
| USA              | openai   | **GPT-5.6 Terra**<br>`openai.gpt-5.6-terra`                                 | N/A       | $2.00            | $12.00            | 1.05M     | 128k       | 2M      | 100     | 10              | N/A                    |
| USA              | openai   | **GPT-5.6 Luna**<br>`openai.gpt-5.6-luna`                                   | N/A       | $0.20            | $1.20             | 1.05M     | 128k       | 2M      | 100     | 10              | N/A                    |
| USA              | openai   | **GPT-5.5**<br>`openai.gpt-5.5`                                             | N/A       | $5.00            | $30.00            | 1.05M     | 128k       | 2M      | 100     | 10              | N/A                    |
| USA              | openai   | **GPT-5.5 Pro**<br>`openai.gpt-5.5-pro`                                     | N/A       | $30.00           | $180.00           | 1.05M     | 128k       | 2M      | 100     | 10              | N/A                    |
| USA              | openai   | **GPT-5.4**<br>`openai.gpt-5.4`                                             | N/A       | $2.50            | $15.00            | 1.05M     | 128k       | 2M      | 100     | 10              | N/A                    |
| USA              | openai   | **GPT-5.4 Mini**<br>`openai.gpt-5.4-mini`                                   | N/A       | $0.75            | $4.50             | 272k      | 128k       | 2M      | 100     | 10              | N/A                    |
| USA              | openai   | **GPT-5.4 Nano**<br>`openai.gpt-5.4-nano`                                   | N/A       | $0.20            | $1.25             | 272k      | 128k       | 2M      | 100     | 10              | N/A                    |
| USA              | openai   | **o4 Mini**<br>`openai.o4-mini`                                             | N/A       | $1.10            | $4.40             | 200k      | 100k       | 2M      | 100     | 10              | N/A                    |
| USA              | openai   | **GPT Image**<br>`openai.gpt-image-1.5`                                     | N/A       | $5.00            | $10.00            | N/A       | N/A        | 2M      | 100     | 10              | N/A                    |
| HS*              | gwdg     | **Qwen 3.6 (Hohe Qual.)**<br>`gwdg.qwen3.6-27b`                             | 27B       | $0.00            | $0.00             | 262k      | 262k       | 500k    | 10      | 10              | temp: 1, top_p: 0.95   |
| HS*              | gwdg     | **Qwen 3.6 (Hohe Qual. - No Thinking)**<br>`gwdg.qwen3.6-27b-no-think`      | 27B       | $0.00            | $0.00             | 262k      | 262k       | 500k    | 10      | 10              | temp: 1, top_p: 0.95   |
| HS*              | gwdg     | **Basemodel (Qwen 3.6 35B A3B - No Think)**<br>`gwdg.qwen3.6-35b-a3b`       | 35B A3B   | $0.00            | $0.00             | 262k      | 262k       | 500k    | 10      | 10              | temp: 1, top_p: 0.95   |
| HS*              | gwdg     | **Qwen 3.6 (Schnell - No Thinking)**<br>`gwdg.qwen3.6-35b-a3b-no-think`     | 35B A3B   | $0.00            | $0.00             | 262k      | 262k       | 500k    | 10      | 10              | temp: 1, top_p: 0.95   |
| HS*              | gwdg     | **Qwen 3.5 (Beste Qual.)**<br>`gwdg.qwen3.5-397b-a17b`                      | 397B A17B | $0.00            | $0.00             | 256k      | 256k       | 500k    | 10      | 10              | temp: 0.6, top_p: 0.95 |
| HS*              | gwdg     | **Qwen 3.5 (Beste Qual. - No Think)**<br>`gwdg.qwen3.5-397b-a17b-no-think`  | 397B A17B | $0.00            | $0.00             | 256k      | 256k       | 500k    | 10      | 10              | temp: 0.6, top_p: 0.95 |
| HS*              | gwdg     | **Qwen 3.5 (Hohe Qual.)**<br>`gwdg.qwen3.5-122b-a10b`                       | 122B A10B | $0.00            | $0.00             | 256k      | 256k       | 500k    | 10      | 10              | temp: 0.6, top_p: 0.95 |
| HS*              | gwdg     | **Qwen 3.5 (Hohe Qual. - No Think)**<br>`gwdg.qwen3.5-122b-a10b-no-think`   | 122B A10B | $0.00            | $0.00             | 256k      | 256k       | 500k    | 10      | 10              | temp: 0.6, top_p: 0.95 |
| HS*              | gwdg     | **Qwen 3 Instruct**<br>`gwdg.qwen3-30b-a3b-instruct-2507`                   | 30B A3B   | $0.00            | $0.00             | 256k      | 256k       | 500k    | 10      | 10              | N/A                    |
| HS*              | gwdg     | **Gemma 4**<br>`gwdg.gemma-4-31b-it`                                        | 122B A10B | $0.00            | $0.00             | 256k      | 256k       | 500k    | 10      | 10              | N/A                    |
| HS*              | gwdg     | **GLM 4.7**<br>`gwdg.glm-4.7`                                               | 358B      | $0.00            | $0.00             | 200k      | 200k       | 500k    | 10      | 10              | temp: 0.7, top_p: 0.8  |
| HS*              | gwdg     | **Mistral Medium 3.5**<br>`gwdg.mistral-medium-3.5-128b`                    | 128B A3B  | $0.00            | $0.00             | 256k      | 16.384k    | 500k    | 10      | 10              | N/A                    |
| HS*              | gwdg     | **DeepSeek V4 Flash**<br>`gwdg.deepseek-v4-flash`                           | 128B A3B  | $0.00            | $0.00             | 1M        | 384k       | 500k    | 10      | 10              | temp: 1, top_p: 1      |
| HS*<br>kiconnect | gwdg     | **OpenAI GPT OSS**<br>`hs-de.openai-gpt-oss-120b`                           | 120B      | $0.00            | $0.00             | 128k      | 128k       | N/A     | N/A     | 10              | N/A                    |
| HS*              | gwdg     | **Apertus**<br>`gwdg.apertus-70b-instruct-2509`                             | 70B       | $0.00            | $0.00             | 65k       | 65k        | 500k    | 10      | 10              | temp: 0.8, top_p: 0.9  |
| HS*              | gwdg     | **Qwen 3 Coder Next**<br>`gwdg.qwen3-coder-next`                            | 80B A3B   | $0.00            | $0.00             | 256k      | 256k       | 500k    | 10      | 10              | N/A                    |
| HS*              | gwdg     | **Devstral 2**<br>`gwdg.devstral-2-123b-instruct-2512`                      | 123B      | $0.00            | $0.00             | 256k      | 256k       | 500k    | 10      | 10              | N/A                    |
| USA              | openai   | **GPT-5.3 Codex**<br>`openai.gpt-5.3-codex`                                 | N/A       | $1.75            | $14.00            | 272k      | 128k       | 2M      | 100     | 10              | N/A                    |
| HS*              | gwdg     | **Qwen 3 Omni**<br>`gwdg.qwen3-omni-30b-a3b-instruct`                       | 30B A3B   | $0.00            | $0.00             | 256k      | 256k       | 500k    | 10      | 10              | N/A                    |
| HS*              | gwdg     | **Llama 3.1 8B Instruct**<br>`gwdg.meta-llama-3.1-8b-instruct`              | 8B        | $0.00            | $0.00             | 128k      | 128k       | 500k    | 10      | 10              | N/A                    |
| HS*              | gwdg     | **Qwen 3 Embedding 4B**<br>`hs-de.qwen3-embedding-4b`                       | 4B        | $0.00            | $0.00             | 32k       | 2.56k      | 500k    | 10      | 10              | N/A                    |
| HS*              | gwdg     | **E5 Mistral Instruct**<br>`hs-de.e5-mistral-7b-instruct`                   | 7B        | $0.00            | $0.00             | 4.096k    | 4.096k     | 500k    | 10      | 10              | N/A                    |
| HS*              | gwdg     | **Multilingual E5 Large Instruct**<br>`gwdg.multilingual-e5-large-instruct` | 0.6B      | $0.00            | $0.00             | 1.024k    | 1.024k     | 500k    | 10      | 10              | N/A                    |

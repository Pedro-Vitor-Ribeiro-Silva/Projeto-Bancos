# Gerenciador de Contas Bancárias

Este projeto é um sistema simples de gerenciamento de contas bancárias, permitindo criação, ativação, desativação, transferência de saldo e visualização de histórico de movimentações financeiras.

## 📌 Funcionalidades

- Criar contas bancárias
- Ativar e desativar contas
- Transferir saldo entre contas
- Movimentar dinheiro (entrada/saída)
- Consultar total de saldo em todas as contas
- Filtrar histórico de movimentações
- Gerar gráficos das contas ativas

## 🛠️ Tecnologias Utilizadas

- **Python** (linguagem principal)
- **SQLModel** (ORM para manipulação do banco de dados SQLite)
- **Matplotlib** (para geração de gráficos)

## 📂 Estrutura do Projeto

```-
📂 projeto
│-- models.py       # Definição dos modelos e do banco de dados
│-- view.py         # Funções de manipulação das contas e movimentações
│-- templates.py    # Interface do usuário (UI)
│-- database.db     # Banco de dados SQLite
```

## 🚀 Como Executar o Projeto

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/Pedro-Vitor-Ribeiro-Silva/Projeto-Bancos.git
   cd seu-repositorio
   ```
2. **Crie um ambiente virtual e instale as dependências:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. **Execute o sistema:**
   ```bash
   python templates.py
   ```

## 📜 Licença

Este projeto está licenciado sob os termos da licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

### 📄 Licença MIT

```
MIT License

Copyright (c) 2025

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```


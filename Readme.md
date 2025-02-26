# 📊 Roblox-Finance

### Gerenciador de Operações Financeiras para Roblox

## 🚀 Sobre o Projeto
Roblox-Finance é uma aplicação desenvolvida em **Python** utilizando **Streamlit** para gerenciar operações de compra e venda, calcular lucros/prejuízos e exibir relatórios financeiros.

O projeto mantém um registro detalhado das operações realizadas e calcula automaticamente os lucros/prejuízos, permitindo uma análise clara das transações.

---

## 🛠️ Tecnologias Utilizadas
- **Python** 🐍
- **Streamlit** 🎨 (Interface Gráfica)
- **PostgreSQL** 🗄️ (Banco de Dados)
- **Pandas** 📊 (Manipulação de Dados)
- **psycopg2** 🔗 (Conexão com PostgreSQL)

---

## 📂 Estrutura do Projeto

```
📁 web-roblox-finance
│── 📄 main.py               # Arquivo principal (Streamlit UI)
│── 📄 operation.py          # Classe responsável pelas operações
│── 📄 profit.py             # Classe responsável pelos cálculos de lucro/prejuízo
│── 📄 ligar_connect.py      # Conexão com o banco de dados
│── 📄 README.md             # Documentação do projeto
```

---

## 📌 Funcionalidades
✅ Registro de operações de compra e venda 🛒
✅ Cálculo automático de lucro/prejuízo 💰
✅ Exibição das operações em tabela 📊
✅ Relatórios dinâmicos 📈
✅ Destaque do lucro/prejuízo total com cores dinâmicas 🟢🔴

---

## ⚙️ Instalação e Configuração

### 1️⃣ Clonar o repositório
```bash
git clone https://github.com/saraiva142/Roblox-Finance-Web.git
cd web-roblox-finance
```

### 2️⃣ Criar um ambiente virtual e ativá-lo
```bash
python -m venv venv
# Ativar no Windows
venv\Scripts\activate
# Ativar no Linux/Mac
source venv/bin/activate
```

### 3️⃣ Instalar dependências
```bash
pip install -r requirements.txt
```

### 4️⃣ Configurar o Banco de Dados PostgreSQL
Certifique-se de que o PostgreSQL está rodando e crie o banco:
```sql
CREATE DATABASE roblox_finance;
```

Execute as tabelas necessárias:
```sql
CREATE TABLE operacoes (
    id SERIAL PRIMARY KEY,
    quantidade NUMERIC(10,3) NOT NULL,
    valor NUMERIC(15,2) NOT NULL,
    operacao VARCHAR(10) CHECK (operacao IN ('compra', 'venda')) NOT NULL,
    data TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE lucros_operacoes (
    id SERIAL PRIMARY KEY,
    operacao_id INT REFERENCES operacoes(id),
    pnl NUMERIC(15,2) NOT NULL,
    data TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### 5️⃣ Rodar a aplicação
```bash
streamlit run main.py
```

---

## 📸 Demonstração

**Tela Inicial**
![Tela Inicial]
(image.png)

**Tabela de Operações**
![Lucro/Prejuízo]

(image-1.png)

**Cálculo de Lucros/Prejuízos**
![alt text]
(image-2.png)

---

## 🏆 Contribuição
Se quiser contribuir com o projeto:
1. Faça um **fork** 🍴
2. Crie uma **branch**: `git checkout -b minha-feature`
3. Faça suas alterações e **commit**: `git commit -m 'Minha nova feature'`
4. Faça um **push** para sua branch: `git push origin minha-feature`
5. Abra um **Pull Request** ✅

---

## 📝 Licença
Este projeto é de código aberto e pode ser usado livremente. 😊

---

💡 **Desenvolvido por João Saraiva** 🚀


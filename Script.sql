-- COMANDO PARA CONECTAR DOCKER: docker run --name my-postgres -e POSTGRES_PASSWORD=mysecretpassword -p 5433:5432 -d --rm postgres:latest

CREATE TABLE operacoes (
    id SERIAL PRIMARY KEY,
    quantidade INT NOT NULL,
    valor NUMERIC(10,2) NOT NULL,
    operacao VARCHAR(10) CHECK (operacao IN ('compra', 'venda')) NOT NULL,
    capital NUMERIC(15,2) GENERATED ALWAYS AS (quantidade * valor) STORED,
    data TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE lucros_operacoes (
    id SERIAL PRIMARY KEY,
    operacao_id INT REFERENCES operacoes(id),
    pnl NUMERIC(15,2) NOT NULL,
    data TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE observacoes (
    id SERIAL PRIMARY KEY,
    operacao_id INT REFERENCES operacoes(id) ON DELETE CASCADE,
    descricao TEXT NOT NULL,
    data TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

from ligar_connect import connection
import pandas as pd
import streamlit as st

# id SERIAL PRIMARY KEY,
#     quantidade INT NOT NULL,
#     valor NUMERIC(10,2) NOT NULL,
#     operacao VARCHAR(10) CHECK (operacao IN ('compra', 'venda')) NOT NULL,
#     capital NUMERIC(15,2) GENERATED ALWAYS AS (quantidade * valor) STORED,
#     data TIMESTAMP DEFAULT CURRENT_TIMESTAMP

class Operation:
    def __init__(self, quantidade, valor, operacao, data):
        self.quantidade = quantidade
        self.valor = valor
        self.operacao = operacao
        self.data = data
    
    def inserir_operacao(self):
        try:
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO operacoes (quantidade, valor, operacao, data) VALUES (%s, %s, %s, %s)",
                (self.quantidade, self.valor, self.operacao, self.data)
            )
            connection.commit()
            cursor.close()
            print("Operação inserida com sucesso.")
        except Exception as e:
            connection.rollback()  # Reverte a transação para limpar o erro
            print(f"Ocorreu um erro ao tentar inserir a operação: {e}")
            
    @staticmethod
    def obter_operacoes():
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM operacoes")
            operacoes = cursor.fetchall()
            colnames = [desc[0] for desc in cursor.description]  # Nome das colunas
            cursor.close()
            
            # Converter os dados para DataFrame do Pandas
            operacoes_df = pd.DataFrame(operacoes, columns=colnames)
            
            return operacoes_df
        except Exception as e:
            print(f"Ocorreu um erro ao tentar obter as operações: {e}")
            return pd.DataFrame()
        
    def edit_operações():
        try:
            cursor = connection.cursor()
            cursor.execute(
                "UPDATE operacoes SET quantidade=%s, valor=%s, operacao=%s, capital=%s, data=%s WHERE id=%s",
                (self.quantidade, self.valor, self.operacao, self.capital, self.data, self.id)
            )
            connection.commit()
            cursor.close()
            print("Operação atualizada com sucesso.")
        except Exception as e:
            connection.rollback()  # Reverte a transação para limpar o erro
            print(f"Ocorreu um erro ao tentar atualizar a operação: {e}")
            
    def delete_operacao(self):
        try:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM operacoes WHERE id=%s", (self.id,))
            connection.commit()
            cursor.close()
            print("Operação deletada com sucesso.")
        except Exception as e:
            connection.rollback()
            print(f"Ocorreu um erro ao tentar deletar a operação: {e}")
        
    
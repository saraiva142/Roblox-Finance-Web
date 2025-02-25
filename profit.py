from ligar_connect import connection
import pandas as pd

class Profit:
    def __init__(self, id, operacao_id, pnl, data):
        self.id = id
        self.operacao_id = operacao_id
        self.pnl = pnl
        self.data = data
    
    def inserir_lucro(self):
        try:
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO lucros_operacoes (operacao_id, pnl, data) VALUES (%s, %s, %s)"
                " ON CONFLICT (operacao_id) DO UPDATE SET pnl = EXCLUDED.pnl, data = EXCLUDED.data;",
                (self.operacao_id, self.pnl, self.data)
            )
            connection.commit()
            cursor.close()
            print("Lucro inserido com sucesso.")
        except Exception as e:
            connection.rollback()
            print(f"Erro ao inserir lucro: {e}")
    
    @staticmethod
    def calcular_pnl():
        try:
            cursor = connection.cursor()
            
            cursor.execute("""
                WITH OperacoesOrdenadas AS (
                    SELECT id, operacao, valor, data
                    FROM operacoes
                    ORDER BY id ASC
                )
                SELECT 
                    o1.id AS id_compra, 
                    o2.id AS id_venda, 
                    o1.valor AS preco_compra, 
                    o2.valor AS preco_venda, 
                    (o2.valor - o1.valor) AS pnl,
                    o2.data AS data_venda
                FROM OperacoesOrdenadas o1
                JOIN OperacoesOrdenadas o2 ON o2.id = o1.id + 1
                WHERE o1.operacao = 'compra' AND o2.operacao = 'venda';
            """)

            registros = cursor.fetchall()
            
            # Inserir ou atualizar cada lucro/prejuízo na tabela de lucros
            for id_compra, id_venda, preco_compra, preco_venda, pnl, data_venda in registros:
                cursor.execute("""
                    INSERT INTO lucros_operacoes (operacao_id, pnl, data)
                        VALUES (%s, %s, %s)
                        ON CONFLICT (operacao_id) DO UPDATE 
                        SET pnl = EXCLUDED.pnl, data = EXCLUDED.data;
                """, (id_venda, pnl, data_venda))

            connection.commit()
            cursor.close()
            print("Tabela de Lucros/Prejuízos atualizada com sucesso.")
        except Exception as e:
            connection.rollback()
            print(f"Erro ao calcular e inserir lucros: {e}")
    
    @staticmethod
    def obter_pnl():
        try:
            cursor = connection.cursor()
            cursor.execute("""
                SELECT operacao_id, pnl, data FROM lucros_operacoes ORDER BY operacao_id ASC;
            """)
            registros = cursor.fetchall()
            cursor.close()
            
            if registros:
                df = pd.DataFrame(registros, columns=["Operação ID", "Lucro/Prejuízo", "Data"])
                return df
            else:
                return pd.DataFrame(columns=["Operação ID", "Lucro/Prejuízo", "Data"])
        except Exception as e:
            print(f"Ocorreu um erro ao tentar obter os lucros: {e}")
            return pd.DataFrame()

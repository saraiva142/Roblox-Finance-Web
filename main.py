import streamlit as st
from operation import Operation
from profit import Profit
import pandas as pd

# Configurando o tema padrão
st.set_page_config(
    page_title="Roblox-Finance",
    page_icon=":blossom:",
    layout="wide",  # wide ou "centered"
)

st.title('Minhas operações no Roblox-Finance :robot_face:')
st.write('João Saraiva')

tab1, tab2, tab3 = st.tabs(["Operações", "Tabela de Operações", "Relatórios"])

with tab1:
    with st.form(key="include_operation"):
        st.title("Operação")
        st.write("Preencher Tabela de Operações")
        input_quantidade = st.number_input(label="Insira a quantidade", format="%.3f", step=0.01)
        input_valor = st.number_input(label="Insira o valor", format="%.2f", step=0.01)
        input_operacao = st.selectbox("Selecione a operação", ["compra", "venda"])
        input_data = st.date_input("Data da operação")
        input_operation_button_submit = st.form_submit_button(label="Enviar")
        
        #input_capital = input_quantidade * input_valor
        

        if input_operation_button_submit:  #(Se o input_botton_submit for True = Apertado)
            operation = Operation(
                valor=input_valor,
                quantidade=input_quantidade,
                operacao=input_operacao,
                data=input_data
            )
            operation.inserir_operacao()
            #ClienteController.Incluir(cliente)
            st.success('Cadastrado com sucesso!', icon="✅")
            #st.write("Quantidade: ", input_quantidade)  Isso é só para debugar, e deu certinho 

    #else:
    #    st.error("É preciso preencher todos os campos")

with tab2:
    st.title("Tabela de Operações")
    
    if st.button("Atualizar tabela"):
        operacoes = Operation.obter_operacoes()
        
        if not operacoes.empty:
            st.dataframe(operacoes)
        else:
            st.warning("Nenhuma operação cadastrada")
            
    if st.button("Visualizar Lucro/Prejuízo"):
        Profit.calcular_pnl()  # Atualiza a tabela de lucros

        # Obtém os lucros/prejuízos
        pnl_data = Profit.obter_pnl()

        if not pnl_data.empty:
            # Exibir a tabela de lucros
            df_pnl = pd.DataFrame(pnl_data, columns=["Operação ID", "Lucro/Prejuízo", "Data"])
            st.dataframe(df_pnl)

            # Calcular e exibir o lucro total
            lucro_total = pnl_data["Lucro/Prejuízo"].astype(float).sum()

            st.metric("Lucro Total", f"R$ {lucro_total:.2f}")
            cor = "green" if lucro_total >= 0 else "red"
            #st.markdown(f'<h3 style="color:{cor};">R$ {lucro_total:.2f}</h3>', unsafe_allow_html=True)

        else:
            st.warning("Nenhuma operação de lucro/prejuízo encontrada.")
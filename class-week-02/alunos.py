import streamlit as st

def main():
  st.title('Hello world')
  st.markdown('Botao')
  botao = st.button('botao')
  if botao:
    st.markdown('clicado')

  st.markdown('checkbox')
  check = st.checkbox('Checkbox')
  if check:
    st.markdown('clicado')

  st.markdown('radio')
  radio = st.radio('Escolha as opcoes', { 'Opt1', 'Opt2' })
  if radio == 'Opt1':
    st.markdown('Opt1')
  if radio == 'Opt2':
    st.markdown('Opt2')

  st.markdown('SelectBox')
  select = st.selectbox('Choose opt', { 'Opt1', 'Opt2' })
  if select == 'Opt1':
    st.markdown('Opt1')
  if select == 'Opt2':
    st.markdown('Opt2')

if __name__ == '__main__':
  main()
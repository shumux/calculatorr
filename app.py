import streamlit as st 
import json 

   




def save_history():
      with open("history.json", 'w', encoding="utf-8") as file:
            json.dump( st.session_state.history, file, indent=4) 


def load_history():
      with open("history.json", "r", encoding="utf-8") as file:
            st.session_state.history = json.load(file)   

if "history" not in st.session_state:
      load_history()


 
theme = st.context.theme.type 
if theme == "dark":
      st.image("logo_dark.png", width = 150)
else:
      st.image("logo_light.png", width= 150 )   



st.title("Калькулятор")


number1 = st.number_input("Введите первое число: ")
number2 = st.number_input("Введите второе число:")

st.write(number1)
st.write(number2)

sign = st.selectbox("выберите операццию:", ["+", "-", 
                                        "*", "/"])
st.write(sign)

if st.button("посчитать"):
    
    if number2 == 0 and sign == "/":
          
          st.write("на ноль делить нельзя!")
    elif sign == "+":
        res = number1+number2
        st.write(res)
        st.session_state.history.append(f"{number1}+ {number2}= {res}")
        save_history()

    elif sign == "-":
            res = number1-number2
            st.write(res)
            st.session_state.history.append(f"{number1}- {number2}= {res}") 
            save_history()   

    elif sign == "/":
            res = number1/number2
            st.write(res)
            st.session_state.history.append(f"{number1}/ {number2}= {res}")
            save_history()

    elif sign == "*":
            res = number1*number2
            st.write(res)
            st.session_state.history.append(f"{number1}* {number2}= {res}")
            save_history()


st.subheader("История операций:")

if st.button("Очистить историю"):
    st.session_state.history.clear()
    save_history()

for i in st.session_state.history:
      st.write(i)         




               
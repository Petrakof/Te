import streamlit as st
from streamlit_extras.dataframe_explorer import dataframe_explorer
import numpy as np
import pandas as pd
import time
from transformers import pipeline
from PIL import  Image
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
  


def intro():
    import streamlit as st
# Title of the application 
    st.write("# Добро пожаловать! 👋")
    st.sidebar.success("Выбрать раздел")
    st.markdown('Анализ тональности чатов Телеграм\n', )
    st.info("Группа 32: Смирнова А., Кожедуб Н., Багаудинов Э., Петраков В.")

    display = Image.open('images/display.jpg')
    display = np.array(display)
    st.image(display)

def mapping_demo():
    import streamlit as st
    from streamlit_extras.dataframe_explorer import dataframe_explorer
    import pandas as pd
    from transformers import pipeline
    import matplotlib.pyplot as plt 
    import seaborn as sns; sns.set()

    st.markdown(f"# {list(page_names_to_funcs.keys())[1]}")
    @st.cache 
    @st.experimental_memo
    def read_data(uploaded_file):
        return pd.read_csv(uploaded_file)
    datafile = st.file_uploader("Загрузите файл csv", ["csv"])
   
    if datafile is None:
        st.info("""Загрузите набор данных (.csv), чтобы приступить к работе.""")
        st.stop() 


    data = read_data(datafile).copy()
   
    model=pipeline("sentiment-analysis",   
                      "blanchefort/rubert-base-cased-sentiment")
                      
    result = st.button('Распознать')
    st.balloons()
    
    df_model = data.copy()
   
    if result:
        lst = []
        for i in df_model["text"]:
            lst.append(model(str(i))[0]["label"])
            df_model["Sentinent"]=pd.DataFrame(lst)

    st.write(df_model)
   
    df_N = df_model[df_model["Sentinent"]=="NEGATIVE"]
    df_n =df_N.user_id.value_counts().sort_index()
    df_n.plot.bar(edgecolor='k', alpha=0.9, stacked = True, cmap="viridis")
    plt.title("Самые негативные user_id	")

def filter_demo():
    import streamlit as st
    from streamlit_extras.dataframe_explorer import dataframe_explorer
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    
page_names_to_funcs = {
    "Главная 👋": intro,
    "Загрузка истории чатов 🔭": mapping_demo,
    "Фильтр данных 🎯": filter_demo,
   }
name = st.sidebar.selectbox("Выбрать раздел", page_names_to_funcs.keys())
page_names_to_funcs[name]()
import pandas as pd
import altair as alt

def visualize_tools(dictionary):

    #explode the df by the languages and tools
    df = pd.DataFrame.from_dict(dictionary)
    boom_lang = df.explode("Programming Languages")
    boom_tools = df.explode("Tools")        


    chart =  (alt.Chart(boom_lang).mark_bar().encode(
        alt.X('count()'),
        alt.Y('Programming Languages', sort='x')

    )) | (alt.Chart(boom_tools).mark_bar().encode(
        alt.X('count()'),
        alt.Y('Tools', sort='x')

    ))

    return chart

    

def parse_df(df, columnname):
    column_list = df[columnname].tolist()
    list_full = []
    for item in column_list:
        split_item = item[1:-1].split(', ')
        for i in split_item:
            list_full.append(i.strip("'"))
            
    return list_full



    
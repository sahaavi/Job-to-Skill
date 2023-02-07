import pandas as pd
import altair as alt

def parse_df(df, columnname):

    try:
        column_list = df[columnname].tolist()
        list_full = []
        for item in column_list:
            split_item = item[1:-1].split(', ')
            for i in split_item:
                list_full.append(i.strip("'"))

        dictionary = {
            columnname: list_full
            }

        df = pd.DataFrame.from_dict(dictionary) 

        return df
    except Exception as e:
        return "Error in chart creation: " + str(e)

def visualize_info(df, df2):
    try:
        chart = (
        alt.Chart(df).mark_bar(color = '#FFCE54').encode(
            alt.X('count()', title = 'Count of Programming Languages', axis=alt.Axis(grid=False,tickMinStep=1,titleFontSize=13, labelFontSize=12)),
            alt.Y('Programming Languages',title=None,  axis=alt.Axis(labelFontSize=11), sort='x')
        ).properties(
            title=alt.TitleParams('In-Demand Skills in Job Descriptions: Prevalence of Programming Languages and Tools',fontSize=16),
            width=500,
            height=200)
            &
        alt.Chart(df2).mark_bar(color = '#007BA7').encode(
            alt.X('count()',title ='Count of Tools', axis=alt.Axis(grid=False,tickMinStep=1, titleFontSize=13, labelFontSize=12)),
            alt.Y('Tools', title=None, sort='x', axis=alt.Axis(labelFontSize=11))).properties(
        width=500,
        height=200))

        return chart

    except Exception as e:
        return "Error in chart creation: " + str(e)

def visualize_location(df, columnname):
    if df[columnname].notna().all():
        try:
            temp = df[columnname].tolist()
            full_list = []
            for item in temp:
                i = item.split(',')[0]
                full_list.append(i)

            df = pd.DataFrame({columnname: full_list})
            df_grouped = df.groupby(columnname).size().reset_index(name='count')
            df_grouped

            base = alt.Chart(df_grouped).encode(
            theta=alt.Theta("count:Q", stack=True), color=alt.Color("Job Location:N", legend=None, scale=alt.Scale(scheme='plasma')))

            pie = base.mark_arc(outerRadius=200)
            text = base.mark_text(radius=225, size=20, align='left').encode(text="count:Q")
            text2 = base.mark_text(radius=260, size=15).encode(text="Job Location:N")
            pie_chart = alt.layer(text,text2, pie).properties(title = alt.TitleParams('Job Distribution by Location', fontSize=16), height=600, width=600)

            return pie_chart
        
        except Exception as e:
            return "Error in chart creation: " + str(e)
        
    else:
        print("No locations available to build chart!")
        return False





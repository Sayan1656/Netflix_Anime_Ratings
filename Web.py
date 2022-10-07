import os
from PIL import Image
import requests
import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
import plotly_express as px

#___Load Anime___
def anime(URL):
    r=requests.get(URL)
    if r.status_code!=200:
        return None
    return r.json()


#___Anime___
Animetion1=anime("https://assets1.lottiefiles.com/packages/lf20_3rwasyjy.json")
Animetion2=anime("https://assets9.lottiefiles.com/packages/lf20_qp1q7mct.json")
Animetion3=anime("https://assets10.lottiefiles.com/private_files/lf30_uqcbmc4h.json")
Animetion4=anime("https://assets10.lottiefiles.com/packages/lf20_F2Mv1p.json")
AlartAnimetion=anime("https://assets6.lottiefiles.com/packages/lf20_Tkwjw8.json")
PopularAnimetion=anime("https://assets9.lottiefiles.com/packages/lf20_AzOvUp.json")
PopularAnimetion2=anime("https://assets1.lottiefiles.com/private_files/lf30_sbjxcjlp.json")


#___Configuration___
page_logo=Image.open(r"TanjiroChibi.jpg")
st.set_page_config(page_title="Netflix anime ratings",page_icon=page_logo,layout="wide")
hide_st_style='''
<style>
#MainMenu{visibility:hidden;}
footer{visibility:hidden"}
</style>'''
st.markdown(hide_st_style,True)


pwd=os.getcwd()
Clean_Data_show=pd.read_excel('Data_clean.xlsx',usecols="A:G").astype(str)
Clean_Data=pd.read_excel('Data_clean.xlsx').astype(str)


#__Sidebar for changing page___
option=["Data","Visualisation","Contact"]
Pages=option_menu(
    menu_title=None,
    options=option,
    default_index=0,
    icons=["Table","Pie chart fill","Person rolodex"],
    orientation="horizontal"
)
st.title(Pages)

#___Page Data___
if(Pages=="Data"):
    with st.container():
        text,Animetion=st.columns(2)
        with text:
            st.markdown('<h2 style="padding-right: 50px">About Dataset</h2><p style="padding-right: 50px">Now days webseries are very much populer, not only among the childern but also a lot of grown ups, It help them to understand a lot of thing about our life, it helps to forget pain an overcome sadness, to choose happyness, sometime help to overcome the pressure.</p>'
                    '<p style="padding-right: 50px">There are a lot of anime platfrom are present now day such as CrunchyRoll, GogoAnime, KissAnime etc and also different platfroms for webseries like Hoichoi, Zee5, MxPlayer etc. But Net flis is such a platfrom, where you can not only see the populer anime show but also some many intresting webseries and lot more.</p>'
                    '<p style="padding-right: 50px">This is a personal project to collect all ratings from TV Series Episodes in the top <a href="https://www.imdb.com/chart/toptv/" style="text-decoration:none">250 TV Series list</a> from IMDb.</p>'
                    '<p style="padding-right: 50px">An monthly updated version of this data is available <a href="https://www.kaggle.com/datasets/wittmannf/episode-ratings-from-imdb-top-250-tv-series" style="text-decoration:none">here</a>.</p>'
                    '<p style="padding-right: 50px">It has been scheduled to update automatically using this <a href="https://www.kaggle.com/code/wittmannf/collect-episode-rating-from-imdb-top-tv-250-series" style="text-decoration:none">kaggle kerne</a>.</p>'
                    ,unsafe_allow_html=True )
            st.write("[Load dataset >](https://www.kaggle.com/datasets/wittmannf/episode-ratings-from-imdb-top-250-tv-series)")
        with Animetion:
            st_lottie(Animetion1,height=300)


    with st.container():
        animation,data=st.columns(2)
        with animation:
            st_lottie(Animetion2,height=300)
        with data:
            st.dataframe(Clean_Data_show)


#___Page Visualisation___
if(Pages=="Visualisation"):
    st.header("#Let's talk about Data...")
    st.subheader("Global distribution of episode rating")
    df1=pd.read_excel(pwd+'\\Data_clean.xlsx',sheet_name='Workbook',usecols='A:B')
    data,graph=st.columns(2)
    with data:
        st.dataframe(df1)
    with graph:
        fig1=px.bar(df1,x='Rating_Episode',y= 'Number of Rating_Episode',color='Number of Rating_Episode')
        st.plotly_chart(fig1)


    
    df2=pd.read_excel(pwd+'\\Data_clean.xlsx',sheet_name='Workbook',usecols='D:E')
    st.write("By considering the graph we can say that the alomost 1000 number of episode gate 8.1 rating, which is the higest number,"
        "therefore we can say that the episode get more rating then 8.1 are the popular episode and those which are below 8.1 are not that much populer.")
    pie,space,question=st.columns(3)
    with pie:
        fig2=px.pie(df2,names='Good_Not',values='Number of Episode',color='Good_Not')
        st.plotly_chart(fig2)
    with question:
        good_ep_count=sum(Clean_Data.Good_Not == "Good")
        not_good_ep_count=sum(Clean_Data.Good_Not == "Not Good")
        ep_count=Clean_Data["Title"].count()
        
        st.header("Summary")
        st.write("There are ",ep_count,"number of episodes (Total) present in Netflix. Among those episodes, their are ",good_ep_count,"numbers of popular episodes"
        " and", not_good_ep_count,"number of episodes are not that much popular (if I consider 8.1 is a minimum rating for a good episode).")
        st.write("Although each and every webseries has their own fan base, different kind of people like different type of webseries, so it is not possible to judge concept"
        " of an webseries based on its rating. So this is my suggestion to wacth a webseries base on your teast not based on its rating. :blush:")

    
    
    df3=pd.read_excel(pwd+'\\Data_clean.xlsx',sheet_name='Workbook',usecols='G:H').astype(str)
    max_gap=df3["Gap_Of_Mean_Rating"].max()
    name_max_gap=df3[df3["Gap_Of_Mean_Rating"]==max_gap]['Title'].values[0]
    text,anime=st.columns(2)
    with text:
        st.markdown('<h2 style="margin-top:10px">#Episode having higher gap...</h2>',unsafe_allow_html=True)
        st.write("There are sevarel webseries having a huge gap between their Mean Episode Rating and their TV Series Rating, But the series named,",name_max_gap,"having maiximum gap between"
        " it's Mean Episode Rating and TV Series Rating, which is", max_gap,".")
    with anime:
        st_lottie(AlartAnimetion,height=200)


    
    df4=pd.read_excel(pwd+'\\Data_Clean.xlsx',sheet_name="Workbook",usecols="J:K")
    df5=pd.read_excel(pwd+'\\Data_Clean.xlsx',sheet_name='Workbook',usecols="M:N")
    num_max_rate_mean=df4["Number of Ep_rate_mean"].max()
    num_max_rate_mid=df5["Number of Ep_rate_median"].max()
    max_rate_mean=df4[df4["Number of Ep_rate_mean"]==num_max_rate_mean]['Ep_rate_mean'].values[0]
    max_rate_mid=df5[df5["Number of Ep_rate_median"]==num_max_rate_mid]['Episode_rating_median'].values[0]

    st.markdown('<h2>#TV Series Distribution...</h2>',unsafe_allow_html=True)
    st.markdown('<h4 style="margin-top:10px">Mean Distribution of TV Series</h4>',unsafe_allow_html=True)
    fig3=px.bar(df4,x="Ep_rate_mean",y="Number of Ep_rate_mean", color="Number of Ep_rate_mean")
    st.plotly_chart(fig3,True)
    st.markdown('<h4 style="margin-top:10px">About distribution</h4>',unsafe_allow_html=True)
    st.write("From the graph of Mean and Median distribution of TV Series, we can assume that the higest mean rating of maximun episode is",max_rate_mean,
    " and higest mid rating of maximum episode is",max_rate_mid,".")
    st.markdown('<h4 style="margin-top:10px">Mid Distribution of TV Series</h4>',unsafe_allow_html=True)
    fig4=px.scatter(df5, x='Episode_rating_median',y='Number of Ep_rate_median',color='Number of Ep_rate_median',log_x=True,size_max=60)
    st.plotly_chart(fig4,True)

    
    max_rate_first=Clean_Data.query('Ocurence=="First"')['Rating_Episode'].max()
    name_max_rate_first=Clean_Data[(Clean_Data['Rating_Episode']==max_rate_first) & (Clean_Data['Ocurence']=="First")]['Title'].values[0]
    max_rate_last=Clean_Data[Clean_Data["Ocurence"]=="Last"]['Rating_Episode'].max()
    name_max_rate_last=Clean_Data[(Clean_Data["Ocurence"]=="Last") & (Clean_Data["Rating_Episode"]==max_rate_last)]['Title'].values[0]
    st.markdown('<h2 style="margin-top:10px">#Popular Episodes...</h2>',unsafe_allow_html=True)
    text1,anime,text2=st.columns(3)
    with text1:
        st.markdown('<h4 style="margin-top:10px">Popular First Episode...</h4>',unsafe_allow_html=True)
        st.write("Among all the webseries the most intresting First episode is: ",name_max_rate_first,", where Valery Legasov speaks into a tape recorder about the Chernobyl nuclear disaster. He talks about Anatoly Dyatlov, who he feels deserves death for what he had done."
        " Finishing the tape, Legasov places it with others he made and hides it outside. He carefully avoids being seen by a car outside his apartment that is always there, watching him. Back inside, he checks his watch as he finishes a cigarette and lays out extra food for his cat. At 1:23:45, he hangs himself...")
    with text2:
        st.markdown('<h4 style="margin-top:10px">Popular Last Episode...</h4>',unsafe_allow_html=True)
        st.write("Among all the webseries the most intresting Last episode is: ",name_max_rate_last,", which is an anime, where Aang, the Avator, fought with fire Lord Ozai during Sozin’s comet. Ozai had the upper hand at the start, but when Aang entered the Avatar state he got the upper hand. And in the end, he took Ozai’s bending away.")
        st.write("Suki, Toph and Sokka finished their mission by destroying all the airships in a ‘airship slide’ and arrived to congrats Aang.")
        st.write("On the other side, Zuko is in a Agni Kai with Azula, who is ‘slipping’. And got the upper hand until Katara appeared around the corner. Azula knew that she couldn’t win so she directed lightning at Zuko, but changed to directed at Katara. Zuko jumped in front of her and the fight ended with Katara bounding Azula’s hands with metal chains.")
    with anime:
        st.markdown('<h4 style="margin-top:50px"> </h4>',unsafe_allow_html=True)
        st_lottie(PopularAnimetion,height=200)
    

    st.markdown('<h2 style="margin-top:10px">#Conclusion</h2>',unsafe_allow_html=True)
    st.write("As an web-series addictor, I can say that webseries is not a thing to judge by it's rating. The thing which help us to overcome our stress in our daily busy life schudule"
    ", that can't be judge by rating or can't be compared with any thing else.")
    st.write("Different people has their own different ideaology, and an webseries was made by keeping this ideology in mind,"
    " so thats why, different webseries has it's own different teast. Some of of them may be romantic on the other hand there are some anime based on action,"
    ' some of them may be comedic but some of them are trageic, there are classical anime like "Mr.Bean", "Chota Bheem" or "Tom & Jerry", as well as Sci-fi anime'
    ' like "Sword Art Online" and "Mobile Suit Gundum".')
    st.write("So choose an webseries series based on your teast not by some ones rating and other's influence.")
    

#___Page Contact___
if(Pages=="Contact"):
    right,left=st.columns(2)
    with right:
        with st.container():
            st.header("Hello, I am Sayan :wave:")
            st.write("Intrested to start my career with an organigation, along with some commitated and dedicated people, to explore my potentioal as well as develope my skill in field of Data Analytices, Frontend Design and Andriod Development.")
        
        with st.container():
            st.subheader(":round_pushpin: Address")
            st.markdown('<h3 style="padding-left:10px; margin-top:-30px">Kolkata</h3>'
            '<h5 style="padding-left:10px; margin-top:-5px">30 Anjan Garh Colony<br>Dum Dum, Kol- 700030</h5>'
            ,unsafe_allow_html=True)

        with st.container():
            st.subheader(":telephone_receiver: Contact")
            st.markdown('<h5 style="padding-left:10px; margin-top:-25px">+916291659798</h5>'
            '<h5 style="padding-left:10px; margin-top:-5px">sayanhalderofficial@gmail.com</h5>'
            ,unsafe_allow_html=True)
            

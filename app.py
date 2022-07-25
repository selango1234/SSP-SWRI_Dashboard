import pandas as pd
import plotly.express as px
import streamlit as st
import plotly.figure_factory as ff


# Variables

particle1Data = pd.read_csv(r'particle1.txt', index_col=0, sep = ",")
particle1Data = particle1Data.iloc[: , :-1]

particle2Data = pd.read_csv(r'particle2.txt', index_col=0, sep = ",")
particle2Data = particle2Data.iloc[: , :-1]

particle3Data = pd.read_csv(r'particle3.txt', index_col=0, sep = ",")
particle3Data = particle3Data.iloc[: , :-1]

particle4Data = pd.read_csv(r'particle4.txt', index_col=0, sep = ",")
particle4Data = particle4Data.iloc[: , :-1]

particle5Data = pd.read_csv(r'particle5.txt', index_col=0, sep = ",")
particle5Data = particle5Data.iloc[: , :-1]

particle6Data = pd.read_csv(r'particle6.txt', index_col=0, sep = ",")
particle6Data = particle6Data.iloc[: , :-1]

particle7Data = pd.read_csv(r'particle7.txt', index_col=0, sep = ",")
particle7Data = particle7Data.iloc[: , :-1]

particle8Data = pd.read_csv(r'particle8.txt', index_col=0, sep = ",")
particle8Data = particle8Data.iloc[: , :-1]

particle9Data = pd.read_csv(r'particle9.txt', index_col=0, sep = ",")
particle9Data = particle9Data.iloc[: , :-1]

particle10Data = pd.read_csv(r'particle10.txt', index_col=0, sep = ",")
particle10Data = particle10Data.iloc[: , :-1]

particle11Data = pd.read_csv(r'particle11.txt', index_col=0, sep = ",")
particle11Data = particle11Data.iloc[: , :-1]

particle12Data = pd.read_csv(r'particle12.txt', index_col=0, sep = ",")
particle12Data = particle12Data.iloc[: , :-1]

particle13Data = pd.read_csv(r'particle13.txt', index_col=0, sep = ",")
particle13Data = particle13Data.iloc[: , :-1]

selectionOptions = ['Particle 1', 'Particle 2', 'Particle 3', "Particle 4", 'Particle 5', 'Particle 6', 'Particle 7', 'Particle 8', 'Particle 9','Particle 10', 'Particle 11', 'Particle 12', 'Particle 13']

data = [particle1Data, particle2Data, particle3Data, particle4Data, particle5Data, particle6Data, particle7Data, particle8Data, particle9Data, particle10Data, particle11Data, particle12Data, particle13Data]

# Functions

def plotStandardData(particleData):
    st.subheader("Time Series Data")

    fig = px.line(particleData, x = "Time (Years)", y = "a", color_discrete_sequence = ["#ff97ff"], title = "Time Evolution of Semi-major axis (a)")
    st.plotly_chart(fig, use_container_width=True)

    fig = px.line(particleData, x = "Time (Years)", color_discrete_sequence = ["#ff0000"], y = "e", title = "Time Evolution of Eccentricity (e)")
    st.plotly_chart(fig, use_container_width=True)

    fig = px.line(particleData, x = "Time (Years)", color_discrete_sequence = ["#ffd700"], y = "i", title = "Time Evolution of Inclination (i)")
    st.plotly_chart(fig, use_container_width=True)

    fig = px.line(particleData, x = "Time (Years)", color_discrete_sequence = ["#90ee90"], y = "OMEGA", title = "Time Evolution of OMEGA")
    st.plotly_chart(fig, use_container_width=True)

    fig = px.line(particleData, x = "Time (Years)", y = "omega", title = "Time Evolution of omega")
    st.plotly_chart(fig, use_container_width=True)

    fig = px.line(particleData, x = "Time (Years)", color_discrete_sequence = ["#7f00ff"], y = "M", title = "Time Evolution of Mean Anomoly (M)")
    st.plotly_chart(fig, use_container_width=True)

def compareVariables(particleData):

    selectionOptions = ['a', 'e', 'i', "OMEGA", 'omega', 'M']
    optionChosen = st.multiselect("Select Two Variables to Compare", selectionOptions)

    if len(optionChosen) == 2:
        fig = px.scatter(particleData, x = optionChosen[0], y = optionChosen[1], marginal_x = "histogram", marginal_y = "violin", title = "Variable Comparison between " + str(optionChosen[0]) + " and " + str(optionChosen[1]), color_discrete_sequence = ["#ff0000"])
        st.plotly_chart(fig, use_container_width = True)


def compareParticles(particle1Data, particle2Data, options):

    fig = px.line(particle1Data, x = "Time (Years)", y = "a", title = "Time Evolution of Semi-major axis (a)")
    fig.add_scatter(x = particle2Data['Time (Years)'], y = particle2Data['a'], name = options[1])
    st.plotly_chart(fig, use_container_width=True)

    fig = px.line(particle1Data, x = "Time (Years)", y = "e", title = "Time Evolution of Eccentricity (e)")
    fig.add_scatter(x = particle2Data['Time (Years)'], y = particle2Data['e'], name = options[1])
    st.plotly_chart(fig, use_container_width=True)

    fig = px.line(particle1Data, x = "Time (Years)", y = "i", title = "Time Evolution of Inclination (i)")
    fig.add_scatter(x = particle2Data['Time (Years)'], y = particle2Data['i'], name = options[1])
    st.plotly_chart(fig, use_container_width=True)

    fig = px.line(particle1Data, x = "Time (Years)", y = "OMEGA", title = "Time Evolution of OMEGA")
    fig.add_scatter(x = particle2Data['Time (Years)'], y = particle2Data['OMEGA'], name = options[1])
    st.plotly_chart(fig, use_container_width=True)

    fig = px.line(particle1Data, x = "Time (Years)", y = "omega", title = "Time Evolution of omega")
    fig.add_scatter(x = particle2Data['Time (Years)'], y = particle2Data['omega'], name = options[1])
    st.plotly_chart(fig, use_container_width=True)

    fig = px.line(particle1Data, x = "Time (Years)", y = "M", title = "Time Evolution of Mean Anomoly (M)")
    fig.add_scatter(x = particle2Data['Time (Years)'], y = particle2Data['M'], name = options[1])
    st.plotly_chart(fig, use_container_width=True)


## STREAMLIT PAGE 

# Set Page Options
st.set_page_config(layout = 'wide')
st.title("SwRI Orbital Evolution of 2001 MZ7")

st.markdown("""
* Data Analysis of 2001 MZ7 Orbital Path 50 MYR Corpus
* Part of Summer Science Program NMT 2022: https://summerscience.org/
* Credit to SwRI for Data Generation: https://www.swri.org/
""")

with st.expander("Particle Analysis"):

    st.header("Particle Analysis")

    optionMap = st.selectbox("What particle would you like to explore?", selectionOptions)
    
    if (optionMap.find("Particle") != -1):

        index = selectionOptions.index(optionMap)

        plotStandardData(data[index])

        compareVariables(data[index])
    

with st.expander("Particle Comparison"):

    st.header("Particle Comparison")

    optionChosen = st.multiselect("Select Two Particles to Compare", selectionOptions)

    if len(optionChosen) == 2:

        index1 = selectionOptions.index(optionChosen[0])

        index2 = selectionOptions.index(optionChosen[1])

        compareParticles(data[index1], data[index2], optionChosen)
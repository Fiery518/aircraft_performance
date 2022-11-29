import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


st.markdown('''
# **A Small Scale Plane Performance Analyzer**

- Enter the data which are required for calculations accordingly for the results required in the sidebar
- Select the graph required for the results to be shown
            
            
            ''')

with st.sidebar.form(key ='Form1'):
    mass = st.number_input('Insert the mass of the plane in Kg',value = 9.07)
    density = st.number_input('Insert the density in SI units Kg/m3',value = 1.225)
    wingSpan = st.number_input('Insert the wingspan in SI units m',value = 1.524)
    chord = st.number_input('enter chord length',value = 0.3227832)
    spanEfficiency = st.number_input('Enter Span Efficiency',value = 0.7)
    fuseLength = st.number_input('Enter Fuse Length',value = 1.1408)
    fuseDiameter = st.number_input('Enter Fuse Diameter',value = 0.1079)
    option = st.selectbox(
    'What performance parameters do you want to check',
    ('Rate of Climb', 'Thrust Required', 'Drag vs Velocity'))
    submit_button = st.form_submit_button(label='Submit')
    
def rateOfClimb(mass,wingSpan,chord,density,fusel,fusedia):
    weight =  mass*9.8
    j = 0
    FR = fusel/fusedia
    RateOfClimb = [0] * 27
    for i in range(9,36):
        rey = i*chord/0.00015111
        Cl = (2*weight)/(density*i*i*wingSpan*chord)
        Cf = 0.644/(rey**0.5)
        Cdi = (Cl**2)/(3.14*0.7*(wingSpan/chord))
        Cdminw= (1.0656*(1+(2.09*(0.0003/chord))+(100*(0.0003/chord)**4))) * Cf * (2*(wingSpan*chord)*(1+0.5*(0.0003/chord))) / (wingSpan*chord)
        Cdminf = (1+(60/((fusel/fusedia)**3))+(0.0025*(fusel/fusedia))) *Cf*((2*fusedia*fusedia)+(4*fusel*fusedia))/(wingSpan*chord)
        Cdminh = 0.00135
        CdminLG = 0.02
        Cdminv = 0.00062
        Cdmin = 0.06162
        Cd = Cdmin + Cdi
        Treq = weight*Cd/Cl
        Preq = Treq*i
        
        RateOfClimb[j] = (((1274-Preq)/weight)/9.81)*3.281
        j = j+1
        
    x = np.arange(29.529,118.116,3.281) 
    y = RateOfClimb
    fig, ax = plt.subplots()
    line, = ax.plot(x, y)
    
    ymax1 = max(y)
    xpos = y.index(ymax1)
    xmax = x[xpos]
    
    

    ax.set_title('Rate of Climb')
    ax.set_xlabel('Velocity (ft/s)')
    ax.set_ylabel('Rate of Climb (ft/s)')
    ax.annotate('Rmax : ' + ("%.3f" % ymax1), xy=(xmax, ymax1), xytext=(3, 1.5),
                   arrowprops=dict(facecolor='black', shrink=0.001))
    ax.vlines(x = xmax, ymin = 0, ymax = ymax1,
           colors = 'black',
           label = 'vline_multiple - full height',linestyles='dashed')
    ax.hlines(y = ymax1, xmin = 0, xmax = xmax,
           colors = 'black',
           label = 'hline_multiple - full height',linestyles='dashed')
    ax.set_ylim(0,4.75)
    st.pyplot(fig)
    

if option == "Rate of Climb":
    rateOfClimb(mass,wingSpan,chord,density,fuseLength,fuseDiameter)
        
    
    

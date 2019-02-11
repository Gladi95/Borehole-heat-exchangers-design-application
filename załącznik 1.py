import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from functools import partial
from math import sqrt, erfc, pi
from scipy.integrate import quad  ## funkcja calkujaca
import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from tkinter import *
import math
import decimal
#oznaczenie zmiennych oraz równań

#zmienne globalne
var_values={}   #{'x1','x2','y','q0','h'}
rr=[]
zz=[]
scores=[]


def rownanie1():
    var_values['x1']  = num1 = moc
    var_values['x2']  = num2 = number
    num3 = sprezarka
    var_values['h']= result = round((((float(num1.get())*24/20)*3/4)/(9.2*float(num2.get())+22.8)*(1+(0.05*float(num3.get())-100)/100)),5)
    label_dlugosc.config(text="Długość odwiertu w  wynosi: " + str(result) + " [m]")
    return

def rownanie2():
    num1 = moc
    num2 = number
    cieplna = round(int(num1.get())*24/20,5)
    label_moc_cieplna.config(text="Moc cieplna pompy wynosi: " + str(cieplna) + " [W]")
    return

def rownanie3():
    num1 = moc
    num2 = number
    chlodnicza = round((int(num1.get())*24/20)*3/4,5)
    label_moc_chlodnicza.config(text="Moc chłodnicza dolnego źródła ciepła wynosi:"  + str(chlodnicza) + " [W]")
    return

def integral():
    global result,rr,zz,scores,colors


    # wartosci stale
    a=2.2/(2473.06*932.27)
    t=3600*100
    T0=273.15+12.37
    q=12617.131/var_values['h']
    counter = 0

    # dane dotyczace osi na wykresie
    r = np.arange(0.1, 10.05, 0.05)   # promien
    z = np.linspace(0,var_values['h'],len(r))  # glebokosc
    rr, zz = np.meshgrid(r, z)

    # funkcja pod calka
    g=lambda h: erfc(sqrt((j**2+(i-h)**2))/(2*sqrt(a*t)))/sqrt(j**2+(i-h)**2)-erfc(sqrt(j**2+(i+h)**2)/(2*sqrt(a*t)))/sqrt(j**2+(i+h)**2)

    # utworzenie 2-wymiarowej tablicy dla zbierania wynikow
    scores=[[] for num in range(len(r))]


    # zagniezdzona petla for liczaca calke dla kazdego zestawienia r i z
    for i in z:
        for j in r:
            w=quad(g,0,var_values['h'])
            scores[counter].append((w[0]*q)/(4*pi*2.2)+T0)
        counter = counter + 1

def plot_3d():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(rr, zz, np.array(scores),cmap=cm.jet)
    ax.set_xlabel('Promien [m]')
    ax.set_ylabel('Glebokosc [m]')
    ax.set_zlabel('Temperatura [K]')
    plt.show()

def wykres():
    try:
        integral()
        plot_3d()
    except ZeroDivisionError:
        label_blad0.config(text=" Nieprawidłowe dane")
    except KeyError:
        label_blad0.config(text=" Nieprawidłowe dane")
def row_jeden():
    try:
        convective_resistance = round(1/(2*pi*float(b11.get())*float(b16.get())),5)
        pipe_resistance = round(math.log(float(b12.get())/float(b11.get()))/(2*pi*float(b14.get())),5)
        grout_resistance = round(1/(4*pi*float(b13.get()))*(math.log(float(b10.get())/float(b12.get()))+math.log(float(b10.get())/float(b15.get()))+(float(b13.get())-float(b4.get()))/(float(b13.get())+float(b4.get()))*math.log(float(b10.get())**4/(float(b10.get())**4-(float(b15.get())/2)**4))),5)
        effective_borehole_thermal_resistance = round(grout_resistance+(convective_resistance+pipe_resistance)/2,5)
        short_term = round(1/float(b4.get())*(0.6619352+(-4.815693)*float(b10.get())+15.03571*float(b10.get())**2+(-0.09879421)*float(b8.get())+0.02917889*float(b5.get())**2+0.1138498*math.log(float(b5.get()))+0.005610933*math.log(float(b5.get()))**2+0.7796329*float(b10.get())*float(b5.get())+(-0.324388)*float(b10.get())*math.log(float(b5.get()))+(-0.01824101)*float(b5.get())*math.log(float(b5.get()))),5)
        medium_term = round(1/float(b4.get())*(0.4132728+0.2912981*float(b10.get())+0.07589286*float(b10.get())**2+0.1563978*float(b5.get())+(-0.2289355)*float(b5.get())**2+(-0.004927554)*math.log(float(b5.get()))+(-0.002694979)*math.log(float(b5.get()))**2+(-0.638036)*float(b10.get())*float(b5.get())+0.2950815*float(b10.get())*math.log(float(b5.get()))+0.149332*float(b5.get())*math.log(float(b5.get()))),5)
        long_term = round(1/float(b4.get())*(0.3057646+0.08987446*float(b10.get())+(-0.09151786)*float(b10.get())**2+(-0.03872451)*float(b5.get())+0.1690853*float(b5.get())**2+-0.02881681*math.log(float(b5.get()))+(-0.002886584)*math.log(float(b5.get()))**2+(-0.1723169)*float(b10.get())*float(b5.get())+0.03112034*float(b10.get())*math.log(float(b5.get()))+(-0.1188438)*float(b5.get())*math.log(float(b5.get()))),5)
        heat_pump_outlet_temperature =round(float(b9.get())+float(b1.get())/(float(b8.get())*math.fabs(float(b1.get()))/1000*float(b7.get())),5)
        average_fluid_temperature =round((float(b9.get())+float(heat_pump_outlet_temperature))/2,5)
        total_length =round((float(b3.get())*float(long_term)+float(b2.get())*float(medium_term)+float(b1.get())*float(short_term)+float(b1.get())*float(effective_borehole_thermal_resistance))/(float(average_fluid_temperature)-float(b6.get())),5)
    except ZeroDivisionError:
        label_blad0.config(text=" Nieprawidłowe dane")
    else:
        label_jeden.config(text=" Opór konwekcyjny: " + str(convective_resistance) + " [(m•K)/W]" )
        label_dwa.config(text=" Opór rury: " + str(pipe_resistance)+ " [(m•K)/W]")
        label_trzy.config(text=" Odporność na zaprawę : "+ str(grout_resistance)+ " [(m•K)/W]")
        label_cztery.config(text=" Skuteczna odporność termiczna odwiertu: " + str(effective_borehole_thermal_resistance) + " [(m•K)/W]")
        label_piec.config(text=" Skuteczna rezystancja gruntu w cyklu 6h: "+ str(short_term) + " [(m•K)/W]")
        label_szesc.config(text= " Skuteczna rezystancja gruntu w cyklu 1 miesiąc: "+ str(medium_term)+ " [(m•K)/W]")
        label_siedem.config(text= " Skuteczna rezystancja gruntu w cyklu 10 lat: " + str(long_term)+ " [(m•K)/W]")
        label_osiem.config( text= " Temperatura wyjściowa pompy ciepła: "+ str(heat_pump_outlet_temperature)+ " [°C]")
        label_dziewiec.config(text=" Średnia temperatura płynu w otworze wiertniczym: "+ str(average_fluid_temperature)+ " [°C]")
        label_dziesiec.config(text=" Całkowita długość: "+ str(total_length)+ " [m]")
    return

def row_wiele():
    try:
        decimal.getcontext().prec = 150
        convective_resistance = round(1 / (2 * pi * float(b11.get()) * float(b16.get())), 5)
        pipe_resistance = round(math.log(float(b12.get()) / float(b11.get())) / (2 * pi * float(b14.get())), 5)
        grout_resistance = round(1 / (4 * pi * float(b13.get())) * (
                    math.log(float(b10.get()) / float(b12.get())) + math.log(float(b10.get()) / float(b15.get())) + (
                        float(b13.get()) - float(b4.get())) / (float(b13.get()) + float(b4.get())) * math.log(
                float(b10.get()) ** 4 / (float(b10.get()) ** 4 - (float(b15.get()) / 2) ** 4))), 5)
        effective_borehole_thermal_resistance = round(grout_resistance + (convective_resistance + pipe_resistance) / 2,
                                                      5)
        short_term = round(1 / float(b4.get()) * (
                    0.6619352 + (-4.815693) * float(b10.get()) + 15.03571 * float(b10.get()) ** 2 + (
                -0.09879421) * float(b8.get()) + 0.02917889 * float(b5.get()) ** 2 + 0.1138498 * math.log(
                float(b5.get())) + 0.005610933 * math.log(float(b5.get())) ** 2 + 0.7796329 * float(b10.get()) * float(
                b5.get()) + (-0.324388) * float(b10.get()) * math.log(float(b5.get())) + (-0.01824101) * float(
                b5.get()) * math.log(float(b5.get()))), 5)
        medium_term = round(1 / float(b4.get()) * (
                    0.4132728 + 0.2912981 * float(b10.get()) + 0.07589286 * float(b10.get()) ** 2 + 0.1563978 * float(
                b5.get()) + (-0.2289355) * float(b5.get()) ** 2 + (-0.004927554) * math.log(float(b5.get())) + (
                        -0.002694979) * math.log(float(b5.get())) ** 2 + (-0.638036) * float(b10.get()) * float(
                b5.get()) + 0.2950815 * float(b10.get()) * math.log(float(b5.get())) + 0.149332 * float(
                b5.get()) * math.log(float(b5.get()))), 5)
        long_term = round(1 / float(b4.get()) * (
                    0.3057646 + 0.08987446 * float(b10.get()) + (-0.09151786) * float(b10.get()) ** 2 + (
                -0.03872451) * float(b5.get()) + 0.1690853 * float(b5.get()) ** 2 + (-0.02881681) * math.log(
                float(b5.get())) + (-0.002886584) * math.log(float(b5.get())) ** 2 + (-0.1723169) * float(
                b10.get()) * float(b5.get()) + 0.03112034 * float(b10.get()) * math.log(float(b5.get())) + (
                        -0.1188438) * float(b5.get()) * math.log(float(b5.get()))), 5)
        heat_pump_outlet_temperature = round(float(b9.get()) + float(b1.get()) / (float(b8.get()) * math.fabs(float(b1.get())) / 1000 * float(b7.get())),5)
        average_fluid_temperature = round((float(b9.get()) + float(heat_pump_outlet_temperature)) / 2, 5)
        total_length = round((float(b3.get()) * float(long_term) + float(b2.get()) * float(medium_term) + float(
            b1.get()) * float(short_term) + float(b1.get()) * float(effective_borehole_thermal_resistance)) /
                             (float(average_fluid_temperature) - float(b6.get())), 5)
       # 1 iteracja

        distance_depth_ratio1 = round(float(b17.get()) / (float(total_length) / float(b18.get())),3)
        logarithm_of_dimensionless_time1 = round(math.log(365.25 * 10 / ((float(total_length) / float(b18.get())) ** 2 / (9 * float(b5.get())))),3)

        temperature_penalty1 = round(float(b3.get()) / (2 * pi * float(b4.get()) * float(total_length)) * (
                7.8189 + (-64.27) * float(distance_depth_ratio1) + 153.87 * float(distance_depth_ratio1) ** 2 + (
            -84.809) * float(distance_depth_ratio1) ** 3 + 3.461 * float(logarithm_of_dimensionless_time1) + (
                    -0.94753) * float(logarithm_of_dimensionless_time1) ** 2 + (-0.060416) * float(
            logarithm_of_dimensionless_time1) ** 3 + 1.5631 * float(b18.get()) + (-0.0089416) * float(
            b18.get()) ** 2 + 0.000019061 * float(b18.get()) ** 3 + (-2.289) * float(b19.get()) + 0.10187 * float(
            b19.get()) ** 2 + 0.006569 * float(b19.get()) ** 3 + (-40.918) * float(distance_depth_ratio1) * float(
            logarithm_of_dimensionless_time1) + 15.557 * float(distance_depth_ratio1) * float(
            logarithm_of_dimensionless_time1) ** 2 + (-19.107) * float(distance_depth_ratio1) * float(
            b18.get()) + 0.10529 * float(distance_depth_ratio1) * float(b18.get()) ** 2 + 25.501 * float(
            distance_depth_ratio1) * float(b19.get()) + (-2.1177) * float(distance_depth_ratio1) * float(
            b19.get()) ** 2 + 77.529 * float(distance_depth_ratio1) ** 2 * float(logarithm_of_dimensionless_time1) + (
                    -50.454) * float(distance_depth_ratio1) ** 2 * float(
            logarithm_of_dimensionless_time1) ** 2 + 76.352 * float(distance_depth_ratio1) ** 2 * float(b18.get()) + (
                    -0.53719) * float(distance_depth_ratio1) ** 2 * float(b18.get()) ** 2 + (-132) * float(
            distance_depth_ratio1) ** 2 * float(b19.get()) + 12.878 * float(distance_depth_ratio1) ** 2 * float(
            b19.get()) ** 2 + 0.12697 * float(logarithm_of_dimensionless_time1) * float(b18.get()) + (
                    -0.00040284) * float(logarithm_of_dimensionless_time1) * float(b18.get()) ** 2 + (
                    -0.072065) * float(logarithm_of_dimensionless_time1) * float(b19.get()) + 0.00095184 * float(
            logarithm_of_dimensionless_time1) * float(b19.get()) ** 2 + (-0.024167) * float(
            logarithm_of_dimensionless_time1) ** 2 * float(b18.get()) + 0.000096811 * float(
            logarithm_of_dimensionless_time1) ** 2 * float(b18.get()) ** 2 + 0.028317 * float(
            logarithm_of_dimensionless_time1) ** 2 * float(b19.get()) + (-0.0010905) * float(
            logarithm_of_dimensionless_time1) ** 2 * float(b19.get()) ** 2 + 0.12207 * float(b18.get()) * float(
            b19.get()) + (-0.007105) * float(b18.get()) * float(b19.get()) ** 2 + (-0.0011129) * float(
            b18.get()) ** 2 * float(b19.get()) + (-0.00045566) * float(b18.get()) ** 2 * float(b19.get()) ** 2),3)

        total_borefield_length1 = round((float(b3.get()) * float(long_term) + float(b2.get()) * float(medium_term) + float(b1.get()) * float(
                short_term) + float(b1.get()) * float(effective_borehole_thermal_resistance)) / (
                    float(average_fluid_temperature) - float(b6.get()) - float(temperature_penalty1)),3)
        # 2 iteracja
        distance_depth_ratio2 = round(float(b17.get()) / (float(total_borefield_length1) / float(b18.get())),3)
        logarithm_of_dimensionless_time2 = round(math.log(365.25 * 10 / ((float(total_borefield_length1) / float(b18.get())) ** 2 / (9 * float(b5.get())))),3)
        temperature_penalty2 = round(float(b3.get()) / (2 * pi * float(b4.get()) * float(total_borefield_length1)) * (
                    7.8189 + (-64.27) * float(distance_depth_ratio2) + 153.87 * float(distance_depth_ratio2) ** 2 + (
                -84.809) * float(distance_depth_ratio2) ** 3 + 3.461 * float(logarithm_of_dimensionless_time2) + (
                        -0.94753) * float(logarithm_of_dimensionless_time2) ** 2 + (-0.060416) * float(
                logarithm_of_dimensionless_time2) ** 3 + 1.5631 * float(b18.get()) + (-0.0089416) * float(
                b18.get()) ** 2 + 0.000019061 * float(b18.get()) ** 3 + (-2.289) * float(b19.get()) + 0.10187 * float(
                b19.get()) ** 2 + 0.006569 * float(b19.get()) ** 3 + (-40.918) * float(distance_depth_ratio2) * float(
                logarithm_of_dimensionless_time2) + 15.557 * float(distance_depth_ratio2) * float(
                logarithm_of_dimensionless_time2) ** 2 + (-19.107) * float(distance_depth_ratio2) * float(
                b18.get()) + 0.10529 * float(distance_depth_ratio2) * float(b18.get()) ** 2 + 25.501 * float(
                distance_depth_ratio2) * float(b19.get()) + (-2.1177) * float(distance_depth_ratio2) * float(
                b19.get()) ** 2 + 77.529 * float(distance_depth_ratio2) ** 2 * float(
                logarithm_of_dimensionless_time2) + (-50.454) * float(distance_depth_ratio2) ** 2 * float(
                logarithm_of_dimensionless_time2) ** 2 + 76.352 * float(distance_depth_ratio2) ** 2 * float(
                b18.get()) + (-0.53719) * float(distance_depth_ratio2) ** 2 * float(b18.get()) ** 2 + (-132) * float(
                distance_depth_ratio2) ** 2 * float(b19.get()) + 12.878 * float(distance_depth_ratio2) ** 2 * float(
                b19.get()) ** 2 + 0.12697 * float(logarithm_of_dimensionless_time2) * float(b18.get()) + (
                        -0.00040284) * float(logarithm_of_dimensionless_time2) * float(b18.get()) ** 2 + (
                        -0.072065) * float(logarithm_of_dimensionless_time2) * float(b19.get()) + 0.00095184 * float(
                logarithm_of_dimensionless_time2) * float(b19.get()) ** 2 + (-0.024167) * float(
                logarithm_of_dimensionless_time2) ** 2 * float(b18.get()) + 0.000096811 * float(
                logarithm_of_dimensionless_time2) ** 2 * float(b18.get()) ** 2 + 0.028317 * float(
                logarithm_of_dimensionless_time2) ** 2 * float(b19.get()) + (-0.0010905) * float(
                logarithm_of_dimensionless_time2) ** 2 * float(b19.get()) ** 2 + 0.12207 * float(b18.get()) * float(
                b19.get()) + (-0.007105) * float(b18.get()) * float(b19.get()) ** 2 + (-0.0011129) * float(
                b18.get()) ** 2 * float(b19.get()) + (-0.00045566) * float(b18.get()) ** 2 * float(b19.get()) ** 2),3)
        total_borefield_length2 = round((float(b3.get()) * float(long_term) + float(b4.get()) * float(medium_term) + float(b1.get()) * float(
                short_term) + float(b1.get()) * float(effective_borehole_thermal_resistance)) / (
                    float(average_fluid_temperature) - float(b6.get()) - float(temperature_penalty2)),3)
        # 3 iteracja
        distance_depth_ratio3 = round(float(b17.get()) / (float(total_borefield_length2) / float(b18.get())),3)
        logarithm_of_dimensionless_time3 = round(math.log(365.25 * 10 / ((float(total_borefield_length2) / float(b18.get())) ** 2 / (9 * float(b5.get())))),3)
        temperature_penalty3  = round(float(b3.get()) / (2 * pi * float(b4.get()) * float(total_borefield_length2)) * (
                    7.8189 + (-64.27) * float(distance_depth_ratio3) + 153.87 * float(distance_depth_ratio3) ** 2 + (
                -84.809) * float(distance_depth_ratio3) ** 3 + 3.461 * float(logarithm_of_dimensionless_time3) + (
                        -0.94753) * float(logarithm_of_dimensionless_time3) ** 2 + (-0.060416) * float(
                logarithm_of_dimensionless_time3) ** 3 + 1.5631 * float(b18.get()) + (-0.0089416) * float(
                b18.get()) ** 2 + 0.000019061 * float(b18.get()) ** 3 + (-2.289) * float(b19.get()) + 0.10187 * float(
                b19.get()) ** 2 + 0.006569 * float(b19.get()) ** 3 + (-40.918) * float(distance_depth_ratio3) * float(
                logarithm_of_dimensionless_time3) + 15.557 * float(distance_depth_ratio3) * float(
                logarithm_of_dimensionless_time3) ** 2 + (-19.107) * float(distance_depth_ratio3) * float(
                b18.get()) + 0.10529 * float(distance_depth_ratio3) * float(b18.get()) ** 2 + 25.501 * float(
                distance_depth_ratio3) * float(b19.get()) + (-2.1177) * float(distance_depth_ratio3) * float(
                b19.get()) ** 2 + 77.529 * float(distance_depth_ratio3) ** 2 * float(
                logarithm_of_dimensionless_time3) + (-50.454) * float(distance_depth_ratio3) ** 2 * float(
                logarithm_of_dimensionless_time3) ** 2 + 76.352 * float(distance_depth_ratio3) ** 2 * float(
                b18.get()) + (-0.53719) * float(distance_depth_ratio3) ** 2 * float(b18.get()) ** 2 + (-132) * float(
                distance_depth_ratio3) ** 2 * float(b19.get()) + 12.878 * float(distance_depth_ratio3) ** 2 * float(
                b19.get()) ** 2 + 0.12697 * float(logarithm_of_dimensionless_time3) * float(b18.get()) + (
                        -0.00040284) * float(logarithm_of_dimensionless_time3) * float(b18.get()) ** 2 + (
                        -0.072065) * float(logarithm_of_dimensionless_time3) * float(b19.get()) + 0.00095184 * float(
                logarithm_of_dimensionless_time3) * float(b19.get()) ** 2 + (-0.024167) * float(
                logarithm_of_dimensionless_time3) ** 2 * float(b18.get()) + 0.000096811 * float(
                logarithm_of_dimensionless_time3) ** 2 * float(b18.get()) ** 2 + 0.028317 * float(
                logarithm_of_dimensionless_time3) ** 2 * float(b19.get()) + (-0.0010905) * float(
                logarithm_of_dimensionless_time3) ** 2 * float(b19.get()) ** 2 + 0.12207 * float(b18.get()) * float(
                b19.get()) + (-0.007105) * float(b18.get()) * float(b19.get()) ** 2 + (-0.0011129) * float(
                b18.get()) ** 2 * float(b19.get()) + (-0.00045566) * float(b18.get()) ** 2 * float(b19.get()) ** 2),3)
        total_borefield_length3 = total_borefield_length2
        # 4 iteracja

        distance_depth_ratio4 = round(float(b17.get()) / (float(total_borefield_length3) / float(b18.get())),3)
        logarithm_of_dimensionless_time4 = round(math.log(365.25 * 10 / ((float(total_borefield_length3) / float(b18.get())) ** 2 / (9 * float(b5.get())))),3)
        temperature_penalty4 = round(float(b3.get()) / (2 * pi * float(b4.get()) * round(float(total_borefield_length3),5)) * (
                   7.8189 + (-64.27) * float(distance_depth_ratio4) + 153.87 * round(float(distance_depth_ratio4) ** 2,5) + (
               -84.809) * round(float(distance_depth_ratio4),5) ** 3 + 3.461 * round(float(logarithm_of_dimensionless_time4),5) + (
                       -0.94753) * round(float(logarithm_of_dimensionless_time4) ** 2,5) + (-0.060416) * round(float(
               logarithm_of_dimensionless_time4) ** 3,5) + 1.5631 * float(b18.get()) + (-0.0089416) * round(float(
               b18.get()) ** 2,5) + 0.000019061 * float(b18.get()) ** 3 + (-2.289) * float(b19.get()) + 0.10187 * round(float(
               b19.get()) ** 2 + 0.006569 * float(b19.get()) ** 3 + (-40.918) * float(distance_depth_ratio4) * float(
               logarithm_of_dimensionless_time4),5) + 15.557 * round(float(distance_depth_ratio4),3) * float(
               logarithm_of_dimensionless_time4) ** 2 + (-19.107) * float(distance_depth_ratio4) * float(
               b18.get()) + 0.10529 * round(float(distance_depth_ratio4),3) * round(float(b18.get()) ** 2,3) + 25.501 * round(float(
                distance_depth_ratio4),5) * float(b19.get()) + (-2.1177) * float(distance_depth_ratio4) * round(float(
                b19.get()) ** 2,5) + 77.529 * round(float(distance_depth_ratio4) ** 2,3) * float(
                logarithm_of_dimensionless_time4) + (-50.454) * float(distance_depth_ratio4) ** 2 * round(float(
                logarithm_of_dimensionless_time4) ** 2,3) + 76.352 * round(float(distance_depth_ratio4) ** 2,3) * float(
                b18.get()) + (-0.53719) * round(float(distance_depth_ratio4) ** 2,3) * float(b18.get()) ** 2 + (-132) * float(
                distance_depth_ratio4) ** 2 * float(b19.get()) + 12.878 * float(distance_depth_ratio4) ** 2 * float(
                b19.get()) ** 2 + 0.12697 * float(logarithm_of_dimensionless_time4) * float(b18.get()) + (
                       -0.00040284) * float(logarithm_of_dimensionless_time4) * round(float(b18.get()) ** 2,3) + (
                       -0.072065) * float(logarithm_of_dimensionless_time4) * float(b19.get()) + 0.00095184 * float(
                logarithm_of_dimensionless_time4) * float(b19.get()) ** 2 + (-0.024167) * round(float(
                logarithm_of_dimensionless_time4) ** 2,3) * float(b18.get()) + 0.000096811 * round(float(
                logarithm_of_dimensionless_time4) ** 2,3) * float(b18.get()) ** 2 + 0.028317 * round(float(
                logarithm_of_dimensionless_time4) ** 2,3) * float(b19.get()) + (-0.0010905) * round(float(
                logarithm_of_dimensionless_time4) ** 2,3) * float(b19.get()) ** 2 + 0.12207 * float(b18.get()) * float(
                b19.get()) + (-0.007105) * float(b18.get()) * float(b19.get()) ** 2 + (-0.0011129) * float(
                b18.get()) ** 2 * float(b19.get()) + (-0.00045566) * float(b18.get()) ** 2 * float(b19.get()) ** 2),5)
        total_borefield_length4 = total_borefield_length2
        #5 iteracja

        distance_depth_ratio5 = round(float(b17.get()) / (float(total_borefield_length4) / float(b18.get())),3)
        logarithm_of_dimensionless_time5 = round(math.log(365.25 * 10 / ((float(total_borefield_length4) / float(b18.get())) ** 2 / (9 * float(b5.get())))),3)
        temperature_penalty5 = round(float(b3.get()) / (2 * pi * float(b4.get()) * float(total_borefield_length4)) * (
                   7.8189 + (-64.27) * float(distance_depth_ratio5) + 153.87 * float(distance_depth_ratio5) ** 2 + (
               -84.809) * float(distance_depth_ratio5) ** 3 + 3.461 * float(logarithm_of_dimensionless_time5) + (
                       -0.94753) * float(logarithm_of_dimensionless_time5) ** 2 + (-0.060416) * float(
               logarithm_of_dimensionless_time5) ** 3 + 1.5631 * float(b18.get()) + (-0.0089416) * float(
               b18.get()) ** 2 + 0.000019061 * float(b18.get()) ** 3 + (-2.289) * float(b19.get()) + 0.10187 * float(
               b19.get()) ** 2 + 0.006569 * float(b19.get()) ** 3 + (-40.918) * float(distance_depth_ratio5) * float(
               logarithm_of_dimensionless_time5) + 15.557 * float(distance_depth_ratio5) * float(
                logarithm_of_dimensionless_time5) ** 2 + (-19.107) * float(distance_depth_ratio5) * float(
                b18.get()) + 0.10529 * float(distance_depth_ratio5) * float(b18.get()) ** 2 + 25.501 * float(
                distance_depth_ratio5) * float(b19.get()) + (-2.1177) * float(distance_depth_ratio5) * float(
                b19.get()) ** 2 + 77.529 * float(distance_depth_ratio5) ** 2 * float(
                logarithm_of_dimensionless_time5) + (-50.454) * float(distance_depth_ratio5) ** 2 * float(
                logarithm_of_dimensionless_time5) ** 2 + 76.352 * float(distance_depth_ratio5) ** 2 * float(
                b18.get()) + (-0.53719) * float(distance_depth_ratio5) ** 2 * float(b18.get()) ** 2 + (-132) * float(
               distance_depth_ratio5) ** 2 * float(b19.get()) + 12.878 * float(distance_depth_ratio5) ** 2 * float(
               b19.get()) ** 2 + 0.12697 * float(logarithm_of_dimensionless_time5) * float(b18.get()) + (
                       -0.00040284) * float(logarithm_of_dimensionless_time5) * float(b18.get()) ** 2 + (
                       -0.072065) * float(logarithm_of_dimensionless_time5) * float(b19.get()) + 0.00095184 * float(
               logarithm_of_dimensionless_time5) * float(b19.get()) ** 2 + (-0.024167) * float(
               logarithm_of_dimensionless_time5) ** 2 * float(b18.get()) + 0.000096811 * float(
               logarithm_of_dimensionless_time5) ** 2 * float(b18.get()) ** 2 + 0.028317 * float(
               logarithm_of_dimensionless_time5) ** 2 * float(b19.get()) + (-0.0010905) * float(
               logarithm_of_dimensionless_time5) ** 2 * float(b19.get()) ** 2 + 0.12207 * float(b18.get()) * float(
               b19.get()) + (-0.007105) * float(b18.get()) * float(b19.get()) ** 2 + (-0.0011129) * float(
               b18.get()) ** 2 * float(b19.get()) + (-0.00045566) * float(b18.get()) ** 2 * float(b19.get()) ** 2),3)
        total_borefield_length5 = total_borefield_length2
        # final
        total_borefield_length = total_borefield_length5
        borehole_depth = float(total_borefield_length) / float(b18.get())
    except ZeroDivisionError:
        label_blad01.config(text=" Nieprawidłowe dane")
    except _tkinter.TclError:
        label_blad01.config(text=" Nieprawidłowe dane")
    else:
        label_1.config(text=" Opór konwekcyjny: " + str(convective_resistance) + " [(m•K)/W]")
        label_2.config(text=" Opór rury: " + str(pipe_resistance) + " [(m•K)/W]")
        label_3.config(text=" Odporność na zaprawę : " + str(grout_resistance) + " [(m•K)/W]")
        label_4.config(text=" Skuteczna odporność termiczna odwiertu: " + str(effective_borehole_thermal_resistance) + " [(m•K)/W]")
        label_5.config(text=" Skuteczna rezystancja gruntu w cyklu 6h: " + str(short_term) + " [(m•K)/W]")
        label_6.config(text=" Skuteczna rezystancja gruntu w cyklu 1 miesiąc: " + str(medium_term) + " [(m•K)/W]")
        label_7.config(text=" Skuteczna rezystancja gruntu w cyklu 10 lat: " + str(long_term) + " [(m•K)/W]")
        label_8.config(text=" Temperatura wyjściowa pompy ciepła: " + str(heat_pump_outlet_temperature) + " [°C]")
        label_9.config(text=" Średnia temperatura płynu w otworze wiertniczym: " + str(average_fluid_temperature) + " [°C]")
        label_10.config(text=" Całkowita długość: " + str(total_length) + " [m]" +"\n")
        label_11.config(text=" Pierwsza iteracja")
        label_12.config(text=" Stosunek odległości do głębokości: " + str(distance_depth_ratio1))
        label_13.config(text=" Logarytm czasu bezwymiarowego : " + str(logarithm_of_dimensionless_time1))
        label_14.config(text=" Kara temperaturowa: " + str(temperature_penalty1) + " [°C]")
        label_15.config(text=" Całkowita długość: " + str(total_borefield_length1) + " [m]"+"\n")
        label_16.config(text=" Druga iteracja " )
        label_17.config(text=" Stosunek odległości do głębokości: " + str(distance_depth_ratio2))
        label_18.config(text=" Logarytm czasu bezwymiarowego : " + str(logarithm_of_dimensionless_time2))
        label_19.config(text=" Kara temperaturowa: " + str(temperature_penalty2) + " [°C]")
        label_20.config(text=" Całkowita długość: " + str(total_borefield_length2) + " [m]")
        label_21.config(text=" Trzecia iteracja ")
        label_22.config(text=" Stosunek odległości do głębokości: " + str(distance_depth_ratio3))
        label_23.config(text=" Logarytm czasu bezwymiarowego : " + str(logarithm_of_dimensionless_time3))
        label_24.config(text=" Kara temperaturowa: " + str(temperature_penalty3) + " [°C]")
        label_25.config(text=" Całkowita długość: " + str(total_borefield_length3) + " [m]"+"\n")
        label_26.config(text=" Czwarta iteracja")
        label_27.config(text=" Stosunek odległości do głębokości: " + str(distance_depth_ratio4))
        label_28.config(text=" Logarytm czasu bezwymiarowego : " + str(logarithm_of_dimensionless_time4))
        label_29.config(text=" Kara temperaturowa: " + str(temperature_penalty4) + " [°C]" )
        label_30.config(text=" Całkowita długość: " + str(total_borefield_length4) + " [m]"+"\n")
        label_31.config(text=" Piąta iteracja")
        label_32.config(text=" Stosunek odległości do głębokości: " + str(distance_depth_ratio5))
        label_33.config(text=" Logarytm czasu bezwymiarowego : " + str(logarithm_of_dimensionless_time5))
        label_34.config(text=" Kara temperaturowa: " + str(temperature_penalty5) + " [°C]")
        label_35.config(text=" Całkowita długość: " + str(total_borefield_length5) + " [m]" )
        label_36.config(text="    " )
        label_37.config(text=" Wyniki końcowe")
        label_38.config(text=" Całkowita długość: "+str(total_borefield_length) + " [m]")
        label_39.config(text=" Głębokość odwiertu: " + str(borehole_depth) + " [m]" )




    return
        # Create instance
win = tk.Tk()


# Add a title
win.title("Aplikacja do projektowania")

tabControl = ttk.Notebook(win)  # Create Tab Control

tab1 = ttk.Frame(tabControl)  # Create a tab
tabControl.add(tab1, text='Obliczenia poglądowe')  # Add the tab
tab2 = ttk.Frame(tabControl)  # Add a second tab
tabControl.add(tab2, text='Obliczenia zaawansowane')  # Make second tab visible
tab3 = ttk.Frame(tabControl)  # Add a second tab
tabControl.add(tab3, text='Instrukcje do obliczeń')  # Make second tab visible

# Packing the scrollbar before the tabControl
scrollbar = tk.Scrollbar(win)
scrollbar.pack(side = tk.RIGHT, fill = tk.Y)

tabControl.pack(expand=1, fill="both")  # Pack to make visible

#Zakładka instrukcje
dane3 = ttk.LabelFrame(tab3, text=' Instrukcje do obliczeń poglądowych: ')
dane3.grid(column=0, row=0, padx=20, pady=2, sticky='W')
dane4 = ttk.LabelFrame(tab3, text=' Instrukcje do obliczeń zaawansowanych: ')
dane4.grid(column=0, row=4, padx=20, pady=2,sticky='W')
x_label = ttk.Label(dane3, text=" Współczynnik przewodzenia gruntu należy podać z zakresu: 1-5" + "\n " +"Czas pracy sprężarki należy podać z zakresu 2000-3500 [h/rok] ")
x_label.grid(column=0, row=0, sticky='W')
z_label = ttk.Label(dane4, text="1) Białe pola uzupełniane są wartościami wstawianymi przez użytkownika" +
                                "\n" +"2 ) W polu obciążenie gruntu, wartość   + oznacza przepływ do gruntu, zaś  - przepływ z gruntu" +
                                "\n" + "3) Dyfuzyjność cieplna należy podać z przedziału 0.025 - 0.2 m²/dzień" +
                                "\n" +"4) Promień otworu należy umieścić z przedziału 0.05 - 0.1 m" +
                                "\n" + "5) Liczbę otworów należy umieścić z przedziału 4-144" )
z_label.grid(column=0, row=4, sticky='W')

# LabelFrame using tab1 as the parent
dane = ttk.LabelFrame(tab1, text=' Wstaw dane ')
dane.grid(column=0, row=0, padx=8, pady=2)



# Modify adding a Label using dane as the parent instead of win
a_label = ttk.Label(dane, text="Zapotrzebowanie na moc: [W]   ")
a_label.grid(column=0, row=0, sticky='W')

b_label = ttk.Label(dane, text="Czas pracy sprężarki: [h/rok]   ")
b_label.grid(column=2, row=0, sticky='W')

c_label = ttk.Label(dane, text="   ")
c_label.grid(column=1, row=2, sticky='W')

label_dlugosc = ttk.Label(dane)
label_dlugosc.grid(column=1, row=3, sticky='W')

label_moc_cieplna = ttk.Label(dane)
label_moc_cieplna.grid(column=1, row=4, sticky='W')

label_moc_chlodnicza = ttk.Label(dane)
label_moc_chlodnicza.grid(column=1, row=5, sticky='W')



# Adding a Textbox Entry widget
moc = tk.DoubleVar()
moc_entered = ttk.Entry(dane, width=40, textvariable=moc)
moc_entered.grid(column=0, row=1, sticky='W')  # align left/West

sprezarka = tk.DoubleVar()
sprezarka_entered = ttk.Entry(dane, width=24, textvariable=sprezarka)
sprezarka_entered.grid(column=2, row=1, sticky='W')  # align left/West

ttk.Label(dane, text="Współczynnik przewodzenia gruntu: ").grid(column=1, row=0)
number = tk.DoubleVar()
number_entered = ttk.Entry(dane, width=24, textvariable=number)
number_entered.grid(column=1, row=1)


labelResult = tk.Label(win)
labelCieplna = tk.Label(win)
labelChlodnicza = tk.Label(win)


# Create a container to hold labels
buttons_frame = ttk.LabelFrame(dane, text=' Wyniki ')
buttons_frame.grid(column=0, row=8, sticky=tk.W)



action = ttk.Button(buttons_frame, text="Oblicz długość odwiertu",width = 40, command=rownanie1)
action.grid(column=0, row=1,sticky=tk.W)
action = ttk.Button(buttons_frame, text="Oblicz moc cieplną pompy",  width = 40, command=rownanie2)
action.grid(column=0, row=2,sticky=tk.W,)
action = ttk.Button(buttons_frame, text="Oblicz moc chłodniczą dolnego źródła ciepła", width = 40, command=rownanie3)
action.grid(column=0, row=3,sticky=tk.W)
action = ttk.Button(buttons_frame, text="Wykres", width = 40,  command=wykres)
action.grid(column=0, row=5,sticky=tk.W)

# Zakładka druga

dane2 = ttk.LabelFrame(tab2, text=' Zestawienia obliczeń na podstawie stowarzyszenia ASHRAE ')
dane2.grid(column=0, row=0, padx=5, pady=4)

opis1_label = ttk.Label(dane2, text=" Wyniki obliczeń:  "+"\n")
opis1_label.grid(column=2, row=0, sticky='W')
opis1_labe2 = ttk.Label(dane2, text="   "+"\n")
opis1_labe2.grid(column=3, row=0, sticky='W')

scrollbar.config(command = dane2.config)

label_jeden = ttk.Label(dane2)
label_jeden.grid(column=2, row=1, sticky='W')
label_dwa = ttk.Label(dane2)
label_dwa.grid(column=2, row=2, sticky='W')
label_trzy = ttk.Label(dane2)
label_trzy.grid(column=2, row=3, sticky='W')
label_cztery = ttk.Label(dane2)
label_cztery.grid(column=2, row=4, sticky='W')
label_piec = ttk.Label(dane2)
label_piec.grid(column=2, row=5, sticky='W')
label_szesc = ttk.Label(dane2)
label_szesc.grid(column=2, row=6, sticky='W')
label_siedem = ttk.Label(dane2)
label_siedem.grid(column=2, row=7, sticky='W')
label_osiem = ttk.Label(dane2)
label_osiem.grid(column=2, row=8, sticky='W')
label_dziewiec = ttk.Label(dane2)
label_dziewiec.grid(column=2, row=9, sticky='W')
label_dziesiec = ttk.Label(dane2)
label_dziesiec.grid(column=2, row=10, sticky='W')

label_1 = ttk.Label(dane2)
label_1.grid(column=3, row=1, sticky='W')
label_2 = ttk.Label(dane2)
label_2.grid(column=3, row=2, sticky='W')
label_3 = ttk.Label(dane2)
label_3.grid(column=3, row=3, sticky='W')
label_4 = ttk.Label(dane2)
label_4.grid(column=3, row=4, sticky='W')
label_5 = ttk.Label(dane2)
label_5.grid(column=3, row=5, sticky='W')
label_6 = ttk.Label(dane2)
label_6.grid(column=3, row=6, sticky='W')
label_7 = ttk.Label(dane2)
label_7.grid(column=3, row=7, sticky='W')
label_8 = ttk.Label(dane2)
label_8.grid(column=3, row=8, sticky='W')
label_9 = ttk.Label(dane2)
label_9.grid(column=3, row=9, sticky='W')
label_10 = ttk.Label(dane2)
label_10.grid(column=3, row=10, sticky='W')
label_11 = ttk.Label(dane2)
label_11.grid(column=3, row=11, sticky='W')
label_12 = ttk.Label(dane2)
label_12.grid(column=3, row=12, sticky='W')
label_13 = ttk.Label(dane2)
label_13.grid(column=3, row=13, sticky='W')
label_14 = ttk.Label(dane2)
label_14.grid(column=3, row=14, sticky='W')
label_15 = ttk.Label(dane2)
label_15.grid(column=3, row=15, sticky='W')
label_16 = ttk.Label(dane2)
label_16.grid(column=3, row=16, sticky='W')
label_17 = ttk.Label(dane2)
label_17.grid(column=3, row=17, sticky='W')
label_18 = ttk.Label(dane2)
label_18.grid(column=3, row=18, sticky='W')
label_19 = ttk.Label(dane2)
label_19.grid(column=3, row=19, sticky='W')
label_20 = ttk.Label(dane2)
label_20.grid(column=3, row=20, sticky='W')
label_21 = ttk.Label(dane2)
label_21.grid(column=4, row=1, sticky='W')
label_22 = ttk.Label(dane2)
label_22.grid(column=4, row=2, sticky='W')
label_23 = ttk.Label(dane2)
label_23.grid(column=4, row=3, sticky='W')
label_24 = ttk.Label(dane2)
label_24.grid(column=4, row=4, sticky='W')
label_25 = ttk.Label(dane2)
label_25.grid(column=4, row=5, sticky='W')
label_26 = ttk.Label(dane2)
label_26.grid(column=4, row=6, sticky='W')
label_27 = ttk.Label(dane2)
label_27.grid(column=4, row=7, sticky='W')
label_28 = ttk.Label(dane2)
label_28.grid(column=4, row=8, sticky='W')
label_29 = ttk.Label(dane2)
label_29.grid(column=4, row=9, sticky='W')
label_30 = ttk.Label(dane2)
label_30.grid(column=4, row=10, sticky='W')
label_31 = ttk.Label(dane2)
label_31.grid(column=4, row=11, sticky='W')
label_32 = ttk.Label(dane2)
label_32.grid(column=4, row=12, sticky='W')
label_33 = ttk.Label(dane2)
label_33.grid(column=4, row=13, sticky='W')
label_34 = ttk.Label(dane2)
label_34.grid(column=4, row=14, sticky='W')
label_35 = ttk.Label(dane2)
label_35.grid(column=4, row=15, sticky='W')
label_36 = ttk.Label(dane2)
label_36.grid(column=4, row=16, sticky='W')
label_37 = ttk.Label(dane2)
label_37.grid(column=4, row=17, sticky='W')
label_38 = ttk.Label(dane2)
label_38.grid(column=4, row=18, sticky='W')
label_39 = ttk.Label(dane2)
label_39.grid(column=4, row=19, sticky='W')

a0_label = ttk.Label(dane2, text="   ")
a0_label.grid(column=0, row=0, sticky='W')
a1_label = ttk.Label(dane2, text="Maksymalne godzinowe obciążenie gruntu: [W] ")
a1_label.grid(column=0, row=1, sticky='W')
a2_label = ttk.Label(dane2, text="Miesięczne obciążenie gruntu: [W] ")
a2_label.grid(column=0, row=2, sticky='W')
a3_label = ttk.Label(dane2, text="Roczne średnie obciążenie gruntu: [W]")
a3_label.grid(column=0, row=3, sticky='W')
a4_label = ttk.Label(dane2, text="Przewodność cieplna: [W/(m•K)]   ")
a4_label.grid(column=0, row=4, sticky='W')
a5_label = ttk.Label(dane2, text="Dyfuzyjność cieplna: [m^2/day]   ")
a5_label.grid(column=0, row=5, sticky='W')
a6_label = ttk.Label(dane2, text="Niezakłócona temperatura gruntu: [°C]   ")
a6_label.grid(column=0, row=6, sticky='W')
a7_label = ttk.Label(dane2, text="Pojemność cieplna ciepła: [J/kg•K]   ")
a7_label.grid(column=0, row=7, sticky='W')
a8_label = ttk.Label(dane2, text="Całkowite natężenie przepływu godzinnego obciążenia gruntu: [(kg•s)/W]   ")
a8_label.grid(column=0, row=8, sticky='W')
a9_label = ttk.Label(dane2, text="Maksymalna / minimalna temperatura na wlocie pompy ciepła: [°C]   ")
a9_label.grid(column=0, row=9, sticky='W')
a10_label = ttk.Label(dane2, text="Promień otworu: [m]   ")
a10_label.grid(column=0, row=10, sticky='W')
a11_label = ttk.Label(dane2, text="Wewnętrzny promień rury: [m]   ")
a11_label.grid(column=0, row=11, sticky='W')
a12_label = ttk.Label(dane2, text="Zewnętrzny promień rury: [m]   ")
a12_label.grid(column=0, row=12, sticky='W')
a13_label = ttk.Label(dane2, text="Gruntowa przewodność cieplna: [W/(m•K)]   ")
a13_label.grid(column=0, row=13, sticky='W')
a14_label = ttk.Label(dane2, text="Przewodność cieplna rury: [W]   ")
a14_label.grid(column=0, row=14, sticky='W')
a15_label = ttk.Label(dane2, text="Odległość między środkami rur: [W]   ")
a15_label.grid(column=0, row=15, sticky='W')
a16_label = ttk.Label(dane2, text="Współczynnik wewnętrznej konwekcji: [W]   ")
a16_label.grid(column=0, row=16, sticky='W')
a17_label = ttk.Label(dane2, text="   ")
a17_label.grid(column=0, row=17, sticky='W')
a18_label = ttk.Label(dane2, text="Dodatkowe parametry dla wielu otworów:   ")
a18_label.grid(column=0, row=18, sticky='W')
a19_label = ttk.Label(dane2, text="Odległość między odwiertami: [W]   ")
a19_label.grid(column=0, row=19, sticky='W')
a20_label = ttk.Label(dane2, text="Liczba odwiertów: [W]   ")
a20_label.grid(column=0, row=20, sticky='W')
a21_label = ttk.Label(dane2, text="Współczynnik proporcji pola z odwiertami:    ")
a21_label.grid(column=0, row=21, sticky='W')

b0_label = ttk.Label(dane2, text="Dane:    ")
b0_label.grid(column=1, row=0, sticky='W')
b1 = tk.DoubleVar()
b1_entered = ttk.Entry(dane2, width=30, textvariable=b1)
b1_entered.grid(column=1, row=1, sticky='W')  # align left/West
b2 = tk.DoubleVar()
b2_entered = ttk.Entry(dane2, width=30, textvariable=b2)
b2_entered.grid(column=1, row=2, sticky='W')  # align left/West
b3 = tk.DoubleVar()
b3_entered = ttk.Entry(dane2, width=30, textvariable=b3)
b3_entered.grid(column=1, row=3, sticky='W')  # align left/West
b4 = tk.DoubleVar()
b4_entered = ttk.Entry(dane2, width=30, textvariable=b4)
b4_entered.grid(column=1, row=4, sticky='W')  # align left/West
b5 = tk.DoubleVar()
b5_entered = ttk.Entry(dane2, width=30, textvariable=b5)
b5_entered.grid(column=1, row=5, sticky='W')  # align left/West
b6 = tk.DoubleVar()
b6_entered = ttk.Entry(dane2, width=30, textvariable=b6)
b6_entered.grid(column=1, row=6, sticky='W')  # align left/West
b7 = tk.DoubleVar()
b7_entered = ttk.Entry(dane2, width=30, textvariable=b7)
b7_entered.grid(column=1, row=7, sticky='W')  # align left/West
b8 = tk.DoubleVar()
b8_entered = ttk.Entry(dane2, width=30, textvariable=b8)
b8_entered.grid(column=1, row=8, sticky='W')  # align left/West
b9 = tk.DoubleVar()
b9_entered = ttk.Entry(dane2, width=30, textvariable=b9)
b9_entered.grid(column=1, row=9, sticky='W')  # align left/West
b10 = tk.DoubleVar()
b10_entered = ttk.Entry(dane2, width=30, textvariable=b10)
b10_entered.grid(column=1, row=10, sticky='W')  # align left/West
b11 = tk.DoubleVar()
b11_entered = ttk.Entry(dane2, width=30, textvariable=b11)
b11_entered.grid(column=1, row=11, sticky='W')  # align left/West
b12 = tk.DoubleVar()
b12_entered = ttk.Entry(dane2, width=30, textvariable=b12)
b12_entered.grid(column=1, row=12, sticky='W')  # align left/West
b13 = tk.DoubleVar()
b13_entered = ttk.Entry(dane2, width=30, textvariable=b13)
b13_entered.grid(column=1, row=13, sticky='W')  # align left/West
b14 = tk.DoubleVar()
b14_entered = ttk.Entry(dane2, width=30, textvariable=b14)
b14_entered.grid(column=1, row=14, sticky='W')  # align left/West
b15 = tk.DoubleVar()
b15_entered = ttk.Entry(dane2, width=30, textvariable=b15)
b15_entered.grid(column=1, row=15, sticky='W')  # align left/West
b16 = tk.DoubleVar()
b16_entered = ttk.Entry(dane2, width=30, textvariable=b16)
b16_entered.grid(column=1, row=16, sticky='W')  # align left/West
b17 = tk.DoubleVar()
b17_entered = ttk.Entry(dane2, width=30, textvariable=b17)
b17_entered.grid(column=1, row=19, sticky='W')  # align left/West
b18 = tk.DoubleVar()
b18_entered = ttk.Entry(dane2, width=30, textvariable=b18)
b18_entered.grid(column=1, row=20, sticky='W')  # align left/West
b19 = tk.DoubleVar()
b19_entered = ttk.Entry(dane2, width=30, textvariable=b19)
b19_entered.grid(column=1, row=21, sticky='W')  # align left/West


label_blad0 = ttk.Label(dane)
label_blad0.grid(column=1, row=6, sticky='W')
label_blad01 = ttk.Label(dane2)
label_blad01.grid(column=1, row=23, sticky='W')

label_opis = ttk.Label(dane2)
label_opis.grid(column=2, row=1, sticky='W')

 #Create a container to hold labels
buttons_frame2 = ttk.LabelFrame(dane2, text=' Wyniki ')
buttons_frame2.grid(column=0, row=23, sticky=tk.W)

action = ttk.Button(buttons_frame2, text="Obliczenia dla pojedyńczego otworu",width = 40, command=row_jeden)
action.grid(column=0, row=24,sticky=tk.W)
action = ttk.Button(buttons_frame2, text="Obliczenia dla wielu otworów",  width = 40, command=row_wiele)
action.grid(column=0, row=25,sticky=tk.W,)

win.mainloop()
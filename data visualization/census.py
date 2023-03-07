import matplotlib.pyplot as plt
from matplotlib.widgets import RadioButtons
from matplotlib.offsetbox import AnchoredText
import pandas as pd
import numpy as np
import os
import math
from clean_data import data_country, data_region, data_world, merge_country_continent


#comentar el codigo
#limpiar codigo de clean data


os.system("cls")
plt.style.use("seaborn")


def filter_df(dataset, zone):
    tempdata = (dataset.loc[dataset["Zone"] == zone])
    return(tempdata)

def stats_calculation(x,y,dataset,atribute,zone):
    x=x.to_numpy()
    y= y.to_numpy()
    xm=np.mean(x)
    ym=np.mean(y)
    xx=np.square(x)
    yy=np.square(y)
    xy=np.multiply(x,y)
    
    xxm=np.mean(xx)
    yym=np.mean(yy)
    xym=np.mean(xy)
    s2x= (xxm-(xm*xm))
    s2y= (yym-(ym*ym))
    sxy=(xym-(xm*ym))

    rxy=sxy/(math.sqrt(s2x)*math.sqrt(s2y))
    r2=round(rxy*rxy,4)
        
    b=round(sxy/s2x,2)
    a=round(ym-(b*xm),2)
    mean= round(filter_df(dataset, zone)[atribute].mean(),2)
    std= round(filter_df(dataset, zone)[atribute].std(),2)
    stats={"r2":r2,"a":a,"b":b,"mean":mean,"std":std}
    return stats



def line_graph(dataset,zone,atribute,yaxis,):
    

    stats=stats_calculation(filter_df(dataset, zone)["Year"],filter_df(dataset, zone)[atribute],dataset,atribute,zone)
    fig, ax = plt.subplots(figsize=(10, 6))
    fig.subplots_adjust(left=0.25)
    ax.set_title(f"{atribute}\n {zone}")
    ax.ticklabel_format(style='plain')
    ax.plot(filter_df(dataset, zone)["Year"], filter_df(dataset, zone)[atribute],"b-")
    if stats["r2"]<=0.5:
        
        box=AnchoredText(f"R^2= {stats['r2']}\n Poor coefficient of determination \nY = {stats['b']}x {stats['a']}", prop=dict(size=10),frameon=True, loc='upper left')

    else:
        ax.plot(filter_df(dataset, zone)["Year"],stats["b"]*filter_df(dataset, zone)["Year"]+stats["a"],"g:")
        box=AnchoredText(f"R^2= {stats['r2']}\nY = {stats['b']}x {stats['a']}", prop=dict(size=10),frameon=True, loc='upper left')
        
    ax.set_xlabel("Years")
    ax.set_ylabel(yaxis)


    box.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
    ax.add_artist(box)

    ax_text = plt.axes([0.025, 0.40, 0.125, 0.3])
    ax_text.set_xticks([])
    ax_text.set_yticks([])
    total_last_year = dataset.loc[(dataset["Zone"] == zone) & (dataset["Year"] == 2021)]
    total_last_year = int(total_last_year[atribute].values)
    ax_text.annotate(text=(yaxis+" 2021"), xy=(0.1, 0.9))
    ax_text.annotate(text=total_last_year, xy=(0.1, 0.80))

    if dataset.equals(data_region)==True:
            count = merge_country_continent.groupby(
                "continent").size()[zone]
            ax_text.annotate(text="Regions", xy=(0.1, 0.70))
            ax_text.annotate(text=count, xy=(0.1, 0.60)) 

    if dataset.equals(data_country)==True:
            continent=merge_country_continent.loc[merge_country_continent["country"]==zone]["continent"]
            ax_text.annotate(text="Continent", xy=(0.1, 0.70))
            ax_text.annotate(text=continent.squeeze(), xy=(0.1, 0.60)) 

    ax_text.annotate(text="mean", xy=(0.1, 0.5))
    ax_text.annotate(text=round(stats["mean"],2), xy=(0.1, 0.40))
    ax_text.annotate(text="std", xy=(0.1, 0.3))
    ax_text.annotate(text=round(stats["std"],2), xy=(0.1, 0.2))

    plt.show()

def bar_graph(dataset,zone,atribute1,atribute2,title,atribute1_abb,atribute2_abb):
    #stats=stats_calculation(filter_df(dataset, zone)["Year"],filter_df(dataset, zone)[atribute],dataset,atribute)
    fig, ax = plt.subplots(figsize=(10, 6))
    data_atribute1_atribute2 =dataset.loc[(dataset["Year"].mod(10)==0) & (dataset["Zone"]==zone)]
    print(data_atribute1_atribute2)

    

    fig.subplots_adjust(left=0.25)
    ax.set_title(f"{title}\n {zone}")
    ax.ticklabel_format(style='plain')


    index =np.arange(len(data_atribute1_atribute2))
    bar_width = 0.35


    ax.bar(index - bar_width/2, filter_df(data_atribute1_atribute2, zone)[atribute1],color="steelblue",width=bar_width)
    ax.bar(index + bar_width/2, filter_df(data_atribute1_atribute2, zone)[atribute2],color="tomato",width=bar_width)
    ax.set_xticks(index,  filter_df(data_atribute1_atribute2, zone)["Year"])

    ax_pie = plt.axes([0.025, 0.40, 0.125, 0.3])
    ax_pie.set_xticks([])
    ax_pie.set_yticks([])


    ax_pie.set_title("Year 2021")

   
    slices_value=[filter_df(data_atribute1_atribute2, zone)[atribute1].tail(1).squeeze(),
    filter_df(data_atribute1_atribute2, zone)[atribute2].tail(1).squeeze()]

    ax_pie.pie(slices_value, explode=[0,0.25] , autopct='%1.1f%%',
            shadow=True, startangle=90,textprops=None,colors=["steelblue","tomato"])
    
    ax_pie.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax_pie.legend([atribute1_abb, atribute2_abb],loc='lower center', bbox_to_anchor=(0.5, -0.3),ncol=1, fancybox=True, shadow=True)

    plt.show()
    print()



def menu():
    while True:
            
        print("0. World")
        print("1.Region")
        print("2.Country/Area")
        print()

        try:
            data=int(input("select a region to visualize"))
            
        except ValueError:
            print("Oops!  That was no valid option.  Try again...")

                
        if data==1:
            data='Region'
            data=data_region
            break
        
        elif data==2:
            data='Country/Area'
            data=data_country
            break

        else:
            print("Oops!  That was no valid option.  Try again...")
    
    while True:
        print()
        options={}
        
        for index ,name  in enumerate(data["Zone"].unique()):
            print(index,name)
            options[index]=name
        try:
            zone= int(input("Select a Zone to visual"))
            
        except ValueError:
            print("Oops!  That was no valid option.  Try again...")
        
        
        if zone in options:
            zone=options[zone]
            break
        else:
            print("Oops!  That was no valid option.  Try again...")

    while True:
        print("Select an attribute to visualize")
        print("1.Total Population (line chart)")
        print("2.Male vs Female population (bar chart)") 
        print("3.Population Density")
        print("4.Median Age (line chart)")
        print("5.Total Deaths (line chart)")
        print("6.Male vs Female Deaths (bar chart)") 
        print("7.Total Births (line chart)")
        print("8.Births vs Deaths (bar)")
        print("9.Exit")
        print("0.Choose other country")

        try:
            attribute= int(input("Select a Zone to visual"))
            
        except ValueError:
            print("Oops!  That was no valid option.  Try again...")

        
        if attribute==1:
            line_graph(data,zone,"Total Population, as of 1 July (thousands)","T.Population (thousands)")

        if attribute==2:
            bar_graph(data,zone,"Male Population, as of 1 July (thousands)","Female Population, as of 1 July (thousands)","Male vs Female Population (thousands)","Male Population","Female Population"  )
            

        if attribute==3:
            pass

        if attribute==4:
            line_graph(data,zone,"Median Age, as of 1 July (years)","M.Age (years)")
            

        if attribute==5:
            line_graph(data,zone,"Total Deaths (thousands)","T.Deaths (thousands)")

            

        if attribute==6:
            bar_graph(data,zone,"Male Deaths (thousands)","Female Deaths (thousands)","Male vs Female Deaths (thousands)","Male Deaths","Female Deaths")
            

        if attribute==7:
            line_graph(data,zone,"Births (thousands)","Births (thousands)")
            

        if attribute==8:
            bar_graph(data,zone,"Births (thousands)","Total Deaths (thousands)", "Births vs Deaths (thousands)","Births","Deaths")
        
        if attribute==9:
            break
        if attribute==0:
            menu()

        



        


menu()


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


#open census file

data= pd.read_csv(r"census-onu.csv",low_memory=False)


#We will work only with total populaton, male population, female population, population density, median age,births,total deaths
#there are other important columns but can be easily calculated and for practical terms will be calculated

data=data[["Region, subregion, country or area *","Type","Year","Total Population, as of 1 July (thousands)",
    "Male Population, as of 1 July (thousands)","Female Population, as of 1 July (thousands)",
    "Population Density, as of 1 July (persons per square km)","Median Age, as of 1 July (years)",
    "Births (thousands)","Total Deaths (thousands)"	,"Male Deaths (thousands)"	,"Female Deaths (thousands)" ]]



data["Type"].unique()

#we are going to work only with world, region, country/area
data=data.loc[(data.Type =="World"  ) |  (data.Type =="Region") |  (data.Type =="Country/Area") ]



#looking for values that are incomplete

incomplete = data[data.isin(["..."]).any(axis=1)]
incomplete["Region, subregion, country or area *"].unique()


#dropping incomplete values

data=data.loc[data["Region, subregion, country or area *"]!= 'Holy See' ]
data[data.isin(["..."]).any(axis=1)]


for col in data.columns:

    if data[col].dtype == "object" and col!= "Region, subregion, country or area *" and col!="Type":
        data[col]=data[col].str.replace(" ","").astype(np.float64)

#verifying not null spaces
data[data.isnull().any(axis=1)]

#spliting datatween world region or area
data=data.rename(columns={"Region, subregion, country or area *":"Zone"})
data_world=data.loc[(data.Type =="World"  ) ].drop(columns="Type")
data_region=data.loc[(data.Type =="Region" ) ].drop(columns="Type")
data_country=data.loc[(data.Type =="Country/Area") ].drop(columns="Type")


for count,zone in enumerate(data["Type"].unique()): print(count,zone)

data_region["Zone"].unique()


# read country_region file

country_region= pd.read_csv(r"country_continent.csv",low_memory=False)


#giving the same format to country_region and data_region

data_region.loc[data_region["Zone"]=="LATIN AMERICA AND THE CARIBBEAN","Zone"]= "S. America"
data_region.loc[data_region["Zone"]=="NORTHERN AMERICA","Zone"]= "N. America"

country_region.loc[country_region["continent"]=="North America", "continent"] = "N. America"
country_region.loc[country_region["continent"]=="South America", "continent"] = "S. America"

for name in data_region["Zone"].unique():
    data_region.loc[data_region["Zone"]==name,"Zone"]= name.title()


#looking for na values in data_country


merge_country_continent=pd.merge(data_country,country_region, how="outer",left_on="Zone",right_on="country")
merge_country_continent=merge_country_continent[["Zone","country","continent"]]
null_merge=merge_country_continent[merge_country_continent.isnull().any(axis=1)]

#Matching names 
country_region.loc[country_region["country"]=="United States", "country"] = "United States of America"
country_region.loc[country_region["country"]=="Falkland Islands", "country"] = "Falkland Islands (Malvinas)"
country_region.loc[country_region["country"]=="DR Congo", "country"] = "Congo"
country_region.loc[country_region["country"]=="Cape Verde", "country"] = "Cabo Verde"
country_region.loc[country_region["country"]=="Brunei", "country"] = "Brunei Darussalam"

data_country.loc[data_country["Zone"]=="T\x81rkiye","Zone"] = "Turkey"
data_country.loc[data_country["Zone"]=="C?te d'Ivoire","Zone"] = "Ivory Coast"
data_country.loc[data_country["Zone"]=="China, Macao SAR","Zone"] = "Macau"
data_country.loc[data_country["Zone"]=="Democratic Republic of the Congo","Zone"] = "Republic of the Congo"
data_country.loc[data_country["Zone"]=="Czechia","Zone"] = "Czech Republic"
data_country.loc[data_country["Zone"]=="Republic of Moldova","Zone"] = "Moldova"
data_country.loc[data_country["Zone"]=="R?union","Zone"] = "Reunion"
data_country.loc[data_country["Zone"]=="China, Hong Kong SAR","Zone"] = "Hong Kong"
data_country.loc[data_country["Zone"]=="State of Palestine","Zone"] = "Palestine"
data_country.loc[data_country["Zone"]=="United Republic of Tanzania","Zone"] = "Tanzania"
data_country.loc[data_country["Zone"]=="Bolivia (Plurinational State of)","Zone"] = "Bolivia"
data_country.loc[data_country["Zone"]=="Venezuela (Bolivarian Republic of)","Zone"] = "Venezuela"
data_country.loc[data_country["Zone"]=="Iran (Islamic Republic of)","Zone"] = "Iran"
data_country.loc[data_country["Zone"]=="Dem. People's Republic of Korea","Zone"] = "North Korea"
data_country.loc[data_country["Zone"]=="Republic of Korea","Zone"] = "South Korea"
data_country.loc[data_country["Zone"]=="Viet Nam","Zone"] = "Vietnam"
data_country.loc[data_country["Zone"]=="Russian Federation","Zone"] = "Russia"
data_country.loc[data_country["Zone"]=="Syrian Arab Republic","Zone"] = "Syria"
data_country.loc[data_country["Zone"]=="Lao People's Democratic Republic","Zone"] = "Laos"
data_country.loc[data_country["Zone"]=="Saint Martin (French part)","Zone"] = "Saint Martin"
data_country.loc[data_country["Zone"]=="Wallis and Futuna Islands","Zone"] = "Wallis and Futuna"
data_country.loc[data_country["Zone"]=="Sint Maarten (Dutch part)","Zone"] = "Sint Maarten"
data_country.loc[data_country["Zone"]=="Cura?ao","Zone"] = "Curacao"
data_country.loc[data_country["Zone"]=="Saint Barth?lemy","Zone"] = "Saint Barthelemy"
data_country.loc[data_country["Zone"]=="China, Taiwan Province of China","Zone"] = "Taiwan"
data_country.loc[data_country["Zone"]=="Micronesia (Fed. States of)","Zone"] = "Micronesia"
data_country.loc[data_country["Zone"]=="Bonaire, Sint Eustatius and Saba","Zone"] = "Bonaire"
data_country.loc[data_country["Zone"]=="Kosovo (under UNSC res. 1244)","Zone"] = "Kosovo"


data_country=data_country.sort_values(["Zone","Year"])

missing_countrys= pd.DataFrame({"continent":["Africa", "Europe",'S. America' ],
                         "country":["Saint Helena", 'Kosovo', 'Bonaire']})


country_region = pd.concat([country_region,missing_countrys],ignore_index=True)

merge_country_continent=pd.merge(data_country,country_region, how="outer",left_on="Zone",right_on="country")
merge_country_continent = merge_country_continent.loc[merge_country_continent["Year"]==2021]
merge_country_continent=merge_country_continent[["Zone","country","continent"]]

null_merge=merge_country_continent[merge_country_continent.isnull().any(axis=1)]

null_merge = null_merge.loc[null_merge["country"]!='Vatican City']

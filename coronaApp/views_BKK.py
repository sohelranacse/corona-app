from django.shortcuts import render
from django.http import HttpResponse

# importing the required libraries
import pandas as pd
import numpy as np
import json
import datetime

# Visualization libraries
import plotly.express as px
import plotly.graph_objects as go

# Create your views here.
df3=pd.read_json('https://cdn.jsdelivr.net/gh/highcharts/highcharts@v7.0.0/samples/data/world-population-density.json')
df_data= pd.read_excel('https://github.com/sohelranacse/analysis-data/blob/main/daily-sales-collection.xlsx?raw=true')

def index(request):
    confirmedGlobal=pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv',encoding='utf-8',na_values=None)
    # deathGLobal=pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
    # recoverGlobal=pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')
    uniqueCountryNames=pd.unique(confirmedGlobal['Country/Region'])
    contryNames,countsVal,logVals,overallCount,dataForMapGraph,maxVal=getBarData(confirmedGlobal,uniqueCountryNames)
    dataForheatMap,dateCat=getHeatMapData(confirmedGlobal,contryNames)
    datasetForLine,axisvalues=getLinebarGroupData(confirmedGlobal,uniqueCountryNames)
    context={'dateCat':dateCat,'dataForheatMap':dataForheatMap,'maxVal':maxVal,'dataForMapGraph':dataForMapGraph,'axisvalues':axisvalues,'datasetForLine':datasetForLine,'uniqueCountryNames':uniqueCountryNames,'contryNames':contryNames,'countsVal':countsVal,'logVals':logVals,'overallCount':overallCount}
    return render(request,'index.html',context)
    

def getBarData(confirmedGlobal,uniqueCountryNames):
    df2=confirmedGlobal[list(confirmedGlobal.columns[1:2])+list([confirmedGlobal.columns[-2]])]
    df2.columns=['Country/Region','values']
    df2=df2.sort_values(by='values',ascending=False)
    contryNames=list(df2['Country/Region'].values)
    countsVal=list(df2['values'].values)
    maxVal=max(countsVal)
    overallCount=sum(countsVal)
    logVals=list(np.log(ind) if ind != 0 else 0 for ind in countsVal )
    dataForMapGraph=getDataforMap(uniqueCountryNames,df2)
    # dictVal=[]
    # for i in range(df2.shape[0]):
    #     dictVal.append(dict(df2.ix[i]))
    return (contryNames,countsVal,logVals,overallCount,dataForMapGraph,maxVal)

def getLinebarGroupData(confirmedGlobal,uniqueCountryNames):
    colNames=confirmedGlobal.columns[4:-1]
    datasetsForLine=[]
    for i in uniqueCountryNames:
        temp={}
        temp['label']=i
        temp['fill']='false'
        temp['data']=confirmedGlobal[confirmedGlobal['Country/Region']==i][colNames].sum().values.tolist()
        datasetsForLine.append(temp)
    return datasetsForLine,list(range(len(colNames)))

def getDataforMap(uniqueCOuntryName,df2):
    dataForMap=[]
    for i in uniqueCOuntryName:
        try:
            tempdf=df3[df3['name']==i]
            temp={}
            temp["code3"]=list(tempdf['code3'].values)[0]
            temp["name"]=i
            temp["value"]=df2[df2['Country/Region']==i]['values'].sum()
            temp["code"]=list(tempdf['code'].values)[0]
            dataForMap.append(temp)
        except:
            pass
    print (len(dataForMap))
    return dataForMap


def getHeatMapData(confirmedGlobal,contryNames):
    df3=confirmedGlobal[list(confirmedGlobal.columns[1:2])+list(list(confirmedGlobal.columns.values)[-6:-1])]
    dataForheatMap=[]
    for i in contryNames:
        try:
            tempdf=df3[df3['Country/Region']==i]
            temp={}
            temp["name"]=i
            temp["data"]=[{'x':j,'y':k} for j,k in zip(tempdf[tempdf.columns[1:]].sum().index,tempdf[tempdf.columns[1:]].sum().values)]
            dataForheatMap.append(temp)
        except:
            pass
    dateCat=list(list(confirmedGlobal.columns.values)[-6:-1])
    return dataForheatMap,dateCat


def drillDownACountry(request):
    print (request.POST.dict())
    countryName=request.POST.get('countryName')
    confirmedGlobal=pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv',encoding='utf-8',na_values=None)
    countryDataSpe=pd.DataFrame(confirmedGlobal[confirmedGlobal['Country/Region']==countryName][confirmedGlobal.columns[4:-1]].sum()).reset_index()
    countryDataSpe.columns=['country','values']
    countryDataSpe['lagVal']=countryDataSpe['values'].shift(1).fillna(0)
    countryDataSpe['incrementVal']=countryDataSpe['values']-countryDataSpe['lagVal']
    countryDataSpe['rollingMean']=countryDataSpe['incrementVal'].rolling(window=4).mean()
    countryDataSpe=countryDataSpe.fillna(0)
    datasetsForLine=[{'yAxisID': 'y-axis-1','label':'Daily Cumulated Data','data':countryDataSpe['values'].values.tolist(),'borderColor':'#03a9fc','backgroundColor':'#03a9fc','fill':'false'},
                    {'yAxisID': 'y-axis-2','label':'Rolling Mean 4 days','data':countryDataSpe['rollingMean'].values.tolist(),'borderColor':'#fc5203','backgroundColor':'#fc5203','fill':'false'}]
    axisvalues=countryDataSpe.index.tolist()
    uniqueCountryNames=pd.unique(confirmedGlobal['Country/Region'])
    contryNames,countsVal,logVals,overallCount,dataForMapGraph,maxVal=getBarData(confirmedGlobal,uniqueCountryNames)
    dataForheatMap,dateCat=getHeatMapData(confirmedGlobal,contryNames)
    context=context={"countryName":countryName,'axisvalues':axisvalues,'datasetsForLine':datasetsForLine,'dateCat':dateCat,'dataForheatMap':dataForheatMap,'maxVal':maxVal,'dataForMapGraph':dataForMapGraph,'uniqueCountryNames':uniqueCountryNames,'contryNames':contryNames,'countsVal':countsVal,'logVals':logVals,'overallCount':overallCount}

    return render(request,'index2.html',context)

def mytest(request):
    df = df_data.copy()
    df.reset_index()
    df.sort_values(by=['Center Name'], inplace=True) # sorting by sales center
    df_final = df.rename(columns={'No.': 'No', 'Center Name': 'Center_Name', 'Collection(%)': 'Collection_Percentage', 'Overall Collection(%)': 'Overall_Collection_Percentage' })
    context = {'Center_Name': list(df_final["Center_Name"]), 'Collection': list(df_final["Collection"])}
    return render(request,'mytest.html', context)


def plotly_graph(request):

    df = df_data.copy()
    df.reset_index()
    df.sort_values(by=['Center Name'], inplace=True) # sorting by sales center
    df_final = df.rename(columns={'No.': 'No', 'Center Name': 'Center_Name', 'Collection(%)': 'Collection_Percentage', 'Overall Collection(%)': 'Overall_Collection_Percentage' })

    # Generate a list of random numbers
    x = list(df_final["Center_Name"])
    y = list(df_final["Collection"])

    # Bar chart colors
    # colors = '#03a9fc'

    # Create a trace json to hold graph data
    trace = {
        'x': x,
        'y': y,
        'type': 'bar',
        # 'type': 'scatter',
        'name': x,
        'marker': {'color': '#03a9fc'}

    }

    # Configure the chart's layout
    layout = {
        'title': {
            'text': 'Sales Center Collections',
            'font': {
                'color': '#000'
            }
        },
        # 'xaxis': {'title': 'X-axis', 'color': '#DCDCDC', 'mirror': 'true', 'showline': 'false'},
        # 'yaxis': {'title': 'Y-axis', 'color': '#DCDCDC', 'mirror': 'true', 'showline': 'true'},
        'xaxis': {'title': 'Sales Center', 'color': '#888', 'titlefont':{'size':18}, 'automargin': 'true'},
        'yaxis': {'title': 'Collection Amount', 'color': '#888', 'titlefont':{'size':18}, 'automargin': 'true'},
        'plot_bgcolor': 'rgb(230, 230, 230)'
        # 'autosize': 'false',
        # 'width': '1300',
        # 'height': '600'
    }

    # Pass trace and layout in the context
    context = {
        "trace": trace,
        "layout": layout,
        "title": "Sales Center Collection"
    }

    return render(request, "plotly_graph.html", context)



# def home(request):
#     return render(request, 'home.html')
def worldWide(request):
    return render(request, 'home.html')
def world(request):
    return render(request, 'world.html')
def asia(request):
    return render(request, 'asia.html')
def europe(request):
    return render(request,'europe.html')
def africa(request):
    return render(request,'africa.html')
def australia(request):
    return render(request,'australia.html')
def southAmerica(request):
    return render(request,'southAmerica.html')
def northAmerica(request):
    return render(request,'northAmerica.html')

    
def stats(request):
    return render(request,'stats.html')


# my country 
def bangladesh(request):

    #main data
    df = pd.read_json('http://wuhan-coronavirus-api.laeyoung.endpoint.ainize.ai/jhu-edu/timeseries?onlyCountries=true&iso3=BGD')['timeseries']
    df = pd.DataFrame(list(df))
    df_new = df.rename(index={0: 'column1'})
    df_new = df_new.T # Transpose column
    df_new_data = pd.DataFrame(list(df_new['column1']))
    df_new_data['Date'] = df_new.index
    df_new_data = df_new_data.rename(columns={'confirmed':'Confirmed','deaths':'Deaths','recovered':'Recovered'})
    df_new_data['New_Confirmed'] = df_new_data.Confirmed.diff().fillna(0).apply(lambda x : x if x > 0 else 0)
    df_new_data['New_Recovered'] = df_new_data.Recovered.diff().fillna(0).apply(lambda x : x if x > 0 else 0)
    df_new_data['New_Deaths'] = df_new_data.Deaths.diff().fillna(0).apply(lambda x : x if x > 0 else 0)
    df = df_new_data[['Date', 'New_Confirmed', 'Confirmed', 'New_Recovered', 'Recovered', 'New_Deaths', 'Deaths']].query('Confirmed > 0')
    df['Date'] = pd.to_datetime(df['Date'])
    df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')
    df.sort_values(by=['Date'], inplace=True)
    # print(df.tail())

    df_30 = df.tail(30)
    # df_30['Date'] = df_30['Date'].dt.strftime('%Y-%m-%d')


    # Create a trace json to hold graph data
    trace = {
        'x': list(df_30["Date"]),
        'y': list(df_30["New_Confirmed"]),
        'type': 'bar',
        'name': 'Confirmed',
        'marker': {
            'color': '#7163F1',
            'width': 1
        }
        # 'orientation': 'h'
    }
    trace2 = {
        'x': list(df_30["Date"]),
        'y': list(df_30["New_Recovered"]),
        'type': 'bar',
        'name': 'Recovered',
        'marker': {
            'color': '#2ECBAC',
            'width': 1
        }
    }
    trace3 = {
        'x': list(df_30["Date"]),
        'y': list(df_30["New_Deaths"]),
        'type': 'bar',
        'name': 'Death',
        'marker': {
            'color': '#F54251',
            'width': 1
        }
    }

    # for scatter
    traceS = {
        'x': list(df_30["Date"]),
        'y': list(df_30["New_Confirmed"]),
        'type': 'scatter',
        'name': 'Confirmed',
        'marker': {
            'color': '#7163F1',
            'width': 1
        }
        # 'orientation': 'h'
    }
    trace2S = {
        'x': list(df_30["Date"]),
        'y': list(df_30["New_Recovered"]),
        'type': 'scatter',
        'name': 'Recovered',
        'marker': {
            'color': '#2ECBAC',
            'width': 1
        }
    }
    trace3S = {
        'x': list(df_30["Date"]),
        'y': list(df_30["New_Deaths"]),
        'type': 'scatter',
        'name': 'Death',
        'marker': {
            'color': '#F54251',
            'width': 1
        }
    }

    
    # past 30 days chart
    tracePast = {
        'x': list(df_30["Date"]),
        'y': list(df_30["Confirmed"]),
        'type': 'bar',
        'name': 'Confirmed',
        'marker': {
            'color': '#7163F1',
            'width': 1
        }
        # 'orientation': 'h'
    }
    trace2Past = {
        'x': list(df_30["Date"]),
        'y': list(df_30["Recovered"]),
        'type': 'bar',
        'name': 'Recovered',
        'marker': {
            'color': '#2ECBAC',
            'width': 1
        }
    }
    trace3Past = {
        'x': list(df_30["Date"]),
        'y': list(df_30["Deaths"]),
        'type': 'bar',
        'name': 'Death',
        'marker': {
            'color': '#F54251',
            'width': 1
        }
    }

    # Configure the chart's layout
    layout = {
        'title': {
            'text': 'Daily Incidences Chart',
            'font': {
                'color': '#000',
                'size': 14
            }
        },
        'xaxis': {
            'title': 'Date',
            'color': '#888', 
            'titlefont':{'size':12}, 
            'automargin': 'true', 
            'showline': 'true'
        },
        'yaxis': {
            'title': '', 
            'color': '#888', 
            'titlefont':{'size':12}, 
            'automargin': 'true', 
            'showline': 'true'
        },
        'height': '400',
        'barmode': 'stack'
    }

    # layout for past 30 days
    layoutPast = {
        'title': {
            'text': 'Past 30 Days',
            'font': {
                'color': '#000',
                'size': 14
            }
        },
        'xaxis': {
            'title': 'Date',
            'color': '#888', 
            'titlefont':{'size':12}, 
            'automargin': 'true', 
            'showline': 'true'
        },
        'yaxis': {
            'title': '', 
            'color': '#888', 
            'titlefont':{'size':12}, 
            'automargin': 'true', 
            'showline': 'true'
        },
        'height': '400',
        'barmode': 'stack'
    }



    # last update
    latest_df = pd.read_json('http://covid19tracker.gov.bd/api/country/latest?onlyCountries=true&iso3=BGD')
    latest_df = latest_df[['TotalTests', 'TotalRecovered', 'TotalCases', 'deaths']]

    # make json
    df.sort_values(by=['Date'], inplace=True, ascending=False)
    json_records = df.reset_index().to_json(orient ='records')
    main_data = [] 
    main_data = json.loads(json_records) 


    # Pass trace and layout in the context
    context = {
        "trace": trace,
        "trace2": trace2,
        "trace3": trace3,
        "traceS": traceS,
        "trace2S": trace2S,
        "trace3S": trace3S,
        "layout": layout,

        "tracePast": tracePast,
        "trace2Past": trace2Past,
        "trace3Past": trace3Past,
        "layoutPast": layoutPast,

        "Days30First": list(df_30["Date"])[0],
        "Days30Last": list(df_30["Date"])[29],

        "lastUpdate": datetime.datetime.utcnow().strftime('%B %d %Y - %H:%M:%S'),

        "TotalTests": list(latest_df['TotalTests'])[0],
        "TotalRecovered": list(latest_df['TotalRecovered'])[0],
        "TotalCases": list(latest_df['TotalCases'])[0],
        "deaths": list(latest_df['deaths'])[0],

        "main_data": main_data
    }
    # print(list(latest_df['deaths'])[0]);

    return render(request,'home-bd.html', context)



def district(request):

    # District data
    district_df = pd.read_json('http://covid19tracker.gov.bd/api/district').features
    district_df = pd.DataFrame(list(district_df))
    district_df1 = district_df.properties
    district_df = pd.DataFrame(list(district_df1))
    district_df = district_df[['name', 'confirmed']]
    # district_df.sort_values(by=['confirmed'], inplace=True, ascending=False)
    district_df.sort_values(by=['confirmed'], inplace=True)
    # print(district_df)

    # Create a trace json to hold graph data
    trace = {
        'x': list(district_df["confirmed"]),
        'y': list(district_df["name"]),
        'type': 'bar',
        # 'type': 'scatter',
        'name': list(district_df["name"]),
        'marker': {'color': '#03a9fc'},
        'orientation': 'h'
    }

    # Configure the chart's layout
    layout = {
        'title': {
            'text': 'District Wise Confirmed Cases',
            'font': {
                'color': '#000'
            }
        },
        # 'xaxis': {'title': 'X-axis', 'color': '#DCDCDC', 'mirror': 'true', 'showline': 'false'},
        # 'yaxis': {'title': 'Y-axis', 'color': '#DCDCDC', 'mirror': 'true', 'showline': 'true'},
        'xaxis': {'title': '', 'color': '#888', 'titlefont':{'size':12}, 'automargin': 'true'},
        'yaxis': {'title': '', 'color': '#888', 'titlefont':{'size':12}, 'automargin': 'true'},
        # 'plot_bgcolor': 'rgb(230, 230, 230)'
        # 'autosize': 'false',
        # 'width': '1300',
        'height': '1000'
    }

    # make json
    district_df.sort_values(by=['confirmed'], inplace=True, ascending=False)
    json_records = district_df.reset_index().to_json(orient ='records')
    data = [] 
    data = json.loads(json_records)

    # Pass trace and layout in the context
    context = {
        "trace": trace,
        "layout": layout,
        "title": "Confirmed",
        'Ddata': data
    }
    return render(request,'district.html', context)


def comparison(request):
    return render(request,'comparison.html')



# main function
def getCountryData(request):
    iso = request.GET['iso']
    
    # last update
    latest_df = pd.read_json('http://covid19tracker.gov.bd/api/country/latest?onlyCountries=true&iso3='+iso+'')
    latest_df['MortalityRate'] = (latest_df['deaths'] * 100)/(latest_df['deaths'] + latest_df['TotalRecovered'] + latest_df['ActiveCases'])
    latest_df = latest_df[['TotalTests', 'TotalRecovered', 'TotalCases', 'deaths', 'SeriousCases', 'RationPerMillion', 'ActiveCases', 'MortalityRate', 'name']]
    # lastUpdate = str(datetime.datetime.utcnow().strftime('%B %d %Y - %H:%M:%S'))

    #main data
    df = pd.read_json('http://wuhan-coronavirus-api.laeyoung.endpoint.ainize.ai/jhu-edu/timeseries?onlyCountries=true&iso3='+iso+'')
    lastUpdate = pd.to_datetime(df.lastupdate).dt.strftime('%B %d %Y - %H:%M:%S')
    df = pd.DataFrame(list(df.timeseries))
    df_new = df.rename(index={0: 'column1'})
    df_new = df_new.T # Transpose column
    df_new_data = pd.DataFrame(list(df_new['column1']))
    df_new_data['Date'] = df_new.index
    df_new_data = df_new_data.rename(columns={'confirmed':'Confirmed','deaths':'Deaths','recovered':'Recovered'})
    df_new_data['New_Confirmed'] = df_new_data.Confirmed.diff().fillna(0).apply(lambda x : x if x > 0 else 0)
    df_new_data['New_Recovered'] = df_new_data.Recovered.diff().fillna(0).apply(lambda x : x if x > 0 else 0)
    df_new_data['New_Deaths'] = df_new_data.Deaths.diff().fillna(0).apply(lambda x : x if x > 0 else 0)
    df = df_new_data[['Date', 'New_Confirmed', 'Confirmed', 'New_Recovered', 'Recovered', 'New_Deaths', 'Deaths']].query('Confirmed > 0')
    df['Date'] = pd.to_datetime(df['Date'])
    df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')
    df.sort_values(by=['Date'], inplace=True)
    # print(df.tail())

    # make last 30 days data
    df_30 = df.tail(30)

    # past 30 days chart
    tracePast = {
        'x': list(df_30["Date"]),
        'y': list(df_30["Confirmed"]),
        'type': 'bar',
        'name': 'Confirmed',
        'marker': {
            'color': '#7163F1',
            'width': 1
        }
        # 'orientation': 'h'
    }
    trace2Past = {
        'x': list(df_30["Date"]),
        'y': list(df_30["Recovered"]),
        'type': 'bar',
        'name': 'Recovered',
        'marker': {
            'color': '#2ECBAC',
            'width': 1
        }
    }
    trace3Past = {
        'x': list(df_30["Date"]),
        'y': list(df_30["Deaths"]),
        'type': 'bar',
        'name': 'Death',
        'marker': {
            'color': '#F54251',
            'width': 1
        }
    }# layout for past 30 days
    layoutPast = {
        'title': {
            'text': 'Past 30 Days Coronavirus Cases From '+list(df_30["Date"])[0]+' To '+list(df_30["Date"])[29],
            'font': {
                'color': '#000',
                'size': 14
            }
        },
        'xaxis': {
            'title': 'Date',
            'color': '#888', 
            'titlefont':{'size':12}, 
            'automargin': 'true', 
            'showline': 'true'
        },
        'yaxis': {
            'title': '', 
            'color': '#888', 
            'titlefont':{'size':12}, 
            'automargin': 'true', 
            'showline': 'true'
        },
        'height': '400',
        'barmode': 'stack'
    }


    # Create a trace json to hold graph data (Daily Incidence)
    trace = {
        'x': list(df_30["Date"]),
        'y': list(df_30["New_Confirmed"]),
        'type': 'bar',
        'name': 'Confirmed',
        'marker': {
            'color': '#7163F1',
            'width': 1
        }
        # 'orientation': 'h'
    }
    trace2 = {
        'x': list(df_30["Date"]),
        'y': list(df_30["New_Recovered"]),
        'type': 'bar',
        'name': 'Recovered',
        'marker': {
            'color': '#2ECBAC',
            'width': 1
        }
    }
    trace3 = {
        'x': list(df_30["Date"]),
        'y': list(df_30["New_Deaths"]),
        'type': 'bar',
        'name': 'Death',
        'marker': {
            'color': '#F54251',
            'width': 1
        }
    }

    # for scatter
    traceS = {
        'x': list(df_30["Date"]),
        'y': list(df_30["New_Confirmed"]),
        'type': 'scatter',
        'name': 'Confirmed',
        'marker': {
            'color': '#7163F1',
            'width': 1
        }
        # 'orientation': 'h'
    }
    trace2S = {
        'x': list(df_30["Date"]),
        'y': list(df_30["New_Recovered"]),
        'type': 'scatter',
        'name': 'Recovered',
        'marker': {
            'color': '#2ECBAC',
            'width': 1
        }
    }
    trace3S = {
        'x': list(df_30["Date"]),
        'y': list(df_30["New_Deaths"]),
        'type': 'scatter',
        'name': 'Death',
        'marker': {
            'color': '#F54251',
            'width': 1
        }
    }
    # Configure the chart's layout
    layout = {
        'title': {
            'text': 'Daily Incidences Chart',
            'font': {
                'color': '#000',
                'size': 14
            }
        },
        'xaxis': {
            'title': 'Date',
            'color': '#888', 
            'titlefont':{'size':12}, 
            'automargin': 'true', 
            'showline': 'true'
        },
        'yaxis': {
            'title': '', 
            'color': '#888', 
            'titlefont':{'size':12}, 
            'automargin': 'true', 
            'showline': 'true'
        },
        'height': '400',
        'barmode': 'stack'
    }
    # daily incidence end

    
    # make json
    df.sort_values(by=['Date'], inplace=True, ascending=False)
    json_records = df.reset_index().to_json(orient ='records')
    main_data = [] 
    main_data = json.loads(json_records)


    # whole data
    # for scatter
    traceAll = {
        'x': list(df["Date"]),
        'y': list(df["New_Confirmed"]),
        'type': 'scatter',
        'name': 'Confirmed',
        'marker': {
            'color': '#7163F1',
            'width': 1
        }
        # 'orientation': 'h'
    }
    traceAll2 = {
        'x': list(df["Date"]),
        'y': list(df["New_Recovered"]),
        'type': 'scatter',
        'name': 'Recovered',
        'marker': {
            'color': '#2ECBAC',
            'width': 1
        }
    }
    traceAll3 = {
        'x': list(df["Date"]),
        'y': list(df["New_Deaths"]),
        'type': 'scatter',
        'name': 'Death',
        'marker': {
            'color': '#F54251',
            'width': 1
        }
    }
    layoutAll = {
        'title': {
            'text': '',
            'font': {
                'color': '#000',
                'size': 14
            }
        },
        'xaxis': {
            'title': 'Date',
            'color': '#888', 
            'titlefont':{'size':12}, 
            'automargin': 'true', 
            'showline': 'true'
        },
        'yaxis': {
            'title': '', 
            'color': '#888', 
            'titlefont':{'size':12}, 
            'automargin': 'true', 
            'showline': 'true'
        },
        'height': '400'
    }

    # str(datetime.datetime.utcnow().strftime('%B %d %Y - %H:%M:%S'))
    json_data = json.dumps({
        "lastUpdate": list(lastUpdate),
        "TotalTests": list(latest_df['TotalTests'])[0],
        "TotalRecovered": list(latest_df['TotalRecovered'])[0],
        "TotalCases": list(latest_df['TotalCases'])[0],
        "deaths": list(latest_df['deaths'])[0],
        "SeriousCases": list(latest_df['SeriousCases'])[0],
        "RationPerMillion": list(latest_df['RationPerMillion'])[0],
        "ActiveCases": list(latest_df['ActiveCases'])[0],
        "MortalityRate": list(latest_df['MortalityRate'])[0],
        "name": list(latest_df['name'])[0],

        "tracePast": tracePast,
        "trace2Past": trace2Past,
        "trace3Past": trace3Past,
        "layoutPast": layoutPast,

        "Days30First": list(df_30["Date"])[0],
        "Days30Last": list(df_30["Date"])[29],
        
        "trace": trace,
        "trace2": trace2,
        "trace3": trace3,
        "traceS": traceS,
        "trace2S": trace2S,
        "trace3S": trace3S,
        "layout": layout,

        "traceAll": traceAll,
        "traceAll2": traceAll2,
        "traceAll3": traceAll3,
        "layoutAll": layoutAll,

        "main_data": main_data
    })

    return HttpResponse(json_data, content_type="application/json")

# ajax loaded
def getDistrictData(request):
    # Dhaka District data
    dhaka_df = pd.read_json('http://covid19tracker.gov.bd/api/dhaka')
    dhaka_df.sort_values(by=['confirmed'], inplace=True)

    # District data
    district_df = pd.read_json('http://covid19tracker.gov.bd/api/district').features
    district_df = pd.DataFrame(list(district_df))
    district_df1 = district_df.properties
    district_df = pd.DataFrame(list(district_df1))
    district_df = district_df[['name', 'confirmed']]
    district_df.sort_values(by=['confirmed'], inplace=True)

    # Create a trace json to hold graph data
    trace = {
        'x': list(district_df["confirmed"]),
        'y': list(district_df["name"]),
        'type': 'bar',
        'name': list(district_df["name"]),
        'marker': {'color': '#03a9fc'},
        'orientation': 'h'
    }

    # Configure the chart's layout
    layout = {
        'title': {
            'text': 'District Wise Confirmed Cases',
            'font': {
                'color': '#000'
            }
        },
        'xaxis': {'title': '', 'color': '#888', 'titlefont':{'size':12}, 'automargin': 'true'},
        'yaxis': {'title': '', 'color': '#888', 'titlefont':{'size':12}, 'automargin': 'true'},
        'height': '1000'
    }

    # make json district
    district_df.sort_values(by=['confirmed'], inplace=True, ascending=False)
    json_records = district_df.reset_index().to_json(orient ='records')
    main_data = [] 
    main_data = json.loads(json_records)

    # make json dhaka district
    dhaka_df.sort_values(by=['confirmed'], inplace=True, ascending=False)
    json_records_dhaka = dhaka_df.reset_index().to_json(orient ='records')
    main_data_dhaka = [] 
    main_data_dhaka = json.loads(json_records_dhaka)

    json_data = json.dumps({        
        "trace": trace,
        "layout": layout,

        "main_data": main_data,
        "main_data_dhaka": main_data_dhaka
    })
    return HttpResponse(json_data, content_type="application/json")

def country(request):
    return render(request,'country.html')
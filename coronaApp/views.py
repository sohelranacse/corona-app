from django.shortcuts import render
from django.http import HttpResponse

# importing the required libraries
import pandas as pd
import numpy as np
import json
from datetime import datetime,timedelta
from io import BytesIO
from urllib.parse import quote

import warnings
warnings.filterwarnings('ignore')

# active functions
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

def country(request):
    return render(request,'country.html')
def about(request):
    return render(request,'about.html')

def comparison(request):
    return render(request,'comparison.html')

def prediction(request):
    return render(request,'prediction.html')

def vaccination(request):
    # Get vaccinations available country
    df = pd.read_csv('https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/locations.csv')
    df = df.query('iso_code == iso_code')
    df = df[['iso_code', 'location']]

    json_records = df.reset_index().to_json(orient ='records')
    data = [] 
    data = json.loads(json_records)

    context = {'country_info': data}
    return render(request,'vaccination.html', context)

def get_country_name(iso):
    df=pd.read_json('https://raw.githubusercontent.com/sohelranacse/analysis-data/main/country.json')
    df = df[df['iso'] == iso]
    return list(df['name'])[0]

def get_vaccine_country_name(iso):
    df=pd.read_csv('https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/locations.csv')
    df = df[df['iso_code'] == iso]
    return list(df['location'])[0]

def getComparisonData(request):
    countryList = request.GET.getlist('country[]')

    i = 0
    m_df = []
    for country in countryList:
        df = pd.read_json('https://master-covid-19-api-laeyoung.endpoint.ainize.ai/jhu-edu/timeseries?onlyCountries=true&iso3='+country+'').timeseries
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
        df = df.rename(columns={'New_Confirmed':'New_Confirmed'+country,'Confirmed':'Confirmed'+country,'New_Recovered':'New_Recovered'+country,'Recovered':'Recovered'+country, 'New_Deaths':'New_Deaths'+country,'Deaths':'Deaths'+country})

        if(len(m_df)>0):
            if(len(m_df) > len(df)):
                m_df = pd.merge(m_df, df, how="left", on=["Date", "Date"]).fillna(0)
            else:
                m_df = pd.merge(df, m_df, how="left", on=["Date", "Date"]).fillna(0)
        else:
            m_df = df

        i += 1

    c_trace = []
    ct_trace = []
    recvered_new_trace = []
    recvered_all_trace = []
    death_new_trace = []
    death_all_trace = []
    k = 0
    for j in countryList:
        tr1 = {
            'x': list(m_df["Date"]),
            'y': list(m_df['New_Confirmed'+countryList[k]]),
            'type': 'scatter',
            'name': get_country_name(countryList[k])
        }
        tr2 = {
            'x': list(m_df["Date"]),
            'y': list(m_df['Confirmed'+countryList[k]]),
            'type': 'scatter',
            'name': get_country_name(countryList[k])
        }
        c_trace.append(tr1)
        ct_trace.append(tr2)

        tr3 = {
            'x': list(m_df["Date"]),
            'y': list(m_df['New_Recovered'+countryList[k]]),
            'type': 'scatter',
            'name': get_country_name(countryList[k])
        }
        tr4 = {
            'x': list(m_df["Date"]),
            'y': list(m_df['Recovered'+countryList[k]]),
            'type': 'scatter',
            'name': get_country_name(countryList[k])
        }
        recvered_new_trace.append(tr3)
        recvered_all_trace.append(tr4)
                
        tr4 = {
            'x': list(m_df["Date"]),
            'y': list(m_df['New_Deaths'+countryList[k]]),
            'type': 'scatter',
            'name': get_country_name(countryList[k])
        }
        tr5 = {
            'x': list(m_df["Date"]),
            'y': list(m_df['Deaths'+countryList[k]]),
            'type': 'scatter',
            'name': get_country_name(countryList[k])
        }
        death_new_trace.append(tr4)
        death_all_trace.append(tr5)

        k += 1

    # print(c_trace)
    
    # json_records = m_df.reset_index().to_json(orient ='records')
    # main_data = []
    # main_data = json.loads(json_records)

    # context
    json_data = json.dumps({        
        "countryList": countryList,
        "c_trace": c_trace,
        "ct_trace": ct_trace,
        "recvered_new_trace": recvered_new_trace,
        "recvered_all_trace": recvered_all_trace,
        "death_new_trace": death_new_trace,
        "death_all_trace": death_all_trace
        # "main_data": main_data
    })
    return HttpResponse(json_data, content_type="application/json")



# main function
def getCountryData(request):
    iso = request.GET['iso']
    
    # last update
    latest_df = pd.read_json('http://covid19tracker.gov.bd/api/country/latest?onlyCountries=true&iso3='+iso+'')
    latest_df['MortalityRate'] = (latest_df['deaths'] * 100)/(latest_df['deaths'] + latest_df['TotalRecovered'] + latest_df['ActiveCases'])
    latest_df = latest_df[['TotalTests', 'TotalRecovered', 'TotalCases', 'deaths', 'SeriousCases', 'RationPerMillion', 'ActiveCases', 'MortalityRate', 'name']]
    # lastUpdate = str(datetime.datetime.utcnow().strftime('%B %d %Y - %H:%M:%S'))

    # main data
    df = pd.read_json('https://master-covid-19-api-laeyoung.endpoint.ainize.ai/jhu-edu/timeseries?onlyCountries=true&iso3='+iso+'')
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
    df_30 = df.tail(60)

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
            'text': 'Past 60 Days Coronavirus Cases From '+list(df_30["Date"])[0]+' To '+list(df_30["Date"])[59],
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
        'mode': 'lines+markers',
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
        'mode': 'lines+markers',
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
        'mode': 'lines+markers',
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
            'automargin': 'true'
        },
        'yaxis': {
            'title': '', 
            'color': '#888', 
            'titlefont':{'size':12}, 
            'automargin': 'true'
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

def export_country_data(request):
    iso = request.GET['iso']
    etype = request.GET['type']

    # main data
    df = pd.read_json('https://master-covid-19-api-laeyoung.endpoint.ainize.ai/jhu-edu/timeseries?onlyCountries=true&iso3='+iso+'')
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
    df.index = np.arange(1, len(df) + 1)

    
    if etype == '1':
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename='+get_country_name(iso)+'_'+list(lastUpdate)[0]+'.csv'
        df.to_csv(path_or_buf=response)
        return response
    else:
        with BytesIO() as b:
            writer = pd.ExcelWriter(b, engine='xlsxwriter')
            df.to_excel(writer, sheet_name='country.xlsx')
            writer.save()
            return HttpResponse(b.getvalue(), content_type='application/vnd.ms-excel')

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

def getVaccineData(request):
    iso = request.GET['iso']
    country = get_vaccine_country_name(iso)

    # country vaccination data
    df = pd.read_csv('https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/country_data/'+quote(country)+'.csv').fillna(0)

    # vaccine chart end
    traceVaccine1 = {
        'x': list(df["date"]),
        'y': list(df["total_vaccinations"]),
        'type': 'scatter',
        'mode': 'lines+markers',
        'name': 'Total Vaccinations',
        'marker': {
            'color': '#7163F1',
            'width': 1
        }
    }
    traceVaccine2 = {
        'x': list(df["date"]),
        'y': list(df["people_vaccinated"]),
        'type': 'scatter',
        'mode': 'lines+markers',
        'name': 'People Vaccinated',
        'marker': {
            'color': '#2ECBAC',
            'width': 1
        }
    }

    # Configure the chart's layout
    vaccineLayoutAll = {
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
        'height': '500'
    }
    # vaccine chart end

    # convert json - vaccination main data
    json_records = df.reset_index().to_json(orient ='records')
    data = [] 
    data = json.loads(json_records)

    # convert json - vaccination summary
    json_records1 = df.tail(1).reset_index().to_json(orient ='records')
    summary_data = [] 
    summary_data = json.loads(json_records1)
    
    json_data = json.dumps({
        "country": country,
        "traceVaccine1": traceVaccine1,
        "traceVaccine2": traceVaccine2,
        "vaccineLayoutAll": vaccineLayoutAll,
        "vaccination_summary": summary_data,
        "main_data": data
    })
    return HttpResponse(json_data, content_type="application/json")

def export_vaccine_data(request):
    iso = request.GET['iso']
    etype = request.GET['type']
    country = get_vaccine_country_name(iso)

    # main data
    df = pd.read_csv('https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/country_data/'+quote(country)+'.csv')
    df.index = np.arange(1, len(df) + 1)
    
    if etype == '1':
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename='+get_vaccine_country_name(iso)+'_vaccination.csv'
        df.to_csv(path_or_buf=response)
        return response
    else:
        with BytesIO() as b:
            writer = pd.ExcelWriter(b, engine='xlsxwriter')
            df.to_excel(writer, sheet_name='country.xlsx')
            writer.save()
            return HttpResponse(b.getvalue(), content_type='application/vnd.ms-excel')

def getPredictionData(request):

    # import model
    from sklearn.linear_model import LinearRegression
    # for modelling
    from statsmodels.tsa.arima_model import ARIMA
    
    iso = request.GET['iso']
    country = get_country_name(iso)

    df = pd.read_csv('https://covid.ourworldindata.org/data/owid-covid-data.csv').query('iso_code == "'+iso+'"')
    df = df.reset_index().fillna(0)
    columns_to_remove = ['index','iso_code', 'continent', 'location', 'tests_units']
    df.drop(labels=columns_to_remove, axis=1, inplace=True)
    df["date"] = pd.to_datetime(df['date']) # object to datetime

    df_copy = df.copy() # make a copy
    df_death = df.copy() # deaths

    ################### CONFIRMED ###################
    # Splitting the data into train and test set (new cases)
    X_train = df.drop(labels='new_cases', axis=1)[df['date'].dt.year <= 2020]
    X_test = df.drop(labels='new_cases', axis=1)[df['date'].dt.year > 2020]
    y_train = df[df['date'].dt.year <= 2020]['new_cases'].values
    y_test = df[df['date'].dt.year > 2020]['new_cases'].values

    # Removing the 'date' column
    X_train.drop(labels='date', axis=True, inplace=True)
    X_test.drop(labels='date', axis=True, inplace=True)

    # linear rigression
    regressor = LinearRegression()
    regressor.fit(X_train,y_train)

    # prediction (new cases)
    predictions = regressor.predict(X_test)

    arima = ARIMA(predictions, order=(5, 1, 0))
    arima = arima.fit(trend='c', full_output=True, disp=True)
    forecast = arima.forecast(steps= 7)
    Predict_New_Confirmed_data = list(forecast[0]) # y values
    ################### CONFIRMED END ###################

    ################### DEATHS ###################
    # Splitting the data into train and test set (new cases)
    X_train = df_death.drop(labels='new_deaths', axis=1)[df_death['date'].dt.year <= 2020]
    X_test = df_death.drop(labels='new_deaths', axis=1)[df_death['date'].dt.year > 2020]
    y_train = df_death[df['date'].dt.year <= 2020]['new_deaths'].values
    y_test = df_death[df['date'].dt.year > 2020]['new_deaths'].values

    # Removing the 'date' column
    X_train.drop(labels='date', axis=True, inplace=True)
    X_test.drop(labels='date', axis=True, inplace=True)

    # linear rigression
    regressor = LinearRegression()
    regressor.fit(X_train,y_train)

    # prediction (new cases)
    predictions_death = regressor.predict(X_test)

    arima = ARIMA(predictions_death, order=(5, 1, 0))
    arima = arima.fit(trend='c', full_output=True, disp=True)
    forecast = arima.forecast(steps= 7)
    Predict_New_Deaths_data = list(forecast[0]) # y values
    ################### DEATHS END ###################

    # date
    data = pd.DataFrame(columns = ['Date','actual_Date','New_Deaths','New_Confirmed'])
    data['Date'] = pd.to_datetime(df_copy['date'])    
    data['actual_Date'] = data['Date'].dt.strftime('%Y-%m-%d') # for tracer
    data['New_Confirmed'] = df_copy['new_cases']
    data['New_Deaths'] = df_copy['new_deaths']

    start_date = data['Date'].max()
    prediction_dates_new_con = [] # x values
    for i in range(7):
        date = start_date + timedelta(days=1)
        prediction_dates_new_con.append(date)
        start_date = date
    
    # global date - use all predicitons
    predictedDate = []
    for pDate in prediction_dates_new_con:
        predictedDate.append(pDate.strftime('%Y-%m-%d'))

    # prediction new confirmed chart start    
    prediction_new_confirmed_traccer1 = {
        'x': list(data["actual_Date"]),
        'y': list(data["New_Confirmed"]),
        'type': 'scatter',
        'name': 'Actual',
        'marker': {
            'color': '#7B6FFF',
            'width': 1
        }
    }
    prediction_new_confirmed_traccer2 = {
        'x': predictedDate,
        'y': Predict_New_Confirmed_data,
        'type': 'scatter',
        'name': 'Predicted',
        'mode': 'lines+markers',
        'marker': {
            'color': '#F5385A',
            'width': 1
        }
    }
    prediction_new_confirmed_layout = {
        'title': {
            'text': 'Coronavirus Confirmed Cases Next 7 Days Prediction - '+country,
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
        'height': '500'
    }
    # prediction new confirmed chart end

    # prediction new deaths chart start    
    prediction_deaths_traccer1 = {
        'x': list(data["actual_Date"]),
        'y': list(data["New_Deaths"]),
        'type': 'scatter',
        'name': 'Actual',
        'marker': {
            'color': '#7B6FFF',
            'width': 1
        }
    }
    prediction_deaths_traccer2 = {
        'x': predictedDate,
        'y': Predict_New_Deaths_data,
        'type': 'scatter',
        'name': 'Predicted',
        'mode': 'lines+markers',
        'marker': {
            'color': '#F5385A',
            'width': 1
        }
    }
    prediction_deaths_layout = {
        'title': {
            'text': 'Coronavirus Deaths Next 7 Days Prediction - '+country,
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
        'height': '500'
    }
    # prediction new deaths chart end

    lastUpdate = pd.to_datetime(df_copy.tail(1).date).dt.strftime('%B %d %Y')

    json_data = json.dumps({
        "name": country,
        "lastUpdate": list(lastUpdate),

        "prediction_new_confirmed_traccer1": prediction_new_confirmed_traccer1,
        "prediction_new_confirmed_traccer2": prediction_new_confirmed_traccer2,
        "prediction_new_confirmed_layout": prediction_new_confirmed_layout,

        "prediction_deaths_traccer1": prediction_deaths_traccer1,
        "prediction_deaths_traccer2": prediction_deaths_traccer2,
        "prediction_deaths_layout": prediction_deaths_layout
    })    
    return HttpResponse(json_data, content_type="application/json")
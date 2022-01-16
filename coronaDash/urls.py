from django.contrib import admin
from django.urls import path
from coronaApp import views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    # url('old',views.index,name='Mainpage'),
    # url('selectCountry',views.drillDownACountry,name='drillDown'),
    # url('mytest',views.mytest,name='mytest'),
    # url('plotly_graph',views.plotly_graph,name='plotly_graph'),

    # my code
    url('^$', views.country, name='country'),


    # url('bangladesh',views.bangladesh,name='bangladesh'),
    # url('worldWide',views.worldWide,name='worldWide'),

    url('world', views.world, name='world'),
    url('asia', views.asia, name='asia'),
    url('europe',views.europe,name='europe'),
    url('africa',views.africa,name='africa'),
    url('australia',views.australia,name='australia'),
    url('southAmerica',views.southAmerica,name='southAmerica'),
    url('northAmerica',views.northAmerica,name='northAmerica'),
    url('about',views.about,name='about'),
    url('vaccination',views.vaccination,name='vaccination'),
    url('prediction',views.prediction,name='prediction'),

    # url('stats',views.stats,name='stats'),
    url('comparison',views.comparison,name='comparison'),
    # url('district',views.district,name='district'),

    # url('country',views.country,name='country'),
    url('getCountryData',views.getCountryData,name='getCountryData'),
    url('getDistrictData',views.getDistrictData,name='getDistrictData'),
    url('getComparisonData',views.getComparisonData,name='getComparisonData'),
    url('export_country_data',views.export_country_data,name='export_country_data'),
    url('getVaccineData',views.getVaccineData,name='getVaccineData'),
    url('export_vaccine_data',views.export_vaccine_data,name='export_vaccine_data'),
    url('getPredictionData',views.getPredictionData,name='getPredictionData'),
]

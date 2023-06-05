import string
from django.shortcuts import render,redirect
import requests
from django.views.decorators.csrf import csrf_exempt

import json
from .models import *
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import *
from collections import Counter
# Create your views here.
def put_data_to_backend():
    file_path = './jsondata.json'
    with open(file_path, 'r') as file:
        json_data = json.load(file)
    for i in json_data:
        if(i['end_year']==""):
            end_year=0
        else:
            end_year=int(i['end_year'])
        if(i['intensity']==""):
            intensity=0
        else:
            intensity=int(i['intensity'])
        if(i['sector']==""):
            sector="-"
        else:
            sector=i['sector']
        if(i['topic']==""):
            i['topic']="-"
        else:
            topic=i['topic']
        if(i['insight']==""):
            i['insight']="-"
        else:
            insight=i['insight']
        if(i['url']==""):
            i['url']="-"
        else:
            url=i['url']
        if(i['region']==""):
            i['region']==""
        else:
            region=i['region']
        if(i['start_year']==""):
            start_year=0
        else:
            start_year=int(i['start_year'])
        if(i['impact']==""):
            impact=0
        else:
            impact=int(i['impact'])
        if(i['added']==""):
            i['added']="-"
        else: 
            added=i['added']
        if(i['published']==""):
            i['published']="-"
        else:
            published=i['published']
        if(i['country']==""):
            i['country']="-"
        else:
            country=i['country']
        if(i['relevance']==""):
            i['relevance']=="-"
        else:
            relevance=i['relevance']
        if(i['pestle']==""):
            i['pestle']=="-"
        else:
            pestle=i['pestle']
        if(i['source']==""):
            i['source']=="-"
        else:
            source=i['source']
        if(i['title']==""):
            i['title']=="-"
        else:
            title=i['title']
        if(i['likelihood']==""):
            likelihood=0
        else:
            likelihood=int(i['likelihood'])
        model_instance = category(
        end_year=end_year,
        intensity=intensity,
        sector=sector,
        topic=topic,
        insight=insight,
        url=url,
        region=region,
        start_year=start_year,
        impact=impact,
        added=added,
        published=published,
        country=country,
        relevance=relevance,
        pestle=pestle,
        source=source,
        title=title,
        likelihood=likelihood
        )
        model_instance.save()

def index(request):
    return render(request,'index.html')
# put_data_to_backend()  DO NOT UN COMMENT THIS UNTIL YOU WANT TO PUT THE JSON DATA TO BACKEND!!!!
intensity_sum=0
filter_type = "a"
filter_value="a"

class categorys(APIView):

    def get(self,request):
        filter_type="a"
        filter_value="a"
        #get data from backend according to the filter
        data = category.objects.all()

        end_year = request.GET.get('end_year')
        if(end_year):
            data = data.filter(end_year=end_year)
            filter_type="end_year"
            filter_value=str(end_year)

        topic = request.GET.get('topic')
        if(topic):
            data = data.filter(topic=topic)
            filter_type="topic"
            filter_value=str(topic)

        sector = request.GET.get('sector')
        if(sector):
            data = data.filter(sector=sector)
            filter_type="sector"
            filter_value = sector


        region = request.GET.get('region')
        if(region):
            data = data.filter(region=region)
            filter_type="region"
            filter_value=region

        pestle = request.GET.get('pestle')
        if(pestle):
            data = data.filter(pestle=pestle)
            filter_type="pestle"
            filter_value=pestle

        country = request.GET.get('country')
        if(country):
            data = data.filter(country=country)
            filter_type="country"
            filter_value=country


        source = request.GET.get('source')
        if(source):
            data = data.filter(source=source)
            filter_type="source"
            filter_value=source

        serializer = categoryserializer(data,many=True)
        # print(serializer.data)
        # prepare data to send to frontend
        intensity=[]
        likelihood=[]
        relevance=[]
        start_year=[]
        country=[]
        unique_end_year=[]
        unique_topic=[]
        unique_sector=[]
        unique_source=[]
        unique_region=[]
        unique_country=[]
        unique_pestle=[]
        for i in serializer.data:
            if(i['intensity']!=0):
                intensity.append(int(i['intensity']))
            if(i['likelihood']!=0):
                likelihood.append(int(i['likelihood']))   
            if(i['relevance']!="-"):
                relevance.append(i['relevance'])   
            if(i['start_year']!="-"):
                start_year.append(i['start_year'])  
            if(i['country']!="-"):
                country.append(i['country'])       
            if(i['end_year']!="-"):
                unique_end_year.append(i['end_year'])
            if(i['topic']!="-"):
                unique_topic.append(i['topic'])
            if(i['sector']!="-"):
                unique_sector.append(i['sector'])
            if(i['source']!="-"):
                unique_source.append(i['source'])
            if(i['region']!="-"):
                unique_region.append(i['region'])      
            if(i['country']!="-"):
                unique_country.append(i['country'])   
            if(i['pestle']!="-"):
                unique_pestle.append(i['pestle'])
        intensity.sort()
        intensity_counter = Counter(intensity)
        # print(intensity_counter)
        intensity_frontend = {}
        for number,count in intensity_counter.items():
            # print(f"Number: {number}, Count: {count}")
            intensity_frontend[number]=count
            intensity_sum=0
        for number,count in intensity_counter.items():
            intensity_sum=intensity_sum+count
        # print(serializer.data)
        # print(intensity_frontend)

        likelihood.sort()
        likelihood_counter = Counter(likelihood)
        # print(intensity_counter)
        likelihood_frontend = {}
        for number,count in likelihood_counter.items():
            # print(f"Number: {number}, Count: {count}")
            likelihood_frontend[number]=count
            likelihood_sum=0
        for number,count in likelihood_counter.items():
            likelihood_sum=likelihood_sum+count
        # print(likelihood_sum)
        # print(likelihood_frontend)


        relevance.sort()
        relevance_counter = Counter(relevance)
        # print(intensity_counter)
        relevance_frontend = {}
        for number,count in relevance_counter.items():
            # print(f"Number: {number}, Count: {count}")
            relevance_frontend[number]=count
            relevance_sum=0
        for number,count in relevance_counter.items():
            relevance_sum=relevance_sum+count
        # print(relevance_sum)
        # print(relevance_frontend)


        start_year.sort()
        start_year_counter = Counter(start_year)
        # print(intensity_counter)
        start_year_frontend = {}
        for number,count in start_year_counter.items():
            # print(f"Number: {number}, Count: {count}")
            start_year_frontend[number]=count
            start_year_sum=0
        for number,count in start_year_counter.items():
            start_year_sum=relevance_sum+count
        # print(start_year_sum)
        # print(start_year_frontend)


        country.sort()
        country_counter = Counter(country)
        # print(intensity_counter)
        country_frontend = {}
        for number,count in country_counter.items():
            # print(f"Number: {number}, Count: {count}")
            country_frontend[number]=count
            country_sum=0
        for number,count in country_counter.items():
            country_sum=relevance_sum+count
        # print(country_sum)
        # print(country_frontend)

        unique_country = list(set(unique_country))
        unique_country.sort()
        unique_end_year = list(set(unique_end_year))
        unique_end_year.sort()
        unique_sector = list(set(unique_sector))
        unique_sector.sort()
        unique_region = list(set(unique_region))
        unique_region.sort()
        unique_source = list(set(unique_source))
        unique_source.sort()
        unique_topic = list(set(unique_topic))
        unique_topic.sort()
        unique_pestle = list(set(unique_pestle))
        unique_pestle.sort()
        
        print(len(unique_topic))
        return render(request,'homepage.html',{'intensity_frontend':intensity_frontend,'intensity_sum':intensity_sum,'country_frontend':country_frontend,'country_sum':country_sum,'start_year_frontend':start_year_frontend,'start_year_sum':start_year_sum,'relevance_frontend':relevance_frontend,'relevance_sum':relevance_sum,'likelihood_frontend':likelihood_frontend,'likelihood_sum':likelihood_sum,'filter_type':filter_type,'filter_value':filter_value,'unique_end_year':unique_end_year,'unique_sector':unique_sector,'unique_region':unique_region,'unique_source'
            :unique_source,'unique_topic':unique_topic,'unique_country':unique_country,'unique_pestle':unique_pestle})
        # return Response({'satus':200 , 'payload':serializer.data})


@csrf_exempt
def display_view(request):
    # Render the display.html template
    formvar = request.POST.get('formvariable') 
    filter_type_get = request.POST.get('filter_type')
    filter_value_get = request.POST.get('filter_value')
    formvar_type=request.POST.get('formvariable_type')



    data = category.objects.all()
    if(formvar_type=="intensity"):
        data = data.filter(intensity=int(formvar))
    if(formvar_type=="likelihood"):
        data = data.filter(likelihood=int(formvar))
    if(formvar_type=="relevance"):
        data = data.filter(relevance=int(formvar))
    if(formvar_type=="start_year"):
        data = data.filter(start_year=int(formvar))
    if(formvar_type=="country"):
        data = data.filter(country=formvar)
    if(filter_type_get=="end_year"):
        filter_value_get = int(filter_value_get)
        data = data.filter(end_year=filter_value_get)
    elif(filter_type_get=="topic"):
        data=data.filter(topic=filter_value_get)
    elif(filter_type_get=="sector"):
        data=data.filter(sector=filter_value_get)
    elif(filter_type_get=="region"):
        data=data.filter(region=filter_value_get)
    elif(filter_type_get=="country"):
        data=data.filter(country=filter_value_get)
    elif(filter_type_get=="pestle"):
        data=data.filter(pestle=filter_value_get)
    elif(filter_type_get=="source"):
        data=data.filter(source=filter_value_get)


    serializer = categoryserializer(data,many=True)
    # print(serializer.data)
    return render(request, 'display.html',{'datas':serializer.data})
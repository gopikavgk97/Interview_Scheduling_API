from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from .models import Candidate,Interviewer
import json
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from django.http import HttpResponse
from django.shortcuts import render, redirect
import datetime

class Add_Candidate_Slot(View):
    def get(self,request):
        start_time=request.GET.get('start_time')
        if(int(start_time)<0 or int(start_time)>24):
            return {"Kindly input time between 00 and 24 hrs"}
        end_time=request.GET.get('end_time')
        if(int(end_time) < 0 or int(end_time) > 24):
            return {"Kindly input time between 00 and 24 hrs"}
        candidate_ID=request.GET.get('candidate_ID')
        candidate_name=request.GET.get('candidate_name')
        print(start_time)
        print(end_time)
        print(candidate_ID,candidate_name)
        data={}

        candidate_data={
            'candidate_ID':candidate_ID,
            'start_time':start_time,
            'end_time':end_time,
            'candidate_name':candidate_name,
        }
        candidate_add=Candidate.objects.create(**candidate_data)
        data={
            "status":f"New Candidate and this timing are added .Reference id:{candidate_add.id}"
        }
        return JsonResponse(data,status=201)

class Add_Interviewer_Slot(View):
    def get(self,request):
        start_time=request.GET.get('start_time')
        if(int(start_time)<0 or int(start_time)>24):
            return {"Kindly input time between 00 and 24 hrs"}
        end_time=request.GET.get('end_time')
        if(int(end_time)<0 or int(end_time)>24):
            return {"Kindly input time between 00 and 24 hrs"}
        interviewer_ID=request.GET.get('interviewer_ID')
        interviewer_name=request.GET.get('interviewer_name')
        print(start_time)
        print(end_time)
        print(interviewer_ID,interviewer_name)
        data={}

        interviewer_data={
            'interviewer_ID':interviewer_ID,
            'start_time':start_time,
            'end_time':end_time,
            'interviewer_name':interviewer_name,
        }
        interviewer_add=Interviewer.objects.create(**interviewer_data)
        data={
            "status":f"Interviewer added with id:{interviewer_add.id}"
        }
        return JsonResponse(data,status=201)

class Calculate_Slot(View):
    def get(self,request):
        interviewer_id=request.GET.get('interviewer_id')
        candidate_id=request.GET.get('candidate_id')
        print(interviewer_id,candidate_id)
        data={}
        #items_count = Products.objects.count()
        #**************************
        mydata = Candidate.objects.filter(candidate_ID=candidate_id).values()
        print(mydata[0])
        start_time_candidate=mydata[0]['start_time']
        print(start_time_candidate)
        end_time_candidate=mydata[0]['end_time']
        print(end_time_candidate)
        c_time=[]
        for i in range(start_time_candidate,end_time_candidate+1):
            c_time.append(i)
        print(c_time)

        mydata = Interviewer.objects.filter(interviewer_ID=interviewer_id).values()
        print(mydata[0])
        start_time_interviewer=mydata[0]['start_time']
        print(start_time_interviewer)
        end_time_interviewer=mydata[0]['end_time']
        print(end_time_interviewer)
        i_time=[]
        for i in range(start_time_interviewer,end_time_interviewer+1):
            i_time.append(i)
        print(i_time)

# input:1)[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
#         [9, 10, 11, 12, 13, 14, 15, 16]
#       2)[9, 10, 11, 12, 13, 14, 15, 16]
#         [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
# output: 9, 10, 11, 12, 13, 14
#         9, 10, 11, 12, 13, 14

        def findcommon(list1=[],list2=[]):
            common=[x for x in list1 if x in list2]
            print(common)
            return common
            
            #return common
        common=findcommon(i_time,c_time)
        temp_lst=[]
        output_lst=[]
        for i in range(0,len(common)-1):
            temp_lst=[]
            #print(common[i],common[i+1])
            temp_lst.append(common[i])
            temp_lst.append(common[i+1])
            temp_tuple=tuple(temp_lst)
            #print(temp_tuple)
            output_lst.append(temp_tuple)
        print(output_lst)
        if len(output_lst)==0:
            data['No Slots are there ']=str(output_lst)
        else:
            data['Available Slots are : ']=str(output_lst)

        return JsonResponse(data,status=201)
        
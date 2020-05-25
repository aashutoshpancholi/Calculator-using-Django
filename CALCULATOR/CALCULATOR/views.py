from django.shortcuts import render

from django.http import HttpResponse, JsonResponse


def CALC_APP(request):
    return render(request, 'CALC_index.html')

def submitquery(request):
    q = request.GET['query']
    try:
        ans = eval(q)
        mydictionary = {
            "q": q,
            "ans": ans,
            "error": False,
            "result": True
        }
        return render(request,'CALC_index.html',context=mydictionary)
    except:
        mydictionary = {
            "error": True,
            "result": False

        }
        return render(request,'CALC_index.html',context=mydictionary)
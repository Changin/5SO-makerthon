from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
import json
from django.conf import settings

# Create your views here.
# pub_date = timezone.datetime.now()

#save image file to server
def set_cctv_image(request):
    if (request.method == 'POST'):
        filename = request.POST['title']
        
        destination = open(settings.MEDIA_ROOT + filename, 'wb+')
        
        for img in request.FILES.getlist('imgs'):
            destination.wirte(img)
            
        destination.close()
        
        #todo : import module, get response data
        if(safe):
            data = {
                "key": "value",
                "pub_date": timezone.datetime.now(),
            }
            return HttpResponse(json.dumps(data), content_type = "application/json")
        else:
            #send image

        #return HttpResponse(json.dumps(data), content_type = "application/json")
    
    else:
        return render(request, 'cctv/main_page.html', {})
        


def get_cctv_data(request):
    
    #todo : import module, get alert data
    #todo : print module data to console
    data = {
        "min": 0,
        "sec": 15,
    }

    return HttpResponse(json.dumps(data), content_type = "application/json")
    #return render(request, 'cctv/main_page.html', {})
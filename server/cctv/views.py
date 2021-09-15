import sys
from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
import json
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import base64

sys.path.append('/makerthon/5SO-makerthon/server/cctv/Module')
from scripts import pedestrian_detection

# Create your views here.
# pub_date = timezone.datetime.now()

flag = 0 ##initialize model variable##

#save image file to server
@csrf_exempt
def set_cctv_image(request):
    if (request.method == 'POST'):
        print("set_cctv_image activated")
        #filename = request.POST['title']
        filename = "testimage.png"
        
        destination = open(settings.MEDIA_ROOT +"/"+ filename, 'wb+')

        data = json.loads(request.body)
        base64_img = data.get('data', None)

        base64_img = base64_img[22:]

        new_base64_img = base64_img + '=' * (4 - len(base64_img) % 4)

        img_byte = base64.b64decode(new_base64_img)
        img = img_byte
        #img = img_byte.decode('ascii')

        
        #print("recieved image, image data : "+img)

        destination.write(img)
            
        destination.close()

        pass  ############# call model !!!
        pedestrian_detection.main(settings.MEDIA_ROOT+"/"+filename, settings.MEDIA_ROOT+"/"+"output.png")
        
        #todo : import module, get response data
        if(warning is 0):   # 이미지 판단 결과 이상 감지 안된 경우
            data = {
                "key": "value",
                "pub_date": timezone.datetime.now(),
            }
            return HttpResponse(json.dumps(data), content_type = "application/json")
        else:   # 이상 감지된 경우
            pass
            #send image path

        #return HttpResponse(json.dumps(data), content_type = "application/json")

    else:
        data = {
            "key": "value",
            "pub_date": timezone.datetime.now(),
        }
        return HttpResponse(json.dumps(data), content_type = "application/json")



def get_cctv_data(request):
    global flag

    #initialize
    if(flag is 0):
        flag = 1
        pass ########   call initialize function!!


    return render(request, 'cctv/main_page.html', {})

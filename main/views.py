from django.shortcuts import render
from django.core.files.storage import FileSystemStorage


# Create your views here.

import cv2

from keras.models import load_model
model = load_model(r"C:\Users\Lenovo\OneDrive\Desktop\lung-cancer\main\trained.h5")


def upload(request):
    if request.method == 'POST' and request.FILES['upload']:
        upload = request.FILES['upload']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)
        img= cv2.imread(r'C:\Users\Lenovo\OneDrive\Desktop\lung-cancer'+file_url)
        img = cv2.resize(img,(300,300))
        img = img/255.0
        img = img.reshape(1,300,300,3)
        model.predict(img)
        prediction = model.predict(img) >= 0.5
        if prediction>=0.5:
            prediction = "Lung is infected"
        else:
            prediction = "Normal"
            print("Prediction: "+prediction)

        return render(request, 'main/upload.html', context={'file_url': file_url,"prediction":prediction})
    return render(request, 'main/upload.html')




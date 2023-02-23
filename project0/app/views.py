from django.shortcuts import render
import re

# Create your views here.
def home(request):
    if request.method=="POST":
        paragraph=request.POST["paragraph"]
        review=re.sub("[^a-zA-z0-9.]"," ",paragraph)
        review=review.lower()
        review=review.split()
        review=" ".join(review)
        d={"review":review}
        return render(request,"response.html",d)
    return render(request,"home.html")
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,"index.html")
def analyzed(request):
    #getting text from the textarea
    djtext=request.GET.get("text","default")
    #checking whether the checkbox is on or off
    djcheck1=request.GET.get("check1","of")
    #checking whether the secong checkbx ison or off
    djcheck2=request.GET.get("check2","of")
    #checking whether the third checkbox is on or off
    djcheck3=request.GET.get("check3","of")
    #checking whether the 4th checkbox is on or off
    djcheck4 = request.GET.get("check4", "of")
    #checking whether the check 5 is on or of
    djcheck5=request.GET.get("check5","of")

    punctuation="""!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~"""
    analyze=''
    if djcheck1=="on":
        for char in djtext:
            if char not in punctuation:
                analyze+=char
        params = {"name": "Entered Text After Removing Punctuation...", "analyzed": analyze}
        return render(request, "analyzed.html", params)
    elif(djcheck2=="on"):
        for char in djtext:
            analyze+=char.upper()
        params = {"name": "Entered Text In UpperCase...", "analyzed": analyze}
        return render(request, "analyzed.html", params)
    elif (djcheck3 == "on"):
        for char in djtext:
            if char !="\n":
                analyze+=char
        params = {"name": "Entered Text After Removing Newline Character", "analyzed": analyze}
        return render(request, "analyzed.html...", params)
    elif (djcheck4 == "on"):
        for index,char in enumerate(djtext):
            if djtext[index] ==" " and djtext[index+1]==" ":
                continue
            else:
                analyze+=djtext[index]
        params = {"name": "Entered Text After Removing Extra space...", "analyzed": analyze}
        return render(request, "analyzed.html", params)
    elif (djcheck5 == "on"):
        taotalchar=len(djtext)
        analyze=str(taotalchar)
        params = {"name": "Total Number of Charcaters In Entered Text...", "analyzed": analyze}
        return render(request, "analyzed.html", params)
    else:
         analyze=djtext
         params = {"name": "Entered Text...", "analyzed": analyze}
         return render(request, "analyzed.html", params)
    # print(djtext)
    # print(djcheck)
def about_us(request):
    return HttpResponse("Welcome to About US Page...")
def contact_us(request):
    return HttpResponse("""Welcome to contact us page....""")
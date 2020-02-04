# I have created this file
from django.http import HttpResponse
from django.shortcuts import render



def analyze(request):
    # to get the text
    djtext=request.POST.get('name','default')
    # to get the checkbox value
    capitalize=request.POST.get('capitalize','off')
    charcounter=request.POST.get('charcounter','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    removepunc=(request.POST.get('removepunc' ,'off'))
    newlineremover=(request.POST.get('newlineremover' ,'off'))

    analyze_text=''
    punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    if removepunc=='on':
        for char in djtext:
            if char not in punctuations:
                analyze_text=analyze_text+char
        prilms={'purpose':'Remove the punctuations','analysed_text':analyze_text}
        djtext=analyze_text
        # return render(request,'analyze.html',prilms)
    if(capitalize=='on'):
        analyze=''
        for char in djtext:
            analyze=analyze+char.upper()
        prilms = {'purpose': 'Text in upper case', 'analysed_text': analyze}
        djtext=analyze
        # return render(request, 'analyze.html', prilms)
    if(newlineremover=='on'):
        analyze=''
        for char in djtext:
            if char!='\n':
                analyze=analyze+char
        prilms = {'purpose': 'removed new line', 'analysed_text': analyze}
        djtext=analyze
        # return render(request, 'analyze.html', prilms)
    if (extraspaceremover == 'on'):
        analyze = ''
        for index,char in enumerate(djtext):
            if not (djtext[index]==" " and djtext[index+1]==" "):
                analyze = analyze + char
        prilms = {'purpose': 'removed space', 'analysed_text': analyze}
        djtext=analyze
        # return render(request, 'analyze.html', prilms)
    if (charcounter == 'on'):
        c=0
        for char in djtext:
            c+=1
        prilms = {'purpose': 'No of characters', 'analysed_text': c}
        djtext=c
        # return render(request, 'analyze.html', prilms)

    if charcounter != 'on' and extraspaceremover != 'on' and newlineremover!='on' and capitalize!='on' and removepunc!='on':
        return HttpResponse("<h1>Please select any operation which we can provide</h1>")

    return render(request, 'analyze.html', prilms)



    # else:
    #     return HttpResponse('Error')





# code for video 6
# def index(request):
#     return HttpResponse('''<h1>Hello</h1> <a href="https://www.youtube.com"> youtube</a><br>
#     <a href="www.flipkart.com"> flipkart</a>''')
#
#
# def pk(request):
#     return HttpResponse("Hello Pritam")
#
# def youtube(request):
#     return HttpResponse("www.youtube.com")


# code for video7
# creating pipelines
#
# def index(Request):
#     return HttpResponse("Home")
#
# def capfirst(Request):
#     return HttpResponse('''<h1>capfirst</h1> <hr><a href="http://127.0.0.1:8000/">Home</a>''' )


# def newlineremover(Request):
#     return HttpResponse('''<h1>newlineremover</h1> <hr><a href="http://127.0.0.1:8000/">Home</a>''')    #Home button in pipelines
#
# def spaceremover(Request):
#     return HttpResponse('''<h1>spaceremover</h1> <hr><a href="http://127.0.0.1:8000/">Home</a>''')
#
# def charcounter(Request):
#     return HttpResponse('''<h1>charcounter</h1> <hr><a href="http://127.0.0.1:8000/">Home</a>''')



# video for creating templates



def index(request):
    return render(request,'index.html')


def about(request):
    return render(request,'about.html')


def contact(request):
    return render(request,'contact.html')
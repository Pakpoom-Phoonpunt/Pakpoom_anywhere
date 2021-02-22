from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Vocab, Definition


def index(request):
    context = {'vocabList': Vocab.objects.all()}
    return render(request,"vocab/index.html",context)

def detail(request, vocab_id):
    vocab = get_object_or_404(Vocab,pk=vocab_id)
    print(vocab)
    context = {'vocab':vocab}
    return render(request,"vocab/detail.html",context)

def addWordPage(request):
    return render(request,"vocab/form.html")

def addWord(request):
    forbiddenList = [""]
    for i in range(1,201):
        forbiddenList.append(" "*i)
    if request.POST.get('vocab') not in forbiddenList and  request.POST.get('def') not in forbiddenList :
        word = Vocab(vocab_text = request.POST.get('vocab'))
        defi = Definition(def_text= request.POST.get('def'), vocab = word)
        word.save()
        defi.save()
        context = {'vocabList': Vocab.objects.all()}
        return render(request,"vocab/index.html",context)
    return HttpResponse("เจ้าไม่ได้ Enter Vocab or Definition ไอ้กรวก")

def home(request):
    return render(request, 'vocab/home.html')
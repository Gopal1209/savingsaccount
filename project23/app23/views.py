from django.shortcuts import render


def showIndex(request):
    return render(request, "index.html")


def send(request):
    data = request.POST.getlist("t")
    sum = 0
    for x in data:
        x = float(x)
        sum = sum + x
    tax = (8 / 100) * sum
    total = sum + tax
    result = {"sum": sum, "tax": tax, "total": total}
    return render(request, "index.html", {"result": result})

from django.shortcuts import render

def post_list(request):

    contex = {
        'keys': 'values',
        
    }
    return render(request, 'blog/post_list.html', contex)
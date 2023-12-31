from django.shortcuts import render
from django.shortcuts import redirect

import markdown2

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def page(request, title):
    if(util.get_entry(title) == None):
        return render(request, "encyclopedia/error.html", {
            "title": title
        })
    return render(request, "encyclopedia/page.html", {
        "title": title,
        "content": markdown2.markdown(util.get_entry(title))
    })

def random(request):
    return redirect("/" + util.get_random_entry())
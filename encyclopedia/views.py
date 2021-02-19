from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import path
import random
import markdown2
from . import util

#Reminder: views should always return an HttpResponse object

"""
Important: redirect(f"wiki/{name}" redirects to currentPattern/wiki/name
           whereas redirect(f"/wiki/{name}) redirects to wiki/name
"""

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

# This view is included in order to mimic the behavior of Wikipedia
# When a user goes to en.wikipedia.org or en.wikipedia.org/wiki it redirects you to en.wikipedia.org/wiki/Main_Page
def main_page(request):
    return redirect('index')

def display(request, page_name):
    #If the page exists, retrieve its content
    #Otherwise display a page not found error
    if page_name in util.list_entries():
        html = markdown2.markdown(util.get_entry(page_name))
        return render(request, "encyclopedia/render_entry.html", {
            "html": html,
            "page_name": page_name
        })
    else:
        raise Http404

def search(request):
    # get returns the value for the given key
    # those keys are submitted with the form
    name = request.GET.get('q')
    if name in util.list_entries():
        return redirect(f"/wiki/{name}")
    else:
        return render(request, "encyclopedia/search.html", {
            "name": name,
            "entries": util.list_entries()
        })

def page_already_exists(request, title):
    return render(request, "encyclopedia/page_already_exists.html", {
        "entry": title
    })

def new_page(request):
    return render(request, "encyclopedia/new_page.html")

def save_page(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    if title in util.list_entries():
        return page_already_exists(request, title)
    else:
        util.save_entry(title, content)
        return redirect(f"/wiki/{title}")

def edit_save(request, page_name):
    content = request.POST.get('text')
    util.save_entry(page_name, content)
    return redirect(f"/wiki/{page_name}")

def random_page(request):
    entries = util.list_entries()
    size = len(entries)
    pos = random.randrange(size)
    entry = entries[pos]
    return redirect(f"/wiki/{entry}")

#Finds the entry title from a given path
#Starts from the end of the path until it finds a '/', and then returns the substring to the right
# def find_title(path):
#     #Position of the last character in the path
#     pos = -1
#     while path[pos] != '/':
#         pos = pos - 2
#     return path[pos+1:]

def edit(request, title):
    #debugger
    # import pdb;pdb.set_trace()
    content = util.get_entry(title)
    return render(request, "encyclopedia/edit_page.html", {
        "content": content,
        "title": title
    })

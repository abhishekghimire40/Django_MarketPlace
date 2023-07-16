from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Item, Category
from .forms import NewItemForm, EditItemForm


# Create your views here.


def items(request):
    query = request.GET.get("query", "")
    category_id = request.GET.get("category", 0)
    items = Item.objects.filter(is_sold=False)
    categories = Category.objects.all()

    if category_id:
        items = items.filter(category_id=category_id)

    if query:
        # if you want to filter using multiple columns then you should use 'Q'  for it
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(
        request,
        "item/items.html",
        {
            "items": items,
            "query": query,
            "categories": categories,
            "category_id": int(category_id),
        },
    )


# view to display detail of a single item
# also we need second param pk as we need to find the single item
def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(
        pk=pk
    )[0:3]
    return render(
        request,
        "item/detail.html",
        {
            "item": item,
            "related_items": related_items,
        },
    )


# view to add a new item to our database
@login_required
def new(request):
    if request.method == "POST":
        form = NewItemForm(request.POST, request.FILES)
        if form.is_valid():
            # As our model has created_by column which is not passed through form
            # so id we directly do save to data base using form.save() it will give error
            # as there is no created_by column coming from our request. so,we save it temporarily
            # using commit=False in form.save()
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect("item:detail", pk=item.id)
    form = NewItemForm()

    return render(request, "item/form.html", {"form": form, "title": "New Item"})


@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()

    return redirect("dashboard:index")


@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    if request.method == "POST":
        form = EditItemForm(request.POST, request.FILES, instance=item)
        form.save()
        return redirect("item:detail", pk=item.id)
    else:
        form = EditItemForm(instance=item)

    return render(request, "item/form.html", {"form": form, "title": "Edit item"})

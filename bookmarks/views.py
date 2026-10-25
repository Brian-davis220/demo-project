from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from .models import Link
from .forms import LinkForm

def link_list(request):
    """Display list of links with optional search and category filter."""
    query = request.GET.get('q', '')
    category = request.GET.get('category', '')
    links = Link.objects.all()
    if query:
        links = links.filter(
            Q(title__icontains=query) |
            Q(url__icontains=query) |
            Q(description__icontains=query)
        )
    if category:
        links = links.filter(category=category)
    context = {
        'links': links,
        'query': query,
        'selected_category': category,
        'categories': Link.Category.choices,
    }
    return render(request, 'bookmarks/link_list.html', context)

def link_create(request):
    """Create a new link."""
    if request.method == 'POST':
        form = LinkForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Link added successfully.')
            return redirect('bookmarks:link_list')
    else:
        form = LinkForm()
    return render(request, 'bookmarks/link_form.html', {'form': form, 'action': 'Add'})

def link_update(request, pk):
    """Edit an existing link."""
    link = get_object_or_404(Link, pk=pk)
    if request.method == 'POST':
        form = LinkForm(request.POST, instance=link)
        if form.is_valid():
            form.save()
            messages.success(request, 'Link updated successfully.')
            return redirect('bookmarks:link_list')
    else:
        form = LinkForm(instance=link)
    return render(request, 'bookmarks/link_form.html', {'form': form, 'action': 'Edit'})

def link_delete(request, pk):
    """Delete a link after confirmation (POST only)."""
    link = get_object_or_404(Link, pk=pk)
    if request.method == 'POST':
        link.delete()
        messages.success(request, 'Link deleted successfully.')
        return redirect('bookmarks:link_list')
    return render(request, 'bookmarks/link_confirm_delete.html', {'link': link})

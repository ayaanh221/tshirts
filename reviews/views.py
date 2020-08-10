from django.shortcuts import get_object_or_404, render

from .models import Review, tshirts


def review_list(request):
    latest_review_list = Review.objects.order_by('-date')[:9]
    context = {'latest_review_list':latest_review_list}
    return render(request, 'reviews/review_list.html', context)


def review_detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    return render(request, 'reviews/review_detail.html', {'review': review})


def tshirts_list(request):
    tshirts_list = tshirts.objects.order_by('-name')
    context = {'tshirts_list':tshirts_list}
    return render(request, 'reviews/tshirts_list.html', context)


def tshirts_detail(request, tshirts_id):
    tshirts = get_object_or_404(tshirts, pk=tshirts_id)
    return render(request, 'reviews/tshirts_detail.html', {'tshirts': tshirts})
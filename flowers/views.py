from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from flowers.models import Bouquet, Shop, BouquetFlower, Buyer, Consult
from django.contrib import messages


def serialize_bouquet(bouquet):
    return {
        "title": bouquet.title,
        "price": bouquet.price,
        "photo": bouquet.photo,
        'slug': bouquet.slug}


def serialize_shop(shop):
    return{
        'title': shop.title,
        'address': shop.address,
        'phone_number': shop.phone_number
    }

def index(request):
    recommended_bouquets = Bouquet.objects.filter(is_recommended=True)[:3]
    shops = Shop.objects.all()
    context = {'recommended_bouquets': [serialize_bouquet(bouquet) for bouquet in recommended_bouquets],
               'shops': [serialize_shop(shop) for shop in shops] }
    return render(request, 'index.html', context)

def catalog(request):
    return render(request, 'catalog.html')


def flower_detail(request):
    return render(request, 'card.html')


def quiz(request):
    return render(request, 'quiz.html')


def quiz_step(request):
    return render(request, 'quiz-step.html')


def result(request):
    return render(request, 'result.html')


def order(request, pk=None):
    return render(request, 'order.html')


def order_step(request):
    return render(request, 'order-step.html')


def consultation(request):
    if request.method == 'POST':
        name = request.POST.get('fname')
        phone = request.POST.get('tel')

        if not name or not phone:
            messages.error(request, 'Пожалуйста, заполните все поля.')
            return render(request, 'consultation.html')

        Consult.objects.create(
            name=name,
            phone_number=phone
        )
        messages.success(request, 'Заявка на консультацию успешно отправлена!')
        return redirect('success_consult')

    return render(request, 'consultation.html')


def card(request, slug):
    bouquet = get_object_or_404(Bouquet, slug=slug)
    bouquet_flowers = BouquetFlower.objects.filter(bouquet=bouquet)
    serialized_flowers = []
    for flower in bouquet_flowers:
        serialized_flowers.append({
            'title': flower.flower,
            'amount': flower.amount,       
        })
    serialized_bouquet = {
        'title': bouquet.title,
        'price': bouquet.price,
        'photo': bouquet.photo,
        'width': bouquet.width,
        'height': bouquet.height,
        'flowers': serialized_flowers
    }
    context = {
        'bouquet': serialized_bouquet
    }
    return render(request, 'card.html', context)


def success_consult(request):
    if request.method == 'POST':
        name = request.POST.get('fname')
        phone = request.POST.get('tel')

        if not name or not phone:
            messages.error(request, 'Пожалуйста, заполните все поля.')
            return render(request, 'consultation.html')

        Consult.objects.create(
            name=name,
            phone_number=phone
        )
        messages.success(request, 'Заявка на консультацию успешно отправлена!')
        return redirect('success_consult')

    return render(request, 'success_consult.html')

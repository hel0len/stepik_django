import random

from django.http import HttpResponseBadRequest, HttpResponseForbidden, HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render

from tours.data import departures, description, subtitle, title, tours


def main_view(request):
    random_tours = dict(random.sample(tours.items(), k=6))
    return render(request, 'index.html', context={'departures': departures,
                                                  'tours': random_tours,
                                                  'title': title,
                                                  'subtitle': subtitle,
                                                  'description': description})


def departure_view(request, departure_id):
    tour_prices = []
    tour_nights = []
    tours_in_departure = {}
    for key, value in tours.items():
        if departure_id == value["departure"]:
            tours_in_departure[key] = value
            tour_prices.append(value['price'])
            tour_nights.append(value['nights'])
    min_price = min(tour_prices)
    max_price = max(tour_prices)
    min_night = min(tour_nights)
    max_night = max(tour_nights)
    return render(request, 'departure.html', context={'departures': departures,
                                                      'departure': departures[departure_id],
                                                      'tours': tours_in_departure,
                                                      'min_price': min_price,
                                                      'max_price': max_price,
                                                      'min_nights': min_night,
                                                      'max_nights': max_night,
                                                      'title': title})


def tour_view(request, tour_id):
    tour = tours[tour_id]
    departure = departures[tour['departure']]
    hotel_rating = '⭐' * int(tour['stars'])
    return render(request, 'tour.html', context={'departures': departures,
                                                 'departure': departure,
                                                 'tour': tours[tour_id],
                                                 'stars': hotel_rating,
                                                 'title': title})


def custom_handler400(request, exception):
    # Call when SuspiciousOperation raised
    return HttpResponseBadRequest('Неверный запрос!')


def custom_handler403(request, exception):
    # Call when PermissionDenied raised
    return HttpResponseForbidden('Доступ запрещен!')


def custom_handler404(request, exception):
    # Call when Http404 raised
    return HttpResponseNotFound('Ресурс не найден!')


def custom_handler500(request):
    # Call when raised some python exception
    return HttpResponseServerError('Ошибка сервера!')

from django.urls import path
import tours.views
from tours.views import custom_handler400, custom_handler403, custom_handler404, custom_handler500

handler400 = custom_handler400
handler403 = custom_handler403
handler404 = custom_handler404
handler500 = custom_handler500

urlpatterns = [
    path('', tours.views.main_view, name='main'),
    path('departure/<str:departure>/', tours.views.departure_view, name='departure'),
    path('tour/<int:id>/', tours.views.tour_view, name='tour')
]

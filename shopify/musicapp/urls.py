from django.urls import path
from musicapp import views, accounts, tracks, tour
from shop import shop


urlpatterns = [
    #  ADMIN
    path('administrator/', views.admin, name='admin'),
    path('registration/', accounts.registration_view, name='registration'),
    path('login/', accounts.login_view, name='login'),
    path('logout/', accounts.logout_view, name='logout'),

    # TOUR
    path('tours/', tour.TourView.as_view(), name='tours'),
    path('addtour/', tour.add_tour, name='newtour'),
    path('touradmin/', tour.TourAdminList.as_view(), name='tours-list'),
    path('updatetour<int:pk>/', tour.edit_tour, name='update-tour'),
    path('deletetour<int:pk>/', tour.delete_tour, name='delete-tour'),


    # TRACK
    path('', tracks.IndexView.as_view(), name='index'),
    path('uploadtrack/', tracks.add_track, name='upload'),
    path('updatetrack/<int:pk>/', tracks.edit_track, name='updatetrack'),
    path('deletetrack/<int:pk>/', tracks.remove_track, name='deletetrack'),
    path('trackadmin/', tracks.AdminViewTracks.as_view(), name='admintracks'),


    # SHOP
    path('shop/', shop.ShopView.as_view(), name='shop'),
    path('addproduct/', shop.add_product, name='add-product'),
    path('productlist/', shop.AdminProductList.as_view(), name='productlist'),
    path('updateproduct/<int:pk>/', shop.edit_product, name='update-product'),
    path('deleteproduct/<int:pk>/', shop.delete_product, name='delete-product'),
    path('updateCart/',shop.updateItem,name='updateCart'),
    path('cart/',shop.cart,name='cart'),
]

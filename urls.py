from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm, MyPasswordChangeForm ,MyPasswordResetForm, MySetPasswordForm

urlpatterns = [
    path('', views.home),

    path('fine/', views.FineView.as_view(), name="fine"),
    path('casual/', views.CasualView.as_view(), name="casual"),
    path('cont/', views.ContView.as_view(), name="cont"),
    path('family/', views.FamilyView.as_view(), name="family"),
    path('fast/', views.FastView.as_view(), name="fast"),
    path('fastfood/', views.FastfoodView.as_view(), name="fastfood"),
    path('cafe/', views.CafeView.as_view(), name="cafe"),
    path('buffet/', views.BuffetView.as_view(), name="buffet"),
    path('truck/', views.TrucksView.as_view(), name="truck"),
    path('pop/', views.PopView.as_view(), name="pop"),

    path('search', views.search, name = "food"),
    path('zsearch', views.zsearch, name = "zfood"),

    path('zrestro', views.zrestro, name = "zrestro"),

    path('zfine', views.ZFineView, name="zfine"),
    path('zcasual', views.ZCasualView, name="zcasual"),
    path('zcont', views.ZContView, name="zcont"),
    path('zfamily', views.ZFamilyView, name="zfamily"),
    path('zfast', views.ZFastView, name="zfast"),
    path('zfastfood', views.ZFastfoodView, name="zfastfood"),
    path('zcafe', views.ZCafeView, name="zcafe"),
    path('zbuffet', views.ZBuffetView, name="zbuffet"),
    path('ztruck', views.ZTrucksView, name="ztruck"),
    path('zpop', views.ZPopView, name="zpop"),

    path('res/', views.RestroView.as_view(), name="res"),
    path('restype/', views.RestrotypeView.as_view(), name="restype"),

    path('productdetail/<int:id>', views.ProductDetailView.as_view(), name="productdetail"),
    #path('food/product-detail/', views.product_detail, name='product-detail'),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name='showcart'),
    path('pluscart/', views.plus_cart),
    path('minuscart/', views.minus_cart),
    path('removecart/', views.remove_cart),


    path('buy/', views.buy_now, name='buy-now'),
    
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    
   # path('products/', views.pro, name='produsts'),
   # path('products/<slug:data>', views.pro, name='productdetails'),
    #path('login/', views.login, name='login'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('URF/', views.URFView.as_view(), name='URF'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='app/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('passchange/', auth_views.PasswordChangeView.as_view(template_name='app/passchange.html', form_class=MyPasswordChangeForm, success_url='/passchdone/'), name='passchange'),
    path('passchdone/', auth_views.PasswordChangeView.as_view(template_name='app/passchdone.html'), name='passchdone'),
    path('passreset/', auth_views.PasswordResetView.as_view(template_name='app/passreset.html', form_class=MyPasswordResetForm), name='passreset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='app/passreset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='app/passreset_confirm.html', form_class=MySetPasswordForm), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='app/passreset_complete.html'), name='password_reset_complete'),
   # path('registration/', views.customerregistration, name='customerregistration'),
   
    path('checkout/', views.checkout, name='checkout'),
    path('paymentdone/', views.payment_done, name='paymentdone'),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  
 

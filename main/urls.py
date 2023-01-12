from django.urls import path
from .views import *


urlpatterns = [
    path('' , registerform , name = "registerform"),
    path("500err" , error505 , name = "500error"),
    path("404err" , error404 , name = "404error"),
    path("success" , successmsg , name = "successmsg"),
    path("RtELrZ0uxYUFdt0ykZn1vCbUjHjFAOQGXPy0Z1xDiw" , newsform),
    path("IXi4NZRd1MnVukyUsDvuEeKZULh5dS2cTvCuhdyiw" , serviceform)
]
from rest_framework.throttling import UserRateThrottle

class JackRateThrottle(UserRateThrottle):
    scope ='jack'
    
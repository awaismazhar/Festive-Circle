from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

class DontPopulateUserModel(DefaultSocialAccountAdapter):
    """ 
    Adapter to disable allauth new signups
    Used at equilang/settings.py with key ACCOUNT_ADAPTER

    https://django-allauth.readthedocs.io/en/latest/advanced.html#custom-redirects """
    

    
    def save_user(self, request, sociallogin, form=None):
        return super(DontPopulateUserModel, self).save_user(
            request, sociallogin, None
        )
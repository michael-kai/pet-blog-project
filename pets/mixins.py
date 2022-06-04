"""
Basic mixins
"""

MAIN_MENU = [
    {'name': 'Login', 'url_name': 'sign-in'},
    {'name': 'Join', 'url_name': 'join'},
    {'name': 'Logout', 'url_name': 'sign-out'},
    {'name': 'Search', 'url_name': 'search'},
    {'name': 'Dogs', 'url_name': 'dogs'},
    {'name': 'Cats', 'url_name': 'cats'},
    {'name': 'Pets Life', 'url_name': 'home'},
]

FOOTER_MENU = [
    {'name': 'Contact', 'url_name': 'contact'},
    {'name': 'Terms and Conditions', 'url_name': 'terms'},
]


class BaseMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = MAIN_MENU
        context['footer'] = FOOTER_MENU
        return context

    @staticmethod
    def get_user_context_func():
        context = {'menu': MAIN_MENU, 'footer': FOOTER_MENU}
        return context


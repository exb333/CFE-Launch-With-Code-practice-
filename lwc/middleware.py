from polls.models import Join
from django.utils.deprecation import MiddlewareMixin
class ReferMiddleware(MiddlewareMixin):
    def process_request(self, request):
        poll_id =  (request.GET.get('ref'))

        try:
            obj = Join.objects.get(ref_id=poll_id)
        except:
            obj = None

        if obj:
            request.session['ref'] = obj.id
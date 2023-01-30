from hitcount.utils import get_hitcount_model
from hitcount.views import HitCountMixin

def update_views(request, object):
    context = {}
    hit_count = get_hitcount_model().objects.get_for_object(object)
    hits = hit_count.hits
    hitcontext = context["hitcount"] = {"pk": hit_count.pk}
    hit_count_response = HitCountMixin.hit_count(request, hit_count)

    if hit_count_response.hit_counted:
        hits = hits+1
        hitcontext["hitcounted"] = hit_count_response.hit_counted
        hitcontext["hit_message"] = hit_count_response.hit_message
        hitcontext["total_hits"] = hits

# def update_views(request, object):
#     context = {}
#     hit_count = get_hitcount_model().objects.get_for_object(object)
#     hits = hit_count.hits
#     hitcontext = context["hitcount"] = {"pk": hit_count.pk}
#     hit_count_response = HitCountMixin.hit_count(request, hit_count)

#     # Increment the hit count every time the function is called
#     hits = hits + 1
#     hit_count.hits = hits
#     hit_count.save()
    
#     hitcontext["total_hits"] = hits
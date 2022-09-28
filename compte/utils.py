
import random
import string
from django.utils.text import slugify



def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_member_id_generator(instance):
    member_new_id= random_string_generator()

    Klass= instance.__class__

    qs_exists= Klass.objects.filter(shipping_id= member_new_id).exists()
    if qs_exists:
        return unique_member_id_generator(instance)
    return member_new_id


from __future__ import absolute_import
import pickle

from django_cryptography.fields import FIELD_CACHE, EncryptedMixin

from django.db import models


class EncryptedPickle2Mixin(EncryptedMixin):

    def _dump(self, value):
        return self._fernet.encrypt(pickle.dumps(value, protocol=2))


def encrypt(base_field):
    """
    modified from django_cryptography.fields to force pickle protocol v2 so data saved by python 3
    can be read by python 2
    """
    def get_encrypted_field(base_class):
        assert not isinstance(base_class, models.Field)
        field_name = 'Encrypted' + base_class.__name__
        if base_class not in FIELD_CACHE:
            FIELD_CACHE[base_class] = type(field_name,
                                           (EncryptedPickle2Mixin, base_class), {
                                               'base_class': base_class,
                                           })
        return FIELD_CACHE[base_class]
    name, path, args, kwargs = base_field.deconstruct()
    return get_encrypted_field(base_field.__class__)(*args, **kwargs)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Monster, MonsterInstance, Summoner


# Monster Database stuff
class MonsterAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Basic Information',  {
            'fields': (
                'name',
                'element',
                'archetype',
                'base_stars',
                'can_awaken',
                'is_awakened',
                'awakens_from',
                'fusion_food',
            )
        }),
        ('Awakening Materials', {
            'fields': (
                'awaken_magic_mats_low',
                'awaken_magic_mats_mid',
                'awaken_magic_mats_high',
                'awaken_ele_mats_low',
                'awaken_ele_mats_mid',
                'awaken_ele_mats_high',
            )
        })
    ]

    list_display = ('image_url', 'name', 'element', 'archetype', 'base_stars', 'awakens_from')
    list_filter = ('element', 'archetype', 'base_stars', 'is_awakened')
    search_fields = ['name']

admin.site.register(Monster, MonsterAdmin)


# User management stuff
class SummonerInline(admin.StackedInline):
    model = Summoner
    can_delete = False
    verbose_name_plural = 'summoner'


class UserAdmin(UserAdmin):
    inlines = (SummonerInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)


# Monster Instances stuff
# class MonsterInstanceAdmin(admin.ModelAdmin):

admin.site.register(MonsterInstance)
# admin.site.register(MonsterInstance, MonsterInstanceAdmin)
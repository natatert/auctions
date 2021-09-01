from django.contrib import admin

from .models import Auction, Bidder


class AuctionAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'address')


class BidderAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_name', 'get_address')

    def get_name(self, obj):
        return obj.auction.name
    get_name.short_description = 'Название аукциона'

    def get_address(self, obj):
        return obj.auction.address
    get_address.short_description = 'Адрес аукциона'


admin.site.register(Auction, AuctionAdmin)
admin.site.register(Bidder, BidderAdmin)

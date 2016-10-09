# -*- coding: utf-8 -*-
import os
from xbmcswift2 import Plugin


plugin = Plugin()

addon_path = plugin.addon.getAddonInfo('path').decode('utf-8')

@plugin.route('/')
def index():
    items = [{
        'label' : 'Radio Record',
        'path' : 'http://air2.radiorecord.ru:805/rr_320',
        'thumbnail': os.path.join(addon_path, 'fanart.jpg'),
        'is_playable': True
    }, {
        'label' : 'Megamix',
        'path' : 'http://air2.radiorecord.ru:805/mix_320',
        'is_playable': True
    }, {
        'label' : 'Record Deep',
        'path' : 'http://air2.radiorecord.ru:805/deep_320',
        'is_playable': True
    }, {
        'label' : 'Record Club',
        'path' : 'http://air2.radiorecord.ru:805/club_320',
        'is_playable': True
    }, {
        'label' : 'Future House',
        'path' : 'http://air2.radiorecord.ru:805/fut_320',
        'is_playable': True
    }, {
        'label' : 'Trancemission',
        'path' : 'http://air2.radiorecord.ru:805/tm_320',
        'is_playable': True
    }, {
        'label' : 'Record Chill-Out',
        'path' : 'http://air2.radiorecord.ru:805/chil_320',
        'is_playable': True
    }, {
        'label' : 'Minimal/Tech',
        'path' : 'http://air2.radiorecord.ru:805/mini_320',
        'is_playable': True
    }, {
        'label' : 'Pirate Station',
        'path' : 'http://air2.radiorecord.ru:805/ps_320',
        'is_playable': True
    }, {
        'label' : 'Russian Mix',
        'path' : 'http://air2.radiorecord.ru:805/rus_320',
        'is_playable': True
    }, {
        'label' : 'Vip House',
        'path' : 'http://air2.radiorecord.ru:805/vip_320',
        'is_playable': True
    }, {
        'label' : 'Record Breaks',
        'path' : 'http://air2.radiorecord.ru:805/brks_320',
        'is_playable': True
    }, {
        'label' : 'Record Dubstep',
        'path' : 'http://air2.radiorecord.ru:805/dub_320',
        'is_playable': True
    }, {
        'label' : 'Record Dancecore',
        'path' : 'http://air2.radiorecord.ru:805/dc_320',
        'is_playable': True
    }, {
        'label' : 'Record Techno',
        'path' : 'http://air2.radiorecord.ru:805/techno_320',
        'is_playable': True
    }, {
        'label' : 'Record Hardstyle',
        'path' : 'http://air2.radiorecord.ru:805/teo_320',
        'is_playable': True
    }, {
        'label' : 'Record Trap',
        'path' : 'http://air2.radiorecord.ru:805/trap_320',
        'is_playable': True
    }, {
        'label' : 'Pump',
        'path' : 'http://air2.radiorecord.ru:805/pump_320',
        'is_playable': True
    }, {
        'label' : 'Record Rock',
        'path' : 'http://air2.radiorecord.ru:805/rock_320',
        'is_playable': True
    }, {
        'label' : 'Yo! FM',
        'path' : 'http://air2.radiorecord.ru:805/yo_320',
        'is_playable': True
    }, {
        'label' : 'Rave FM',
        'path' : 'http://air2.radiorecord.ru:805/rave_320',
        'is_playable': True
    }, {
        'label' : u'Супердиско 90-х',
        'path' : 'http://air2.radiorecord.ru:805/sd90_320',
        'is_playable': True
    }, {
        'label' : u'Медляк FM',
        'path' : 'http://air2.radiorecord.ru:805/mdl_320',
        'is_playable': True
    }, {
        'label' : u'Гоп FM',
        'path' : 'http://air2.radiorecord.ru:805/gop_320',
        'is_playable': True
    }]

    return items


if __name__ == '__main__':
    plugin.run()
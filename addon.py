# -*- coding: utf-8 -*-
import os
from xbmcswift2 import Plugin


plugin = Plugin()

path = plugin.addon.getAddonInfo('path').decode('utf-8')
media= os.path.join(path, 'resources', 'media')

@plugin.route('/')
def index():
    items = [{
        'label' : 'Radio Record',
        'path' : 'http://air2.radiorecord.ru:805/rr_320',
        'thumbnail': os.path.join(media, 'rr.jpg'),
        'is_playable': True
    }, {
        'label' : 'Megamix',
        'path' : 'http://air2.radiorecord.ru:805/mix_320',
        'thumbnail': os.path.join(media, 'mix.jpg'),
        'is_playable': True
    }, {
        'label' : 'Record Deep',
        'path' : 'http://air2.radiorecord.ru:805/deep_320',
        'thumbnail': os.path.join(media, 'deep.jpg'),
        'is_playable': True
    }, {
        'label' : 'Record Club',
        'thumbnail': os.path.join(media, 'club.jpg'),
        'path' : 'http://air2.radiorecord.ru:805/club_320',
        'is_playable': True
    }, {
        'label' : 'Future House',
        'thumbnail': os.path.join(media, 'fut.jpg'),
        'path' : 'http://air2.radiorecord.ru:805/fut_320',
        'is_playable': True
    }, {
        'label' : 'Trancemission',
        'path' : 'http://air2.radiorecord.ru:805/tm_320',
        'thumbnail': os.path.join(media, 'tm.jpg'),
        'is_playable': True
    }, {
        'label' : 'Record Chill-Out',
        'path' : 'http://air2.radiorecord.ru:805/chil_320',
        'thumbnail': os.path.join(media, 'chil.jpg'),
        'is_playable': True
    }, {
        'label' : 'Minimal/Tech',
        'path' : 'http://air2.radiorecord.ru:805/mini_320',
        'thumbnail': os.path.join(media, 'mini.jpg'),
        'is_playable': True
    }, {
        'label' : 'Pirate Station',
        'path' : 'http://air2.radiorecord.ru:805/ps_320',
        'thumbnail': os.path.join(media, 'ps.jpg'),
        'is_playable': True
    }, {
        'label' : 'Russian Mix',
        'path' : 'http://air2.radiorecord.ru:805/rus_320',
        'thumbnail': os.path.join(media, 'rus.jpg'),
        'is_playable': True
    }, {
        'label' : 'Vip House',
        'path' : 'http://air2.radiorecord.ru:805/vip_320',
        'thumbnail': os.path.join(media, 'vip.jpg'),
        'is_playable': True
    }, {
        'label' : 'Record Breaks',
        'path' : 'http://air2.radiorecord.ru:805/brks_320',
        'thumbnail': os.path.join(media, 'brks.jpg'),
        'is_playable': True
    }, {
        'label' : 'Record Dubstep',
        'path' : 'http://air2.radiorecord.ru:805/dub_320',
        'thumbnail': os.path.join(media, 'dub.jpg'),
        'is_playable': True
    }, {
        'label' : 'Record Dancecore',
        'path' : 'http://air2.radiorecord.ru:805/dc_320',
        'thumbnail': os.path.join(media, 'dc.jpg'),
        'is_playable': True
    }, {
        'label' : 'Record Techno',
        'path' : 'http://air2.radiorecord.ru:805/techno_320',
        'thumbnail': os.path.join(media, 'techno.jpg'),
        'is_playable': True
    }, {
        'label' : 'Record Hardstyle',
        'path' : 'http://air2.radiorecord.ru:805/teo_320',
        'thumbnail': os.path.join(media, 'teo.jpg'),
        'is_playable': True
    }, {
        'label' : 'Record Trap',
        'path' : 'http://air2.radiorecord.ru:805/trap_320',
        'thumbnail': os.path.join(media, 'trap.jpg'),
        'is_playable': True
    }, {
        'label' : 'Pump',
        'path' : 'http://air2.radiorecord.ru:805/pump_320',
        'thumbnail': os.path.join(media, 'pump.jpg'),
        'is_playable': True
    }, {
        'label' : 'Record Rock',
        'path' : 'http://air2.radiorecord.ru:805/rock_320',
        'thumbnail': os.path.join(media, 'rock.jpg'),
        'is_playable': True
    }, {
        'label' : 'Yo! FM',
        'path' : 'http://air2.radiorecord.ru:805/yo_320',
        'thumbnail': os.path.join(media, 'yo.jpg'),
        'is_playable': True
    }, {
        'label' : 'Rave FM',
        'path' : 'http://air2.radiorecord.ru:805/rave_320',
        'thumbnail': os.path.join(media, 'rave.jpg'),
        'is_playable': True
    }, {
        'label' : u'Супердиско 90-х',
        'path' : 'http://air2.radiorecord.ru:805/sd90_320',
        'thumbnail': os.path.join(media, 'sd90.jpg'),
        'is_playable': True
    }, {
        'label' : u'Медляк FM',
        'path' : 'http://air2.radiorecord.ru:805/mdl_320',
        'thumbnail': os.path.join(media, 'mdl.jpg'),
        'is_playable': True
    }, {
        'label' : u'Гоп FM',
        'path' : 'http://air2.radiorecord.ru:805/gop_320',
        'thumbnail': os.path.join(media, 'gop.jpg'),
        'is_playable': True
    }]

    return items


if __name__ == '__main__':
    plugin.run()
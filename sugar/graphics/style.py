# Copyright (C) 2006, Red Hat, Inc.
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place - Suite 330,
# Boston, MA 02111-1307, USA.

import logging

import gtk

### Deprecated: we should drop this once we removed stylesheets ###

_styles = {}

screen_factor = gtk.gdk.screen_width() / 1200.0

space_unit = 9 * screen_factor
separator_thickness = 3 * screen_factor

standard_icon_scale = 1.0 * screen_factor
small_icon_scale    = 0.5 * screen_factor
medium_icon_scale   = 1.5 * screen_factor
large_icon_scale    = 2.0 * screen_factor
xlarge_icon_scale   = 3.0 * screen_factor

default_font_size   = 9.0 * screen_factor

def load_stylesheet(module):
    for objname in dir(module):
        if not objname.startswith('_'):
            obj = getattr(module, objname)    
            if isinstance(obj, dict):
                register_stylesheet(objname.replace('_', '.'), obj)

def register_stylesheet(name, style):
    _styles[name] = style

def apply_stylesheet(item, stylesheet_name):
    if _styles.has_key(stylesheet_name):
        style_sheet = _styles[stylesheet_name]
        for name in style_sheet.keys():
            item.set_property(name, style_sheet[name])
    else:
        logging.debug('Stylesheet %s not found.' % stylesheet_name)

def get_font_description(style, relative_size):
    base_size = 18 * screen_factor
    return '%s %dpx' % (style, int(base_size * relative_size))

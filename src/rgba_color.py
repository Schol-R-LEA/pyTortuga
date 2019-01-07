#! python3

from enum import *

class RGBA_Color(object):


    def __init__(self, **kw):
        """Class for representing RGB color with an Alpha channel
        in a toolkit-independent fashion. Color and alpha values 
        are represented as integer per-mil values between 0 and 1000.
        accepted keywords:
        red 
        green
        blue
        alpha
        color - can be an RGB hex string, a list of two-character 
        hex strings, a list of strings of percentages, a list of
        integers, a list of floats, a list of decimals, or an 
        existing Color object.
        blends - a list of values in the same forms as the 'color'
        keyword argument, which should be blended to form the
        new color.

        If more than one keyword is present, then the four color
        arguments take preendence. 
"""
        self.red, self.green, self.blue = decimal(0.0)
        self.alpha = decimal(1.0)

        keys = kw.keys()
        color_kws = list(set(['red','green', 'blue', 'alpha']) & set(keys))

        if color_kws != []:
            if 'red' in color_kws:
                red = kw['red']:
            if 'blue' in color_kws:
                


        elif 'color' in keys:
            color = kw['color']
            if type(color) is RGBA_Color:
                
            blends.append(kw['color'])
        elif 'name' in keys:
            name = kw['name']
            if name in COLORS:
                blends.append(COLORS[name])
        elif 'hex' in keys:
            base = None
            hex_str = kw['hex']
            try:
                hex_red = int(hex_str[:2], 16)
                hex_green = int(hex_str[3:4], 16)
                hex_blue = int(hex_str[5:6], 16)
                hex_alpha = 0
                if length(hex_str) > 6:
                    hex_alpha = int(hex_str[7:8], 16)
                blends.append(Color(hex_red, hex_green, hex_blue, hex_alpha))
            except:
                pass
        
        if length(blends) > 0:
            for blend_color in blends:
                self.blend(blend_color)
        

    def blend(self, color):
        
                                
                           

    def __str__(self, **kw):
        kw.keys()
        with_alpha = False
        background_color = None
        if 'alpha' in keys:
            with_alpha = kw['alpha']
        elif 'background_color' in keys: 
            background_color = kw['background_color']:
        
        

# Copyright 2020-2020, Ansys Government Initiatives 
"""
This module is used to communicate color information between Python and STK.

Color is the color object type and Colors is the factory for creating Color objects.
"""

import typing

from .exceptions import STKColorError

class Color(object):
    """An opaque color representation that can be used with the STK Object Model."""
    def __init__(self):
        self._r = 0
        self._g = 0
        self._b = 0
        
    def __eq__(self, other):
        return self._r == other._r and self._g == other._g and self._b == other._b
        
    def _ToOLECOLOR(self) -> int:
        return self._r + self._g*256 + self._b*256*256
        
    def _FromOLECOLOR(self, ole:int):
        self._r = ole % 256
        self._g = (ole // 256) % 256
        self._b = (ole // (256*256)) % 256
        
    @staticmethod
    def _validate_rgb(val):
        if val > 255 or val < 0:
            raise STKColorError("RGB values should be between 0 and 255, inclusive.")
        return val
        
    def _ToArgb(self) -> int:
        alpha = 255 #fully opaque
        return self._b + self._g*256 + self._r*256*256 + alpha*256*256*256
        
    @classmethod
    def FromRGB(cls, r:int, g:int, b:int) -> "Color":
        """Create a new Color from R, G, B values."""
        c = Color()
        c._r = Color._validate_rgb(r)
        c._g = Color._validate_rgb(g)
        c._b = Color._validate_rgb(b)
        return c
        
    def GetRGB(self) -> typing.Tuple[int, int, int]:
        """Return the R, G, B representation of this color."""
        return (self._r, self._g, self._b)
            
class ColorRGBA(object):
    """A variably translucent color representation that can be used with certain methods in the STK Object Model."""
    def __init__(self, c:Color, alpha=255):
        self._color = c
        self._alpha = alpha
        
    def __eq__(self, other):
        return self._color == other._color and self._alpha == other._alpha
        
    def _ToArgb(self) -> int:
        return self._color._b + self._color._g*256 + self._color._r*256*256 + self._alpha*256*256*256

    @property
    def alpha(self) -> float:
        """Alpha ranges between 0 (fully translucent) and 255 (fully opaque)."""
        return self._alpha
        
    @alpha.setter
    def alpha(self, value:int) -> None:
        if value >= 0 and value <= 255:
            self._alpha = value
        else:
            raise STKColorError("Alpha value should be between 0 (fully translucent) and 255 (fully opaque), inclusive.")
            
    @property
    def color(self) -> Color:
        """The Color value that contains R, G, B values"""
        return self._color

class _ColorsImpl(object):
    @staticmethod
    def FromRGB(r:int, g:int, b:int) -> Color:
        return Color.FromRGB(r, g, b)
    
class Colors(object):
    """
    A factory for creating Color objects that may be used with the STK object model.
    
    Contains factory methods and named colors.
    """
    @staticmethod
    def FromRGB(r:int, g:int, b:int) -> Color:
        """Create a new Color from R, G, B values in the range [0, 255]."""
        return _ColorsImpl.FromRGB(r, g, b)
        
    @staticmethod
    def FromRGBA(r:int, g:int, b:int, a:int) -> ColorRGBA:
        """Create a new Color from R, G, B, A values in the range [0, 255]."""
        c = _ColorsImpl.FromRGB(r, g, b)
        return ColorRGBA(c, a)
        
    AliceBlue            = _ColorsImpl.FromRGB(240,  248,  255)
    AntiqueWhite         = _ColorsImpl.FromRGB(250,  235,  215)
    Aqua                 = _ColorsImpl.FromRGB(0,    255,  255)
    Aquamarine           = _ColorsImpl.FromRGB(127,  255,  212)
    Azure                = _ColorsImpl.FromRGB(240,  255,  255)
    Beige                = _ColorsImpl.FromRGB(245,  245,  220)
    Bisque               = _ColorsImpl.FromRGB(255,  228,  196)
    Black                = _ColorsImpl.FromRGB(0,    0,    0  )
    BlanchedAlmond       = _ColorsImpl.FromRGB(255,  235,  205)
    Blue                 = _ColorsImpl.FromRGB(0,    0,    255)
    BlueViolet           = _ColorsImpl.FromRGB(138,  43,   226)
    Brown                = _ColorsImpl.FromRGB(165,  42,   42 )
    Burlywood            = _ColorsImpl.FromRGB(222,  184,  135)
    CadetBlue            = _ColorsImpl.FromRGB(95,   158,  160)
    Chartreuse           = _ColorsImpl.FromRGB(127,  255,  0  )
    Chocolate            = _ColorsImpl.FromRGB(210,  105,  30 )
    Coral                = _ColorsImpl.FromRGB(255,  127,  80 )
    CornflowerBlue       = _ColorsImpl.FromRGB(100,  149,  237)
    Cornsilk             = _ColorsImpl.FromRGB(255,  248,  220)
    Crimson              = _ColorsImpl.FromRGB(220,  20,   60 )
    Cyan                 = _ColorsImpl.FromRGB(0,    255,  255)
    DarkBlue             = _ColorsImpl.FromRGB(0,    0,    139)
    DarkCyan             = _ColorsImpl.FromRGB(0,    139,  139)
    DarkGoldenrod        = _ColorsImpl.FromRGB(184,  134,  11 )
    DarkGray             = _ColorsImpl.FromRGB(169,  169,  169)
    DarkGreen            = _ColorsImpl.FromRGB(0,    100,  0  )
    DarkGrey             = _ColorsImpl.FromRGB(169,  169,  169)
    DarkKhaki            = _ColorsImpl.FromRGB(189,  183,  107)
    DarkMagenta          = _ColorsImpl.FromRGB(139,  0,    139)
    DarkOliveGreen       = _ColorsImpl.FromRGB(85,   107,  47 )
    DarkOrange           = _ColorsImpl.FromRGB(255,  140,  0  )
    DarkOrchid           = _ColorsImpl.FromRGB(153,  50,   204)
    DarkRed              = _ColorsImpl.FromRGB(139,  0,    0  )
    DarkSalmon           = _ColorsImpl.FromRGB(233,  150,  122)
    DarkSeaGreen         = _ColorsImpl.FromRGB(143,  188,  143)
    DarkSlateBlue        = _ColorsImpl.FromRGB(72,   61,   139)
    DarkSlateGray        = _ColorsImpl.FromRGB(47,   79,   79 )
    DarkSlateGrey        = _ColorsImpl.FromRGB(47,   79,   79 )
    DarkTurquoise        = _ColorsImpl.FromRGB(0,    206,  209)
    DarkViolet           = _ColorsImpl.FromRGB(148,  0,    211)
    DeepPink             = _ColorsImpl.FromRGB(255,  20,   147)
    DeepSkyBlue          = _ColorsImpl.FromRGB(0,    191,  255)
    DimGray              = _ColorsImpl.FromRGB(105,  105,  105)
    DimGrey              = _ColorsImpl.FromRGB(105,  105,  105)
    DodgerBlue           = _ColorsImpl.FromRGB(30,   144,  255)
    FireBrick            = _ColorsImpl.FromRGB(178,  34,   34 )
    FloralWhite          = _ColorsImpl.FromRGB(255,  250,  240)
    ForestGreen          = _ColorsImpl.FromRGB(34,   139,  34 )
    Fuchsia              = _ColorsImpl.FromRGB(255,  0,    255)
    Gainsboro            = _ColorsImpl.FromRGB(220,  220,  220)
    GhostWhite           = _ColorsImpl.FromRGB(248,  248,  255)
    Gold                 = _ColorsImpl.FromRGB(255,  215,  0  )
    Goldenrod            = _ColorsImpl.FromRGB(218,  165,  32 )
    Gray                 = _ColorsImpl.FromRGB(128,  128,  128)
    Green                = _ColorsImpl.FromRGB(0,    128,  0  )
    GreenYellow          = _ColorsImpl.FromRGB(173,  255,  47 )
    Grey                 = _ColorsImpl.FromRGB(128,  128,  128)
    Honeydew             = _ColorsImpl.FromRGB(240,  255,  240)
    HotPink              = _ColorsImpl.FromRGB(255,  105,  180)
    IndianRed            = _ColorsImpl.FromRGB(205,  92,   92 )
    Indigo               = _ColorsImpl.FromRGB(75,   0,    130)
    Ivory                = _ColorsImpl.FromRGB(255,  255,  240)
    Khaki                = _ColorsImpl.FromRGB(240,  230,  140)
    Lavender             = _ColorsImpl.FromRGB(230,  230,  250)
    LavenderBlush        = _ColorsImpl.FromRGB(255,  240,  245)
    Lawngreen            = _ColorsImpl.FromRGB(124,  252,  0  )
    LemonChiffon         = _ColorsImpl.FromRGB(255,  250,  205)
    LightBlue            = _ColorsImpl.FromRGB(173,  216,  230)
    LightCoral           = _ColorsImpl.FromRGB(240,  128,  128)
    LightCyan            = _ColorsImpl.FromRGB(224,  255,  255)
    LightGoldenrodYellow = _ColorsImpl.FromRGB(250,  250,  210)
    LightGray            = _ColorsImpl.FromRGB(211,  211,  211)
    LightGreen           = _ColorsImpl.FromRGB(144,  238,  144)
    LightGrey            = _ColorsImpl.FromRGB(211,  211,  211)
    LightPink            = _ColorsImpl.FromRGB(255,  182,  193)
    LightSalmon          = _ColorsImpl.FromRGB(255,  160,  122)
    LightSeaGreen        = _ColorsImpl.FromRGB(32,   178,  170)
    LightSkyBlue         = _ColorsImpl.FromRGB(135,  206,  250)
    LightSlateGray       = _ColorsImpl.FromRGB(119,  136,  153)
    LightSlateGrey       = _ColorsImpl.FromRGB(119,  136,  153)
    LightSteelBlue       = _ColorsImpl.FromRGB(176,  196,  222)
    LightYellow          = _ColorsImpl.FromRGB(255,  255,  224)
    Lime                 = _ColorsImpl.FromRGB(0,    255,  0  )
    LimeGreen            = _ColorsImpl.FromRGB(50,   205,  50 )
    Linen                = _ColorsImpl.FromRGB(250,  240,  230)
    Magenta              = _ColorsImpl.FromRGB(255,  0,    255)
    Maroon               = _ColorsImpl.FromRGB(128,  0,    0  )
    MediumAquamarine     = _ColorsImpl.FromRGB(102,  205,  170)
    MediumBlue           = _ColorsImpl.FromRGB(0,    0,    205)
    MediumOrchid         = _ColorsImpl.FromRGB(186,  85,   211)
    MediumPurple         = _ColorsImpl.FromRGB(147,  112,  219)
    MediumSeaGreen       = _ColorsImpl.FromRGB(60,   179,  113)
    MediumSlateBlue      = _ColorsImpl.FromRGB(123,  104,  238)
    MediumSpringGreen    = _ColorsImpl.FromRGB(0,    250,  154)
    MediumTurquoise      = _ColorsImpl.FromRGB(72,   209,  204)
    MediumVioletRed      = _ColorsImpl.FromRGB(199,  21,   133)
    MidnightBlue         = _ColorsImpl.FromRGB(25,   25,   112)
    MintCream            = _ColorsImpl.FromRGB(245,  255,  250)
    MistyRose            = _ColorsImpl.FromRGB(255,  228,  225)
    Moccasin             = _ColorsImpl.FromRGB(255,  228,  181)
    NavajoWhite          = _ColorsImpl.FromRGB(255,  222,  173)
    Navy                 = _ColorsImpl.FromRGB(0,    0,    128)
    OldLace              = _ColorsImpl.FromRGB(253,  245,  230)
    Olive                = _ColorsImpl.FromRGB(128,  128,  0  )
    OliveDrab            = _ColorsImpl.FromRGB(107,  142,  35 )
    Orange               = _ColorsImpl.FromRGB(255,  165,  0  )
    OrangeRed            = _ColorsImpl.FromRGB(255,  69,   0  )
    Orchid               = _ColorsImpl.FromRGB(218,  112,  214)
    PaleGoldenrod        = _ColorsImpl.FromRGB(238,  232,  170)
    PaleGreen            = _ColorsImpl.FromRGB(152,  251,  152)
    PaleTurquoise        = _ColorsImpl.FromRGB(175,  238,  238)
    PaleVioletRed        = _ColorsImpl.FromRGB(219,  112,  147)
    PapayaWhip           = _ColorsImpl.FromRGB(255,  239,  213)
    PeachPuff            = _ColorsImpl.FromRGB(255,  218,  185)
    Peru                 = _ColorsImpl.FromRGB(205,  133,  63 )
    Pink                 = _ColorsImpl.FromRGB(255,  192,  203)
    Plum                 = _ColorsImpl.FromRGB(221,  160,  221)
    PowderBlue           = _ColorsImpl.FromRGB(176,  224,  230)
    Purple               = _ColorsImpl.FromRGB(128,  0,    128)
    Red                  = _ColorsImpl.FromRGB(255,  0,    0  )
    RosyBrown            = _ColorsImpl.FromRGB(188,  143,  143)
    RoyalBlue            = _ColorsImpl.FromRGB(65,   105,  225)
    SaddleBrown          = _ColorsImpl.FromRGB(139,  69,   19 )
    Salmon               = _ColorsImpl.FromRGB(250,  128,  114)
    SandyBrown           = _ColorsImpl.FromRGB(244,  164,  96 )
    SeaGreen             = _ColorsImpl.FromRGB(46,   139,  87 )
    Seashell             = _ColorsImpl.FromRGB(255,  245,  238)
    Sienna               = _ColorsImpl.FromRGB(160,  82,   45 )
    Silver               = _ColorsImpl.FromRGB(192,  192,  192)
    SkyBlue              = _ColorsImpl.FromRGB(135,  206,  235)
    SlateBlue            = _ColorsImpl.FromRGB(106,  90,   205)
    SlateGray            = _ColorsImpl.FromRGB(112,  128,  144)
    SlateGrey            = _ColorsImpl.FromRGB(112,  128,  144)
    Snow                 = _ColorsImpl.FromRGB(255,  250,  250)
    SpringGreen          = _ColorsImpl.FromRGB(0,    255,  127)
    SteelBlue            = _ColorsImpl.FromRGB(70,   130,  180)
    Tan                  = _ColorsImpl.FromRGB(210,  180,  140)
    Teal                 = _ColorsImpl.FromRGB(0,    128,  128)
    Thistle              = _ColorsImpl.FromRGB(216,  191,  216)
    Tomato               = _ColorsImpl.FromRGB(255,  99,   71 )
    Turquoise            = _ColorsImpl.FromRGB(64,   224,  208)
    Violet               = _ColorsImpl.FromRGB(238,  130,  238)
    Wheat                = _ColorsImpl.FromRGB(245,  222,  179)
    White                = _ColorsImpl.FromRGB(255,  255,  255)
    WhiteSmoke           = _ColorsImpl.FromRGB(245,  245,  245)
    Yellow               = _ColorsImpl.FromRGB(255,  255,  0  )
    YellowGreen          = _ColorsImpl.FromRGB(154,  205,  50 )

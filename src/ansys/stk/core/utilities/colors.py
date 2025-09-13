# Copyright (C) 2022 - 2025 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
Used to communicate color information.

Color is the color object type and Colors is the factory for creating Color objects.
"""

import typing


class Color(object):
    """
    An opaque color representation that can be used with the Object Model.

    Examples
    --------
    Get and set a four-channel color for the graphics of an STK graphics primitive:
    >>> from ansys.stk.core.utilities.colors import Colors, ColorRGBA
    >>>
    >>> manager = root.current_scenario.scene_manager
    >>> point = manager.initializers.point_batch_primitive.initialize()
    >>>
    >>> lla_pts = [39.88, -75.25, 0, 38.85, -77.04, 0, 37.37, -121.92, 0]
    >>>
    >>> colors = [Colors.Red, ColorRGBA(Colors.Blue, 127), Colors.from_rgba(0, 255, 0, 127)]
    >>>
    >>> point.set_cartographic_with_colors("Earth", lla_pts, colors)

    Get and set a three-channel color for the graphics of an STK graphics primitive:
    >>> from ansys.stk.core.stkobjects import STKObjectType
    >>> from ansys.stk.core.utilities.colors import Color, Colors
    >>>
    >>> facility = root.current_scenario.children.new(STKObjectType.FACILITY, "facility1")
    >>>
    >>> facility.graphics.color = Colors.Blue
    >>> facility.graphics.color = Color.from_rgb(127, 255, 212)
    >>> (r, g, b) = facility.graphics.color.get_rgb()
    """

    def __init__(self):
        """Construct an object of type Color."""
        self._r = 0
        self._g = 0
        self._b = 0

    def __eq__(self, other):
        """Check equality of the underlying references."""
        return self._r == other._r and self._g == other._g and self._b == other._b

    def _to_ole_color(self) -> int:
        return self._r + self._g*256 + self._b*256*256

    def _from_ole_color(self, ole:int):
        self._r = ole % 256
        self._g = (ole // 256) % 256
        self._b = (ole // (256*256)) % 256

    @staticmethod
    def _validate_rgb(val):
        if val > 255 or val < 0:
            raise RuntimeError("RGB values should be between 0 and 255, inclusive.")
        return val

    def _to_argb(self) -> int:
        alpha = 255 #fully opaque
        return self._b + self._g*256 + self._r*256*256 + alpha*256*256*256

    @classmethod
    def from_rgb(cls, r:int, g:int, b:int) -> "Color":
        """Create a new Color from R, G, B values."""
        c = Color()
        c._r = Color._validate_rgb(r)
        c._g = Color._validate_rgb(g)
        c._b = Color._validate_rgb(b)
        return c

    def get_rgb(self) -> typing.Tuple[int, int, int]:
        """Return the R, G, B representation of this color."""
        return (self._r, self._g, self._b)

class ColorRGBA(object):
    """
    A variably translucent color representation that can be used with certain methods in the Object Model.

    Examples
    --------
    Get and set a four-channel color for the graphics of an STK graphics primitive:
    >>> from ansys.stk.core.utilities.colors import Colors, ColorRGBA
    >>>
    >>> manager = root.current_scenario.scene_manager
    >>> point = manager.initializers.point_batch_primitive.initialize()
    >>>
    >>> lla_pts = [39.88, -75.25, 0, 38.85, -77.04, 0, 37.37, -121.92, 0]
    >>>
    >>> colors = [Colors.Red, ColorRGBA(Colors.Blue, 127), Colors.from_rgba(0, 255, 0, 127)]
    >>>
    >>> point.set_cartographic_with_colors("Earth", lla_pts, colors)
    """

    def __init__(self, c:Color, alpha=255):
        """Construct an object of type ColorRGBA."""
        self._color = c
        self._alpha = alpha

    def __eq__(self, other):
        """Check equality of the underlying references."""
        return self._color == other._color and self._alpha == other._alpha

    def _to_argb(self) -> int:
        return self._color._b + self._color._g*256 + self._color._r*256*256 + self._alpha*256*256*256

    @property
    def alpha(self) -> float:
        """Gets or sets the ColorRGBA object's value for alpha, which ranges between 0 (fully translucent) and 255 (fully opaque)."""
        return self._alpha

    @alpha.setter
    def alpha(self, value:int) -> None:
        if value >= 0 and value <= 255:
            self._alpha = value
        else:
            raise RuntimeError("Alpha value should be between 0 (fully translucent) and 255 (fully opaque), inclusive.")

    @property
    def color(self) -> Color:
        """The Color value that contains R, G, B values."""
        return self._color

class _ColorsImpl(object):
    @staticmethod
    def from_rgb(r:int, g:int, b:int) -> Color:
        return Color.from_rgb(r, g, b)

class Colors(object):
    """
    A factory for creating Color objects that may be used with the Object Model.

    Contains factory methods and named colors.

    Examples
    --------
    Get and set a four-channel color for the graphics of an STK graphics primitive:
    >>> from ansys.stk.core.utilities.colors import Colors, ColorRGBA
    >>>
    >>> manager = root.current_scenario.scene_manager
    >>> point = manager.initializers.point_batch_primitive.initialize()
    >>>
    >>> lla_pts = [39.88, -75.25, 0, 38.85, -77.04, 0, 37.37, -121.92, 0]
    >>>
    >>> colors = [Colors.Red, ColorRGBA(Colors.Blue, 127), Colors.from_rgba(0, 255, 0, 127)]
    >>>
    >>> point.set_cartographic_with_colors("Earth", lla_pts, colors)

    Get and set a three-channel color for the graphics of an STK graphics primitive:
    >>> from ansys.stk.core.stkobjects import STKObjectType
    >>> from ansys.stk.core.utilities.colors import Color, Colors
    >>>
    >>> facility = root.current_scenario.children.new(STKObjectType.FACILITY, "facility1")
    >>>
    >>> facility.graphics.color = Colors.Blue
    >>> facility.graphics.color = Color.from_rgb(127, 255, 212)
    >>> (r, g, b) = facility.graphics.color.get_rgb()
    """

    @staticmethod
    def from_rgb(r:int, g:int, b:int) -> Color:
        """Create a new Color from R, G, B values in the range [0, 255]."""
        return _ColorsImpl.from_rgb(r, g, b)

    @staticmethod
    def from_rgba(r:int, g:int, b:int, a:int) -> ColorRGBA:
        """Create a new Color from R, G, B, A values in the range [0, 255]."""
        c = _ColorsImpl.from_rgb(r, g, b)
        return ColorRGBA(c, a)

    @staticmethod
    def from_argb(*args):
        """Create a new Color from an arbitrary number of values in the range [0, 255], inferred from the arguments provided."""
        if len(args) == 1: # argb
            return _ColorsImpl.from_rgb((args[0] & 0xFF0000) >> 16, (args[0] & 0x00FF00) >> 8, args[0] & 0xFF)
        elif len(args) == 3: # r, g, b
            return _ColorsImpl.from_rgb(args[0], args[1], args[2])
        elif len(args) == 4: # a, r, g, b
            return _ColorsImpl.from_rgb(args[1], args[2], args[3])
        else:
            raise RuntimeError('unsupported color conversion')

    AliceBlue            = _ColorsImpl.from_rgb(240,  248,  255)
    AntiqueWhite         = _ColorsImpl.from_rgb(250,  235,  215)
    Aqua                 = _ColorsImpl.from_rgb(0,    255,  255)
    Aquamarine           = _ColorsImpl.from_rgb(127,  255,  212)
    Azure                = _ColorsImpl.from_rgb(240,  255,  255)
    Beige                = _ColorsImpl.from_rgb(245,  245,  220)
    Bisque               = _ColorsImpl.from_rgb(255,  228,  196)
    Black                = _ColorsImpl.from_rgb(0,    0,    0  )
    BlanchedAlmond       = _ColorsImpl.from_rgb(255,  235,  205)
    Blue                 = _ColorsImpl.from_rgb(0,    0,    255)
    BlueViolet           = _ColorsImpl.from_rgb(138,  43,   226)
    Brown                = _ColorsImpl.from_rgb(165,  42,   42 )
    Burlywood            = _ColorsImpl.from_rgb(222,  184,  135)
    CadetBlue            = _ColorsImpl.from_rgb(95,   158,  160)
    Chartreuse           = _ColorsImpl.from_rgb(127,  255,  0  )
    Chocolate            = _ColorsImpl.from_rgb(210,  105,  30 )
    Coral                = _ColorsImpl.from_rgb(255,  127,  80 )
    CornflowerBlue       = _ColorsImpl.from_rgb(100,  149,  237)
    Cornsilk             = _ColorsImpl.from_rgb(255,  248,  220)
    Crimson              = _ColorsImpl.from_rgb(220,  20,   60 )
    Cyan                 = _ColorsImpl.from_rgb(0,    255,  255)
    DarkBlue             = _ColorsImpl.from_rgb(0,    0,    139)
    DarkCyan             = _ColorsImpl.from_rgb(0,    139,  139)
    DarkGoldenrod        = _ColorsImpl.from_rgb(184,  134,  11 )
    DarkGray             = _ColorsImpl.from_rgb(169,  169,  169)
    DarkGreen            = _ColorsImpl.from_rgb(0,    100,  0  )
    DarkGrey             = _ColorsImpl.from_rgb(169,  169,  169)
    DarkKhaki            = _ColorsImpl.from_rgb(189,  183,  107)
    DarkMagenta          = _ColorsImpl.from_rgb(139,  0,    139)
    DarkOliveGreen       = _ColorsImpl.from_rgb(85,   107,  47 )
    DarkOrange           = _ColorsImpl.from_rgb(255,  140,  0  )
    DarkOrchid           = _ColorsImpl.from_rgb(153,  50,   204)
    DarkRed              = _ColorsImpl.from_rgb(139,  0,    0  )
    DarkSalmon           = _ColorsImpl.from_rgb(233,  150,  122)
    DarkSeaGreen         = _ColorsImpl.from_rgb(143,  188,  143)
    DarkSlateBlue        = _ColorsImpl.from_rgb(72,   61,   139)
    DarkSlateGray        = _ColorsImpl.from_rgb(47,   79,   79 )
    DarkSlateGrey        = _ColorsImpl.from_rgb(47,   79,   79 )
    DarkTurquoise        = _ColorsImpl.from_rgb(0,    206,  209)
    DarkViolet           = _ColorsImpl.from_rgb(148,  0,    211)
    DeepPink             = _ColorsImpl.from_rgb(255,  20,   147)
    DeepSkyBlue          = _ColorsImpl.from_rgb(0,    191,  255)
    DimGray              = _ColorsImpl.from_rgb(105,  105,  105)
    DimGrey              = _ColorsImpl.from_rgb(105,  105,  105)
    DodgerBlue           = _ColorsImpl.from_rgb(30,   144,  255)
    FireBrick            = _ColorsImpl.from_rgb(178,  34,   34 )
    FloralWhite          = _ColorsImpl.from_rgb(255,  250,  240)
    ForestGreen          = _ColorsImpl.from_rgb(34,   139,  34 )
    Fuchsia              = _ColorsImpl.from_rgb(255,  0,    255)
    Gainsboro            = _ColorsImpl.from_rgb(220,  220,  220)
    GhostWhite           = _ColorsImpl.from_rgb(248,  248,  255)
    Gold                 = _ColorsImpl.from_rgb(255,  215,  0  )
    Goldenrod            = _ColorsImpl.from_rgb(218,  165,  32 )
    Gray                 = _ColorsImpl.from_rgb(128,  128,  128)
    Green                = _ColorsImpl.from_rgb(0,    128,  0  )
    GreenYellow          = _ColorsImpl.from_rgb(173,  255,  47 )
    Grey                 = _ColorsImpl.from_rgb(128,  128,  128)
    Honeydew             = _ColorsImpl.from_rgb(240,  255,  240)
    HotPink              = _ColorsImpl.from_rgb(255,  105,  180)
    IndianRed            = _ColorsImpl.from_rgb(205,  92,   92 )
    Indigo               = _ColorsImpl.from_rgb(75,   0,    130)
    Ivory                = _ColorsImpl.from_rgb(255,  255,  240)
    Khaki                = _ColorsImpl.from_rgb(240,  230,  140)
    Lavender             = _ColorsImpl.from_rgb(230,  230,  250)
    LavenderBlush        = _ColorsImpl.from_rgb(255,  240,  245)
    Lawngreen            = _ColorsImpl.from_rgb(124,  252,  0  )
    LemonChiffon         = _ColorsImpl.from_rgb(255,  250,  205)
    LightBlue            = _ColorsImpl.from_rgb(173,  216,  230)
    LightCoral           = _ColorsImpl.from_rgb(240,  128,  128)
    LightCyan            = _ColorsImpl.from_rgb(224,  255,  255)
    LightGoldenrodYellow = _ColorsImpl.from_rgb(250,  250,  210)
    LightGray            = _ColorsImpl.from_rgb(211,  211,  211)
    LightGreen           = _ColorsImpl.from_rgb(144,  238,  144)
    LightGrey            = _ColorsImpl.from_rgb(211,  211,  211)
    LightPink            = _ColorsImpl.from_rgb(255,  182,  193)
    LightSalmon          = _ColorsImpl.from_rgb(255,  160,  122)
    LightSeaGreen        = _ColorsImpl.from_rgb(32,   178,  170)
    LightSkyBlue         = _ColorsImpl.from_rgb(135,  206,  250)
    LightSlateGray       = _ColorsImpl.from_rgb(119,  136,  153)
    LightSlateGrey       = _ColorsImpl.from_rgb(119,  136,  153)
    LightSteelBlue       = _ColorsImpl.from_rgb(176,  196,  222)
    LightYellow          = _ColorsImpl.from_rgb(255,  255,  224)
    Lime                 = _ColorsImpl.from_rgb(0,    255,  0  )
    LimeGreen            = _ColorsImpl.from_rgb(50,   205,  50 )
    Linen                = _ColorsImpl.from_rgb(250,  240,  230)
    Magenta              = _ColorsImpl.from_rgb(255,  0,    255)
    Maroon               = _ColorsImpl.from_rgb(128,  0,    0  )
    MediumAquamarine     = _ColorsImpl.from_rgb(102,  205,  170)
    MediumBlue           = _ColorsImpl.from_rgb(0,    0,    205)
    MediumOrchid         = _ColorsImpl.from_rgb(186,  85,   211)
    MediumPurple         = _ColorsImpl.from_rgb(147,  112,  219)
    MediumSeaGreen       = _ColorsImpl.from_rgb(60,   179,  113)
    MediumSlateBlue      = _ColorsImpl.from_rgb(123,  104,  238)
    MediumSpringGreen    = _ColorsImpl.from_rgb(0,    250,  154)
    MediumTurquoise      = _ColorsImpl.from_rgb(72,   209,  204)
    MediumVioletRed      = _ColorsImpl.from_rgb(199,  21,   133)
    MidnightBlue         = _ColorsImpl.from_rgb(25,   25,   112)
    MintCream            = _ColorsImpl.from_rgb(245,  255,  250)
    MistyRose            = _ColorsImpl.from_rgb(255,  228,  225)
    Moccasin             = _ColorsImpl.from_rgb(255,  228,  181)
    NavajoWhite          = _ColorsImpl.from_rgb(255,  222,  173)
    Navy                 = _ColorsImpl.from_rgb(0,    0,    128)
    OldLace              = _ColorsImpl.from_rgb(253,  245,  230)
    Olive                = _ColorsImpl.from_rgb(128,  128,  0  )
    OliveDrab            = _ColorsImpl.from_rgb(107,  142,  35 )
    Orange               = _ColorsImpl.from_rgb(255,  165,  0  )
    OrangeRed            = _ColorsImpl.from_rgb(255,  69,   0  )
    Orchid               = _ColorsImpl.from_rgb(218,  112,  214)
    PaleGoldenrod        = _ColorsImpl.from_rgb(238,  232,  170)
    PaleGreen            = _ColorsImpl.from_rgb(152,  251,  152)
    PaleTurquoise        = _ColorsImpl.from_rgb(175,  238,  238)
    PaleVioletRed        = _ColorsImpl.from_rgb(219,  112,  147)
    PapayaWhip           = _ColorsImpl.from_rgb(255,  239,  213)
    PeachPuff            = _ColorsImpl.from_rgb(255,  218,  185)
    Peru                 = _ColorsImpl.from_rgb(205,  133,  63 )
    Pink                 = _ColorsImpl.from_rgb(255,  192,  203)
    Plum                 = _ColorsImpl.from_rgb(221,  160,  221)
    PowderBlue           = _ColorsImpl.from_rgb(176,  224,  230)
    Purple               = _ColorsImpl.from_rgb(128,  0,    128)
    Red                  = _ColorsImpl.from_rgb(255,  0,    0  )
    RosyBrown            = _ColorsImpl.from_rgb(188,  143,  143)
    RoyalBlue            = _ColorsImpl.from_rgb(65,   105,  225)
    SaddleBrown          = _ColorsImpl.from_rgb(139,  69,   19 )
    Salmon               = _ColorsImpl.from_rgb(250,  128,  114)
    SandyBrown           = _ColorsImpl.from_rgb(244,  164,  96 )
    SeaGreen             = _ColorsImpl.from_rgb(46,   139,  87 )
    Seashell             = _ColorsImpl.from_rgb(255,  245,  238)
    Sienna               = _ColorsImpl.from_rgb(160,  82,   45 )
    Silver               = _ColorsImpl.from_rgb(192,  192,  192)
    SkyBlue              = _ColorsImpl.from_rgb(135,  206,  235)
    SlateBlue            = _ColorsImpl.from_rgb(106,  90,   205)
    SlateGray            = _ColorsImpl.from_rgb(112,  128,  144)
    SlateGrey            = _ColorsImpl.from_rgb(112,  128,  144)
    Snow                 = _ColorsImpl.from_rgb(255,  250,  250)
    SpringGreen          = _ColorsImpl.from_rgb(0,    255,  127)
    SteelBlue            = _ColorsImpl.from_rgb(70,   130,  180)
    Tan                  = _ColorsImpl.from_rgb(210,  180,  140)
    Teal                 = _ColorsImpl.from_rgb(0,    128,  128)
    Thistle              = _ColorsImpl.from_rgb(216,  191,  216)
    Tomato               = _ColorsImpl.from_rgb(255,  99,   71 )
    Turquoise            = _ColorsImpl.from_rgb(64,   224,  208)
    Violet               = _ColorsImpl.from_rgb(238,  130,  238)
    Wheat                = _ColorsImpl.from_rgb(245,  222,  179)
    White                = _ColorsImpl.from_rgb(255,  255,  255)
    WhiteSmoke           = _ColorsImpl.from_rgb(245,  245,  245)
    Yellow               = _ColorsImpl.from_rgb(255,  255,  0  )
    YellowGreen          = _ColorsImpl.from_rgb(154,  205,  50 )

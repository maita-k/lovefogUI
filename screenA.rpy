

define inerfacefont = "EncodeSansExpanded-SemiBold.ttf"
define menuFont = "EncodeSansExpanded-SemiBold.ttf"
define titleFont = "EncodeSansExpanded-Black.ttf"
define bbFont = "Boba Date.otf"
transform oHover:
    on hide:
        alpha 1
        linear 0.25 alpha 0

image textBox:
    align(0.5, .5)
    Solid(gui.idle_color)
    size(1920, 300)
    alpha .9

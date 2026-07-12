from pathlib import Path
from kivy.core.text import LabelBase 

# Get the root directory of the fonts module.
# Our fonts are stored under the same directory,
# so we'll use it to determine our font filepaths.
path_root = str(Path(__file__).resolve().parent) + "/"

# Likewise, point further towards the directories for each font's TTF files.
faraway_root = path_root + "faraway/ttf/"

def register_fonts():
    """
        Registers all of the custom fonts,
        and their variants, used in this app.
    """
    LabelBase.register(
        name = "Faraway",
        fn_regular = faraway_root + "faraway.ttf",
        fn_italic = faraway_root + "faraway_italic.ttf",
        fn_bold = faraway_root + "faraway_bold.ttf"
    )

    LabelBase.register(
        name = "Faraway Large",
        fn_regular = faraway_root + "faraway_large.ttf",
        fn_bold = faraway_root + "faraway_large_bold.ttf"
    )

    LabelBase.register(
        name = "Faraway Upper",
        fn_regular = faraway_root + "faraway_upper.ttf",
        fn_bold = faraway_root + "faraway_upper_bold.ttf"
    )

    LabelBase.register(
        name = "Faraway Wide",
        fn_regular = faraway_root + "faraway_wide.ttf",
        fn_italic = faraway_root + "faraway_wide_italic.ttf",
        fn_bold = faraway_root + "faraway_wide_bold.ttf"
    )

    LabelBase.register(
        name = "Faraway Mono",
        fn_regular = faraway_root + "faraway_mono.ttf"
    )

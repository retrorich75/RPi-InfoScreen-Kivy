# -*- coding: utf-8 -*-
'''This is a custom layout for the RPi InfoScreen wordclock screen.

    Custom layouts can be created for the screen by creating a new file in the
    "layouts" folder.

    Each layout must have the following variables:
        LAYOUT:   The grid layout. Must be a single string.
        MAP:      The mapping required for various times (see notes below)
        COLS:     The number of columns required for the grid layout
        SIZE:     The size of the individual box containing your letter.
                  Tuple in (x, y) format.
        FONTSIZE: Font size for the letter
'''

# Layout is a single string variable which will be looped over by the parser.
# Extra "u" is required before each line with Extended Unicode character(s)
LAYOUT = ("SONORLELBORE" #0-11 
          u"ÈRL'UNAZDUEI" #12-23
          "QTREOTTONOVE" #24-44
          "DIECIRUNDICI" #36-59
          "RDODOCISETTE" #48-74
          "QUATTROCDSEI" #60-89
          "UCINQUEAMENO" #72-83
          "ECUNOQUARTOI" #84-95
          "VENTIMCINQUE" #96-107
          "PDIECIPMEZZA") #108-119

# Map instructions:
# The clock works by rounding the time to the nearest 5 minutes.
# This means that you need to have settings for each five minute interval "m00"
# "m00", "m05".
# The clock also works on a 12 hour basis rather than 24 hour:
# "h00", "h01" etc.
# There are three optional parameters:
#   "all": Anything that is always shown regardless of the time e.g. "It is..."
#   "am":  Wording/symbol to indicate morning.
#   "pm":  Wording/symbol to indicate afternoon/evening
MAP = {
       "all": [], #
       "m00": [], #
       "m05": [84, 102, 103, 104, 105, 106, 107], #E CINQUE
       "m10": [84, 109, 110, 111, 112, 113], #E DIECI
       "m15": [84, 86, 87, 89, 90, 91, 92, 93, 94], #E UN QUARTO
       "m20": [84, 96, 97, 98, 99, 100], #E VENTI
       "m25": [84, 96, 97, 98, 99, 100, 102, 103, 104, 105, 106, 107], #VENTI CINQUE
       "m30": [84, 115, 116, 117, 118, 119], #E MEZZA
       "m35": [80, 81, 82, 83, 96, 97, 98, 99, 100, 102, 103, 104, 105, 106, 107], #MENO VENTI CINQUE
       "m40": [80, 81, 82, 83, 96, 97, 98, 99, 100], #MENO VENTI
       "m45": [80, 81, 82, 83, 86, 87, 89, 90, 91, 92, 93, 94], #MENO UN QUARTO
       "m50": [80, 81, 82, 83, 109, 110, 111, 112, 113], #MENO DIECI
       "m55": [80, 81, 82, 83, 102, 103, 104, 105, 106, 107], #MENO CINQUE
       "h01": [12, 14, 15, 16, 17, 18], #È L'UNA
       "h02": [0, 1, 2, 3, 5, 6, 20, 21, 22], #SONO LE DUE
       "h03": [0, 1, 2, 3, 5, 6, 25, 26, 27], #SONO LE TRE
       "h04": [0, 1, 2, 3, 5, 6, 60, 61, 62, 63, 64, 65, 66], #SONO LE QUATTRO
       "h05": [0, 1, 2, 3, 5, 6, 73, 74, 75, 76, 77, 78], #SONO LE CINQUE
       "h06": [0, 1, 2, 3, 5, 6, 69, 70, 71], #SONO LE SEI
       "h07": [0, 1, 2, 3, 5, 6, 55, 56, 57, 58, 59], #SONO LE SETTE
       "h08": [0, 1, 2, 3, 5, 6, 28, 29, 30, 31], #SONO LE OTTO
       "h09": [0, 1, 2, 3, 5, 6, 32, 33, 34, 35], #SONO LE NOVE
       "h10": [0, 1, 2, 3, 5, 6, 36, 37, 38, 39, 40], #SONO LE DIECI
       "h11": [0, 1, 2, 3, 5, 6, 42, 43, 44, 45, 46, 47], #SONO LE UNDICI
       "h12": [0, 1, 2, 3, 5, 6, 49, 50, 51, 52, 53, 54], #SONO LE DODOCI
       "am": [],
       "pm": []
  }

# Number of columns in grid layout
COLS = 12

# Size of letter in grid (x, y)
SIZE = (66, 48)

# Font size of letter
FONTSIZE = 40

# Is our language one where we need to increment the hour after 30 mins
# e.g. 9:40 is "Twenty to ten"
HOUR_INCREMENT = True

HOUR_INCREMENT_TIME = 30

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
LAYOUT = (u"ÈSONOL'LETPX" #0-12 extra "u" before each line with Extended Unicode character(s)
          "XUNADUEDIECI" #12-23
          "CINQUEYSETTE" #24-44
          "TREZERPINOVE" #36-59
          "OTTOTVNOVELN" #48-74
          "DODOCIUNDICI" #60-89
          "QUATTROSEIWE" #72-83
          "MENOQUINDICI" #84-95
          "DIECIBTRENTA" #96-107
          "VENTIHCINQUE") #108-119

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
       "m05": [83, 114, 115, 116, 117, 118, 119], #CINQUE E
       "m10": [83, 19, 20, 21, 22, 23], #DIECI E
       "m15": [83, 88, 89, 90, 91, 92, 93, 94, 95], #QUINDICI
       "m20": [108, 109, 110, 111, 112], #VENTI
       "m25": [108, 109, 110, 111, 112, 114, 115, 116, 117, 118, 119], #VENTI & CINQUE
       "m30": [102, 103, 104, 105, 106, 107], #TRENTA
       "m35": [102, 103, 104, 105, 106, 107, 114, 115, 116, 117, 118, 119],#TRENTA & CINQUE
       "m40": [84, 85, 86, 87, 108, 109, 110, 111, 112], #MENO VENTI
       "m45": [84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95], #MENO QUINDICI
       "m50": [84, 85, 86, 87, 96, 97, 98, 99, 100], #MENO DIECI
       "m55": [84, 85, 86, 87, 114, 115, 116, 117, 118, 119], #MENO CINQUE
       "h01": [0, 6, 7, 13, 14, 15], #È L'UNA
       "h02": [1, 2, 3, 4, 7, 8, 16, 17, 18], #SONO LE DUE
       "h03": [1, 2, 3, 4, 7, 8, 36, 37, 38], #SONO LE TRE
       "h04": [1, 2, 3, 4, 7, 8, 72, 75, 76, 77, 78], #SONO LE QUATTRO
       "h05": [1, 2, 3, 4, 7, 8, 24, 25, 26, 27, 28, 29], #SONO LE CINQUE
       "h06": [1, 2, 3, 4, 7, 8, 79, 80, 81], #SONO LE SEI
       "h07": [1, 2, 3, 4, 7, 8, 31, 32, 33, 34, 35], #SONO LE SETTE
       "h08": [1, 2, 3, 4, 7, 8, 48, 49, 50, 51, 52], #SONO LE OTTO
       "h09": [1, 2, 3, 4, 7, 8, 54, 55, 56, 57], #SONO LE NOVE
       "h10": [1, 2, 3, 4, 7, 8, 96, 97, 98, 99, 100], #SONO LE DIECI
       "h11": [1, 2, 3, 4, 7, 8, 66, 67, 68, 69, 70, 71], #SONO LE UNDICI
       "h12": [1, 2, 3, 4, 7, 8, 60, 61, 62, 63, 64, 65], #SONO LE DODOCI
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

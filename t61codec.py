"""
Python Character Mapping Codec for T61

See https://en.wikipedia.org/wiki/ITU_T.61
"""

# pylint: disable=invalid-name, no-member, redefined-builtin

import codecs
from typing import Tuple

try:
    import importlib.metadata as imlib
except ImportError:
    import importlib_metadata as imlib  # type: ignore


__version__ = imlib.Distribution.from_name("t61codec").version


class Codec(codecs.Codec):
    """
    Main implementation for the T.61 codec, based on
    :py:func:`codecs.charmap_encode` and :py:func:`codecs.charmap_decode`
    """

    def encode(self, input: str, errors: str = "strict") -> Tuple[bytes, int]:
        return codecs.charmap_encode(input, errors, ENCODING_TABLE)  # type: ignore

    def decode(self, input: str, errors: str = "strict") -> Tuple[str, int]:
        return codecs.charmap_decode(input, errors, DECODING_TABLE)  # type: ignore


class IncrementalEncoder(codecs.IncrementalEncoder):
    """
    See :py:class:`codecs.IncrementalEncoder`
    """

    def encode(self, input: str, final: bool = False) -> bytes:
        return codecs.charmap_encode(  # type: ignore
            input, self.errors, ENCODING_TABLE
        )[0]


class IncrementalDecoder(codecs.IncrementalDecoder):
    """
    See :py:class:`codecs.IncrementalDecoder`
    """

    def decode(self, input: bytes, final: bool = False) -> str:
        return codecs.charmap_decode(  # type: ignore
            input, self.errors, DECODING_TABLE
        )[0]


class StreamWriter(Codec, codecs.StreamWriter):
    """
    See :py:class:`codecs.StreamWriter`
    """


class StreamReader(Codec, codecs.StreamReader):
    """
    See :py:class:`codecs.StreamReader`
    """


def getregentry() -> codecs.CodecInfo:
    """
    Creates a :py:class:`codecs.CodecInfo` instance for use in the registry
    """
    return codecs.CodecInfo(
        name="t.61",
        encode=Codec().encode,
        decode=Codec().decode,
        incrementalencoder=IncrementalEncoder,
        incrementaldecoder=IncrementalDecoder,
        streamreader=StreamReader,
        streamwriter=StreamWriter,
    )


DECODING_TABLE = (
    "\x00"  # 0x00 -> NULL
    "\x01"  # 0x01 -> START OF HEADING
    "\x02"  # 0x02 -> START OF TEXT
    "\x03"  # 0x03 -> END OF TEXT
    "\x04"  # 0x04 -> END OF TRANSMISSION
    "\x05"  # 0x05 -> ENQUIRY
    "\x06"  # 0x06 -> ACKNOWLEDGE
    "\x07"  # 0x07 -> BELL
    "\x08"  # 0x08 -> BACKSPACE
    "\t"  # 0x09 -> HORIZONTAL TABULATION
    "\n"  # 0x0A -> LINE FEED
    "\x0b"  # 0x0B -> VERTICAL TABULATION
    "\x0c"  # 0x0C -> FORM FEED
    "\r"  # 0x0D -> CARRIAGE RETURN
    "\x0e"  # 0x0E -> SHIFT OUT
    "\x0f"  # 0x0F -> SHIFT IN
    "\x10"  # 0x10 -> DATA LINK ESCAPE
    "\x11"  # 0x11 -> DEVICE CONTROL ONE
    "\x12"  # 0x12 -> DEVICE CONTROL TWO
    "\x13"  # 0x13 -> DEVICE CONTROL THREE
    "\x14"  # 0x14 -> DEVICE CONTROL FOUR
    "\x15"  # 0x15 -> NEGATIVE ACKNOWLEDGE
    "\x16"  # 0x16 -> SYNCHRONOUS IDLE
    "\x17"  # 0x17 -> END OF TRANSMISSION BLOCK
    "\x18"  # 0x18 -> CANCEL
    "\x19"  # 0x19 -> END OF MEDIUM
    "\x1a"  # 0x1A -> SUBSTITUTE
    "\x1b"  # 0x1B -> ESCAPE
    "\x1c"  # 0x1C -> FILE SEPARATOR
    "\x1d"  # 0x1D -> GROUP SEPARATOR
    "\x1e"  # 0x1E -> RECORD SEPARATOR
    "\x1f"  # 0x1F -> UNIT SEPARATOR
    " "  # 0x20 -> SPACE
    "!"  # 0x21 -> EXCLAMATION MARK
    '"'  # 0x22 -> QUOTATION MARK
    "\ufffe"  # 0x23 -> *unmapped*
    "\ufffe"  # 0x24 -> *unmapped*
    "%"  # 0x25 -> PERCENT SIGN
    "&"  # 0x26 -> AMPERSAND
    "'"  # 0x27 -> APOSTROPHE
    "("  # 0x28 -> LEFT PARENTHESIS
    ")"  # 0x29 -> RIGHT PARENTHESIS
    "*"  # 0x2A -> ASTERISK
    "+"  # 0x2B -> PLUS SIGN
    ","  # 0x2C -> COMMA
    "-"  # 0x2D -> HYPHEN-MINUS
    "."  # 0x2E -> FULL STOP
    "/"  # 0x2F -> SOLIDUS
    "0"  # 0x30 -> DIGIT ZERO
    "1"  # 0x31 -> DIGIT ONE
    "2"  # 0x32 -> DIGIT TWO
    "3"  # 0x33 -> DIGIT THREE
    "4"  # 0x34 -> DIGIT FOUR
    "5"  # 0x35 -> DIGIT FIVE
    "6"  # 0x36 -> DIGIT SIX
    "7"  # 0x37 -> DIGIT SEVEN
    "8"  # 0x38 -> DIGIT EIGHT
    "9"  # 0x39 -> DIGIT NINE
    ":"  # 0x3A -> COLON
    ";"  # 0x3B -> SEMICOLON
    "<"  # 0x3C -> LESS-THAN SIGN
    "="  # 0x3D -> EQUALS SIGN
    ">"  # 0x3E -> GREATER-THAN SIGN
    "?"  # 0x3F -> QUESTION MARK
    "@"  # 0x40 -> COMMERCIAL AT
    "A"  # 0x41 -> LATIN CAPITAL LETTER A
    "B"  # 0x42 -> LATIN CAPITAL LETTER B
    "C"  # 0x43 -> LATIN CAPITAL LETTER C
    "D"  # 0x44 -> LATIN CAPITAL LETTER D
    "E"  # 0x45 -> LATIN CAPITAL LETTER E
    "F"  # 0x46 -> LATIN CAPITAL LETTER F
    "G"  # 0x47 -> LATIN CAPITAL LETTER G
    "H"  # 0x48 -> LATIN CAPITAL LETTER H
    "I"  # 0x49 -> LATIN CAPITAL LETTER I
    "J"  # 0x4A -> LATIN CAPITAL LETTER J
    "K"  # 0x4B -> LATIN CAPITAL LETTER K
    "L"  # 0x4C -> LATIN CAPITAL LETTER L
    "M"  # 0x4D -> LATIN CAPITAL LETTER M
    "N"  # 0x4E -> LATIN CAPITAL LETTER N
    "O"  # 0x4F -> LATIN CAPITAL LETTER O
    "P"  # 0x50 -> LATIN CAPITAL LETTER P
    "Q"  # 0x51 -> LATIN CAPITAL LETTER Q
    "R"  # 0x52 -> LATIN CAPITAL LETTER R
    "S"  # 0x53 -> LATIN CAPITAL LETTER S
    "T"  # 0x54 -> LATIN CAPITAL LETTER T
    "U"  # 0x55 -> LATIN CAPITAL LETTER U
    "V"  # 0x56 -> LATIN CAPITAL LETTER V
    "W"  # 0x57 -> LATIN CAPITAL LETTER W
    "X"  # 0x58 -> LATIN CAPITAL LETTER X
    "Y"  # 0x59 -> LATIN CAPITAL LETTER Y
    "Z"  # 0x5A -> LATIN CAPITAL LETTER Z
    "["  # 0x5B -> LEFT SQUARE BRACKET
    "\ufffe"  # 0x5C -> *unmapped*
    "]"  # 0x5D -> RIGHT SQUARE BRACKET
    "\ufffe"  # 0x5E -> *unmapped*
    "_"  # 0x5F -> LOW LINE
    "\ufffe"  # 0x60 -> *unmapped*
    "a"  # 0x61 -> LATIN SMALL LETTER A
    "b"  # 0x62 -> LATIN SMALL LETTER B
    "c"  # 0x63 -> LATIN SMALL LETTER C
    "d"  # 0x64 -> LATIN SMALL LETTER D
    "e"  # 0x65 -> LATIN SMALL LETTER E
    "f"  # 0x66 -> LATIN SMALL LETTER F
    "g"  # 0x67 -> LATIN SMALL LETTER G
    "h"  # 0x68 -> LATIN SMALL LETTER H
    "i"  # 0x69 -> LATIN SMALL LETTER I
    "j"  # 0x6A -> LATIN SMALL LETTER J
    "k"  # 0x6B -> LATIN SMALL LETTER K
    "l"  # 0x6C -> LATIN SMALL LETTER L
    "m"  # 0x6D -> LATIN SMALL LETTER M
    "n"  # 0x6E -> LATIN SMALL LETTER N
    "o"  # 0x6F -> LATIN SMALL LETTER O
    "p"  # 0x70 -> LATIN SMALL LETTER P
    "q"  # 0x71 -> LATIN SMALL LETTER Q
    "r"  # 0x72 -> LATIN SMALL LETTER R
    "s"  # 0x73 -> LATIN SMALL LETTER S
    "t"  # 0x74 -> LATIN SMALL LETTER T
    "u"  # 0x75 -> LATIN SMALL LETTER U
    "v"  # 0x76 -> LATIN SMALL LETTER V
    "w"  # 0x77 -> LATIN SMALL LETTER W
    "x"  # 0x78 -> LATIN SMALL LETTER X
    "y"  # 0x79 -> LATIN SMALL LETTER Y
    "z"  # 0x7A -> LATIN SMALL LETTER Z
    "\ufffe"  # 0x7B -> *unmapped*
    "|"  # 0x7C -> VERTICAL LINE
    "\ufffe"  # 0x7D -> *unmapped*
    "\ufffe"  # 0x7E -> *unmapped*
    "\x7f"  # 0x7F -> DELETE
    "\x80"  # 0x80 -> PADDING CHARACTER
    "\x81"  # 0x81 -> HIGH OCTET PRESET
    "\x82"  # 0x82 -> BREAK PERMITTED HERE (BPH)
    "\x83"  # 0x83 -> NO BREAK HERE (NBH)
    "\x84"  # 0x84 -> INDEX (IND)
    "\x85"  # 0x85 -> NEXT LINE (NEL)
    "\x86"  # 0x86 -> START OF SELECTED AREA (SSA)
    "\x87"  # 0x87 -> END OF SELECTED AREA (ESA)
    "\x88"  # 0x88 -> CHARACTER TABULATION SET (HTS)
    "\x89"  # 0x89 -> CHARACTER TABULATION WITH JUSTIFICATION (HTJ)
    "\x8a"  # 0x8a -> LINE TABULATION SET (VTS)
    "\x8b"  # 0x8b -> PARTIAL LINE FORWARD (PLD)
    "\x8c"  # 0x8c -> PARTIAL LINE BACKWARD (PLU)
    "\x8d"  # 0x8d -> REVERSE LINE FEED (RI)
    "\x8e"  # 0x8e -> SINGLE-SHIFT TWO (SS2)
    "\x8f"  # 0x8f -> SINGLE-SHIFT THREE (SS3)
    "\x90"  # 0x90 -> DEVICE CONTROL STRING (DCS)
    "\x91"  # 0x91 -> PRIVATE USE ONE (PU1)
    "\x92"  # 0x92 -> PRIVATE USE TWO (PU2)
    "\x93"  # 0x93 -> SET TRANSMIT STATE (STS)
    "\x94"  # 0x94 -> CANCEL CHARACTER (CCH)
    "\x95"  # 0x95 -> MESSAGE WAITING (MW)
    "\x96"  # 0x96 -> START OF GUARDED AREA (SPA)
    "\x97"  # 0x97 -> END OF GUARDED AREA (EPA)
    "\x98"  # 0x98 -> START OF STRING (SOS)
    "\x99"  # 0x99 -> SINGLE GRAPHIC CHARACTER INTRODUCER (SGCI)
    "\x9a"  # 0x9a -> SINGLE CHARACTER INTRODUCER (SCI)
    "\x9b"  # 0x9b -> CONTROL SEQUENCE INTRODUCER (CSI)
    "\x9c"  # 0x9c -> STRING TERMINATOR (ST)
    "\x9d"  # 0x9d -> OPERATING SYSTEM COMMAND (OSC)
    "\x9e"  # 0x9e -> PRIVACY MESSAGE (PM)
    "\x9f"  # 0x9f -> APPLICATION PROGRAM COMMAND (APC)
    "\xa0"  # 0xA0 -> NO-BREAK SPACE
    "\xa1"  # 0xA1 -> INVERTED EXCLAMATION MARK
    "\xa2"  # 0xA2 -> CENT SIGN
    "\xa3"  # 0xA3 -> POUND SIGN
    "$"  # 0xA4 -> DOLLAR SIGN
    "\xa5"  # 0xA5 -> YEN SIGN
    "#"  # 0xA6 -> NUMBER SIGN
    "\xa7"  # 0xA7 -> SECTION SIGN
    "\xa4"  # 0xA8 -> CURRENCY SIGN
    "\ufffe"  # 0xA9 -> *unmapped*
    "\ufffe"  # 0xAA -> *unmapped*
    "\xab"  # 0xAB -> LEFT-POINTING DOUBLE ANGLE QUOTATION MARK
    "\ufffe"  # 0xAC -> *unmapped*
    "\ufffe"  # 0xAD -> *unmapped*
    "\ufffe"  # 0xAE -> *unmapped*
    "\ufffe"  # 0xAF -> *unmapped*
    "\xb0"  # 0xB0 -> DEGREE SIGN
    "\xb1"  # 0xB1 -> PLUS-MINUS SIGN
    "\xb2"  # 0xB2 -> SUPERSCRIPT TWO
    "\xb3"  # 0xB3 -> SUPERSCRIPT THREE
    "\xd7"  # 0xD7 -> MULTIPLICATION SIGN
    "\xb5"  # 0xB5 -> MICRO SIGN
    "\xb6"  # 0xB6 -> PILCROW SIGN
    "\xb7"  # 0xB7 -> MIDDLE DOT
    "\xf7"  # 0xF7 -> DIVISION SIGN
    "\ufffe"  # 0xF8 -> *unmapped*
    "\ufffe"  # 0xF9 -> *unmapped*
    "\xbb"  # 0xBB -> RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK
    "\xbc"  # 0xBC -> VULGAR FRACTION ONE QUARTER
    "\xbd"  # 0xBD -> VULGAR FRACTION ONE HALF
    "\xbe"  # 0xBE -> VULGAR FRACTION THREE QUARTERS
    "\xbf"  # 0xBF -> INVERTED QUESTION MARK
    "\ufffe"  # 0xC0 -> *unmapped*
    "\u0300"  # 0xC1 -> COMBINING GRAVE ACCENT
    "\u0301"  # 0xC2 -> COMBINING ACUTE ACCENT
    "\u0302"  # 0xC3 -> COMBINING CIRCUMFLEX ACCENT
    "\u0303"  # 0xC4 -> COMBINING TILDE
    "\u0304"  # 0xC5 -> COMBINING MACRON
    "\u0306"  # 0xC6 -> COMBINING BREVE
    "\u0307"  # 0xC7 -> COMBINING DOT ABOVE
    "\u0308"  # 0xC8 -> COMBINING DIAERESIS
    "\ufffe"  # 0xC9 -> *unmapped*
    "\u030a"  # 0xCA -> COMBINING RING ABOVE
    "\u0327"  # 0xCB -> COMBINING CEDILLA
    "\u0332"  # 0xCC -> COMBINING LOW LINE
    "\u030b"  # 0xCD -> COMBINING DOUBLE ACUTE ACCENT
    "\u032b"  # 0xCE -> COMBINING INVERTED DOUBLE ARCH BELOW
    "\u030c"  # 0xCF -> COMBINING CARON
    "\ufffe"  # 0xD0 -> *unmapped*
    "\ufffe"  # 0xD1 -> *unmapped*
    "\ufffe"  # 0xD2 -> *unmapped*
    "\ufffe"  # 0xD3 -> *unmapped*
    "\ufffe"  # 0xD4 -> *unmapped*
    "\ufffe"  # 0xD5 -> *unmapped*
    "\ufffe"  # 0xD6 -> *unmapped*
    "\ufffe"  # 0xD7 -> *unmapped*
    "\ufffe"  # 0xD8 -> *unmapped*
    "\ufffe"  # 0xD9 -> *unmapped*
    "\ufffe"  # 0xDA -> *unmapped*
    "\ufffe"  # 0xDB -> *unmapped*
    "\ufffe"  # 0xDC -> *unmapped*
    "\ufffe"  # 0xDD -> *unmapped*
    "\ufffe"  # 0xDE -> *unmapped*
    "\ufffe"  # 0xDF -> *unmapped*
    "\u2126"  # 0xE0 -> OHM SIGN
    "\u00c6"  # 0xE1 -> LATIN CAPITAL LETTER AE
    "\u00d0"  # 0xE2 -> LATIN CAPITAL LETTER ETH
    "\u00aa"  # 0xE3 -> FEMININE ORDINAL INDICATOR
    "\u0126"  # 0xE4 -> LATIN CAPITAL LETTER H WITH STROKE
    "\ufffe"  # 0xE5 -> *unmapped*
    "\u0132"  # 0xE6 -> LATIN CAPITAL LIGATURE IJ
    "\u013f"  # 0xE7 -> LATIN CAPITAL LETTER L WITH MIDDLE DOT
    "\u0141"  # 0xE8 -> LATIN CAPITAL LETTER L WITH STROKE
    "\u00d8"  # 0xE9 -> LATIN CAPITAL LETTER O WITH STROKE
    "\u0152"  # 0xEA -> LATIN CAPITAL LIGATURE OE
    "\u00ba"  # 0xEB -> MASCULINE ORDINAL INDICATOR
    "\u00de"  # 0xEC -> LATIN CAPITAL LETTER THORN
    "\u0166"  # 0xED -> LATIN CAPITAL LETTER T WITH STROKE
    "\u014a"  # 0xEE -> LATIN CAPITAL LETTER ENG
    "\u0149"  # 0xEF -> LATIN SMALL LETTER N PRECEDED BY APOSTROPHE
    "\u0138"  # 0xF0 -> LATIN SMALL LETTER KRA
    "\u00e6"  # 0xF1 -> LATIN SMALL LETTER AE
    "\u0111"  # 0xF2 -> LATIN SMALL LETTER D WITH STROKE
    "\u00f0"  # 0xF3 -> LATIN SMALL LETTER ETH
    "\u0127"  # 0xF4 -> LATIN SMALL LETTER H WITH STROKE
    "\u0131"  # 0xF5 -> LATIN SMALL LETTER DOTLESS I
    "\u0133"  # 0xF6 -> LATIN SMALL LIGATURE IJ
    "\u0140"  # 0xF7 -> LATIN SMALL LETTER L WITH MIDDLE DOT
    "\u0142"  # 0xF8 -> LATIN SMALL LETTER L WITH STROKE
    "\u00f8"  # 0xF9 -> LATIN SMALL LETTER O WITH STROKE
    "\u0153"  # 0xFA -> LATIN SMALL LIGATURE OE
    "\u00df"  # 0xFB -> LATIN SMALL LETTER SHARP S
    "\u00fe"  # 0xFC -> LATIN SMALL LETTER THORN
    "\u0167"  # 0xFD -> LATIN SMALL LETTER T WITH STROKE
    "\u014b"  # 0xFE -> LATIN SMALL LETTER ENG
    "\ufffe"  # 0xFF -> *unmapped*
)

# Encoding table
ENCODING_TABLE = codecs.charmap_build(DECODING_TABLE)  # type: ignore


def search_function(encoding: str) -> codecs.CodecInfo:
    """
    A search function which can be used with :py:func:`codecs.register`.

    As a convenience, there is also :func:`~.register` in this module.
    """
    if encoding.lower() in ("t61", "t.61"):
        return getregentry()
    return codecs.lookup(encoding)  # type: ignore


def register() -> None:
    """
    Convenience function which registers a new default Python search function

    Example:

    >>> import t61codec
    >>> t61codec.register()
    >>> b'Hello T.61: \\xe0'.decode('t.61')
    'Hello T.61: Ω'
    """
    codecs.register(search_function)

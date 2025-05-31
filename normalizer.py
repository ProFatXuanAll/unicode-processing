r"""Map unicodes as a normalization method."""

import unicodedata
from typing import ClassVar

__all__ = [
  'MapUnicodesTextNormalizer',
]


class MapUnicodesTextNormalizer:
  r"""
  Map unicodes as a normalization method.

  More unicodes need to be mapped (those in category ``Sc`` and ``Zs``).
  To make this utility faster, one should avoid using ``unicodedata.category``.
  """

  disallowed_unicode_category: ClassVar[set[str]] = {
    'Cc',
    'Cf',
    'Mc',
    'Me',
    'Mn',
    'Pc',
    'Pd',
    'Pe',
    'Pf',
    'Pi',
    'Po',
    'Ps',
    'Sm',
    'So',
    'Zl',
    'Zp',
  }
  unicode_map: ClassVar[dict[str, str]] = {
    '\u00b4': '´',  # Acute Accent. # noqa: RUF001
    '\u02dd': '´',  # Double Acute Accent. # noqa: RUF001
    '\u02f6': '´',  # Modifier Letter Middle Double Acute Accent. # noqa: RUF001
    '\u1ffd': '´',  # Greek Oxia. # noqa: RUF001
    '\uff40': '´',  # Fullwidth Grave Accent. # noqa: RUF001
    '\u0026': '&',  # Ampersand.
    '\u214b': '&',  # Turned Ampersand.
    '\ufe60': '&',  # Small Ampersand.
    '\uff06': '&',  # Fullwidth Ampersand.
    '\U00016b3a': '&',  # Pahawh Hmong Sign Vos Thiab.
    '\u0027': "'",  # Apostrophe.
    '\uff07': "'",  # Fullwidth Apostrophe.
    '\U00011a41': "'",  # Zanabazar Square Mark Tsheg.
    '\u002a': '*',  # Asterisk.
    '\u066d': '*',  # Arabic Five Pointed Star.
    '\u2042': '*',  # Asterism.
    '\u2051': '*',  # Two Asterisks Aligned Vertically.
    '\u2055': '*',  # Flower Punctuation Mark.
    '\u2217': '*',  # Asterisk Operator.
    '\u22c6': '*',  # Star Operator.
    '\u22c7': '*',  # Division Times.
    '\u204e': '*',  # Low Asterisk.
    '\ua60e': '*',  # Vai Full Stop.
    '\ua673': '*',  # Slavonic Asterisk.
    '\ufe61': '*',  # Small Asterisk.
    '\uff0a': '*',  # Fullwidth Asterisk.
    '\u003a': ':',  # Colon.
    '\u02f8': ':',  # Modifier Letter Raised Colon.
    '\u0589': ':',  # Armenian Full Stop.
    '\u05c3': ':',  # Hebrew Punctuation Sof Pasuq.
    '\u0703': ':',  # Syriac Supralinear Colon.
    '\u0704': ':',  # Syriac Sublinear Colon.
    '\u0706': ':',  # Syriac Colon Skewed Left.
    '\u0707': ':',  # Syriac Colon Skewed Right.
    '\u0708': ':',  # Syriac Supralinear Colon Skewed Left.
    '\u0709': ':',  # Syriac Sublinear Colon Skewed Right.
    '\u0831': ':',  # Samaritan Punctuation Afsaaq.
    '\u0fd2': ':',  # Tibetan Mark Nyis Tsheg.
    '\u1361': ':',  # Ethiopic Wordspace.
    '\u1366': ':',  # Ethiopic Preface Colon.
    '\u1367': ':',  # Ethiopic Question Mark.
    '\u16ec': ':',  # Runic Multiple Punctuation.
    '\u1804': ':',  # Mongolian Colon.
    '\u1a1e': ':',  # Buginese Pallawa.
    '\u1b5d': ':',  # Balinese Carik Pamungkah.
    '\u205a': ':',  # Two Dot Punctuation.
    '\u205d': ':',  # Tricolon.
    '\u205e': ':',  # Vertical Four Dots.
    '\u2236': ':',  # Ratio.
    '\u22ee': ':',  # Vertical Ellipsis.
    '\u2982': ':',  # Z Notation Type Colon.
    '\u2999': ':',  # Dotted Fence.
    '\u2af6': ':',  # Triple Colon Operator.
    '\u2e3d': ':',  # Vertical Six Dots.
    '\ua789': ':',  # Modifier Letter Colon.
    '\ufbbd': ':',  # Arabic Symbol Two Dots Vertically Above.
    '\ufbbe': ':',  # Arabic Symbol Two Dots Vertically Below.
    '\ufe13': ':',  # Presentation Form For Vertical Colon.
    '\ufe19': ':',  # Presentation Form For Vertical Horizontal Ellipsis.
    '\ufe30': ':',  # Presentation Form For Vertical Two Dot Leader.
    '\ufe55': ':',  # Small Colon.
    '\uff1a': ':',  # Fullwidth Colon.
    '\U00010af5': ':',  # Manichaean Punctuation Two Dots.
    '\U0001104a': ':',  # Brahmi Punctuation Double Dot.
    '\U0001123a': ':',  # Khojki Word Separator.
    '\U000112a9': ':',  # Multani Section Mark.
    '\U00011ef7': ':',  # Makasar Passimbang.
    '\u002c': ',',  # Comma.
    '\u02db': ',',  # Ogonek.
    '\u0375': ',',  # Greek Lower Numeral Sign.
    '\u060c': ',',  # Arabic Comma.
    '\u066b': ',',  # Arabic Decimal Separator.
    '\u066c': ',',  # Arabic Thousands Separator.
    '\u201a': ',',  # Single Low-9 Quotation Mark.
    '\u201e': ',',  # Double Low-9 Quotation Mark.
    '\u2e12': ',',  # Hypodiastole.
    '\u2e32': ',',  # Turned Comma.
    '\u2e34': ',',  # Raised Comma.
    '\u2e41': ',',  # Reversed Comma.
    '\u3001': ',',  # Ideographic Comma.
    '\uaa5d': ',',  # Cham Punctuation Danda.
    '\ufe45': ',',  # Sesame Dot.
    '\ufe46': ',',  # White Sesame Dot.
    '\ufe50': ',',  # Small Comma.
    '\ufe51': ',',  # Small Ideographic Comma.
    '\uff0c': ',',  # Fullwidth Comma.
    '\uff64': ',',  # Halfwidth Ideographic Comma.
    '\U00010100': ',',  # Aegean Word Separator Line.
    '\U000111c8': ',',  # Sharada Separator.
    '\U0001144d': ',',  # Newa Comma.
    '\U00011c43': ',',  # Bhaiksuki Word Separator.
    '\U00016e97': ',',  # Medefaidrin Comma.
    '\U00016e98': ',',  # Medefaidrin Full Stop.
    '\u0040': '@',  # Commercial At.
    '\ufe6b': '@',  # Small Commercial At.
    '\uff20': '@',  # Fullwidth Commercial At.
    '\u003d': '=',  # Equals Sign.
    '\u02ed': '=',  # Modifier Letter Unaspirated.
    '\u083a': '=',  # Samaritan Punctuation Zaef.
    '\u1400': '=',  # Canadian Syllabics Hyphen.
    '\u2017': '=',  # Double Low Line.
    '\u207c': '=',  # Superscript Equals Sign.
    '\u208c': '=',  # Subscript Equals Sign.
    '\u2242': '=',  # Minus Tilde.
    '\u2243': '=',  # Asymptotically Equal To.
    '\u2244': '=',  # Not Asymptotically Equal To.
    '\u2245': '=',  # Approximately Equal To.
    '\u2246': '=',  # Approximately But Not Actually Equal To.
    '\u2247': '=',  # Neither Approximately Nor Actually Equal To.
    '\u2248': '=',  # Almost Equal To.
    '\u2249': '=',  # Not Almost Equal To.
    '\u224a': '=',  # Almost Equal or Equal To.
    '\u224b': '=',  # Triple Tilde.
    '\u224c': '=',  # All Equal To.
    '\u224d': '=',  # Equivalent To.
    '\u224e': '=',  # Geometrically Equivalent To.
    '\u224f': '=',  # Difference Between.
    '\u2250': '=',  # Approaches the Limit.
    '\u2251': '=',  # Geometrically Equal To.
    '\u2252': '=',  # Approximately Equal to or the Image Of.
    '\u2253': '=',  # Image of or Approximately Equal To.
    '\u2254': '=',  # Colon Equals.
    '\u2255': '=',  # Equals Colon.
    '\u2256': '=',  # Ring In Equal To.
    '\u2257': '=',  # Ring Equal To.
    '\u2258': '=',  # Corresponds To.
    '\u2259': '=',  # Estimates.
    '\u225a': '=',  # Equiangular To.
    '\u225b': '=',  # Star Equals.
    '\u225c': '=',  # Delta Equal To.
    '\u225d': '=',  # Equal to By Definition.
    '\u225e': '=',  # Measured By.
    '\u225f': '=',  # Questioned Equal To.
    '\u2260': '=',  # Not Equal To.
    '\u2261': '=',  # Identical To.
    '\u2262': '=',  # Not Identical To.
    '\u2263': '=',  # Strictly Equivalent To.
    '\u22cd': '=',  # Reversed Tilde Equals.
    '\u2a66': '=',  # Equals Sign with Dot Below.
    '\u2a67': '=',  # Identical with Dot Above.
    '\u2a6c': '=',  # Similar Minus Similar.
    '\u2a6d': '=',  # Congruent with Dot Above.
    '\u2a6e': '=',  # Equals with Asterisk.
    '\u2a6f': '=',  # Almost Equal to with Circumflex Accent.
    '\u2a70': '=',  # Approximately Equal or Equal To.
    '\u2a73': '=',  # Equals Sign Above Tilde Operator.
    '\u2a74': '=',  # Double Colon Equal.
    '\u2a75': '=',  # Two Consecutive Equals Signs.
    '\u2a76': '=',  # Three Consecutive Equals Signs.
    '\u2a77': '=',  # Equals Sign with Two Dots Above and Two Dots Below.
    '\u2a78': '=',  # Equivalent with Four Dots Above.
    '\u2aae': '=',  # Equals Sign with Bumpy Above.
    '\u2e40': '=',  # Double Hyphen.
    '\ua4ff': '=',  # Lisu Punctuation Full Stop.
    '\ua78a': '=',  # Modifier Letter Short Equals Sign.
    '\ufe66': '=',  # Small Equals Sign.
    '\uff1d': '=',  # Fullwidth Equals Sign.
    '\U000110bf': '=',  # Kaithi Double Section Mark.
    '\U000111de': '=',  # Sharada Section Mark-1.
    '\U0001123c': '=',  # Khojki Double Section Mark.
    '\U0001bc9f': '=',  # Duployan Punctuation Chinook Full Stop.
    '\u002e': '.',  # Full Stop.
    '\u00b7': '.',  # Middle Dot.
    '\u02d9': '.',  # Dot Above.
    '\u0387': '.',  # Greek Ano Teleia.
    '\u06d4': '.',  # Arabic Full Stop.
    '\u0701': '.',  # Syriac Supralinear Full Stop.
    '\u0702': '.',  # Syriac Sublinear Full Stop.
    '\u0830': '.',  # Samaritan Punctuation Nequdaa.
    '\u0a76': '.',  # Gurmukhi Abbreviation Sign.
    '\u0f0b': '.',  # Tibetan Mark Intersyllabic Tsheg.
    '\u0f0c': '.',  # Tibetan Mark Delimiter Tsheg Bstar.
    '\u16eb': '.',  # Runic Single Punctuation.
    '\u1801': '.',  # Mongolian Ellipsis.
    '\u1802': '.',  # Mongolian Comma.
    '\u2022': '.',  # Bullet.
    '\u2024': '.',  # One Dot Leader.
    '\u2025': '.',  # Two Dot Leader.
    '\u2026': '.',  # Horizontal Ellipsis.
    '\u2027': '.',  # Hyphenation Point.
    '\u2219': '.',  # Bullet Operator.
    '\u22c5': '.',  # Dot Operator.
    '\u2981': '.',  # Z Notation Spot.
    '\u2e31': '.',  # Word Separator Middle Dot.
    '\u2e33': '.',  # Raised Dot.
    '\u30fb': '.',  # Katakana Middle Dot.
    '\ufbb2': '.',  # Arabic Symbol Dot Above.
    '\ufbb3': '.',  # Arabic Symbol Dot Below.
    '\ufe52': '.',  # Small Full Stop.
    '\uff0e': '.',  # Fullwidth Full Stop.
    '\uff65': '.',  # Halfwidth Katakana Middle Dot.
    '\U00010101': '.',  # Aegean Word Separator Dot.
    '\U0001091f': '.',  # Phoenician Word Separator.
    '\U00010a50': '.',  # Kharoshthi Punctuation Dot.
    '\U00010af4': '.',  # Manichaean Punctuation Dot.
    '\U00011049': '.',  # Brahmi Punctuation Dot.
    '\U00011174': '.',  # Mahajani Abbreviation Sign.
    '\U000111c7': '.',  # Sharada Abbreviation Sign.
    '\U000115c4': '.',  # Siddham Separator Dot.
    '\u0060': '`',  # Grave Accent.
    '\u02f4': '`',  # Modifier Letter Middle Grave Accent.
    '\u02f5': '`',  # Modifier Letter Middle Double Grave Accent.
    '\u1fef': '`',  # Greek Varia.
    '\u003e': '>',  # Greater-Than Sign.
    '\u00bb': '>',  # Right-Pointing Double Angle Quotation Mark.
    '\u02c3': '>',  # Modifier Letter Right Arrowhead.
    '\u02f2': '>',  # Modifier Letter Low Right Arrowhead.
    '\u169b': '>',  # Ogham Feather Mark.
    '\u1808': '>',  # Mongolian Manchu Comma.
    '\u1809': '>',  # Mongolian Manchu Full Stop.
    '\u203a': '>',  # Single Right-Pointing Angle Quotation Mark.
    '\u2265': '>',  # Greater-Than or Equal To.
    '\u2267': '>',  # Greater-Than Over Equal To.
    '\u2269': '>',  # Greater-Than But Not Equal To.
    '\u226b': '>',  # Much Greater-Than.
    '\u226f': '>',  # Not Greater-Than.
    '\u2271': '>',  # Neither Greater-Than Nor Equal To.
    '\u2273': '>',  # Greater-Than or Equivalent To.
    '\u2275': '>',  # Neither Greater-Than Nor Equivalent To.
    '\u227b': '>',  # Succeeds.
    '\u227d': '>',  # Succeeds or Equal To.
    '\u227f': '>',  # Succeeds or Equivalent To.
    '\u2281': '>',  # Does Not Succeed.
    '\u22b1': '>',  # Succeeds Under Relation.
    '\u22d7': '>',  # Greater-Than with Dot.
    '\u22d9': '>',  # Very Much Greater-Than.
    '\u22dd': '>',  # Equal to or Greater-Than.
    '\u22df': '>',  # Equal to or Succeeds.
    '\u22e1': '>',  # Does Not Succeed or Equal.
    '\u22e7': '>',  # Greater-Than But Not Equivalent To.
    '\u22e9': '>',  # Succeeds But Not Equivalent To.
    '\u232a': '>',  # Right-Pointing Angle Bracket.
    '\u276d': '>',  # Medium Right-Pointing Angle Bracket Ornament.
    '\u276f': '>',  # Heavy Right-Pointing Angle Quotation Mark Ornament.
    '\u2771': '>',  # Heavy Right-Pointing Angle Bracket Ornament.
    '\u27e9': '>',  # Mathematical Right Angle Bracket.
    '\u27eb': '>',  # Mathematical Right Double Angle Bracket.
    '\u297d': '>',  # Right Fish Tail.
    '\u298a': '>',  # Z Notation Right Binding Bracket.
    '\u2992': '>',  # Right Angle Bracket with Dot.
    '\u2994': '>',  # Right Arc Greater-Than Bracket.
    '\u29a0': '>',  # Spherical Angle Opening Left.
    '\u29fd': '>',  # Right-Pointing Curved Angle Bracket.
    '\u2a20': '>',  # Z Notation Schema Piping.
    '\u2a7a': '>',  # Greater-Than with Circle Inside.
    '\u2a7c': '>',  # Greater-Than with Question Mark Above.
    '\u2a7e': '>',  # Greater-Than or Slanted Equal To.
    '\u2a80': '>',  # Greater-Than or Slanted Equal to with Dot Inside.
    '\u2a82': '>',  # Greater-Than or Slanted Equal to with Dot Above.
    '\u2a84': '>',  # Greater-Than or Slanted Equal to with Dot Above Left.
    '\u2a86': '>',  # Greater-Than or Approximate.
    '\u2a88': '>',  # Greater-Than and Single-Line Not Equal To.
    '\u2a8a': '>',  # Greater-Than and Not Approximate.
    '\u2a8e': '>',  # Greater-Than Above Similar or Equal.
    '\u2a96': '>',  # Slanted Equal to or Greater-Than.
    '\u2a98': '>',  # Slanted Equal to or Greater-Than with Dot Inside.
    '\u2a9a': '>',  # Double-Line Equal to or Greater-Than.
    '\u2a9c': '>',  # Double-Line Slanted Equal to or Greater-Than.
    '\u2a9e': '>',  # Similar or Greater-Than.
    '\u2aa0': '>',  # Similar Above Greater-Than Above Equals Sign.
    '\u2aa2': '>',  # Double Nested Greater-Than.
    '\u2aad': '>',  # Larger Than or Equal To.
    '\u2ab0': '>',  # Succeeds Above Single-Line Equals Sign.
    '\u2ab2': '>',  # Succeeds Above Single-Line Not Equal To.
    '\u2ab4': '>',  # Succeeds Above Equals Sign.
    '\u2ab6': '>',  # Succeeds Above Not Equal To.
    '\u2ab8': '>',  # Succeeds Above Almost Equal To.
    '\u2aba': '>',  # Succeeds Above Not Almost Equal To.
    '\u2abc': '>',  # Double Succeeds.
    '\u2af8': '>',  # Triple Nested Greater-Than.
    '\u2afa': '>',  # Double-Line Slanted Greater-Than or Equal To.
    '\u2e03': '>',  # Right Substitution Bracket.
    '\u2e05': '>',  # Right Dotted Substitution Bracket.
    '\u2e16': '>',  # Dotted Right-Pointing Angle.
    '\u3009': '>',  # Right Angle Bracket.
    '\u300b': '>',  # Right Double Angle Bracket.
    '\ufe3e': '>',  # Presentation Form For Vertical Right Double Angle Bracket.
    '\ufe40': '>',  # Presentation Form For Vertical Right Angle Bracket.
    '\ufe65': '>',  # Small Greater-Than Sign.
    '\uff1e': '>',  # Fullwidth Greater-Than Sign.
    '\u002d': '-',  # Hyphen-Minus.
    '\u058a': '-',  # Armenian Hyphen.
    '\u05be': '-',  # Hebrew Punctuation Maqaf.
    '\u1680': '-',  # Ogham Space Mark.
    '\u1806': '-',  # Mongolian Todo Soft Hyphen.
    '\u180a': '-',  # Mongolian Nirugu.
    '\u2010': '-',  # Hyphen.
    '\u2011': '-',  # Non-Breaking Hyphen.
    '\u2012': '-',  # Figure Dash.
    '\u2013': '-',  # En Dash.
    '\u2014': '-',  # Em Dash.
    '\u2015': '-',  # Horizontal Bar.
    '\u2043': '-',  # Hyphen Bullet.
    '\u207b': '-',  # Superscript Minus.
    '\u208b': '-',  # Subscript Minus.
    '\u2212': '-',  # Minus Sign.
    '\u23af': '-',  # Horizontal Line Extension.
    '\u23bb': '-',  # Horizontal Scan Line-3.
    '\u29ff': '-',  # Miny.
    '\u2a29': '-',  # Minus Sign with Comma Above.
    '\u2a2a': '-',  # Minus Sign with Dot Below.
    '\u2a2b': '-',  # Minus Sign with Falling Dots.
    '\u2a2c': '-',  # Minus Sign with Rising Dots.
    '\u2e3a': '-',  # Two-Em Dash.
    '\u2e3b': '-',  # Three-Em Dash.
    '\u30a0': '-',  # Katakana-Hiragana Double Hyphen.
    '\ufe58': '-',  # Small Em Dash.
    '\ufe63': '-',  # Small Hyphen-Minus.
    '\uff0d': '-',  # Fullwidth Hyphen-Minus.
    '\U0001104b': '-',  # Brahmi Punctuation Line.
    '\U000110be': '-',  # Kaithi Section Mark.
    '\u02ea': '「',  # Modifier Letter Yin Departing Tone Mark.
    '\u02f9': '「',  # Modifier Letter Begin High Tone.
    '\u02fb': '「',  # Modifier Letter Begin Low Tone.
    '\u221f': '「',  # Right Angle.
    '\u2308': '「',  # Left Ceiling.
    '\u230a': '「',  # Left Floor.
    '\u23a1': '「',  # Left Square Bracket Upper Corner.
    '\u23a3': '「',  # Left Square Bracket Lower Corner.
    '\u2a3d': '「',  # Righthand Interior Product.
    '\u2e22': '「',  # Top Left Half Bracket.
    '\u2e24': '「',  # Bottom Left Half Bracket.
    '\u300c': '「',  # Left Corner Bracket.
    '\u300e': '「',  # Left White Corner Bracket.
    '\ua712': '「',  # Modifier Letter Extra-High Left-Stem Tone Bar.
    '\ua716': '「',  # Modifier Letter Extra-Low Left-Stem Tone Bar.
    '\ufe41': '「',  # Presentation Form For Vertical Left Corner Bracket.
    '\ufe43': '「',  # Presentation Form For Vertical Left White Corner Bracket.
    '\uff62': '「',  # Halfwidth Left Corner Bracket.
    '\u007b': '{',  # Left Curly Bracket.
    '\u23a8': '{',  # Left Curly Bracket Middle Piece.
    '\u23de': '{',  # Top Curly Bracket.
    '\u2774': '{',  # Medium Left Curly Bracket Ornament.
    '\u2983': '{',  # Left White Curly Bracket.
    '\ufe37': '{',  # Presentation Form For Vertical Left Curly Bracket.
    '\ufe5b': '{',  # Small Left Curly Bracket.
    '\uff5b': '{',  # Fullwidth Left Curly Bracket.
    '\u201c': '“',  # Left Double Quotation Mark.
    '\u201f': '“',  # Double High-Reversed-9 Quotation Mark.
    '\u2036': '“',  # Reversed Double Prime.
    '\u2037': '“',  # Reversed Triple Prime.
    '\u2e42': '“',  # Double Low-Reversed-9 Quotation Mark.
    '\u301d': '“',  # Reversed Double Prime Quotation Mark.
    '\u309b': '“',  # Katakana-Hiragana Voiced Sound Mark.
    '\u0028': '(',  # Left Parenthesis.
    '\u02d3': '(',  # Modifier Letter Centred Left Half Ring.
    '\u2040': '(',  # Character Tie.
    '\u2054': '(',  # Inverted Undertie.
    '\u207d': '(',  # Superscript Left Parenthesis.
    '\u208d': '(',  # Subscript Left Parenthesis.
    '\u23dc': '(',  # Top Parenthesis.
    '\u2768': '(',  # Medium Left Parenthesis Ornament.
    '\u276a': '(',  # Medium Flattened Left Parenthesis Ornament.
    '\u2985': '(',  # Left White Parenthesis.
    '\u2987': '(',  # Z Notation Left Image Bracket.
    '\u2995': '(',  # Double Left Arc Greater-Than Bracket.
    '\u2e26': '(',  # Left Sideways U Bracket.
    '\u2e28': '(',  # Left Double Parenthesis.
    '\ufd3e': '(',  # Ornate Left Parenthesis.
    '\ufe35': '(',  # Presentation Form For Vertical Left Parenthesis.
    '\ufe59': '(',  # Small Left Parenthesis.
    '\uff08': '(',  # Fullwidth Left Parenthesis.
    '\uff5f': '(',  # Fullwidth Left White Parenthesis.
    '\u055d': '‘',  # Armenian Comma. # noqa: RUF001
    '\u2018': '‘',  # Left Single Quotation Mark. # noqa: RUF001
    '\u201b': '‘',  # Single High-Reversed-9 Quotation Mark. # noqa: RUF001
    '\u2035': '‘',  # Reversed Prime. # noqa: RUF001
    '\u2e0c': '‘',  # Left Raised Omission Bracket. # noqa: RUF001
    '\u2e1c': '‘',  # Left Low Paraphrase Bracket. # noqa: RUF001
    '\U00010ead': '‘',  # Yezidi Hyphenation Mark. # noqa: RUF001
    '\u005b': '[',  # Left Square Bracket.
    '\u2045': '[',  # Left Square Bracket with Quill.
    '\u23e0': '[',  # Top Tortoise Shell Bracket.
    '\u2772': '[',  # Light Left Tortoise Shell Bracket Ornament.
    '\u27e6': '[',  # Mathematical Left White Square Bracket.
    '\u27ec': '[',  # Mathematical Left White Tortoise Shell Bracket.
    '\u27ee': '[',  # Mathematical Left Flattened Parenthesis.
    '\u298b': '[',  # Left Square Bracket with Underbar.
    '\u298d': '[',  # Left Square Bracket with Tick In Top Corner.
    '\u298f': '[',  # Left Square Bracket with Tick In Bottom Corner.
    '\u2997': '[',  # Left Black Tortoise Shell Bracket.
    '\u3010': '[',  # Left Black Lenticular Bracket.
    '\u3014': '[',  # Left Tortoise Shell Bracket.
    '\u3016': '[',  # Left White Lenticular Bracket.
    '\u3018': '[',  # Left White Tortoise Shell Bracket.
    '\u301a': '[',  # Left White Square Bracket.
    '\ufe17': '[',  # Presentation Form For Vertical Left White Lenticular Bracket.
    '\ufe39': '[',  # Presentation Form For Vertical Left Tortoise Shell Bracket.
    '\ufe3b': '[',  # Presentation Form For Vertical Left Black Lenticular Bracket.
    '\ufe47': '[',  # Presentation Form For Vertical Left Square Bracket.
    '\ufe5d': '[',  # Small Left Tortoise Shell Bracket.
    '\uff3b': '[',  # Fullwidth Left Square Bracket.
    '\u003c': '<',  # Less-Than Sign.
    '\u00ab': '<',  # Left-Pointing Double Angle Quotation Mark.
    '\u02c2': '<',  # Modifier Letter Left Arrowhead.
    '\u02f1': '<',  # Modifier Letter Low Left Arrowhead.
    '\u169c': '<',  # Ogham Reversed Feather Mark.
    '\u2039': '<',  # Single Left-Pointing Angle Quotation Mark.
    '\u2222': '<',  # Spherical Angle.
    '\u2264': '<',  # Less-Than or Equal To.
    '\u2266': '<',  # Less-Than Over Equal To.
    '\u2268': '<',  # Less-Than But Not Equal To.
    '\u226a': '<',  # Much Less-Than.
    '\u226e': '<',  # Not Less-Than.
    '\u2270': '<',  # Neither Less-Than Nor Equal To.
    '\u2272': '<',  # Less-Than or Equivalent To.
    '\u2274': '<',  # Neither Less-Than Nor Equivalent To.
    '\u227a': '<',  # Precedes.
    '\u227c': '<',  # Precedes or Equal To.
    '\u227e': '<',  # Precedes or Equivalent To.
    '\u2280': '<',  # Does Not Precede.
    '\u22b0': '<',  # Precedes Under Relation.
    '\u22d6': '<',  # Less-Than with Dot.
    '\u22d8': '<',  # Very Much Less-Than.
    '\u22dc': '<',  # Equal to or Less-Than.
    '\u22de': '<',  # Equal to or Precedes.
    '\u22e0': '<',  # Does Not Precede or Equal.
    '\u22e6': '<',  # Less-Than But Not Equivalent To.
    '\u22e8': '<',  # Precedes But Not Equivalent To.
    '\u2329': '<',  # Left-Pointing Angle Bracket.
    '\u276c': '<',  # Medium Left-Pointing Angle Bracket Ornament.
    '\u276e': '<',  # Heavy Left-Pointing Angle Quotation Mark Ornament.
    '\u2770': '<',  # Heavy Left-Pointing Angle Bracket Ornament.
    '\u27e8': '<',  # Mathematical Left Angle Bracket.
    '\u27ea': '<',  # Mathematical Left Double Angle Bracket.
    '\u297c': '<',  # Left Fish Tail.
    '\u2989': '<',  # Z Notation Left Binding Bracket.
    '\u2991': '<',  # Left Angle Bracket with Dot.
    '\u2993': '<',  # Left Arc Less-Than Bracket.
    '\u29fc': '<',  # Left-Pointing Curved Angle Bracket.
    '\u2a79': '<',  # Less-Than with Circle Inside.
    '\u2a7b': '<',  # Less-Than with Question Mark Above.
    '\u2a7d': '<',  # Less-Than or Slanted Equal To.
    '\u2a7f': '<',  # Less-Than or Slanted Equal to with Dot Inside.
    '\u2a81': '<',  # Less-Than or Slanted Equal to with Dot Above.
    '\u2a83': '<',  # Less-Than or Slanted Equal to with Dot Above Right.
    '\u2a85': '<',  # Less-Than or Approximate.
    '\u2a87': '<',  # Less-Than and Single-Line Not Equal To.
    '\u2a89': '<',  # Less-Than and Not Approximate.
    '\u2a8d': '<',  # Less-Than Above Similar or Equal.
    '\u2a95': '<',  # Slanted Equal to or Less-Than.
    '\u2a97': '<',  # Slanted Equal to or Less-Than with Dot Inside.
    '\u2a99': '<',  # Double-Line Equal to or Less-Than.
    '\u2a9b': '<',  # Double-Line Slanted Equal to or Less-Than.
    '\u2a9d': '<',  # Similar or Less-Than.
    '\u2a9f': '<',  # Similar Above Less-Than Above Equals Sign.
    '\u2aa1': '<',  # Double Nested Less-Than.
    '\u2aa3': '<',  # Double Nested Less-Than with Underbar.
    '\u2aac': '<',  # Smaller Than or Equal To.
    '\u2aaf': '<',  # Precedes Above Single-Line Equals Sign.
    '\u2ab1': '<',  # Precedes Above Single-Line Not Equal To.
    '\u2ab3': '<',  # Precedes Above Equals Sign.
    '\u2ab5': '<',  # Precedes Above Not Equal To.
    '\u2ab7': '<',  # Precedes Above Almost Equal To.
    '\u2ab9': '<',  # Precedes Above Not Almost Equal To.
    '\u2abb': '<',  # Double Precedes.
    '\u2af7': '<',  # Triple Nested Less-Than.
    '\u2af9': '<',  # Double-Line Slanted Less-Than or Equal To.
    '\u2e02': '<',  # Left Substitution Bracket.
    '\u2e04': '<',  # Left Dotted Substitution Bracket.
    '\u3008': '<',  # Left Angle Bracket.
    '\u300a': '<',  # Left Double Angle Bracket.
    '\ufe3d': '<',  # Presentation Form For Vertical Left Double Angle Bracket.
    '\ufe3f': '<',  # Presentation Form For Vertical Left Angle Bracket.
    '\ufe64': '<',  # Small Less-Than Sign.
    '\uff1c': '<',  # Fullwidth Less-Than Sign.
    '\u005f': '_',  # Low Line.
    '\u2e0f': '_',  # Paragraphos.
    '\u2e10': '_',  # Forked Paragraphos.
    '\u2e11': '_',  # Reversed Forked Paragraphos.
    '\ufe4d': '_',  # Dashed Low Line.
    '\ufe4e': '_',  # Centreline Low Line.
    '\ufe4f': '_',  # Wavy Low Line.
    '\uff3f': '_',  # Fullwidth Low Line.
    '\u00d7': '×',  # Multiplication Sign. # noqa: RUF001
    '\u02df': '×',  # Modifier Letter Cross Accent. # noqa: RUF001
    '\u166e': '×',  # Canadian Syllabics Full Stop. # noqa: RUF001
    '\u1c3d': '×',  # Lepcha Punctuation Cer-Wa. # noqa: RUF001
    '\u1c3e': '×',  # Lepcha Punctuation Tshook Cer-Wa. # noqa: RUF001
    '\u2a09': '×',  # N-Ary Times Operator. # noqa: RUF001
    '\u2a2f': '×',  # Vector or Cross Product. # noqa: RUF001
    '\u2a30': '×',  # Multiplication Sign with Dot Above. # noqa: RUF001
    '\u2a31': '×',  # Multiplication Sign with Underbar. # noqa: RUF001
    '\u2a32': '×',  # Semidirect Product with Bottom Closed. # noqa: RUF001
    '\u2e3c': '×',  # Stenographic Full Stop. # noqa: RUF001
    '\U00010102': '×',  # Aegean Check Mark. # noqa: RUF001
    '\u0025': '%',  # Percent Sign.
    '\u0609': '%',  # Arabic-Indic Per Mille Sign.
    '\u060a': '%',  # Arabic-Indic Per Ten Thousand Sign.
    '\u066a': '%',  # Arabic Percent Sign.
    '\u2030': '%',  # Per Mille Sign.
    '\u2031': '%',  # Per Ten Thousand Sign.
    '\u2052': '%',  # Commercial Minus Sign.
    '\u2e13': '%',  # Dotted Obelos.
    '\ufe6a': '%',  # Small Percent Sign.
    '\uff05': '%',  # Fullwidth Percent Sign.
    '\u002b': '+',  # Plus Sign.
    '\u16ed': '+',  # Runic Cross Punctuation.
    '\u207a': '+',  # Superscript Plus Sign.
    '\u208a': '+',  # Subscript Plus Sign.
    '\u2214': '+',  # Dot Plus.
    '\u29fe': '+',  # Tiny.
    '\u2a22': '+',  # Plus Sign with Small Circle Above.
    '\u2a23': '+',  # Plus Sign with Circumflex Accent Above.
    '\u2a24': '+',  # Plus Sign with Tilde Above.
    '\u2a25': '+',  # Plus Sign with Dot Below.
    '\u2a26': '+',  # Plus Sign with Tilde Below.
    '\u2a27': '+',  # Plus Sign with Subscript Two.
    '\u2a28': '+',  # Plus Sign with Black Triangle.
    '\ufe62': '+',  # Small Plus Sign.
    '\uff0b': '+',  # Fullwidth Plus Sign.
    '\u003f': '?',  # Question Mark.
    '\u00bf': '?',  # Inverted Question Mark.
    '\u061f': '?',  # Arabic Question Mark.
    '\u2047': '?',  # Double Question Mark.
    '\u2048': '?',  # Question Exclamation Mark.
    '\u2049': '?',  # Exclamation Question Mark.
    '\u2e18': '?',  # Inverted Interrobang.
    '\u2e2e': '?',  # Reversed Question Mark.
    '\u2e4c': '?',  # Medieval Comma.
    '\ufe16': '?',  # Presentation Form For Vertical Question Mark.
    '\ufe56': '?',  # Small Question Mark.
    '\uff1f': '?',  # Fullwidth Question Mark.
    '\U000119e2': '?',  # Nandinagari Sign Siddham.
    '\u0022': '"',  # Quotation Mark.
    '\uff02': '"',  # Fullwidth Quotation Mark.
    '\U00011944': '"',  # Dives Akuru Double Danda.
    '\u005c': '\\',  # Reverse Solidus.
    '\u2216': '\\',  # Set Minus.
    '\u29f5': '\\',  # Reverse Solidus Operator.
    '\u29f7': '\\',  # Reverse Solidus with Horizontal Stroke.
    '\u29f9': '\\',  # Big Reverse Solidus
    '\u2cf9': '\\',  # Coptic Old Nubian Full Stop.
    '\u2cfb': '\\',  # Coptic Old Nubian Indirect Question Mark.
    '\ufe68': '\\',  # Small Reverse Solidus.
    '\uff3c': '\\',  # Fullwidth Reverse Solidus.
    '\u02e5': '」',  # Modifier Letter Extra-High Tone Bar.
    '\u02e9': '」',  # Modifier Letter Extra-Low Tone Bar.
    '\u02fa': '」',  # Modifier Letter End High Tone.
    '\u02fc': '」',  # Modifier Letter End Low Tone.
    '\u02fe': '」',  # Modifier Letter Open Shelf.
    '\u2142': '」',  # Turned Sans-Serif Capital L.
    '\u2143': '」',  # Reversed Sans-Serif Capital L.
    '\u2309': '」',  # Right Ceiling.
    '\u230b': '」',  # Right Floor.
    '\u23a4': '」',  # Right Square Bracket Upper Corner.
    '\u23a6': '」',  # Right Square Bracket Lower Corner.
    '\u2a3c': '」',  # Interior Product.
    '\u2e23': '」',  # Top Right Half Bracket.
    '\u2e25': '」',  # Bottom Right Half Bracket.
    '\u300d': '」',  # Right Corner Bracket.
    '\u300f': '」',  # Right White Corner Bracket.
    '\ufe42': '」',  # Presentation Form For Vertical Right Corner Bracket.
    '\ufe44': '」',  # Presentation Form For Vertical Right White Corner Bracket.
    '\uff63': '」',  # Halfwidth Right Corner Bracket.
    '\u007d': '}',  # Right Curly Bracket.
    '\u23ac': '}',  # Right Curly Bracket Middle Piece.
    '\u23df': '}',  # Bottom Curly Bracket.
    '\u2775': '}',  # Medium Right Curly Bracket Ornament.
    '\u2984': '}',  # Right White Curly Bracket.
    '\ufe38': '}',  # Presentation Form For Vertical Right Curly Bracket.
    '\ufe5c': '}',  # Small Right Curly Bracket.
    '\uff5d': '}',  # Fullwidth Right Curly Bracket.
    '\u05f4': '”',  # Hebrew Punctuation Gershayim.
    '\u1cd3': '”',  # Vedic Sign Nihshvasa.
    '\u201d': '”',  # Right Double Quotation Mark.
    '\u2033': '”',  # Double Prime.
    '\u2034': '”',  # Triple Prime.
    '\u2057': '”',  # Quadruple Prime.
    '\u2e17': '”',  # Double Oblique Hyphen.
    '\u3003': '”',  # Ditto Mark.
    '\u301e': '”',  # Double Prime Quotation Mark.
    '\u301f': '”',  # Low Double Prime Quotation Mark.
    '\u0029': ')',  # Right Parenthesis.
    '\u02d2': ')',  # Modifier Letter Centred Right Half Ring.
    '\u203f': ')',  # Undertie.
    '\u207e': ')',  # Superscript Right Parenthesis.
    '\u208e': ')',  # Subscript Right Parenthesis.
    '\u23dd': ')',  # Bottom Parenthesis.
    '\u2769': ')',  # Medium Right Parenthesis Ornament.
    '\u276b': ')',  # Medium Flattened Right Parenthesis Ornament.
    '\u2986': ')',  # Right White Parenthesis.
    '\u2988': ')',  # Z Notation Right Image Bracket.
    '\u2996': ')',  # Double Right Arc Less-Than Bracket.
    '\u2e27': ')',  # Right Sideways U Bracket.
    '\u2e29': ')',  # Right Double Parenthesis.
    '\ufd3f': ')',  # Ornate Right Parenthesis.
    '\ufe36': ')',  # Presentation Form For Vertical Right Parenthesis.
    '\ufe5a': ')',  # Small Right Parenthesis.
    '\uff09': ')',  # Fullwidth Right Parenthesis.
    '\uff60': ')',  # Fullwidth Right White Parenthesis.
    '\u0384': '’',  # Greek Tonos. # noqa: RUF001
    '\u055a': '’',  # Armenian Apostrophe. # noqa: RUF001
    '\u055b': '’',  # Armenian Emphasis Mark. # noqa: RUF001
    '\u05f3': '’',  # Hebrew Punctuation Geresh. # noqa: RUF001
    '\u2019': '’',  # Right Single Quotation Mark. # noqa: RUF001
    '\u2032': '’',  # Prime. # noqa: RUF001
    '\u2e0d': '’',  # Right Raised Omission Bracket. # noqa: RUF001
    '\u2e1d': '’',  # Right Low Paraphrase Bracket. # noqa: RUF001
    '\u2cff': '’',  # Coptic Morphological Divider. # noqa: RUF001
    '\ufe10': '’',  # Presentation Form For Vertical Comma. # noqa: RUF001
    '\ufe11': '’',  # Presentation Form For Vertical Ideographic Comma. # noqa: RUF001
    '\u005d': ']',  # Right Square Bracket.
    '\u2046': ']',  # Right Square Bracket with Quill.
    '\u23e1': ']',  # Bottom Tortoise Shell Bracket.
    '\u2773': ']',  # Light Right Tortoise Shell Bracket Ornament.
    '\u27e7': ']',  # Mathematical Right White Square Bracket.
    '\u27ed': ']',  # Mathematical Right White Tortoise Shell Bracket.
    '\u27ef': ']',  # Mathematical Right Flattened Parenthesis.
    '\u298c': ']',  # Right Square Bracket with Underbar.
    '\u298e': ']',  # Right Square Bracket with Tick In Bottom Corner.
    '\u2990': ']',  # Right Square Bracket with Tick In Top Corner.
    '\u2998': ']',  # Right Black Tortoise Shell Bracket.
    '\u3011': ']',  # Right Black Lenticular Bracket.
    '\u3015': ']',  # Right Tortoise Shell Bracket.
    '\u3017': ']',  # Right White Lenticular Bracket.
    '\u3019': ']',  # Right White Tortoise Shell Bracket.
    '\u301b': ']',  # Right White Square Bracket.
    '\ufe18': ']',  # Presentation Form For Vertical Right White Lenticular Brakcet.
    '\ufe3a': ']',  # Presentation Form For Vertical Right Tortoise Shell Bracket.
    '\ufe3c': ']',  # Presentation Form For Vertical Right Black Lenticular Bracket.
    '\ufe48': ']',  # Presentation Form For Vertical Right Square Bracket.
    '\ufe5e': ']',  # Small Right Tortoise Shell Bracket.
    '\uff3d': ']',  # Fullwidth Right Square Bracket.
    '\u003b': ';',  # Semicolon.
    '\u061b': ';',  # Arabic Semicolon.
    '\u037e': ';',  # Greek Question Mark.
    '\u204f': ';',  # Reversed Semicolon.
    '\u2a1f': ';',  # Z Notation Schema Composition.
    '\u2a3e': ';',  # Z Notation Relational Composition.
    '\u2e35': ';',  # Turned Semicolon.
    '\u2e44': ';',  # Double Suspension Mark.
    '\u2e49': ';',  # Double Stacked Comma.
    '\u2e4e': ';',  # Punctus Elevatus Mark.
    '\ua9c7': ';',  # Javanese Pada Pangkat.
    '\ufe14': ';',  # Presentation Form For Vertical Semicolon.
    '\ufe54': ';',  # Small Semicolon.
    '\uff1b': ';',  # Fullwidth Semicolon.
    '\U0001145a': ';',  # Newa Double Comma.
    '\u00a7': '§',  # Section Sign.
    '\u00b6': '§',  # Pilcrow Sign.
    '\u204b': '§',  # Reversed Pilcrow Sign.
    '\u002f': '/',  # Solidus.
    '\u060d': '/',  # Arabic Date Separator.
    '\u1735': '/',  # Philippine Single Punctuation.
    '\u1736': '/',  # Philippine Double Punctuation.
    '\u2044': '/',  # Fraction Slash.
    '\u2215': '/',  # Division Slash.
    '\u29f6': '/',  # Solidus with Overbar.
    '\u29f8': '/',  # Big Solidus.
    '\u2afb': '/',  # Triple Solidus Binary Relation.
    '\u2afd': '/',  # Double Solidus Operator.
    '\u2cfa': '/',  # Coptic Old Nubian Direct Question Mark.
    '\u2cfc': '/',  # Coptic Old Nubian Verse Divider.
    '\u2d70': '/',  # Tifinagh Separator Mark.
    '\u2e4a': '/',  # Dotted Solidus.
    '\ua6f3': '/',  # Bamum Full Stop.
    '\ua6f4': '/',  # Bamum Colon.
    '\uff0f': '/',  # Fullwidth Solidus.
    '\u007e': '~',  # Tilde.
    '\u02dc': '~',  # Small Tilde.
    '\u02f7': '~',  # Modifier Letter Low Tilde.
    '\u055c': '~',  # Armenian Exclamation Mark.
    '\u1fc0': '~',  # Greek Perispomeni.
    '\u2053': '~',  # Swung Dash.
    '\u223b': '~',  # Homothetic.
    '\u223c': '~',  # Tilde Operator.
    '\u223d': '~',  # Reversed Tilde.
    '\u223e': '~',  # Inverted Lazy S.
    '\u223f': '~',  # Sine Wave.
    '\u2241': '~',  # Not Tilde.
    '\u2a6a': '~',  # Tilde Operator with Dot Above.
    '\u2a6b': '~',  # Tilde Operator with Rising Dots.
    '\u2e09': '~',  # Left Transposition Bracket.
    '\u2e0a': '~',  # Right Transposition Bracket.
    '\u301c': '~',  # Wave Dash.
    '\u3030': '~',  # Wavy Dash.
    '\uff5e': '~',  # Fullwidth Tilde.
  }

  def normalize_text(self, *, text: str) -> str:
    """Perform text normalization."""
    return ''.join(self.__replace_character(char=char) for char in text)

  def __replace_character(self, *, char: str) -> str:
    if (norm_char := self.unicode_map.get(char)) is not None:
      return norm_char
    if self.__is_unicode_category_allowed(char=char):
      return char
    return ''

  def __is_unicode_category_allowed(self, *, char: str) -> bool:
    return unicodedata.category(char) not in self.disallowed_unicode_category

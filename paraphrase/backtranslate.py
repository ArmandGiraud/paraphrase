#!/usr/bin/env python

"""using google translate api to get sentence variations
"""

__author__ = "Armand Giraud"
__license__ = "Apache"
__version__ = "1.0.1"
__maintainer__ = "Armand Giraud"
__email__ = "armand.giraud.ag@gmail.com"
__status__ = "Dev"


def simple_backtranslate(original, lang_tmp = "en"):
    """simple function translationg original string to anoter language,
    and back into original sentence.

    Input
    ----------
    original: string to be translated

    Parameters
    ----------
    lang_temp: intermediate language for translation
    see: https://ctrlq.org/code/19899-google-translate-languages for the complete list of available languages

    Returns
    ----------
    paraphrased string of the original sentence
    """
    
    import textblob
    t = textblob.blob.TextBlob(original)
    translated = str(t.translate(from_lang = "fr", to = lang_tmp))
    blob = textblob.blob.TextBlob(translated)
    tr = blob.translate(from_lang = lang_tmp, to = "fr")
    return str(tr)
""" from https://github.com/keithito/tacotron

Defines the set of symbols used in text input to the model.
"""
# Padding and basic punctuation
_pad = "_"
_punctuation = "،؛:.!؟۔"  # Arabic punctuation marks

# Arabic letters (basic letters)
_letters_arabic = "ابتثجحخدذرزسشصضطظعغفقكلمنهويءأإآؤئة"

# Arabic diacritical marks (tashkeel)
_diacritics = "ًٌٍَُِّْٰٓٔ"  # Fatha, Damma, Kasra, Shadda, Sukun, etc.

# Additional characters that might appear in Arabic text
_additional_arabic = "؀؁؂؃؄؅؆؇؈؉؊؋،؍؎؏ؘؙؚؐؑؒؓؔؕؖؗ؛؜؝؞؟ؠءآأؤإئابةتثجحخدذرزسشصضطظعغفقكلمنهوىيًٌٍَُِّْٰٱٲٳٴٵٶٷٸٹٺٻټٽپٿڀځڂڃڄڅچڇڈډڊڋڌڍڎڏڐڑڒړڔڕږڗژڙښڛڜڝڞڟڠڡڢڣڤڥڦڧڨکڪګڬڭڮگڰڱڲڳڴڵڶڷڸڹںڻڼڽھڿۀۃۄۅۆۇۈۉۊۋیۍێۏېۑےۓ۔ەۖۗۘۙۚۛۜ۝۞ۣ۟۠ۡۢۤۥۦۧۨ۩۪ۭ۫۬ۮۯ"

# Combining all symbols
symbols = ([_pad] + 
          list(_punctuation) + 
          list(_letters_arabic) + 
          list(_diacritics) + 
          list(_additional_arabic))

# Remove duplicates while preserving order
symbols = list(dict.fromkeys(symbols))

# Special symbol ids
SPACE_ID = symbols.index(" ")

# For debugging/verification
print(f"Total number of symbols: {len(symbols)}")
print(f"Sample of symbols: {''.join(symbols[:20])}")



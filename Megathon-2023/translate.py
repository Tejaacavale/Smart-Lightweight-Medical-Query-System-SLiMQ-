# pip install argostranslate

import argostranslate.package
import argostranslate.translate

def translate_hindi_to_english (text): 
    from_code = "hi"
    to_code = "en"

    # Download and install Argos Translate package
    argostranslate.package.update_package_index()
    available_packages = argostranslate.package.get_available_packages()
    package_to_install = next(
        filter(
            lambda x: x.from_code == from_code and x.to_code == to_code, available_packages
        )
    )
    argostranslate.package.install_from_path(package_to_install.download())
    
    # Translate
    translatedText = argostranslate.translate.translate(text, from_code, to_code)

    return translatedText

def translate_english_to_hindi (text): 
    from_code = "en"
    to_code = "hi"
    
    # Download and install Argos Translate package
    argostranslate.package.update_package_index()
    available_packages = argostranslate.package.get_available_packages()
    package_to_install = next(
        filter(
            lambda x: x.from_code == from_code and x.to_code == to_code, available_packages
        )
    )
    argostranslate.package.install_from_path(package_to_install.download())
    
    # Translate
    translatedText = argostranslate.translate.translate(text, from_code, to_code)

    return translatedText

# Final wrapper function
def translate_from (text, original_language):
    if original_language == "hi":
        return translate_hindi_to_english (text)
    elif original_language == "en":
        return translate_english_to_hindi (text)

print(translate_from("लाइटनिंग चोर एक 2005 काल्पनिक-एडवेंचर उपन्यास है जो ग्रीक पौराणिक कथाओं पर आधारित है। यह लेखक रिक रिओर्डन द्वारा लिखित पहला युवा वयस्क पुस्तक है। यह पर्सी जैक्सन और ओलंपियंस श्रृंखला में पहली पुस्तक है। श्रृंखला एक आधुनिक 12 वर्षीय पर्सी जैक्सन नाम के रोमांच के बारे में है, जिसके बाद उन्हें पता चलता है कि वह एक डेमीगोड (हाल्फ-मान, आधे-गॉड) है। पर्सी एक घातक महिला का बेटा है, जिसका नाम सैली और ग्रीक देवता पोसिडोन है। पर्सी और उसके दोस्त ग्रीक देवताओं ज़ीउस, पोसिडोन और हेड्स के बीच युद्ध को रोकने की कोशिश करते हैं।", 'hi'))
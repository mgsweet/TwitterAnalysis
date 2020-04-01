lanCodeList=[
    {"code":"am","lan":"Amharic"},
    {"code":"pt","lan":"Portuguese"},
    {"code":"ar","lan":"Arabic"},
    {"code":"is","lan":"Icelandic"},
    {"code":"ro","lan":"Romanian"},
    {"code":"hy","lan":"Armenian"},
    {"code":"in","lan":"Indonesian"},
    {"code":"ru","lan":"Russian"},
    {"code":"bn","lan":"Bengali"},
    {"code":"it","lan":"Italian"},
    {"code":"sr","lan":"Serbian"},
    {"code":"bg","lan":"Bulgarian"},
    {"code":"ja","lan":"Japanese"},
    {"code":"sd","lan":"Sindhi"},
    {"code":"kn","lan":"Kannada"},
    {"code":"si","lan":"Sinhala"},
    {"code":"zh","lan":"Chinese"},
    {"code":"km","lan":"Khmer"},
    {"code":"sk","lan":"Slovak"},
    {"code":"cs","lan":"Czech"},
    {"code":"ko","lan":"Korean"},
    {"code":"sl","lan":"Slovenian"},
    {"code":"da","lan":"Danish"},
    {"code":"lo","lan":"Lao"},
    {"code":"ckb","lan":"Sorani Kurdish"},
    {"code":"nl","lan":"Dutch"},
    {"code":"lv","lan":"Latvian"},
    {"code":"es","lan":"Spanish"},
    {"code":"en","lan":"English"},
    {"code":"lt","lan":"Lithuanian"},
    {"code":"sv","lan":"Swedish"},
    {"code":"et","lan":"Estonian"},
    {"code":"ml","lan":"Malayalam"},
    {"code":"tl","lan":"Tagalog"},
    {"code":"fi","lan":"Finnish"},
    {"code":"dv","lan":"Maldivian"},
    {"code":"ta","lan":"Tamil"},
    {"code":"fr","lan":"French"},
    {"code":"mr","lan":"Marathi"},
    {"code":"te","lan":"Telugu"},
    {"code":"ka","lan":"Georgian"},
    {"code":"ne","lan":"Nepali"},
    {"code":"th","lan":"Thai"},
    {"code":"de","lan":"German"},
    {"code":"no","lan":"Norwegian"},
    {"code":"bo","lan":"Tibetan"},
    {"code":"el","lan":"Greek"},
    {"code":"or","lan":"Oriya"},
    {"code":"tr","lan":"Turkish"},
    {"code":"gu","lan":"Gujarati"},
    {"code":"pa","lan":"Panjabi"},
    {"code":"uk","lan":"Ukrainian"},
    {"code":"ht","lan":"Haitian"},
    {"code":"ps","lan":"Pashto"},
    {"code":"ur","lan":"Urdu"},
    {"code":"iw","lan":"Hebrew"},
    {"code":"fa","lan":"Persian"},
    {"code":"ug","lan":"Uyghur"},
    {"code":"hi","lan":"Hindi"},
    {"code":"pl","lan":"Polish"},
    {"code":"vi","lan":"Vietnamese"},
    {"code":"cy","lan":"Welsh"},
    {"code":"ab","lan":"Abkhazian"},
    {"code":"om","lan":"Afan"},
    {"code":"aa","lan":"Afar"},
    {"code":"af","lan":"Afrikaans"},
    {"code":"sq","lan":"Albanian"},
    {"code":"as","lan":"Assamese"},
    {"code":"ay","lan":"Aymara"},
    {"code":"az","lan":"Azerbaijani"},
    {"code":"ba","lan":"Bashkir"},
    {"code":"eu","lan":"Basque"},
    {"code":"bn","lan":"Bengali"},
    {"code":"dz","lan":"Bhutani"},
    {"code":"bh","lan":"Bihari"},
    {"code":"bi","lan":"Bislama"},
    {"code":"br","lan":"Breton"},
    {"code":"my","lan":"Burmese"},
    {"code":"be","lan":"Byelorussian"},
    {"code":"km","lan":"Cambodian"},
    {"code":"ca","lan":"Catalan"},
    {"code":"co","lan":"Corsican"},
    {"code":"hr","lan":"Croatian"},
    {"code":"eo","lan":"Esperanto"},
    {"code":"fo","lan":"Faroese"},
    {"code":"fj","lan":"Fiji"},
    {"code":"fy","lan":"Frisian"},
    {"code":"gl","lan":"Galician"},
    {"code":"kl","lan":"Greenlandic"},
    {"code":"gn","lan":"Guarani"},
    {"code":"ha","lan":"Hausa"},
    {"code":"hu","lan":"Hungarian"},
    {"code":"ia","lan":"Interlingua"},
    {"code":"ie","lan":"Interlingue"},
    {"code":"iu","lan":"Inuktitut"},
    {"code":"ik","lan":"Inupiak"},
    {"code":"ga","lan":"Irish"},
    {"code":"jv","lan":"Javanese"},
    {"code":"ks","lan":"Kashmiri"},
    {"code":"kk","lan":"Kazakh"},
    {"code":"rw","lan":"Kinyarwanda"},
    {"code":"ky","lan":"Kirghiz"},
    {"code":"rn","lan":"Kurundi"},
    {"code":"ku","lan":"Kurdish"},
    {"code":"lo","lan":"Laothian"},
    {"code":"la","lan":"Latin"},
    {"code":"lv","lan":"Latvian"},
    {"code":"ln","lan":"Lingala"},
    {"code":"mk","lan":"Macedonian"},
    {"code":"mg","lan":"Malagasy"},
    {"code":"ms","lan":"Malay"},
    {"code":"mt","lan":"Maltese"},
    {"code":"mi","lan":"Maori"},
    {"code":"mo","lan":"Moldavian"},
    {"code":"mn","lan":"Mongolian"},
    {"code":"na","lan":"Nauru"},
    {"code":"oc","lan":"Occitan"},
    {"code":"pa","lan":"Punjabi"},
    {"code":"qu","lan":"Quechua"},
    {"code":"rm","lan":"Rhaeto-romance"},
    {"code":"sm","lan":"Samoan"},
    {"code":"sg","lan":"Sangho"},
    {"code":"sa","lan":"Sanskrit"},
    {"code":"gd","lan":"Scots Gaelic"},
    {"code":"sh","lan":"Serbo-croatian"},
    {"code":"st","lan":"Sesotho"},
    {"code":"tn","lan":"Setswana"},
    {"code":"sn","lan":"Shona"},
    {"code":"si","lan":"Singhalese"},
    {"code":"ss","lan":"Siswati"},
    {"code":"so","lan":"Somali"},
    {"code":"su","lan":"Sundanese"},
    {"code":"sw","lan":"Swahili"},
    {"code":"tg","lan":"Tajik"},
    {"code":"tt","lan":"Tatar"},
    {"code":"ti","lan":"Tigrinya"},
    {"code":"to","lan":"Tonga"},
    {"code":"ts","lan":"Tsonga"},
    {"code":"tk","lan":"Turkmen"},
    {"code":"tw","lan":"Twi"},
    {"code":"ug","lan":"Uigur"},
    {"code":"uz","lan":"Uzbek"},
    {"code":"vo","lan":"Volapuk"},
    {"code":"wo","lan":"Wolof"},
    {"code":"xh","lan":"Xhosa"},
    {"code":"yi","lan":"Yiddish"},
    {"code":"yo","lan":"Yoruba"},
    {"code":"za","lan":"Zhuang"},
    {"code":"zu","lan":"Zulu"},
    {"code":"und","lan":"Undefined"}]


def lanName(s,mylist):
    for i in mylist:
        if (i['code']==s):
            return i['lan']
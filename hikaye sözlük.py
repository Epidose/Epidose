metin = """
Am Himmel tanzen die Vögel fröhlich,
Die Blätter spielen im Wind.
Die Gipfel der Berge sind schneeweiß,
Das Lied der Natur umhüllt mein Herz.

Der Himmel spiegelt sich im Teich, blau und weit,
Die Erde wird von Blumen in grünen Armen gehalten.
Die Leichtigkeit des Windes im Wald spaziert,
Ich verliere mich im Geheimnis der Natur.

Beim Sonnenuntergang beginnt das Farbenspiel,
Orange, Rosa, Lila tanzen am Himmel.
Die unendliche Landschaft vor meinen Augen,
Die Magie der Natur nährt meine Seele.

Der Schatten der Bäume, in den ich eintauche, erfrischt,
Ein weiches Bett auf dem grünen Gras.
In der Stille der Natur finde ich Frieden,
Jeder Moment, jede Berührung erzählt eine Geschichte.

Die Natur ist der Kern des Lebens, der in meinem Herzen widerhallt,
Vom Himmel bis zur Erde, jedes Detail ist verzaubert.
Mit unendlicher Dankbarkeit umarme ich die Natur,
Dieses Sonett ist eine Huldigung an ihre Schönheit.
"""

# Almanca kelimeleri İngilizce anlamlarıyla eşleştirelim
sozluk = {
    "Am": "At the",
    "Himmel": "sky",
    "tanzen": "dance",
    "die": "the",
    "Vögel": "birds",
    "fröhlich": "joyfully",
    "Blätter": "leaves",
    "spielen": "play",
    "im": "in the",
    "Wind": "wind",
    "Gipfel": "summits",
    "der": "the",
    "Berge": "mountains",
    "sind": "are",
    "schneeweiß": "snow-white",
    "Das": "The",
    "Lied": "song",
    "Natur": "nature",
    "umhüllt": "envelops",
    "mein": "my",
    "Herz": "heart",
    "spiegelt": "reflects",
    "sich": "itself",
    "Teich": "pond",
    "blau": "blue",
    "und": "and",
    "weit": "wide",
    "Erde": "earth",
    "wird": "is",
    "von": "by",
    "Blumen": "flowers",
    "in": "in",
    "grünen": "green",
    "Armen": "arms",
    "gehalten": "held",
    "Leichtigkeit": "lightness",
    "des": "of the",
    "Waldes": "forest",
    "spaziert": "strolls",
    "Ich": "I",
    "verliere": "lose",
    "mich": "myself",
    "im": "in the",
    "Geheimnis": "mystery",
    "Sonnenuntergang": "sunset",
    "beginnt": "begins",
    "das": "the",
    "Farbenspiel": "play of colors",
    "Orange": "orange",
    "Rosa": "pink",
    "Lila": "purple",
    "tanzen": "dance",
    "vor": "before",
    "meinen": "my",
    "Augen": "eyes",
    "unendliche": "endless",
    "Landschaft": "landscape",
    "Die": "The",
    "Magie": "magic",
    "der": "of the",
    "Stille": "silence",
    "finde": "find",
    "ich": "I",
    "Frieden": "peace",
    "Jeder": "every",
    "Moment": "moment",
    "jede": "every",
    "Berührung": "touch",
    "erzählt": "tells",
    "eine": "a",
    "Geschichte": "story",
    "Natur": "nature",
    "ist": "is",
    "der": "the",
    "Kern": "core",
    "des": "of the",
    "Lebens": "life",
    "widerhallt": "resounds",
    "Vom": "From",
    "Himmel": "sky",
    "bis": "to",
    "zur": "the",
    "Erde": "earth",
    "jedes": "every",
    "Detail": "detail",
    "ist": "is",
    "verzaubert": "enchanted",
    "Mit": "With",
    "unendlicher": "infinite",
    "Dankbarkeit": "gratitude",
    "umarme": "embrace",
    "ich": "I",
    "die": "the",
    "Natur": "nature",
    "Dieses": "This",
    "Sonett": "sonnet",
    "ist": "is",
    "eine": "a",
    "Huldigung": "tribute",
    "an": "to",
    "ihre": "its",
    "Schönheit": "beauty",
}

# Metni kelimelere ayır
metin_kelimeler = metin.split()

# Kullanıcıdan bir kelime iste
arama_kelimesi = input("Anlamını öğrenmek istediğiniz kelimeyi girin: ")

# Kelimenin sözlükte olup olmadığını kontrol et
if arama_kelimesi in sozluk:
    print(f"{arama_kelimesi} kelimesinin İngilizce anlamı: {sozluk[arama_kelimesi]}")
else:
    print(f"{arama_kelimesi} kelimesi sözlükte bulunamadı.")

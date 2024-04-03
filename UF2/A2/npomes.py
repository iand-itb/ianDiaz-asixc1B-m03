def getAppleSongStanza(applesCount):
    stanza = f"{applesCount} pometes té el pomer,\n" \
             f"de {applesCount} una, de {applesCount} una,\n" \
             f"{applesCount} pometes té el pomer,\n" \
             f"de {applesCount} una en caigué.\n" \
             f"Si mireu el vent d'on vé\n" \
             f"veureu el pomer com dansa,\n" \
             f"si mireu el vent d'on vé\n" \
             f"veureu com dansa el pomer.\n"

    return stanza

def getAppleSong(applesCount):
    if applesCount == 0:
        return 0
    else:
        print(getAppleSongStanza(applesCount))
        return getAppleSong(applesCount - 1)

getAppleSong(995)
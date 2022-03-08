def maganhangzok_torles(s):
    maganhangzok = "aáeéiíoóöőuúüűAÁEÉIÍOÓÖŐUÚÜŰ"
    massalhangzos_s = ""
    for k in s:
        if k not in maganhangzok:
            massalhangzos_s += k
    return massalhangzos_s

print(maganhangzok_torles("informatika") )
print(maganhangzok_torles("aábeéiífoóöoujúüupAÁEÉIÍOÓÖOUÚÜUs"))
e = int("010001", 16)
s = int("7BAFF51CA54182F5A70181B0EC1F8603C1A39324D5A2CB49422886AE1FFDB49E009AF19ABD7D772E199BEC3046690494134B75E1201E6856D99887DCA32DBB403CF99553678D458748AA43C90A387AD3FF767F7314BF05FC1880347072706809BF3BCBDB59EA54032E5485869E7063B3EFDA8C5A6D19D1A5B3B279F2E70AF90B4C2FE485856639273539EEE50B6232EFC9D75903884F315FC377D842F948088F7E259F36BD4FECD1EB770D8FB24CE66E945E57DDE29E3EF1FB327C675940BCEE04A70D18BDC74BDE31CC32894280E2722A19B7D5FE15474E9ED5DCD51C264C7F8FA13A5372698752AB0658D857181435B430D58746FA64BE492E8D3D7D9F33A2", 16) #you get this when you replace *0x6df4e0 with 0x8
m = int("3031300d0609608648016503040201050004207e6bb673f061cfd23cba009e648143fb07ac77dcd1681f6a9af9d5fe7c0f7f4b", 16)
n = int("AE1EC41FDD978C18CB43F9587F9B85DF804603100611497DCB445D157E44E717C78D53FAC3644DEA302645F6CFF852A785C3DAEA525BE01A4B1960D6512D97C677436ED17D03A55DDD8E41D737456C2B1512D533806EB048C5570269CBDFABB5E335821CE69C892A825A3896FC46990A8F6FECC759DAD9D6FD76BBF55BAA34B0789CACE898B6CC8CDBB50A0BFE7073A31DAF0B67845F76B71D42942B03FC02D6D68789C6CEF502C39AA0FB392E5E84BD1581E7295BDF6C45463FEA20A5220413381B82A72F95B1BB29AC6E833B70EB5B9F9D43B4D56A94ECBD02C1CBC8C8EED903485BD2A379A8B81B8FE20216EE6019A5F19656A483CCD9C23EB3B17678050B", 16)
p = int("F5D2772FA3DA0B5AB6A0DEE2897983D6EB0EB9B63A94860EAD14271669C2DDEB089569971093DBBDC46C7E230709FE1BE1967051FB6113F4D836CF792AE3893E487851C500F022E942E2C91FF5BC391E5401F2C41CFE9744AA76048578CC1FEB59B0B705834EE672CE7AE53B06D78831A3701BB58A0746C3B492D8B7DCDDB133", 16)
q = int("B5544FFA117E94D9CA58FF9DB5CBA8E498D4B8192CA578C2D4E1D8828B0329EDE2CA737BBBB3AC25DD11DF04EBE1971D25B0AC3C73D26018A3C52381A520EACEF826ACBA73EBB5EA3569872FEBEC53C6B188FA6DD3B8343C22652C4A5CF2FC34EBCEA888037DBEDA22C55076A15AE1A8827F620AA64A775021851B0BF2808CC9", 16)

# print (s%n)
print ((pow(s, e)-m)%q)
# print (s%q)
# print n%p
# print (n%q)
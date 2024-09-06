#Name:ethan morris
#class: 5th hour
#Assignment: hw4
from pyexpat import features

print('hello world')
albumDict = {
    "artist": "travis scott",
    "album": "utopia",
    "year": "2023",
}
print(albumDict)
print(albumDict["album"])

albumDict["song"] = "I Know?"
print(albumDict)
albumDict.update({"tracklist": 4})
print(albumDict)
albumDictKeys = albumDict.keys()
print(albumDictKeys)
albumDictValues = albumDict.values()
print(albumDictValues)

albumDict.pop("tracklist")
print(albumDict)
albumDict.clear()
print(albumDict)

MusicFriday = {
    "release1": {
        "album": "SoS",
        "year": 2023,
        "features": True,
    },
    "release2": {
        "album": "GEMINI!",
        "year": 2024,
        "features": False,
    }
}
print(MusicFriday["release1"])

print(MusicFriday["release2"]["features"])

print(MusicFriday["release1"]["album"],MusicFriday["release2"]["album"])

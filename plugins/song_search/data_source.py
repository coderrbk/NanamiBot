import requests

key = "https://netease-cloud-music-api-pearl-kappa.vercel.app/"
# 是我自己的key，但是拿去用也没事。
proxies = {"https" : None, "http" : None}
async def get_song(songname: str):
    api = "cloudsearch?keywords="
    query = requests.get("{}{}{}".format(key, api, songname), verify=False, proxies=proxies)
    songdict = query.json()
    if len(songdict["result"]["songs"]):
        for i in range(len(songdict["result"]["songs"])):
            song_url = await get_song_url(songdict["result"]["songs"][i]["id"])
            if song_url!=-1:
                return song_url
    return -1

async def get_song_url(id: int):
    api = "song/url?id="
    print("{}{}{}".format(key, api, id))
    query = requests.get("{}{}{}".format(key, api, id), verify=False, proxies=proxies)
    url = query.json()
    if url["data"][0]["url"]!=None:
        return url["data"][0]["url"]
    else:
        return -1
from mpi4py import MPI
import json

comm = MPI.COMM_WORLD
comm_size = comm.size
comm_rank = comm.rank


def getRankOfHashtagAndLang(filePath):
    hashtagDict = {}
    langDict = {}
    with open(filePath, 'r', encoding='utf-8') as f:
        for index, line in enumerate(f):
            # Different process handle different lines.
            if (index % comm_size != comm_rank):
                continue
            # Skip line not in JSON structure
            try:
                # Line data format may be like '{...},\n' or '{...}}\n'.
                if line[-2] == ',':
                    jsonObj = json.loads(line[: -2])
                else:
                    jsonObj = json.loads(line[: -1])
                # Count hashtag
                hashtagDatas = jsonObj['doc']['entities']['hashtags']
                for hashtagData in hashtagDatas:
                    # Parse hashtag and 
                    hashtag = hashtagData['text'].lower()
                    if hashtag in hashtagDict:
                        hashtagDict[hashtag] += 1
                    else:
                        hashtagDict[hashtag] = 1
                # Count lang
                lang = jsonObj['doc']['lang']
                if lang in langDict:
                    langDict[lang] += 1
                else:
                    langDict[lang] = 1
            except Exception:
                print("Can not read line: ", index)
                continue
    # Gather data to root 0
    hashtagDictArr = comm.gather(hashtagDict, root=0)
    langDictArr = comm.gather(langDict, root=0)
    if comm_rank == 0:
        hashtagRank = _getRankFromDictArr(hashtagDictArr)
        langRank = _getRankFromDictArr(langDictArr)
        _printHashTagRank(hashtagRank, 10)

def _getRankFromDictArr(dictArr):
    rankDict = {}
    for d in dictArr:
        for k, v in d.items():
            if k in rankDict:
                rankDict[k] += v
            else:
                rankDict[k] = v
    rank = sorted(rankDict.items(), key=lambda d: d[1], reverse=True)
    return rank

def _printHashTagRank(hashtagRank, maxRank):
    currentRank = 0
    preCount = -1
    sameCount = 1
    for key, count in hashtagRank:
        if preCount == count:
            sameCount += 1
        else:
            preCount = count
            currentRank += sameCount
            sameCount = 1
        if currentRank > maxRank:
            break
        print(str(currentRank) + '. #' + key + ', ' + str(count))
        
if __name__ == '__main__':
    getRankOfHashtagAndLang('smallTwitter.json')

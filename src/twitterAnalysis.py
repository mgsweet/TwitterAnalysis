from mpi4py import MPI
import platform
import sys
import getopt
import json
from languageCode import getLangName
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

comm = MPI.COMM_WORLD
comm_size = comm.size
comm_rank = comm.rank

def getRankOfHashtagAndLang(filePath):
    """
    Use to analysis the tweet data and get the rank of hashtag and language used.
    """
    hashtagDict = {}
    langDict = {}
    with open(filePath, 'r', encoding='utf-8') as f:
        for index, line in enumerate(f):
            # Different process handle different lines.
            if (index % comm_size != comm_rank):
                continue
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
                # Skip line not in JSON structure
                # print("Can not read line: ", index)
                continue
    # Gather data to root 0
    hashtagDictArr = comm.gather(hashtagDict, root=0)
    langDictArr = comm.gather(langDict, root=0)
    if comm_rank == 0:
        hashtagRank = _getRankFromDictArr(hashtagDictArr)
        langRank = _getRankFromDictArr(langDictArr)
        _printRank("Hashtag Rank: ", hashtagRank, 10, _genHashTagPrint)
        _printRank("Language Rank: ", langRank, 10, _genLangTagPrint)

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

def _genHashTagPrint(rank, key, count):
    return str(rank) + '. #' + key + ', ' + format(count, ',')


def _genLangTagPrint(rank, key, count):
    return str(rank) + '. ' \
        + getLangName(key) \
        + '(' + str(key) + '), ' + format(count, ',')

def _printRank(title, hashtagRank, maxRank, formatGenFunc):
    print("-------------------------------------")
    print(title)
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
        print(formatGenFunc(currentRank, key, count))


if __name__ == '__main__':
    if (sys.version_info[0] < 3):
        if (comm_rank == 0):
            print("Must run in python3, current python version: ",
                  platform.python_version())
    else:
        dataPath = "data/bigTwitter.json"
        try:
            opts, args = getopt.getopt(sys.argv[1:], "hf:", ["help", "file="])
        except getopt.GetoptError:
            if (comm_rank == 0):
                print('twitterAnalysis.py -f <datapath>')
            sys.exit()
        for opt, arg in opts:
            if opt == '-h':
                if (comm_rank == 0):
                    print('twitterAnalysis.py -f <datapath>')
                sys.exit()
            elif opt in ("-f", "--file"):
                dataPath = arg
        if (comm_rank == 0):
            print("Running, use core: ", comm_size)
        getRankOfHashtagAndLang(dataPath)

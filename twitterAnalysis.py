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
                    hashtag = hashtagData['text']
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
    print("Process: ", comm_rank, ' : ')
    print("hashtagDict: \n", hashtagDict)
    print("langDict: \n", langDict)


if __name__ == '__main__':
    getRankOfHashtagAndLang('tinyTwitter.json')

#Count_Hamlet_Voca.py

def replacePunctuations(line):
    for ch in line:
        if ch in "~@#$%^&*()_-+=<>?/,.:;{}[]|\'""":
            line = line.replace(ch, " ")
        return line

def processLine(line, wordCount):
    #用空格代替标点
    line = replacePunctuations(line)
    #从每行获取单词，已存在+1，不存在创建
    for word in line.split():
        wordCount[word] = wordCount.get(word,0) + 1

def main():
    file = open(input("Input the filename:").strip(), "r")

    #建立空字典
    wordCount = {}
    for line in file:
        processLine(line.lower(), wordCount)

    #获取数据对
    pairs = list(wordCount.items())
    #等同于items.sort(key=lambda x:x[1], reverse=True)且不用颠倒键值
    items = [[x,y] for (y,x) in pairs]
    items.sort()

    #输出结果，TOP10
    for i in range(len(items)-1, len(items)-10-1, -1):
        print(items[i][1]+"\t"+str(items[i][0]))

    file.close()

if __name__ == '__main__':
    main()

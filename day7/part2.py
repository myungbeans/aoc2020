def getAllRules(filename):
    file = open(filename, 'r')
    rules = file.read().split('\n')[0:-1]  # last line is \n\n

    rulesDict = {}

    for rule in rules:
        parentAndChild = rule.split(' contain ')
        outerbag = parentAndChild[0].replace(' bags', '')
        innerbags = parentAndChild[1].replace(' bags', '').replace(' bag', '')[0:-1].split(', ')  # [0:-1] to remove the '.' at the end of the sentence
        rulesDict[outerbag] = {}
        for inner in innerbags:
            if inner != 'no other':
                numAndBag = inner.split(' ', 1)
                num = int(numAndBag[0])
                bag = numAndBag[1]
                rulesDict[outerbag][bag] = num

    return rulesDict


class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

    def insert(self, data):
        newNode = Node(data)
        self.children.append(newNode)
        return newNode

    def treeToStr(self, level=0):
        print ('\t'*level + repr(self.data))
        for child in self.children:
            child.treeToStr(level+1)


def buildTreeFromRules(currentNode, allRules):
    if currentNode.data in allRules:
        for child in allRules[currentNode.data]:
            childNode = currentNode.insert(child)
            buildTreeFromRules(childNode, allRules)


def getAllPathsToGold(node, path=None):
    allPaths = []

    if path is None:
        path = []

    path.append(node.data)

    if node.data == 'shiny gold' and len(path) > 1:
        allPaths.append(path)
        return allPaths

    if node.children:
        for child in node.children:
            allPaths.extend(getAllPathsToGold(child, path[:]))

    return allPaths


def main():
    allRules = getAllRules('test.txt')
    allPathsToGold = []
    # build all trees
    for outerbag in allRules:
        root = Node(outerbag)
        buildTreeFromRules(root, allRules)
        root.treeToStr()
        pathsToGoldFromThisRoot = getAllPathsToGold(root)
        if len(pathsToGoldFromThisRoot) > 0:
            allPathsToGold.append(outerbag)

    return len(allPathsToGold)


if __name__ == "__main__":
    print(main())

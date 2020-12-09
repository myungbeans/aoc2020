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
    instances = []

    def __init__(self, data):
        self.data = data
        self.children = []
        Node.instances.append(self)

    def insert(self, data):
        newNode = Node(data)
        self.children.append(newNode)
        return newNode

    def treeToStr(self, level=0):
        print ('\t'*level + repr(self.data))
        for child in self.children:
            child.treeToStr(level+1)


def buildAllNodesFromRules(currentNode, allRules):
    if currentNode.data in allRules:
        for child in allRules[currentNode.data]:
            for x in range(allRules[currentNode.data][child]):
                childNode = currentNode.insert(child)
                buildAllNodesFromRules(childNode, allRules)


def getAllPaths(currentNode, path=None):
    allPaths = []

    if path is None:
        path = []

    path.append(currentNode.data)

    if currentNode.children:
        for child in currentNode.children:
            allPaths.extend(getAllPaths(child, path[:]))
    else:
        allPaths.append(path)
    return allPaths


def main():
    allRules = getAllRules('input.txt')

    # build gold tree
    root = Node('shiny gold')
    buildAllNodesFromRules(root, allRules)
    root.treeToStr()

    return len(Node.instances) - 1


if __name__ == "__main__":
    print(main())

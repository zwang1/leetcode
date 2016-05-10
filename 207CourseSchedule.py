__author__ = 'zhengyiwang'
import Queue

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        #find a loop
        coursemap = {}
        for first, second  in prerequisites:
            if first not in coursemap:
                coursemap[first] = [second]
            else:
                coursemap[first].append(second)

        finished = set()
        for i in range(numCourses):
            if self.findloop(finished,coursemap, [], i):
                return False
        return True

    def findloop(self, finished, coursemap, path, c):
        if c in finished:
            return False
        if c in path:
            return True
        loop = False
        if c in coursemap:
            for othercourse in coursemap[c]:
                loop = loop or self.findloop(finished, coursemap, path + [c], othercourse)
        finished.add(c)
        return loop
class Solution2(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        inedge = [0] * numCourses
        coursemap = {}
        for first, second  in prerequisites:
            if first not in coursemap:
                coursemap[first] = [second]
            else:
                coursemap[first].append(second)

            inedge[second] += 1
        updated = True
        while updated:

            updated = False
            for c in range(len(inedge)):
                if inedge[c] == 0:
                    updated = True
                    inedge[c] -= 1
                    if c not in coursemap:
                        continue
                    for othercourse in coursemap[c]:
                        inedge[othercourse] -= 1
        for ine in inedge:
            if ine > 0:
                return False
        return True

class Solution3(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        inedge = [0] * numCourses
        coursemap = {}
        queue = Queue.Queue()

        for first, second  in prerequisites:
            if first not in coursemap:
                coursemap[first] = [second]
            else:
                coursemap[first].append(second)

            inedge[second] += 1
        updated = True
        for i in range(len(inedge)):
            if inedge[i] == 0:
                queue.put(i)

        while len(queue) > 0:
            c = queue.get()
            if c not in coursemap:
                continue
            for othercourse in coursemap[c]:
                inedge[othercourse] -= 1
                if inedge[othercourse] == 0:
                    queue.put(othercourse)
        for ine in inedge:
            if ine > 0:
                return False
        return True

if __name__ == "__main__":
    s= Solution3()
    print s.canFinish(2, [[0,1]])

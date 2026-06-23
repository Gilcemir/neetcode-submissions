# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        rootList = [root] if root else []
        q = deque(rootList)
        res = []

        while q:
            size = len(q)
            for i in range(size):
                node = q.popleft()
                v = str(node.val) if node else "n"
                res.append(v)

                if node:
                    q.append(node.left)
                    q.append(node.right)
        
        return ','.join(res).strip(',n')
        

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        data_q = deque([x for x in data.split(',')]) # use popleft
        
        node = TreeNode(data_q.popleft())
        q = deque([node])

        while q:
            size = len(q)
            for i in range(size):
                curr = q.popleft()

                if data_q:
                    v = data_q.popleft()
                    if v != "n":
                        l_node = TreeNode(v)
                        curr.left = l_node
                        q.append(l_node)
                
                if data_q:
                    v = data_q.popleft()
                    if v != "n":
                        r_node = TreeNode(v)
                        curr.right = r_node
                        q.append(r_node)


        return node


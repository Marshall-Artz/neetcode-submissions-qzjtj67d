class Solution:

    def __init__(self):
        self.folders = {}
    
    def insert(self, path: str) -> None:
        paths = path.split("/")[1:]

        curPath = self.folders
        for folder in paths:
            if folder not in curPath:
                curPath[folder] = {}
            curPath = curPath[folder]
    
    def remove(self, path: str) -> None:
        paths = path.split("/")[1:]

        # Go to path
        curPath = self.folders
        for path in paths:
            if path not in curPath:
                return
            
            curPath = curPath[path]
        
        # Empty folder of subfolders
        curPath.clear()
    
    def get(self) -> List[str]:
        res = []

        sub = []
        def dfs(cur: dict) -> None:
            if not cur:
                res.append("".join(sub.copy()))
                return
            
            for folder in cur.keys():
                sub.append("/" + folder)
                dfs(cur[folder])
                sub.pop()
        
        dfs(self.folders)
        return res

    def removeSubfolders(self, folders: List[str]) -> List[str]:
        # Insert all folders:
        for folder in folders:
            self.insert(folder)
        
        # Remove subfolders
        for folder in folders:
            self.remove(folder)

        # Get folder list
        return self.get()
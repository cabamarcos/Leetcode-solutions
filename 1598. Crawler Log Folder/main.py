class Solution(object):
    def minOperations(self, logs):
        folders = []
        for log in logs:
            if log == "../":
                if folders:
                    folders.pop()
            elif log != "./":
                folders.append(log)
        
        return len(folders)

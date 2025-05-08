class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        t = [(tasks[i][0], tasks[i][1], i) for i in range(n)]
        t.sort()
        
        res = []
        pq = []
        curr_time = 0
        idx = 0
        
        while len(res) < n:
            while idx < n and t[idx][0] <= curr_time:
                heapq.heappush(pq, (t[idx][1], t[idx][2]))
                idx += 1
            
            if pq:
                proc_time, task_idx = heapq.heappop(pq)
                res.append(task_idx)
                curr_time += proc_time
            else:
                if idx < n:
                    curr_time = t[idx][0]
        
        return res
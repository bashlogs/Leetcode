class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        userStatus = [0] * numberOfUsers
        userTime = [0] * numberOfUsers
        curr_time = 0
        count = 0

        events = sorted(events, key = lambda x: (int(x[1]), 0 if x[0] == "OFFLINE" else 1))

        for event, time, mentions in events:
            time = int(time)

            if event == "MESSAGE":
                curr_time = time
                if mentions == "HERE":
                    for i in range(numberOfUsers):
                        if userTime[i] <= time:
                            userStatus[i] += 1
                elif mentions == "ALL":
                    count += 1
                else:
                    for mention in mentions.split(" "):
                        ids = int(mention[2:])
                        userStatus[ids] += 1

            if event == "OFFLINE":
                userTime[int(mentions)] = time + 60

        for i in range(numberOfUsers):
            userStatus[i] += count

        return userStatus
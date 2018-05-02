#16.10 Living People
def livingPeople(people):
    births = [person.birth for person in people]
    deaths = [person.death + 1 for person in people]

    births.sort(reverse = True)
    deaths.sort(reverse = True)

    cnt = 0
    maxPeople = 0
    res = 0
    for year in xrange(births[-1], births[0] - 1, -1):
        #cal birth
        while year == births[-1]:
            cnt += 1
        while year == deaths[-1]:
            cnt -= 1
        if cnt > maxPeople:
            res = year
            maxPeople = cnt
    return res

class NonPositiveError(Exception):
    pass

class PositiveList(list):
    def append(self, number):
        if number > 0:
            super(PositiveList, self).append(number)
        else: 
            raise NonPositiveError


k = PositiveList()
for i in range(5):
    try:
        k.append(int(input()))
    except NonPositiveError:
        pass

print(k)


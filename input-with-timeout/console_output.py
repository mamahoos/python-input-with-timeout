import sys, typing


CR = '\r'
LF = '\n'


class Endl(object):
    pass

class Cout(object):
    def __lshift__(self, other: typing.Any) -> typing.Self:
        sys.stdout.write(CR + LF if isinstance(other, Endl) else str(other))
        sys.stdout.flush()
        return self
    
cout = Cout()
endl = Endl()

# ------ #

if __name__ == "__main__":
    cout << "Hello, World!" << endl

import re


class IPv7:
    hypernet_pattern = re.compile(r"\[([^]]*)\]")

    def __init__(self, addr):
        self.hypernet = self.hypernet_pattern.findall(addr)
        for s in self.hypernet:
            addr = addr.replace(s, " ")
        self.regular = addr.split()

    @property
    def tls(self):
        def abba(s):
            for i in range(len(s)-3):
                a, b, c, d = s[i:i+4]
                if a == d and b == c and a != b:
                    return True
            return False

        return any(map(abba, self.regular)) and not any(map(abba, self.hypernet))

    @property
    def ssl(self):
        def aba(s):
            for i in range(len(s)-2):
                a, b, c = s[i:i+3]
                if a == c and a != b and any(b + a + b in s for s in self.hypernet):
                    return True
            return False

        return any(map(aba, self.regular))


def part1(ips):
    return sum(ip.tls for ip in ips)


def part2(ips):
    return sum(ip.ssl for ip in ips)


def main(inputs):
    print("Day 07")
    ips = list(map(IPv7, inputs))
    A = part1(ips)
    print(f"{A=}")
    B = part2(ips)
    print(f"{B=}")

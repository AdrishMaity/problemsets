'''
Random Teams

time limit per test: 1 second
memory limit per test: 256 megabytes
input: standard input
output: standard output

n participants of the competition were split into m teams in some manner so that each team has at least one participant.
After the competition each pair of participants from the same team became friends.

Your task is to write a program that will find the minimum and the maximum number of pairs of friends
that could have formed by the end of the competition.

Input
The only line of input contains two integers n and m,
separated by a single space (1 ≤ m ≤ n ≤ 109) — the number of participants and the number of teams respectively.

Output
The only line of the output should contain two integers kmin and kmax
— the minimum possible number of pairs of friends and the maximum possible number of pairs of friends respectively.


Link: http://codeforces.com/problemset/problem/478/B

'''
import math

def nC2(n):
        return (n * (n-1) //2)


def main():

    n, m = map(int, input().split(' '))

    # minimum possible number of pairs
    # x = n //m , y = n%m, total = (m - y) * nC2(x) + y * nC2(x+1)

    x = n // m
    y = n % m

    minimumPossibleNumPairs = (m - y) * nC2(x) + y * nC2(x+1)

    # maximum possible number of pairs
    # (n - m + 1)c2

    maximumPossibleNumPairs = nC2(n - m + 1)

    print(minimumPossibleNumPairs, maximumPossibleNumPairs)


if __name__ == "__main__":
    main()

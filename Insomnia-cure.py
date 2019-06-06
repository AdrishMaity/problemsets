'''
Insomnia cure

time limit per test: 2 seconds
memory limit per test: 256 megabytes
input: standard input
output: standard output

«One dragon. Two dragon. Three dragon», — the princess was counting.
She had trouble falling asleep, and she got bored of counting lambs when she was nine.

However, just counting dragons was boring as well, so she entertained herself at best she could.
Tonight she imagined that all dragons were here to steal her, and she was fighting them off.
Every k-th dragon got punched in the face with a frying pan. Every l-th dragon got his tail shut into the balcony door.
Every m-th dragon got his paws trampled with sharp heels.
Finally, she threatened every n-th dragon to call her mom, and he withdrew in panic.

How many imaginary dragons suffered moral or physical damage tonight, if the princess counted a total of d dragons?

Input
Input data contains integer numbers k, l, m, n and d,
each number in a separate line (1 ≤ k, l, m, n ≤ 10, 1 ≤ d ≤ 105).

Output
Output the number of damaged dragons.

link: http://codeforces.com/problemset/problem/148/A

'''

def main():
    k = int(input()) # every kth physical damage
    l = int(input()) # every lth physical damage
    m = int(input()) # every mth physical damage
    n = int(input()) # every nth mental damage
    d = int(input()) # total dragons

    damageCount = 0

    for curDragon in range(1,d+1):
        #print('current status ',curDragon,': ' , curDragon % k, curDragon % l, curDragon % m)

        if curDragon % k == 0 or curDragon % l == 0 or curDragon % m == 0 or curDragon % n == 0:
            damageCount += 1

    print(damageCount)


if __name__=="__main__":
    main()

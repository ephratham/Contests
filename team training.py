import sys
input = sys.stdin.readline

def main():
    t = int(input())
    results = []

    for _ in range(t):
        n, x = map(int, input().split())
        a = list(map(int, input().split()))
        a.sort(reverse=True)

        count = 0
        team_size = 0

        for skill in a:
            team_size += 1
            if skill * team_size >= x:
                count += 1
                team_size = 0

        results.append(str(count))

    print('\n'.join(results))

if __name__ == "__main__":
    main()

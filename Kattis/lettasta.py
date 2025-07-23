num_problems = int(input())
num_teams = int(input())
problem_names = input().split()
total_scores = [0] * num_problems

for _ in range(num_teams):
    scores = list(map(int, input().split()))
    for i in range(num_problems):
        total_scores[i] += scores[i]

max_index = total_scores.index(max(total_scores))
print(problem_names[max_index])

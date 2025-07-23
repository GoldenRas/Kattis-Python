from collections import defaultdict

def main():
    n = int(input())
    course_combinations = defaultdict(int)
    
    for _ in range(n):
        courses = tuple(sorted(map(int, input().split())))
        course_combinations[courses] += 1
    
    max_popularity = max(course_combinations.values())
    most_popular_count = sum(count for count in course_combinations.values() if count == max_popularity)
    
    print(most_popular_count)

if __name__ == "__main__":
    main()

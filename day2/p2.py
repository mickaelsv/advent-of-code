# not my version

def is_safe_report(report):
    values = list(map(int, report.split()))

    def is_safe(values):
        increasing = all(
            values[i] < values[i + 1] and 1 <= values[i + 1] - values[i] <= 3
            for i in range(len(values) - 1)
        )
        decreasing = all(
            values[i] > values[i + 1] and 1 <= values[i] - values[i + 1] <= 3
            for i in range(len(values) - 1)
        )
        return increasing or decreasing

    if is_safe(values):
        return True

    return any(is_safe(values[:i] + values[i + 1 :]) for i in range(len(values)))


def count_safe_reports(reports):
    return sum(1 for report in reports if is_safe_report(report))


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        reports = f.readlines()
    safe_count = count_safe_reports(reports)
    print(f"Number of safe reports: {safe_count}")
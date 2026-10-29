def attendance_percentage(attended, total_classes):
    if total_classes <= 0: raise ValueError("Total classes must be positive.")
    return attended / total_classes * 100

def is_eligible(percent):
    return percent >= 75

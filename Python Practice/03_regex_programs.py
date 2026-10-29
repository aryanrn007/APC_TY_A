# APL Practical Programs: Regular Expressions (Regex)
import re

# 11. Validate email
email = input("Enter email: ")
pattern = r"[\\w.-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,6}"
print("Valid Email" if re.fullmatch(pattern, email) else "Invalid Email")

# 12. Extract 10-digit phone numbers
text = input("Enter text: ")
print(re.findall(r"\\b\\d{10}\\b", text))

# 13. Extract URLs
text = input("Enter text: ")
print(re.findall(r"https?://\\S+|www\\.\\S+", text))

# 14. Password strength checker
password = input("Enter password: ")
pattern = r"(?=.*[A-Z])(?=.*[a-z])(?=.*\\d)(?=.*[!@#$%^&*()_-]).{8,}"
print("Strong Password" if re.fullmatch(pattern, password) else "Weak Password")

# 15. Extract dates in DD/MM/YYYY format
text = input("Enter text: ")
print(re.findall(r"\\b\\d{2}/\\d{2}/\\d{4}\\b", text))

# 16. Remove HTML tags
text = input("Enter HTML: ")
print(re.sub(r"<[^>]*>", "", text))

# 17. Extract hashtags
text = input("Enter post: ")
print(re.findall(r"#\\w+", text))

# 18. Count file extensions
files = ["a.txt", "b.pdf", "c.txt", "d.png"]
frequency = {}
for filename in files:
    match = re.findall(r"\\.[^.]+$", filename)
    if match:
        ext = match[0]
        frequency[ext] = frequency.get(ext, 0) + 1
print(frequency)

# 19. Validate IPv4 address
ip = input("Enter IPv4 address: ")
pattern = r"(?:\\d{1,3}\\.){3}\\d{1,3}"
valid = bool(re.fullmatch(pattern, ip)) and all(0 <= int(part) <= 255 for part in ip.split("."))
print("Valid IP" if valid else "Invalid IP")

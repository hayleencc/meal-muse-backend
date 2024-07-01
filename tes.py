import sys

# Remove duplicates while preserving order
sys.path = list(dict.fromkeys(sys.path))

print(sys.path)

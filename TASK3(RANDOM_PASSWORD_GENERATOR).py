import random
import string
import secrets
def generate_password(length, low, medium, high, very_high):
# generates a random password of the specified length and complexity.
  characters = ""
  if low:
    characters += string.ascii_lowercase
  if medium:
    characters += string.ascii_letters
  if high:
    characters += string.digits + string.ascii_letters
  if very_high:
    characters += string.punctuation + string.ascii_letters + string.digits
  if not characters:
    print("Please select at least one character type.")
    return

  password = ''.join(secrets.choice(characters) for _ in range(length))
  return password


def main():
  # Get user input for password length and complexity
  while True:
    length = int(input("Enter password length (min 6): "))
    if length >= 6:
      break
    print("Password length must be at least 8 characters.")

  complexity = input("Choose complexity (low, medium, high, very_high): ")
  low = 'low' in complexity
  medium = 'medium' in complexity
  high = 'high' in complexity
  very_high = 'very_high' in complexity

  # Generate and display password
  password = generate_password(length, low, medium, high, very_high)
  print("Generated password:", password)


if __name__ == "__main__":
  main()
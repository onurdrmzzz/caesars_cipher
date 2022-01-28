from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == 'decode':
      shift_amount *= -1
  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = (position + shift_amount)%26
      end_text += alphabet[new_position]
    else:
      end_text += char 
  print(f"The {cipher_direction}d text is {end_text}")

print(logo)

answer = True
while answer:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  caesar(text, shift, direction)
  question = input("Type 'yes' if you want to go again. Otherwise type 'no' \n")
  if question == 'no':
    answer = False

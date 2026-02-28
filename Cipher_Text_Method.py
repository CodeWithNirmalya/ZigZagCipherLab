class RailFence:

    def __init__(self):
        self.rail_count = int(input("How many rails you want: "))
        self.text = input("Enter the sentence: ").replace(" ", "")

    # ---------------- ENCRYPTION ----------------
    def encrypt(self):
        rails = [""] * self.rail_count
        current_rail = 0
        direction = 1

        for char in self.text:
            rails[current_rail] += char

            if current_rail == 0:
                direction = 1
            elif current_rail == self.rail_count - 1:
                direction = -1

            current_rail += direction

        cipher = "".join(rails)
        print("Cipher Text:", cipher)
        return cipher


    # ---------------- DECRYPTION ----------------
    def decrypt(self, cipher):
        # Step 1: Create empty matrix
        pattern = [[None for _ in range(len(cipher))]
                   for _ in range(self.rail_count)]

        # Step 2: Mark zigzag positions with '*'
        current_rail = 0
        direction = 1

        for col in range(len(cipher)):
            pattern[current_rail][col] = "*"

            if current_rail == 0:
                direction = 1
            elif current_rail == self.rail_count - 1:
                direction = -1

            current_rail += direction

        # Step 3: Fill marked positions with cipher letters
        index = 0
        for r in range(self.rail_count):
            for c in range(len(cipher)):
                if pattern[r][c] == "*" and index < len(cipher):
                    pattern[r][c] = cipher[index]
                    index += 1

        # Step 4: Read zigzag to reconstruct original
        result = ""
        current_rail = 0
        direction = 1

        for col in range(len(cipher)):
            result += pattern[current_rail][col]

            if current_rail == 0:
                direction = 1
            elif current_rail == self.rail_count - 1:
                direction = -1

            current_rail += direction

        print("Decrypted Text:", result)


# ---------------- RUN ----------------
rf = RailFence()

cipher_text = rf.encrypt()
rf.decrypt(cipher_text)
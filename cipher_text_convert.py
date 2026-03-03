class RailFence:
    """Rail Fence transposition cipher — encrypt and decrypt."""

    def __init__(self, rails: int):
        if rails < 2:
            raise ValueError("Rail count must be at least 2.")
        self.rails = rails

    def _zigzag(self, length: int):
        """Generator yielding (rail_index) for each position."""
        rail, direction = 0, 1
        for _ in range(length):
            yield rail
            if rail == 0:
                direction = 1
            elif rail == self.rails - 1:
                direction = -1
            rail += direction

    def encrypt(self, plaintext: str) -> str:
        if self.rails >= len(plaintext):
            return plaintext
        fence = [""] * self.rails
        for char, rail in zip(plaintext, self._zigzag(len(plaintext))):
            fence[rail] += char
        return "".join(fence)

    def decrypt(self, ciphertext: str) -> str:
        n = len(ciphertext)
        if self.rails >= n:
            return ciphertext
        # Map each position to its rail
        pattern = list(self._zigzag(n))
        # Sort positions by rail to find reading order
        indices = sorted(range(n), key=lambda i: pattern[i])
        # Place each cipher character back in its original position
        result = [""] * n
        for pos, idx in enumerate(indices):
            result[idx] = ciphertext[pos]
        return "".join(result)

    def visualize(self, text: str) -> str:
        """Returns an ASCII art fence diagram."""
        n = len(text)
        grid = [["·"] * n for _ in range(self.rails)]
        for col, rail in zip(range(n), self._zigzag(n)):
            grid[rail][col] = text[col]
        rows = []
        for i, row in enumerate(grid):
            rows.append(f"Rail {i+1}: " + " ".join(row))
        return "\n".join(rows)


# ── CLI demo ──
if __name__ == "__main__":
    rails = int(input("Number of rails: "))
    cipher = RailFence(rails)

    print("\n[1] Encrypt  [2] Decrypt")
    choice = input("Choose: ").strip()

    if choice == "1":
        text = input("Plaintext: ")
        enc = cipher.encrypt(text)
        print(f"\nCiphertext : {enc}")
        print(f"\n{cipher.visualize(text)}")
    elif choice == "2":
        text = input("Ciphertext: ")
        dec = cipher.decrypt(text)
        print(f"\nPlaintext  : {dec}")
    else:
        print("Invalid choice.")
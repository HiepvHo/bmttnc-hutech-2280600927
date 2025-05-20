class TranspositionCipher:
    def __init__(self):
        pass

    def encrypt(self, text, key):
        encrypted_text = ''
        for col in range(key):
            pointer = col
            while pointer < len(text):
                encrypted_text += text[pointer]
                pointer += key
        return encrypted_text

    def decrypt(self, text, key):
        num_rows = (len(text) + key - 1) // key  # TINH SO HANG DUNG
        matrix = [[''] * key for _ in range(num_rows)]  # TAOMATRANAOMATRAN
        
        pos = 0
        for col in range(key):
            current_row = 0
            while current_row < num_rows and pos < len(text):
                # KIEM TRA COT DU KY TU KHONGKHONG
                if current_row == num_rows - 1 and col >= len(text) % key and len(text) % key != 0:
                    break
                matrix[current_row][col] = text[pos]
                current_row += 1
                pos += 1

        decrypted_text = ''
        for row in range(num_rows):
            for col in range(key):
                if matrix[row][col]:
                    decrypted_text += matrix[row][col]
        return decrypted_text

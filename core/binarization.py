class binarization:
    def __init__(self):
        self.entry = ""

    def binarize(self, entry: str) -> str:
        self.entry = entry
        return ''.join(format(b, '08b') for b in entry.encode('utf-8'))
    
    def debinarize(self, binary_str: str) -> str:
        try:
            bytes_list = [int(binary_str[i:i+8], 2) for i in range(0, len(binary_str), 8)]
            return bytes(bytes_list).decode('utf-8')
        except Exception:
            return ""

if __name__ == "__main__":
    txt = "hellow world"
    binarizer = binarization()
    binary_txt = binarizer.binarize(txt)
    print("Binary:", binary_txt)
    decoded = binarizer.debinarize(binary_txt)
    print("Decoded:", decoded)
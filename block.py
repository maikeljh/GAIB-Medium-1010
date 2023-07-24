class Block:
    def __init__(self, block, color, score):
        self.block = block
        self.color = color
        self.score = score
    
    def __len__(self):
        return len(self.block)

    def __getitem__(self, index):
        return self.block[index]
import numpy as np

import matplotlib.pyplot as plt
 
bit = "11010000110010101101100011011000110111101110111001000000111011101101111011100100110110001100100"

def plot_bit_sequence(bit_sequence):

    # Plotar apenas os últimos 20 bits
    bit_sequence = bit_sequence[-20:] if len(bit_sequence) > 20 else bit_sequence

    # adicionar uma linha reta para 0 um salto de linha para 1
    y = [1 if bit == '1' else 0 for bit in bit_sequence]
    x = np.arange(len(y))
    plt.plot(x, y, marker='o', linestyle='-')
    plt.ylim(-0.5, 1.5)
    plt.yticks([0, 1], ['0', '1'])
    plt.xlabel('Bit Position')
    plt.title('Bit Sequence Plot (Últimos 20 bits)')
    plt.grid()
    plt.savefig('bit_sequence_plot.png')
    # plt.show()

if __name__ == "__main__":
    plot_bit_sequence(bit)
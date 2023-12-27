import matplotlib.pyplot as plt

def plot_data(data):
    plt.figure(figsize=(10,5))
    plt.hist(data)
    plt.show()

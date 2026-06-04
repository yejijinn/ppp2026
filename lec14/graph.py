import matplotlib.pyplot as plt
import numpy as np
#import koreanize_matplotlib


def main():
    fig, ax = plt.subplots(figsize=(15, 6))
    
    year = [str(x+2001) for x in range(20)]
    rain = np.random.rand(20) * 200 + 1000

    ax.bar(year, rain, color="b")

    ax.set_ylabel("연평균강우량(mm)")

    fig.savefig("./bar_rain.png")

    plt.show()

if __name__ == "__main__":
    main()
from base64 import b64encode
from io import BytesIO

import matplotlib.pyplot as plt
import seaborn as sns

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = b64encode(image_png)
    graph = graph.decode("utf-8")
    buffer.close()
    return graph

def get_chart(data):
    plt.switch_backend("AGG")
    fig = plt.figure(figsize=(10, 4))
    sns.barplot(data=data, order=["rotten_tomatoes", "metacritic", "imdb", "fandango"])
    plt.tight_layout()
    chart = get_graph()
    return chart
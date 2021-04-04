import pandas as pd

df = {
    'id' : [0, 1],
    'meaning' : ['block', 'space'],
    'color' : [[0, 0, 0], [255, 255, 255]]
}

mapping = pd.DataFrame(data = df)

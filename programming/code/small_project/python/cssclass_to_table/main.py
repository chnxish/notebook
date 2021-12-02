import numpy as np
import plotly.graph_objects as go

""" Input:
.p-0{padding:0!important}.p-1{padding:.25rem!important}.p-2{padding:.5rem!important}
"""
""" Output:
| Class |          Content         |
| .p-0  | padding:0!important      |
| .p-1  | padding:.25rem!important |
| .p-2  | padding:.5rem!important  |
"""
def main():
    print('Enter data:', end='')
    data = input()

    rows = data.split('}')
    
    vs = []
    for r in rows:
        x = r.split('{')
        vs.append(x)
    vs.pop()

    vs = np.array(vs)
    vs = vs.transpose()


    fig = go.Figure(data=[go.Table(
        columnorder = [1, 2],
        columnwidth = [80, 400],
        header = dict(
            values=['Class', 'Content'],
            line_color='darkslategray',
            fill_color='royalblue',
            align=['left', 'center'],
            font=dict(color='white', size=12),
        ),
        cells = dict(
            values=vs,
            line_color='darkslategray',
            fill=dict(color=['paleturquoise', 'white']),
            align=['left', 'center'],
            font_size=12,
            height=30
        )
    )])

    fig.show()

if __name__ == '__main__':
    main()

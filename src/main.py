from .plot import generate_graphs as g
import pandas as pd

if __name__ == "__main__":
    CSV_PATH = "data/csv_files/mockup/respostas_questionario.csv"
    
    df = pd.read_csv(CSV_PATH)

    try:
        print("\nGENERATING THE GRAPHS:\n")
        g.generate_graph_1(df)
        print("graph1 is OK")
        g.generate_graph_2(df)
        print("graph2 is OK")
        g.generate_graph_3(df)
        print("graph3 is OK")
        g.generate_graph_4(df)
        print("graph4 is OK")
        g.generate_graph_5(df)
        print("graph5 is OK")
        g.generate_graph_6(df)
        print("graph6 is OK")
    except:
        print("Something got wrong...")

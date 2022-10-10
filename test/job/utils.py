import pandas as pd

# load text files into a dataframe
def read_file_text(name, sep=',', source=None):
    df = pd.read_csv(name, sep=sep)
    if source is not None:
        df["__source__"] = source  

    return df

# save dataframe to text
def save_file_text(df, name, index=False):
    df.to_csv(name, index=index)

# unify data frames
def unify_data(files):
    df = pd.concat( [read_file_text(f["file"], f["sep"], f["source"]) for f in files], ignore_index=True )
    
    return df
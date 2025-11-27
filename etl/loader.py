def load(df, out_path):
    df.to_csv(out_path, index=False)
    return out_path

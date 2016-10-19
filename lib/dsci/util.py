import inflection


def clean_column(col):
    col = col.replace(' ', '_')
    return inflection.underscore(col)


def clean_columns(df):
    df.columns = df.columns.map(clean_column)
    return df

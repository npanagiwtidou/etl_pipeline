def identify_remove_duplicates(df):
    if df.duplicated().sum() > 0:
        print("The number of duplicated data is:", df.duplicated().sum())
        df_cleaned = df.drop_duplicates(keep='first')
        print('Shape of data before removing duplicated rows', df.shape)
        print('Shape of data after removing duplicated rows', df_cleaned.shape)
    else:
        print('No duplicated data found')
        df_cleaned = df

    return df_cleaned
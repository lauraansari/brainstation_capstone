def extract:

extracted_df = []

extracted_df = data_df[
    (data_df['County']=='Los Angeles') &
    (data_df['dt'].dt.year >= 1980)]

return extracted_df


# def merging:

# temperature_df = pd.read_csv('data/temperature.csv')

# cities_temp_df.rename(columns={'dt': 'Date'}, inplace=True)
# cities_temp_df = cities_temp_df.set_index('Date')
# combined_df = pd.merge(cities_aqi_df, cities_temp_df, how='right', on='Date')
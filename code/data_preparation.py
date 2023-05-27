"""
## DATA CLEANING MODULE
Data source: https://www.kaggle.com/datasets/khsamaha/aviation-accident-database-synopses

This module cleans the data in preperation for analysis

"""
import pandas as pd

# Create a custom mapping function for airplane models based on reserached model patterns
def model_cleaning_function(model):
    model = str(model)
    if model.startswith('1') or model.startswith('2'):
         model = model[:3]
    elif any(map(model.startswith, ['PA','A','DA','G','SR','C','L'])):
        model = model[:4]
    elif model.startswith('HAWKER'):
         model = 'HAWKER'
    else: 
        model = model
    return model

def private_or_commercial(make):
    private = ['Beech', 'Cessna', 'Cirrus', 'Piper', 'Diamond']
    commercial = ['Lockheed', 'Airbus', 'Grumman', 'Raytheon', 'Boeing']
    if make in private:
        return 'Private Enterprise'
    elif make in commercial:
        return 'Commercial'
    else:
        return 'Unknown'
    
def commercial_model_cleaning_function(model):
    top_commercial_models_list = ['A330', '747', '777', '727', 'CRJ', 'A320', '747', '737', 'DC3']
    model = str(model)
    for top_model in top_commercial_models_list:
        if model.startswith(top_model):
            return top_model
            break
        else:
            return model

def cleaning_aviation_data(aviation_raw):
    """Cleans aviation data"""
    # Assign to variable for cleaning
    aviation_data_cleaned = aviation_raw
    # Strip out extra spaces
    aviation_data_cleaned.columns = aviation_data_cleaned.columns.str.strip()
    # Replace . with _
    aviation_data_cleaned.columns = aviation_data_cleaned.columns.str.replace(".","_")
    # Lowercase all names
    aviation_data_cleaned.columns = aviation_data_cleaned.columns.str.lower()
    
    # Drop duplicates
    aviation_data_cleaned = aviation_data_cleaned.drop_duplicates()
    # Drip duplicate events but keep the first reported event
    aviation_data_cleaned = aviation_data_cleaned.drop_duplicates(subset=['event_id'], keep='first')
    
    # Including data only from the USA
    usa_filter = aviation_data_cleaned['country'] == 'United States'
    aviation_data_cleaned = aviation_data_cleaned[usa_filter]
    # Drop the country column since there is now only one value
    aviation_data_cleaned = aviation_data_cleaned.drop('country', axis=1)
    
    # We don't want any amateur built airplanes so let's remove the data 
    pro_filter = aviation_data_cleaned['amateur_built'] == 'No'
    aviation_data_cleaned = aviation_data_cleaned[pro_filter]
    # Now drop the amateur_built column since all remaining aircraft are professionally built
    aviation_data_cleaned = aviation_data_cleaned.drop('amateur_built', axis=1)
    
    # Remove the incidents, only keep accidents
    aviation_data_cleaned = aviation_data_cleaned[aviation_data_cleaned['investigation_type']=='Accident']
    
    # Combine different makes but changing the case
    aviation_data_cleaned['make'] = aviation_data_cleaned['make'].str.title()
    ## Create a list of top brands and a map
    top_makes_list = ['Beech', 'Cessna', 'Cirrus', 'Piper', 'Diamond',
                  'Lockheed', 'Airbus', 'Grumman', 'Raytheon', 'Boeing']
    top_makes_map = {}

    for make in top_makes_list:
        beech_dict = aviation_data_cleaned[aviation_data_cleaned['make']
                                           .str.contains(make)]['make'].value_counts().to_frame()
        beech_dict['make'] = make
        top_makes_map.update(dict(beech_dict['make']))
    
    # Apply the Top Makes Map to the data
    top_makes_filter = aviation_data_cleaned['make'].isin(top_makes_list)
    aviation_data_cleaned[top_makes_filter]['make'] = aviation_data_cleaned['make'].map(top_makes_map)
    # Add a column designating Top Makes
    aviation_data_cleaned['top_make'] = aviation_data_cleaned['make'].isin(top_makes_list)
    # Create a column to designate commercial or private
    aviation_data_cleaned['use_category'] = aviation_data_cleaned['make'].apply(private_or_commercial)
    
    # Model Cleaning
    # Remove exccess white space from data and remove "-"
    aviation_data_cleaned['model'] = aviation_data_cleaned['model'].str.strip().str.replace('-','').str.replace(' ','')
    # Apply Model Cleaning functions
    aviation_data_cleaned['model'] = aviation_data_cleaned['model'].apply(model_cleaning_function)
    aviation_data_cleaned['model'] = aviation_data_cleaned['model'].apply(commercial_model_cleaning_function)
    
    # Add a column for top models
    top_commercial_models_list = ['A330', '747', '777', '727', 'CRJ', 'A320', '747', '737', 'DC3']
    only_private = aviation_data_cleaned['use_category'] == 'Private Enterprise'
    top_models_list = aviation_data_cleaned[top_makes_filter & only_private].groupby(['make','model']).count().reset_index()
    top_models_list = list(top_models_list.sort_values('event_date',ascending=False).groupby('make').head(3)['model'])
    top_models_list.extend(top_commercial_models_list)
    aviation_data_cleaned['top_model'] = aviation_data_cleaned['model'].isin(top_models_list)
    
    # Update the column to the correct datetime type
    aviation_data_cleaned['event_date'] = pd.to_datetime(aviation_data_cleaned['event_date'])
    
    # There are only a few datapoints before 1082 so let's remove them
    aviation_data_cleaned = aviation_data_cleaned[aviation_data_cleaned['event_date'].dt.year >= 1982]
    
    # Drop columns with irrelevant data
    aviation_data_cleaned = aviation_data_cleaned.drop([
    'event_id',
    'accident_number',
    'registration_number',
    'publication_date',
    'investigation_type',
    'report_status'
    ], axis=1)
    
    # Pull out columns to drop with over 60% missing data
    missing_data = (aviation_data_cleaned.isna().sum() / len(aviation_data_cleaned)).sort_values(ascending=False)
    columns_to_drop = missing_data[missing_data.values > 0.6].index.to_list()
    aviation_data_cleaned = aviation_data_cleaned.drop(columns_to_drop, axis=1)
    
    # Drop events with no location since there are only 10
    aviation_data_cleaned = aviation_data_cleaned[aviation_data_cleaned['location'].notna()]
    
    # Replace missing airport data with unknowns
    aviation_data_cleaned[['airport_code', 'airport_name']] = aviation_data_cleaned[['airport_code','airport_name']].fillna('Unknown')
    
    # We can drop these rows since there's only 15
    aviation_data_cleaned.dropna(subset=['injury_severity'], inplace=True)

    # Replace total uninjured with median
    total_uninjured_median = aviation_data_cleaned['total_uninjured'].median()
    aviation_data_cleaned['total_uninjured'].fillna(value=total_uninjured_median, inplace=True)
    
    # Assume missing injury data had 0 in column
    aviation_data_cleaned['total_fatal_injuries'].fillna(value=0, inplace=True)
    aviation_data_cleaned['total_serious_injuries'].fillna(value=0, inplace=True)
    aviation_data_cleaned['total_minor_injuries'].fillna(value=0, inplace=True)
    
    # Replace NaNs in these columns with unknowns
    aviation_data_cleaned['aircraft_damage'].fillna(value='Unknown', inplace=True)
    aviation_data_cleaned['make'].fillna(value='Unknown', inplace=True)
    aviation_data_cleaned['model'].fillna(value='Unknown', inplace=True)
    aviation_data_cleaned['purpose_of_flight'].fillna(value='Unknown', inplace=True)
    aviation_data_cleaned['weather_condition'].fillna(value='Unknown', inplace=True)
    aviation_data_cleaned['broad_phase_of_flight'].fillna(value='Unknown', inplace=True)
    
    # Create a map for the number of engines
    filter_nans = aviation_data_cleaned['number_of_engines'].notna()
    enginer_number_map = dict(aviation_data_cleaned[filter_nans].groupby(['make', 'model'])['number_of_engines'].agg(lambda x : pd.Series.mode(x)[0]))
    # Apply this map to the numer of enginers column to replace missing values
    aviation_data_cleaned['engine_number_map'] = tuple(zip(aviation_data_cleaned['make'], aviation_data_cleaned['model']))
    # Map the engine number to the new column
    aviation_data_cleaned['engine_number_map'] = aviation_data_cleaned['engine_number_map'].map(enginer_number_map)
    
    # Fill the missing number of engine data with the best guess based on make and model
    aviation_data_cleaned['number_of_engines'].fillna(value=aviation_data_cleaned['engine_number_map'], inplace=True)
    # Drop the remaining missing records with number of enginnes missing
    aviation_data_cleaned = aviation_data_cleaned[aviation_data_cleaned['number_of_engines'].notna()]
    
    # Create a map for the engine type based on the make and model
    engine_type_dict = aviation_data_cleaned.groupby(['make', 'model', 'engine_type']).size().reset_index().rename(columns={0:'count'})
    # Create a new column to map the data to
    engine_type_dict['make_model'] = tuple(zip(engine_type_dict['make'], engine_type_dict['model']))
    # Make this data frame into a map
    engine_type_map = dict(zip(engine_type_dict['make_model'], engine_type_dict['engine_type']))
    # Map the engine type to a column
    aviation_data_cleaned['engine_type_map'] = tuple(zip(aviation_data_cleaned['make'], aviation_data_cleaned['model']))
    aviation_data_cleaned['engine_type_map'] = aviation_data_cleaned['engine_type_map'].map(engine_type_map)
    
    # Fill the missing number of engine data with the best guess based on make and model
    aviation_data_cleaned['engine_type'].fillna(value=aviation_data_cleaned['engine_type_map'], inplace=True)
    
    # We still have some null values so lets replace the rest with 'Unknown'
    aviation_data_cleaned['engine_type'].fillna(value='Unknown', inplace=True)
    
    # Drop Extra Columns
    aviation_data_cleaned.drop(columns=['engine_number_map', 'engine_type_map'], inplace=True)
    # Created Total Passenger Count Column
    aviation_data_cleaned['passenger_count'] = aviation_data_cleaned[['total_fatal_injuries','total_serious_injuries','total_minor_injuries','total_uninjured']].sum(axis=1)
    
    # Add new city and state columns
    aviation_data_cleaned[['city', 'state']] = aviation_data_cleaned['location'].str.rsplit(', ', 1, expand = True)
    aviation_data_cleaned['city'] = aviation_data_cleaned['city'].str.capitalize()
    # Drop rows with null states
    aviation_data_cleaned = aviation_data_cleaned[aviation_data_cleaned['state'].notna()]
    
    # Update weather conditions names
    weather_map = { 'VMC' : 'Visual Meteorological Conditions',
                     'IMC' : 'Instrument Meteorological Conditions',
                     'Unknown' : 'Unknown Meteorological Conditions',
                     'UNK' : 'Unknown Meteorological Conditions',
                     'Unk' : 'Unknown Meteorological Conditions'
    }

    aviation_data_cleaned['weather_condition'] = aviation_data_cleaned['weather_condition'].map(weather_map)
    
    # Clean up the injury severity
    aviation_data_cleaned['injury_severity'] = aviation_data_cleaned['injury_severity'].str.split('(', 1, expand = True)
    
    # Create a column call fatality rate to figure out the deadliness of the accident
    aviation_data_cleaned['fatality_rate'] = aviation_data_cleaned['total_fatal_injuries']/aviation_data_cleaned['passenger_count']
    # Create a column call fatality rate to figure out the deadliness of the accident
    aviation_data_cleaned['percent_uninjured'] = aviation_data_cleaned['total_uninjured']/aviation_data_cleaned['passenger_count']

    return aviation_data_cleaned

def full_clean(file_path,output_path):
    """
    Main cleaning function that will call support functions
    Assumption: 
        - Your data files will be saved in a data folder and named "Aviation_Data.csv"
    -
    Input:
    df : Pandas dataframe
    -
    Output:
    summary : Pandas dataframe, cleaned and ready for anaysis
    """
    aviation_raw = pd.read_csv(file_path)
    aviation_data_cleaned = cleaning_aviation_data(aviation_raw)
    aviation_data_cleaned.to_csv(output_path)
    
    return aviation_data_cleaned
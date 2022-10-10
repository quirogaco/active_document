import utils

# description of each file
files = [ 
    {
        'file'  : './Input/data_source_1/sample_data.1.csv', 
        'sep'   : ',', 
        'source': 'data_1'
    },
    {
        'file'  : './Input/data_source_1/sample_data.2.dat', 
        'sep'   : '|', 
        'source': 'data_2'
    },
    {
        'file'  : './Input/data_source_2/sample_data.3.dat', 
        'sep'   : ',', 
        'source': 'data_3'
    }
]

# process data
df_unique = utils.unify_data(files)
utils.save_file_text(df_unique, "./Output/consolidated_output.1.csv")
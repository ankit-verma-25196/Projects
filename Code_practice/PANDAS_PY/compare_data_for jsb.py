def parse_csv_2():
    # Take Expected OTHER DATA and SIG DATA Csv's from file repo server and process it using pandas to get the difference
    # Check How to highlight not matched data
    other_data_cols = ["Content MD5", "Score", "Category", "SA Risk", "DA Risk", "SSA Risk", "Threat Name", "#BINS", "#IMGS", "JSON Size",
                       "PCAP Size"]

    url_observed_other_data = "http://10.65.10.149/sec-test/" + str(filename_other_data)
    url_observed_sig_data = "http://10.65.10.149/sec-test/" + str(filename_sig_data)

    url_expected_other_data = "http://10.65.10.149/sec-test/expected_other_data.csv"
    url_expected_sig_data = "http://10.65.10.149/sec-test/expected_sig_data.csv"

    # Storing Data from CSV's and then converting it to Data Frame
    expected_other_data = pd.read_csv(url_expected_other_data, header=None, names=other_data_cols)
    df_expected_other_data = pd.DataFrame(expected_other_data)
    print(df_expected_other_data.head())

    observed_other_data = pd.read_csv(url_observed_other_data, header=None, names=other_data_cols)
    df_observed_other_data = pd.DataFrame(observed_other_data)
    print(df_observed_other_data.head())

    expected_sig_data = pd.read_csv(url_expected_sig_data, header=None, names=other_data_cols)
    df_expected_sig_data = pd.DataFrame(expected_sig_data)
    print(df_expected_sig_data.head())

    observed_sig_data = pd.read_csv(url_observed_sig_data, header=None, names=other_data_cols)
    df_observed_sig_data = pd.DataFrame(observed_sig_data)
    print(df_observed_sig_data.head())

    # Compare OTHER DATA

    # Compare SIG DATA



#    pd.set_option('max_columns', None)
#    pd.set_option('display.max_colwidth', 50)
    #pd.set_option('display.max_columns', 0)
    df = pd.DataFrame(csv_data)
    print(df.head())


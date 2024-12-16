# Print the quality of the dataset (empty cells, duplicates, null values, and formatting consistancy)
def print_data_quality(dataset):
  # Print all rows that has empty cells
  if len(dataset.index) == 0:
    strs = ''

    for i in dataset.columns:
      strs += str(i) + ' '

    print(strs[:-1])
  else:
    print('No empty rows/cells found')

  # Check for and print all duplicate rows if any
  duplicate_rows = dataset[dataset.duplicated(keep=False)]

  if not duplicate_rows.empty:
    print('Duplicate Rows:')
    print(duplicate_rows)
  else:
    print('No duplicate rows found')

# Clean the dataset
def clean_data(dataset):
  print_data_quality(dataset)

  clean_dataset = dataset.dropna()
  clean_dataset = dataset.drop_duplicates()

  return clean_dataset

### Waveform analysis

This applications aims to predict waveforms from a CSV sample data.

It accepts the following parameters to run the prediction:
```json
{
    "name": "Test curve",
    "csv_file_path" : "file.csv",
    "options": {
        "x_column" : "A",
        "y_column" : "B"
    },
    "remove_mean" : true,
    "threshold" : {
        "lower" : -10.0,
        "upper" : 10.0
     }
}
```
- name: Output Data name
- csv_file_path: File path to the CSV data
- x_column: X column data
- y_column: Y column data
- remove_mean (optional): Remove mean from the Y data
- threshold (optional): Ignore data above/bellow the threshold values

### Algorithm
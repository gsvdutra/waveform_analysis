### Waveform analysis

To install the required packages
```
make dev
```

To run the application
```
make run_dev
```

Currently available functions:
- Linear

$x + y$

- Sinus


- Sinc 


- 

| Function | Equation | Reference |
| :---:   | :---: | :---: |
| Linear | $y = ax + b$| linear |
| Sinus | $y = A \cdot sin(\omega c + \phi) + c$| sinus |
| Sinc | $y = A \frac{sin(\omega c + \phi)}{x} + c$| sinc |
| xSin | $y = A \cdot x \cdot sin(\omega c + \phi) + c$| x_sin |
| Square | $y = square$ | square |
| Sawtooth | $y = sawtooth$ | sawtooth |



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
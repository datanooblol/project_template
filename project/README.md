# Project Structures
```python
|--configs: store your configurations  
|--data  
|  |--raw: raw data from source  
|  |--interim: intermediate process  
|  |--processed: precessed data  
|  |--results: model results  
|  |--test_data: data for unit test  
|--docs  
|--jobs  
|  |--job_script: main program  
|  |--test_script: test program or functions  
|  |--logs: log for debugging  
|--notebooks: for experimenting or exploring purposes  
|--references  
|--reports  
|  |--charts: store charts or figures used in reports  
|--udf  
|  |--extract: functions for extracting data from source  
|  |--load: functions for load/save/write results or stages  
|  |--model: functions for training and inferencing  
|  |--transform: functions for transforming data for further analysis  
|  |--utils: functions for generating logging objects
|  |--visualize: functions for exploring or reporting  
|  |--__init__.py  
|--README.md: explain a project structure 
```  
# Log Structures  
```python

[datetime]|elapsed|module(extract, transform, load)|function name|line number|step(start, end, epoch)|shape  

# transform:  
[2022-04-10 17:41:29,624]|0.000000|transform|test_a|6|start|(20, 1)  
[2022-04-10 17:41:29,625]|0.000128|transform|test_a|6|end|(15, 1)  

# extract:  
[2022-04-10 17:41:32,039]|0.006357|extract|extract_train_raw|13|epoch|(891, 12)  

# load:  
[2022-04-10 17:41:32,062]|0.014953|load|load_train_interim|25|epoch|(891, 12)
```
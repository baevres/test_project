# test_project
The records from MainTable I save in main_lst by circles "while" and "for". Every iteration saves next 3 records 
from current record. 
At first I thought to make an infinity circle which every second will return current iteration.
For it I thought to use generator and operator "yield". But Amazon AWS can't to keep interims data. It was the main problem in implementation which took much more time that planed.
Now I use module "datetime" that's why function "lambda_handler" returns part of main_lst by using index, ex.: main_lst[current_second].

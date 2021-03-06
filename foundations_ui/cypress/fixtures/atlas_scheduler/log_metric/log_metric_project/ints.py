import foundations
from time import sleep

foundations.log_metric("metric_int", 1)
foundations.log_metric("metric_large_int", 8888888888888888888888888)
foundations.log_metric("metric_list_of_ints", [1, 2])
foundations.log_metric("metric_long_list_of_ints", [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2])
foundations.log_metric("metric_long_list_of_long_ints", [8888888888888888888888888,
                                                  8888888888888888888888888,
                                                  8888888888888888888888888,
                                                  8888888888888888888888888,
                                                  8888888888888888888888888,
                                                  8888888888888888888888888,
                                                  8888888888888888888888888,
                                                  8888888888888888888888888,
                                                  8888888888888888888888888,
                                                  8888888888888888888888888,
                                                  8888888888888888888888888,
                                                  8888888888888888888888888,
                                                  8888888888888888888888888,
                                                  8888888888888888888888888,
                                                  8888888888888888888888888,
                                                  8888888888888888888888888,
                                                  8888888888888888888888888,
                                                  8888888888888888888888888,
                                                  8888888888888888888888888,
                                                  8888888888888888888888888,
                                                  8888888888888888888888888,
                                                  8888888888888888888888888,
                                                  8888888888888888888888888])
foundations.log_metric("metric_mixed_type", 1)
for i in range(20):
  foundations.log_metric("metric_repeat", i)
  sleep(.1)

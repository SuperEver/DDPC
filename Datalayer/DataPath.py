#coding:utf-8
import os

training_path = '/Users/zhangjustin/work/citydata/season_1/training_data'
traindata_list = []

with open('/Users/zhangjustin/work/citydata/season_1/train_data.list', 'r') as f:
    for line in f:
        traindata_list.append(line.strip())
    f.close()

map_path = os.path.join(training_path, 'cluster_map')
order_path = os.path.join(training_path, 'order_data')
poi_path = os.path.join(training_path, 'poi_data')
traffic_path = os.path.join(training_path, 'traffic_data')
weather_path = os.path.join(training_path, 'weather_data')

map_prefix = 'cluster_map'
order_prefix = 'order_data'
poi_prefix = 'poi_data'
traffic_prefix = 'traffic_data'
weather_prefix = 'weather_data'

runtime_path = '/Users/zhangjustin/work/citydata/season_1/runtime'
label_filename = 'label.pkl'


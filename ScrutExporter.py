import json
import requests

class Exporter:
    def __init__(self, logstash = None):
        self.logstash = logstash
        pass

    def logstash_exporter(self,scrutinizer_data):
        returned_data = scrutinizer_data['report']['graph']['timeseries']['inbound']
        data_type = scrutinizer_data['report']['table']['inbound']['columns'][1]['title']
        data_rows = scrutinizer_data['report']['table']['inbound']['rows']
        total_rows = len(data_rows)
        progress_counter = 1

        for element in data_rows:
            progress = round((progress_counter / total_rows)*100, 2)
            label = element[1]['rawValue']
            octet_count = int(element[6]['rawValue'])
            epoch_time = int(element[7]['rawValue']) *1000
            doc = json.dumps({
                data_type : label,
                "bits":octet_count,
                "date":epoch_time
                
            })
            print('{}% sent to Logstash'.format(progress), end='\r')
            progress_counter += 1
            data_back = requests.post(url=self.logstash, data=doc)
        print('\n')
        print('Completed')
        print('Last Message From Logstash {}'.format(data_back.content))


           

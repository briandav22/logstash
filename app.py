from ScrutRequester import ReportAPI, Requester
from ScrutExporter import Exporter

report_params = ReportAPI()
logstash_server = "http://your_logstash:8080"
report_params.report_options(
    filters={"sdfDips_0": "in_GROUP_ALL",
            "sdfIPGroups_0": "ex_16800000_src"}, 
    reportTypeLang="srcHosts")

report_params.report_direction(
    report_direction="inbound",
    max_rows=10000 )

report_params.make_object()

scrut_requester = Requester(
    authToken="scrutinizerAPIToken", 
    hostname="ScrutinizerHostname or IP")

print("Getting Scrutinizer Data")    
data = scrut_requester.make_request(report_params.params)

print("Sending Data to Logstash")
scrut_exporter = Exporter(logstash=logstash_server)

scrut_exporter.logstash_exporter(data)

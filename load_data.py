import os
import django
import csv
from datetime import datetime
import pytz

# Ensure the path is correct based on your directory structure
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cyberthreat.settings')
django.setup()

from analysis.models import CyberThreat

def load_data(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            naive_timestamp = datetime.strptime(row['Timestamp'], '%Y-%m-%d %H:%M:%S')
            aware_timestamp = pytz.utc.localize(naive_timestamp)
            CyberThreat.objects.create(
                timestamp=aware_timestamp,
                source_ip=row['Source IP Address'],
                destination_ip=row['Destination IP Address'],
                source_port=row['Source Port'],
                destination_port=row['Destination Port'],
                protocol=row['Protocol'],
                packet_length=row['Packet Length'],
                packet_type=row['Packet Type'],
                traffic_type=row['Traffic Type'],
                payload_data=row['Payload Data'],
                malware_indicators=row['Malware Indicators'] == 'True',
                anomaly_scores=float(row['Anomaly Scores']),
                alerts_warnings=row['Alerts/Warnings'] == 'True',
                attack_type=row['Attack Type'],
                attack_signature=row['Attack Signature'],
                action_taken=row['Action Taken'],
                severity_level=row['Severity Level'],
                user_information=row['User Information'],
                device_information=row['Device Information'],
                network_segment=row['Network Segment'],
                geo_location_data=row['Geo-location Data'],
                proxy_information=row['Proxy Information'] == 'True',
                firewall_logs=row['Firewall Logs'],
                ids_ips_alerts=row['IDS/IPS Alerts'] == 'True',
                log_source=row['Log Source']
            )

# Call the function with the path to your dataset
load_data('dataset/data.csv')

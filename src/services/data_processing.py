import csv


class DataProcessing:
    def output_array_to_csv(data: list):
        csv_path = './slack.csv'
        # csv出力ではデータが二次元配列になっている必要がある
        data_for_csv = []
        for record in data:
            data_for_csv.append([record])
        with open(csv_path, 'w', newline='', encoding='utf_8_sig') as f:
            w = csv.writer(f)
            w.writerows(data_for_csv)

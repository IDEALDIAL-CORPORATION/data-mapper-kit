from typing import Dict, Any

class DataMapper:
    def __init__(self, mapping: Dict[str, str]) -> None:
        self.mapping = mapping

    def map_data(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        mapped_data = {}
        for key, value in input_data.items():
            if key in self.mapping:
                mapped_key = self.mapping[key]
                mapped_data[mapped_key] = value
        return mapped_data

if __name__ == '__main__':
    sample_mapping = {'name': 'full_name', 'age': 'years'}
    mapper = DataMapper(sample_mapping)
    data = {'name': 'John', 'age': 30}
    print(mapper.map_data(data))

from pathlib import Path

from core.data.data_engine import TestDataEngine

if __name__ == "__main__":
    data = TestDataEngine().load_json(Path(__file__).with_name("tempData.json"))
    print(
        data["string"],
        data["number"],
        data["boolean"],
        data["array"],
        data["object"],
        data["nested"],
    )

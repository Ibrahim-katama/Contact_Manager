import os
from src.storage import save_contacts, load_contacts

def test_save_and_load_contacts(monkeypatch, tmp_path):
    temp_csv = tmp_path / "test_contacts.csv"
    monkeypatch.setattr("src.storage.CONTACTS_FILE", str(temp_csv))

    test_data = [
        {
            "first_name": "Jannet",
            "middle_name": "",
            "last_name": "Malaika",
            "number": "9876543210",
            "email": "jane@example.com"
        }
    ]

    save_contacts(test_data)
    assert os.path.exists(temp_csv)

    loaded = load_contacts()
    assert len(loaded) == 1
    assert loaded[0]["first_name"] == "Jannet"
    assert loaded[0]["number"] == "9876543210"
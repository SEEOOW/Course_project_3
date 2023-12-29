import os.path

from src import utils
from config import ROOT_DIR


def test_load_all_operations():
    TEST_DATA_PATH = os.path.join(ROOT_DIR, 'tests', 'data_for_test.json')
    assert utils.load_all_operations(TEST_DATA_PATH) == [1, 2, 3]

def test_executed_operations():
    executed_operations = [
  {
    "id": 911,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041"
  },
  {
    "id": 126,
    "state": "CANCELED",
    "date": "2021-12-26T10:50:58.294041"
  },
  {
    "id": 353,
    "state": "EXECUTED",
    "date": "2018-06-30T02:08:58.425572",
  }]
    expected_result = [
  {
    "id": 911,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041"
  },
  {
    "id": 353,
    "state": "EXECUTED",
    "date": "2018-06-30T02:08:58.425572",
  }]
    assert utils.executed_operations(executed_operations) == expected_result

def test_sorted_operations():
    sorted_operations = [
  {
    "state": "EXECUTED",
    "date": "2019-06-01T06:46:16.803326",
    },
  {
    "state": "EXECUTED",
    "date": "2018-07-31T12:25:32.579413",
      },
  {
    "state": "EXECUTED",
    "date": "2019-04-11T23:10:21.514616",
  }]
    expected_result = [
  {
    "state": "EXECUTED",
    "date": "2019-06-01T06:46:16.803326",
    },
  {
    "state": "EXECUTED",
    "date": "2019-04-11T23:10:21.514616",
    },
  {
    "state": "EXECUTED",
    "date": "2018-07-31T12:25:32.579413",
    }]
    assert utils.sorted_operations(sorted_operations) == expected_result


def test_hidden_requisites():
  hidden_requisites_none = ""
  hidden_requisites_account = "Счет 7322275323904829567"
  hidden_requisites_card = "МИР 8193813157568899"
  assert utils.hidden_requisites(hidden_requisites_none) == "None"
  assert utils.hidden_requisites(hidden_requisites_account) == "Счет **9567"
  assert utils.hidden_requisites(hidden_requisites_card) == "МИР 8193 81** **** 8899"


def test_formatted_operations():
  operation = [
  {
      "id": 260972664,
      "state": "EXECUTED",
      "date": "2018-01-23T01:48:30.477053",
      "operationAmount": {
        "amount": "2974.30",
        "currency": {
          "name": "USD",
          "code": "USD"
        }
      },
      "description": "Перевод с карты на карту",
      "from": "Visa Classic 3414396880443483",
      "to": "Visa Gold 2684274847577419"
  }]
  assert utils.formatted_operations(operation) == "23.01.2018 Перевод с карты на карту\nVisa Classic 3414 39** **** 3483 -> Visa Gold 2684 27** **** 7419\n2974.30 USD\n"



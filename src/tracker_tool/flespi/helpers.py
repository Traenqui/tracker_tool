"""Helperfunction to generate a felspi report"""
import json
import os

import pandas


def settings(emei):
    """This function reads in all the .json files and parses them for the desired settings

    Args:
        emei (str): the serialnumber of a tracker

    Returns:
        pandas.Dataframe: return a table-link object with the trackerdata
    """
    path = f".\\temp\\{emei}.json"
    print(f"{os.path.exists(path)=}")
    tracker_data = {}
    with open(path, "r", encoding="UTF-16") as fcc_file:
        fcc_data = json.load(fcc_file)
        for ele in fcc_data["result"]:

            tracker_data["Seriennummer"] = emei
            match ele["name"]:
                case "ignition_detection":
                    if ele["current"]["ign"]["source"] == 4:
                        tracker_data["ignition_detection"] = "Ignition"
                        tracker_data["ignition_detection_high"] = ele["current"]["ign"][
                            "high"
                        ]
                        tracker_data["ignition_detection_low"] = ele["current"]["ign"][
                            "low"
                        ]
                        tracker_data["ignition_detection_source"] = ele["current"][
                            "ign"
                        ]["source"]

                    elif ele["current"]["ign"]["source"] == 1:
                        tracker_data["ignition_detection"] = "DIN 1"
                        tracker_data["ignition_detection_source"] = ele["current"][
                            "ign"
                        ]["source"]
                    else:
                        tracker_data["ignition_detection"] = "Unknown"

                case "getver":
                    tracker_data["model"] = ele["current"]["hardware_model"]

                case "motion_detection":
                    tracker_data["motion_detection_can"] = ele["current"]["can"]
                    tracker_data["motion_detection_gps"] = ele["current"]["gps"]
                    tracker_data["motion_detection_ignition"] = ele["current"][
                        "ignition"
                    ]
                    tracker_data["motion_detection_movement"] = ele["current"][
                        "movement"
                    ]

                case "battery_chagrge_mode":
                    try:
                        tracker_data["battery_chagrge_mode"] = ele["current"]["mode"]
                    except TypeError:
                        continue
                case "home_network":
                    tracker_data["home_network_sleep"] = (
                        int(ele["current"]["on_stop"]["min_period"]) / 60 / 60
                    )

                case "roaming_network":
                    tracker_data["roaming_network_sleep"] = (
                        int(ele["current"]["on_stop"]["min_period"]) / 60 / 60
                    )

                case "unknown_network":
                    tracker_data["unknown_network_sleep"] = (
                        int(ele["current"]["on_stop"]["min_period"]) / 60 / 60
                    )

                case _:
                    continue

        temp = pandas.DataFrame(data=tracker_data, index=[0])
        return temp

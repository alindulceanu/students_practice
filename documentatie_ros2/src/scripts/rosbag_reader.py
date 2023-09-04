import argparse
from rclpy.serialization import deserialize_message
from rosidl_runtime_py.utilities import get_message
from geometry_msgs.msg import Twist
import rosbag2_py
import pandas as pd

def read_messages(input_bag: str):
    first = "-1"

    reader = rosbag2_py.SequentialReader()
    reader.open(
        rosbag2_py.StorageOptions(uri=input_bag, storage_id="mcap"),
        rosbag2_py.ConverterOptions(
            input_serialization_format="cdr", output_serialization_format="cdr"
        ),
    )

    topic_types = reader.get_all_topics_and_types()

    def typename(topic_name):
        for topic_type in topic_types:
            if topic_type.name == topic_name:
                return topic_type.type
        raise ValueError(f"topic {topic_name} not in bag")

    while reader.has_next():
        topic, data, timestamp = reader.read_next()
        frame = int((timestamp % (10 ** 14)) / (10 ** 9))

        if first == "-1":
            first = frame

        msg_type = get_message(typename(topic))
        msg = deserialize_message(data, msg_type)
        yield topic, msg, frame - first
    del reader

def main(args = None):
    df = pd.DataFrame(columns=["FRAME", "TOPIC", "linX", "linY", "linZ", "angX", "angY", "angZ"])

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "input", help="input bag path (folder or filepath) to read from"
    )
    parser.add_argument('-t', '--topic', action='append')
    parser.add_argument('-f', '--frame', action='append')
    parser.add_argument('-v', '--value', action='append')

    args = parser.parse_args()

    for topic, msg, frame in read_messages(args.input):
        if isinstance(msg, Twist):
            new_row = {"FRAME": frame, "TOPIC": topic, "linX": msg.linear.x, "linY": msg.linear.y, "linZ": msg.linear.z, "angX": msg.angular.x, "angY": msg.angular.y, "angZ": msg.angular.z}
            df.loc[len(df)] = new_row
            df.to_csv("~/ros2_ws/src/my_robot_controller/data2.csv")
        else:
            print("Error")

    try:
        for top in args.topic:
            for frm in args.frame:
                for val in args.value:
                    print(f"\n Search result: {df.loc[(df['FRAME'] == int(frm)) & (df['TOPIC'] == str(top)), val].values}", f" topic: {top}, frame: {frm}, column: {val}\n")

    except:
        print("[ERROR] Invalid input!")

if __name__ == "__main__":
    main()